import graphene

from apiUtils.schemaObjects import SongDto
from sortedcontainers import SortedList


class Song:
    def __init__(self, url, title="blank", likes=0):
        self.title = title
        self.url = url
        self.likes = likes


def to_graphene_song(song):
    return SongDto(title=song.title, url=song.url, likes=song.likes)


# def get_sorted_songs():
#     return my_songs.sort(key=lambda song: song.likes)


def pop_sorted_songs():
    my_songs.pop(0)
    return my_songs


def append_song(song):
    my_songs.add(song)


def remove_song(song):
    my_songs.remove(song)


def get_songs():
    return my_songs


# list structure that is always sorted on likes
my_songs = SortedList(
    [
        Song(title="You give love a bad name", url="asdfasdfgzlxczv94"),
        Song(title="Mick Gordon - Inferno", url="asdf4fdsadf", likes=666),
    ],
    # quick fix to make sort in descending order
    key=lambda song: 1 / (1 + song.likes),
)

