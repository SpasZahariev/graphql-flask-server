from flask import Flask, render_template
import os
import graphene
from flask_graphql import GraphQLView

from apiUtils.query import Query
from apiUtils.mutation import Mutation
from flask_socketio import SocketIO, emit
from flask_cors import CORS


basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
# this is the simplest Cors solution - it will enable All paths and All origins
CORS(app)
# for something more fine grained use
# CORS(app, resources={r"/api/*": {"origins": "*"}})

app.debug = True


app.config["SECRET_KEY"] = "secret!"
socketio = SocketIO(app)


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


if __name__ == "__main__":
    socketio.run(app)
    # app.run()
