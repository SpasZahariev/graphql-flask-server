from flask import Flask, render_template
import os
import graphene
from flask_graphql import GraphQLView


from flask_socketio import SocketIO, emit, join_room, leave_room
from flask_cors import CORS

import logging


basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
# this is the simplest Cors solution - it will enable All paths and All origins
CORS(app)
# for something more fine grained use
# CORS(app, resources={r"/api/*": {"origins": "*"}})

app.debug = True


app.config["SECRET_KEY"] = "secret!"
socketio = SocketIO(app, cors_allowed_origins="*")


# this is the only way to avoid putting everything in the main module
# it is not pretty but this is the best way to do this in python
import apiUtils.socket_methods
from apiUtils.query import Query
from apiUtils.mutation import Mutation

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

##to print to gunicorn logger
gunicorn_error_logger = logging.getLogger("gunicorn.error")
app.logger.handlers.extend(gunicorn_error_logger.handlers)
app.logger.setLevel(logging.DEBUG)
app.logger.debug("this will show in the log  2!")
# app.logger.debug("what is __name__ : ", __name__)

# in windows you can do: SET PORT=5600
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    socketio.run(app, host="0.0.0.0", port=port)
    # app.run()
