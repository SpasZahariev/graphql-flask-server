# Imports
from flask import Flask
import os
import graphene
from flask_graphql import GraphQLView

# app initialization
basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.debug = True

# python classes
class MySong:
    def __init__(self, url, title="blank", likes=0):
        self.title = title
        self.url = url
        self.likes = likes


my_songs = [
    MySong(title="You give love a bad name", url="asdfasdfgzlxczv94"),
    MySong(title="Mick Gordon - Inferno", url="asdf4fdsadf", likes=666),
]


def to_graphene_song(song):
    return Song(title=song.title, url=song.url, likes=song.likes)


class MyRoom:
    def __init__(self, usernames, songs, pin="0000"):
        self.usernames = usernames
        self.songs = songs
        self.pin = pin


my_rooms = [MyRoom(["Spas", "Mac", "Zack"], my_songs, "1111")]


def to_graphene_room(room):
    return Room(pin=room.pin, usernames=room.usernames, songs=room.songs)


# class Company(Enum):
#     YOUTUBE = "y"
#     SPOTIFY = "s"

####################################################
####         GraphQL Schema Objects    ####
####################################################
class Song(graphene.ObjectType):
    title = graphene.String()
    url = graphene.String()
    likes = graphene.Int()


class Room(graphene.ObjectType):
    pin = graphene.Int()
    usernames = graphene.List(graphene.String)
    songs = graphene.List(Song)


class Query(graphene.ObjectType):
    rooms = graphene.List(Room)
    songs = graphene.List(Song)

    def resolve_songs(self, info):
        return list(map(to_graphene_song, my_songs))

    def resolve_rooms(self, info):
        return list(map(to_graphene_room, my_rooms))


schema = graphene.Schema(query=Query)

app.add_url_rule(
    "/graphql",
    view_func=GraphQLView.as_view(
        "graphql", schema=schema, graphiql=True  # for having the GraphiQL interface
    ),
)

# TO-DO
@app.route("/")
def index():
    return "<p> Hello World</p>"


if __name__ == "__main__":
    app.run()

q = """
{
  rooms {
    pin
    usernames
    songs {
      title
      url
      likes
    }
  }
  songs {
    title
    url
    likes
  }
}
"""
