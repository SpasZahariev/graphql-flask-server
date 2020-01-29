from flask import Flask
import os
import graphene
from flask_graphql import GraphQLView

from apiUtils.query import Query
from apiUtils.mutation import Mutation

# Imports

# app initialization
basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.debug = True

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
