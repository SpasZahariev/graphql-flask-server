# it is not pretty but this is the best way to do this in python
try:
    from __main__ import socketio
except ImportError:
    from main import socketio

import json


# @socketio.on("connect")
# def handle_connect():
#     print("A client has connected")


# @socketio.on("disconnect")
# def handle_disconnect():
#     print("One client disconnected")


def emit_usernames(usernames):
    socketio.emit("usernames_channel", json.dumps(usernames, indent=4))


def emit_playlist(serialized_songs):
    socketio.emit("playlist_channel", json.dumps(serialized_songs, indent=4))

