import graphene
from apiUtils.schemaObjects import SongDto


class Song:
    def __init__(self, url, title="blank", likes=0):
        self.title = title
        self.url = url
        self.likes = likes


def to_graphene_song(song):
    return SongDto(title=song.title, url=song.url, likes=song.likes)


my_songs = [
    Song(title="You give love a bad name", url="asdfasdfgzlxczv94"),
    Song(title="Mick Gordon - Inferno", url="asdf4fdsadf", likes=666),
]
