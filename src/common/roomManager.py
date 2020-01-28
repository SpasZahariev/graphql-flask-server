import graphene
from apiUtils.schemaObjects import SongDto
from apiUtils.schemaObjects import RoomDto
from common.songManager import my_songs


class Room:
    def __init__(self, usernames, songs, pin="0000"):
        self.usernames = usernames
        self.songs = songs
        self.pin = pin


def to_graphene_room(room):
    return RoomDto(pin=room.pin, usernames=room.usernames, songs=room.songs)


my_rooms = [Room(["Spas", "Mac", "Zack"], my_songs, "1111")]
