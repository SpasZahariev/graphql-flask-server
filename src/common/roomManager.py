import graphene
from apiUtils.schemaObjects import SongDto
from apiUtils.schemaObjects import RoomDto
from common.songManager import Playlist, Song
from random import randint


class Room:
    def __init__(self, usernames, playlist, pin="0000"):
        self.usernames = usernames
        self.playlist = playlist
        self.pin = pin


def to_graphene_room(room):
    return RoomDto(
        pin=room.pin, usernames=room.usernames, songs=room.playlist.get_graphene_songs()
    )


# throws stopIteration if pin is not there
def get_specific_room(pin):
    return room_dict.get(pin)
    # return next(room for room in my_rooms if room.pin == pin)


def get_room_values():
    return room_dict.values()


def create_room():
    random_pin = str(randint(0, 9999))
    room_dict[random_pin] = Room([], Playlist(), random_pin)


room_dict = {}
room_dict["1111"] = Room(["Spas", "Mac", "Zack"], Playlist(), "1111")
room_dict["1111"].playlist.append_song(
    Song(title="You give love a bad name", url="asdfasdfgzlxczv94")
)
room_dict["1111"].playlist.append_song(
    Song(title="Mick Gordon - Inferno", url="asdf4fdsadf", likes=666)
)

