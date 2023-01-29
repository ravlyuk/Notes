from graphene_django import DjangoObjectType
from graphene_django_cud.mutations import DjangoUpdateMutation, DjangoPatchMutation, DjangoCreateMutation, \
    DjangoDeleteMutation

from .models import Person


class PersonNode(DjangoObjectType):
    class Meta:
        model = Person


class CreatePersonMutationCud(DjangoCreateMutation):
    class Meta:
        model = Person


class UpdatePersonMutationCud(DjangoUpdateMutation):
    class Meta:
        model = Person


class PatchPersonMutationCud(DjangoPatchMutation):
    class Meta:
        model = Person


class DeletePersonMutationCud(DjangoDeleteMutation):
    class Meta:
        model = Person
