import graphene


class SongDto(graphene.ObjectType):
    title = graphene.String()
    url = graphene.String()
    likes = graphene.Int()


class RoomDto(graphene.ObjectType):
    pin = graphene.Int()
    usernames = graphene.List(graphene.String)
    songs = graphene.List(SongDto)
