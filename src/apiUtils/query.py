import graphene
from apiUtils.schemaObjects import SongDto, RoomDto
from common.roomManager import my_rooms, Room, to_graphene_room
from common.songManager import my_songs, Song, to_graphene_song


class Query(graphene.ObjectType):
    # first declare what objects we return
    songs = graphene.List(SongDto)
    rooms = graphene.List(RoomDto)

    # then create resolvers that return them
    def resolve_songs(self, info):
        return list(map(to_graphene_song, my_songs))

    def resolve_rooms(self, info):
        return list(map(to_graphene_room, my_rooms))
