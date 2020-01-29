import graphene
from apiUtils.schemaObjects import SongDto
from common.songManager import (
    Song,
    to_graphene_song,
    append_song,
    get_songs,
    remove_song,
)


class PutSong(graphene.Mutation):
    # what the muatition returns
    songs = graphene.Field(graphene.List(SongDto))

    # arguments that can be passed in to the mutation
    class Arguments:
        title = graphene.String()
        url = graphene.String()

    # function that resolves the mutation
    def mutate(self, info, title, url):
        # if info.context.get("is_vip"):
        # username = username.upper()
        append_song(Song(url=url, title=title))
        return PutSong(map(to_graphene_song, get_songs()))


class LikeSong(graphene.Mutation):
    songs = graphene.Field(graphene.List(SongDto))

    class Arguments:
        title = graphene.String()

    def mutate(self, info, title):
        for song in get_songs():
            if song.title == title:
                # unfortunately there is no update => remove and then add it back in
                remove_song(song)
                song.likes += 1
                append_song(song)
                break
        return LikeSong(map(to_graphene_song, get_songs()))


class Mutation(graphene.ObjectType):
    put_song = PutSong.Field()
    like_song = LikeSong.Field()


# mutation { putSong (title: "t3", url: "u5") { songs { title url likes } }}

# mutation {
#   likeSong(title: "t2") {
#     songs {
#       title
#       url
#       likes
#     }
#   }
# }

