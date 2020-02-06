import graphene
import namesgenerator
from apiUtils.schemaObjects import SongDto, RoomDto
from common.roomManager import (
    get_specific_room,
    create_room,
    to_graphene_room,
    reset_rooms,
)
from common.songManager import Playlist, Song
from flask_socketio import SocketIO, emit
from random import randint
import json
import __main__

# from __main__ import socketio


class PutSong(graphene.Mutation):
    # what the muatition returns
    songs = graphene.Field(graphene.List(SongDto))

    # arguments that can be passed in to the mutation
    class Arguments:
        pin = graphene.String()
        title = graphene.String()
        url = graphene.String()
        username = graphene.String(required=False, default_value="Host")
        company = graphene.String(required=False, default_value="YOUTUBE")

    # function that resolves the mutation
    def mutate(self, info, pin, title, url, username, company):
        # if info.context.get("is_vip"):
        # username = username.upper()
        player = get_specific_room(pin).playlist
        player.append_song(
            Song(url=url, title=title, company=company, username=username)
        )
        # socket io emitting to everybody in room
        __main__.socketio.emit(
            "playlist_channel", json.dumps(player.get_serialized_songs(), indent=4)
        )
        # emit("playlist_channel", {"data": message["data"]}, broadcast=True)
        return PutSong(player.get_graphene_songs())


class LikeSong(graphene.Mutation):
    songs = graphene.Field(graphene.List(SongDto))

    class Arguments:
        pin = graphene.String()
        title = graphene.String()

    def mutate(self, info, pin, title):
        player = get_specific_room(pin).playlist
        for song in player.get_songs():
            if song.title == title:
                # unfortunately there is no update => remove and then add it back in
                player.remove_song(song)
                song.likes += 1
                player.append_song(song)
                break
        # socket io emitting to everybody in room
        __main__.socketio.emit(
            "playlist_channel", json.dumps(player.get_serialized_songs(), indent=4)
        )
        return LikeSong(player.get_graphene_songs())


class AddUser(graphene.Mutation):
    usernames = graphene.Field(graphene.List(graphene.String))

    class Arguments:
        pin = graphene.String()

    # function that resolves the mutation
    def mutate(self, info, pin):
        room = get_specific_room(pin)
        room.usernames.append(namesgenerator.get_random_name())

        # socket io emitting to everybody in room
        __main__.socketio.emit(
            "usernames_channel", json.dumps(room.usernames), indent=4
        )
        return AddUser(room.usernames)


class PutRoom(graphene.Mutation):
    room = graphene.Field(RoomDto)

    class Arguments:
        clear = graphene.Boolean(required=False, default_value=False)

    def mutate(self, info, clear):
        if clear:
            reset_rooms()
        return PutRoom(to_graphene_room(create_room()))


class Mutation(graphene.ObjectType):
    put_song = PutSong.Field()
    like_song = LikeSong.Field()
    add_user = AddUser.Field()
    put_room = PutRoom.Field()


# mutation { putSong (title: "t4", url: "u5", pin:"1111") { songs { title url likes } }}
# mutation { putSong (title: "t4", url: "u5", pin:"1111", username: "guy", company:"SPOTIFY") { songs { title url likes username company} }}


# mutation {
#   likeSong(title: "t4", pin:"1111") {
#     songs {
#       title
#       url
#       likes
#     }
#   }
# }


# mutation {
# 	putRoom {
#     room {
#       usernames
#       pin
#       songs {
#         title
#         url
#         likes
#         company
#       }
#     }
#   }
# }
