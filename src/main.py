from flask import Flask, render_template
import os
import graphene
from flask_graphql import GraphQLView

from apiUtils.query import Query
from apiUtils.mutation import Mutation
from flask_socketio import SocketIO, emit

# from graphql_ws import gevent


# Imports

# app initialization
basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.debug = True


app.config["SECRET_KEY"] = "secret!"
socketio = SocketIO(app)


# python classes

# class Company(Enum):
#     YOUTUBE = "y"
#     SPOTIFY = "s"

####################################################
####         GraphQL Schema Objects    ####
####################################################

schema = graphene.Schema(query=Query, mutation=Mutation)


app.add_url_rule(
    "/graphql",
    view_func=GraphQLView.as_view(
        "graphql", schema=schema, graphiql=True  # for having the GraphiQL interface
    ),
)

# TO-DO
@app.route("/")
def index():
    # return "<p> Hello World</p>"
    return render_template("index.html")


@socketio.on("create")
def lol_message(message):
    print("lol check this out   ", message)
    emit("response_channel", {"data": "created smth <-- the server said this!"})


# my event channel the server is listening to
@socketio.on("my event", namespace="/test")
def test_message(message):
    emit("my response", {"data": message["data"]})


@socketio.on("my broadcast event", namespace="/test")
def test_message(message):
    emit("response_channel", {"data": message["data"]}, broadcast=True)


# connect channel
@socketio.on("connect", namespace="/test")
def test_connect():
    emit("response_channel", {"data": "Connected <-- the server said this!"})


@socketio.on("disconnect", namespace="/test")
def test_disconnect():
    print("Client disconnected")


if __name__ == "__main__":
    socketio.run(app)
    # app.run()
