import graphene
from graphene_django import DjangoObjectType
from graphene_django.rest_framework.mutation import SerializerMutation

from .serializers import PersonSerializer
from .models import Person


class SnippetType(DjangoObjectType):
    class Meta:
        model = Person


class AwesomeModelMutation(SerializerMutation):
    class Meta:
        serializer_class = PersonSerializer
        model_operations = ['create', 'update']
        lookup_field = 'id'


class SnippetMutation(graphene.Mutation):
    class Arguments:
        # The input arguments for this mutation
        id = graphene.ID()
        title = graphene.String(required=True)
        body = graphene.String(required=True)

    # The class attributes define the response of the mutation
    person = graphene.Field(SnippetType)

    @classmethod
    def mutate(cls, root, info, title, body, id):
        person = Person.objects.get(pk=id)
        person.title = title
        person.body = body
        person.save()
        # Notice we return an instance of this mutation
        return SnippetMutation(person=person)


class Mutations(graphene.ObjectType):
    update_snippet = SnippetMutation.Field()


class Query(graphene.ObjectType):
    all_snippets = graphene.List(SnippetType)

    def resolve_all_snippets(self, info, **kwargs):
        return Person.objects.all()


schema = graphene.Schema(query=Query, mutation=Mutations, auto_camelcase=False)
