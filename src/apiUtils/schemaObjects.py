import graphene


class SongDto(graphene.ObjectType):
    title = graphene.String()
    url = graphene.String()
    likes = graphene.Int()
    username = graphene.String()
    company = graphene.String()


class RoomDto(graphene.ObjectType):
    pin = graphene.String()
    usernames = graphene.List(graphene.String)
    songs = graphene.List(SongDto)
