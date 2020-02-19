import graphene
import namesgenerator
from apiUtils.schemaObjects import SongDto
from apiUtils.schemaObjects import RoomDto
from common.songManager import Playlist, Song
from random import randint
from sortedcontainers import SortedList


class Room:
    def __init__(
        self, pin="0000", usernames=["Host"], playlist=Playlist(),
    ):
        self.pin = pin
        self.usernames = usernames
        self.playlist = playlist

    def get_serialized_room(self):
        return {
            "pin": self.pin,
            "usernames": self.usernames,
            "playlist": self.playlist.get_serialized_songs(),
        }

    def create_user(self):
        username = namesgenerator.get_random_name()
        self.usernames.append(username)
        return username


def to_graphene_room(room):
    return RoomDto(
        pin=room.pin, usernames=room.usernames, songs=room.playlist.get_graphene_songs()
    )


# throws stopIteration if pin is not there
def get_specific_room(pin):
    return room_dict.get(pin)
    # return next(room for room in my_rooms if room.pin == pin)


def is_in_room(pin):
    return pin in room_dict


def get_room_values():
    return room_dict.values()


def create_room():
    random_pin = str(randint(0, 9999))
    while random_pin in room_dict:
        # in case I am running out of memory
        if len(room_dict) > 1000:
            reset_rooms()
        random_pin = str(randint(0, 9999))

    # prepend with zeros if pin is less than 4 symbols
    random_pin = ("0" * (4 - len(random_pin))) + random_pin

    room_dict[random_pin] = Room(pin=random_pin)
    return room_dict[random_pin]


def reset_rooms():
    room_dict = {}


room_dict = {}
room_dict["1111"] = Room(
    pin="1111",
    usernames=[
        "Spas",
        namesgenerator.get_random_name(),
        namesgenerator.get_random_name(),
        namesgenerator.get_random_name(),
    ],
    playlist=Playlist(),
)
room_dict["1111"].playlist.append_song(
    Song(title="You give love a bad name", url="asdfasdfgzlxczv94")
)
room_dict["1111"].playlist.append_song(
    Song(title="Mick Gordon - Inferno", url="asdf4fdsadf", likes=666)
)

# import json

# print(room_dict["1111"].get_serialized_room())
# print(json.dumps(room_dict["1111"].get_serialized_room(), indent=4))
