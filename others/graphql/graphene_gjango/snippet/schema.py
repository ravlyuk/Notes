import graphene
from graphene_django.rest_framework.mutation import SerializerMutation

from .graphene_django_cui_mutations import UpdatePersonMutationCud, PatchPersonMutationCud, CreatePersonMutationCud, \
    DeletePersonMutationCud
from .graphene_django_mutations import PersonType, UpdatePersonMutation, RemovePersonMutation, CreatePersonMutation
from .models import Person
from .serializers import PersonSerializer


# https://www.howtographql.com/graphql-python/3-mutations/

class MyAwesomeMutation(SerializerMutation):
    class Meta:
        serializer_class = PersonSerializer
        model_operations = ['create', 'update']
        lookup_field = 'id'


class Mutations(graphene.ObjectType):
    # graphene_django_mutations
    create_person = CreatePersonMutation.Field()
    update_person = UpdatePersonMutation.Field()
    delete_person = RemovePersonMutation.Field()

    # graphene_django_cui_mutations
    update_person_cui = UpdatePersonMutationCud.Field()
    patch_person_cui = PatchPersonMutationCud.Field()
    create_person_cui = CreatePersonMutationCud.Field()
    delete_person_cui = DeletePersonMutationCud.Field()


class Query(graphene.ObjectType):
    persons = graphene.List(PersonType)

    def resolve_persons(self, info, **kwargs):
        return Person.objects.all()


schema = graphene.Schema(query=Query, mutation=Mutations, auto_camelcase=False)
