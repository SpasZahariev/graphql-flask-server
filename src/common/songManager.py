import graphene

from apiUtils.schemaObjects import SongDto
from sortedcontainers import SortedList
from common.brandType import Brand

# user is the person who added the song
class Song:
    def __init__(self, url, title="blank", company="YOUTUBE", username="Host", likes=0):
        self.title = title
        self.url = url
        self.likes = likes
        self.username = username
        self.company = Brand.YOUTUBE if company != "SPOTIFY" else Brand.SPOTIFY


def to_graphene_song(song):
    return SongDto(
        title=song.title,
        url=song.url,
        likes=song.likes,
        username=song.username,
        company=song.company,
    )


class Playlist:
    def __init__(self):
        # quick fix to make sort in descending order of likes
        self.songs = SortedList([], key=lambda song: 1 / (1 + song.likes))

    def get_graphene_songs(self):
        return map(to_graphene_song, self.songs)

    def dequeue_songs(self, first=1):
        del self.songs[:first]
        return self.songs

    def append_song(self, song):
        self.songs.add(song)

    def remove_song(self, song):
        self.songs.remove(song)

    def like_song(self, title):
        for song in self.songs:
            if song.title == title:
                # unfortunately there is no update => remove and then add it back in
                self.remove_song(song)
                song.likes += 1
                self.append_song(song)
                break

    def get_songs(self):
        return self.songs

    def get_serialized_songs(self):
        return list(map(lambda x: x.__dict__, self.songs))

    # def get_sorted_songs():
    #     return my_songs.sort(key=lambda song: song.likes)


# # list structure that is always sorted on likes
# songQueue = SortedList(
#     [
#         Song(title="You give love a bad name", url="asdfasdfgzlxczv94"),
#         Song(title="Mick Gordon - Inferno", url="asdf4fdsadf", likes=666),
#     ],
#     key=lambda song: 1 / (1 + song.likes),
# )

