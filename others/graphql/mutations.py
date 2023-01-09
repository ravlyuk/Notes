import json
from datetime import datetime

import graphene


class User(graphene.ObjectType):
    id = graphene.ID()
    username = graphene.String()
    last_login = graphene.DateTime()


class Query(graphene.ObjectType):
    users = graphene.List(User, first=graphene.Int())

    def resolve_users(self, info, first):
        result = [
            User(username='Alice', last_login=datetime.now()),
            User(username='Bob', last_login=datetime.now()),
            User(username='Steven', last_login=datetime.now()),
        ]
        return result[:first]


class CreateUser(graphene.Mutation):
    class Arguments:
        username = graphene.String()

    user = graphene.Field(User)

    def mutate(self, info, username):
        if info.context.get('is_vip'):
            username = username.upper()
        user = User(username=username)
        return CreateUser(user=user)


class Mutations(graphene.ObjectType):
    create_user = CreateUser.Field()


schema = graphene.Schema(query=Query, mutation=Mutations, auto_camelcase=False)

result = schema.execute(
    '''
    mutation create_user($username: String) {
        create_user(username: $username){
            user {
                username
            } 
        }
    }
    ''',
    variable_values={'username': 'Yevhenii'},
    context={'is_vip': True}
)

items = dict(result.data.items())
print(json.dumps(items, indent=4))
