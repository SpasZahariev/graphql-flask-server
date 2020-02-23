from flask import Flask, render_template
import os
import graphene
from flask_graphql import GraphQLView

from apiUtils.query import Query
from apiUtils.mutation import Mutation
from flask_socketio import SocketIO, emit, join_room, leave_room
from flask_cors import CORS


basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
# this is the simplest Cors solution - it will enable All paths and All origins
CORS(app)
# for something more fine grained use
# CORS(app, resources={r"/api/*": {"origins": "*"}})

app.debug = True


app.config["SECRET_KEY"] = "secret!"
socketio = SocketIO(app, cors_allowed_origins="*")


schema = graphene.Schema(query=Query, mutation=Mutation)

app.add_url_rule(
    "/graphql",
    view_func=GraphQLView.as_view(
        "graphql", schema=schema, graphiql=True  # for having the GraphiQL interface
    ),
)


@app.route("/")
def index():
    return "<p> Hello World</p>"


# @socketio.on('join')
# def on_join(data):
#     username = data['username']
#     room = data['room']
#     join_room(room)
#     send(username + ' has entered the room.', room=room)


@socketio.on("connect")
def test_connect():
    print("A client has connected")


@socketio.on("disconnect")
def test_disconnect():
    print("One client disconnected")


if __name__ == "__main__":
    socketio.run(app)
    # app.run()
