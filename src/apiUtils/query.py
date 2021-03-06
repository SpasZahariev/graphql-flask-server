import graphene
from apiUtils.schemaObjects import SongDto, RoomDto
from common.roomManager import (
    get_room_values,
    Room,
    to_graphene_room,
    get_specific_room,
)
from flask_socketio import SocketIO, emit

# import json
# import __main__
from apiUtils.socket_methods import emit_usernames

# from common.songManager import Playlist Song, to_graphene_song


class Query(graphene.ObjectType):
    # first declare what objects we return
    # songs = graphene.List(SongDto)
    rooms = graphene.List(RoomDto)
    room = graphene.Field(RoomDto, pin=graphene.String(required=True))

    # then create resolvers that return them
    # def resolve_songs(self, info):
    #     return list(map(to_graphene_song, songQueue))

    def resolve_rooms(self, info):
        return map(to_graphene_room, get_room_values())

    # whenever this is called a user will join the room
    def resolve_room(self, info, pin):
        print("attemptin to join room with pin: ", pin)

        target_room = get_specific_room(pin)
        # if target_room = NoneType throw error back to client (room with this pin does not exist)
        target_room.create_user()

        emit_usernames(target_room.usernames)

        return to_graphene_room(target_room)


# query {
#   room(pin:"1111") {
#         pin
#     usernames
#     songs {
#       title
#       url
#       likes
#       company
#     }
#   }
# }
