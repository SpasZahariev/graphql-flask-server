import graphene
import json
from datetime import datetime


class User(graphene.ObjectType):
    id = graphene.ID()
    username = graphene.String()
    last_login = graphene.DateTime(required=False)


class Query(graphene.ObjectType):
    users = graphene.List(User, first=graphene.Int())

    # the method name is important
    def resolve_users(self, info, first):
        return [
            User(username="Alice", last_login=datetime.now()),
            User(username="Bob", last_login=datetime.now()),
            User(username="Steven", last_login=datetime.now()),
        ][:first]


class CreateUser(graphene.Mutation):
    class Arguments:
        username = graphene.String()

    user = graphene.Field(User)

    def mutate(self, info, username):
        if info.context.get("is_vip"):
            username = username.upper()
        user = User(username=username)
        return CreateUser(user=user)


class Mutations(graphene.ObjectType):
    create_user = CreateUser.Field()


schema = graphene.Schema(query=Query, mutation=Mutations)


# we query the schema with this object
result = schema.execute(
    """
    mutation createUser {
        createUser(username: "Alice") {
            user {
                username
            }
        }
    }
    """,
    context={"is_vip": False},
)

items = dict(result.data.items())
# print(result.data.items())
print(json.dumps(items, indent=4))

