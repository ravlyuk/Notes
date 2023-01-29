import graphene
from graphene_django import DjangoObjectType

from .models import Person


class PersonType(DjangoObjectType):
    class Meta:
        model = Person


class CreatePersonMutation(graphene.Mutation):
    class Arguments:
        # The input arguments for this mutation
        first_name = graphene.String(required=True, description="First name")
        last_name = graphene.String(required=True)
        birth_date = graphene.Date()
        phone = graphene.String()
        email = graphene.String()
        city = graphene.String()
        post_code = graphene.Int()
        profession = graphene.String()

    # The class attributes define the response of the mutation
    person = graphene.Field(PersonType)

    @classmethod
    def mutate(cls, root, info, first_name, last_name, birth_date, phone, email, city, post_code, profession):
        person = Person(
            first_name=first_name,
            last_name=last_name,
            birth_date=birth_date,
            phone=phone,
            email=email,
            city=city,
            post_code=post_code,
            profession=profession,
        )
        person.save()
        # Notice we return an instance of this mutation
        return CreatePersonMutation(person=person)


class UpdatePersonMutation(graphene.Mutation):
    class Arguments:
        # The input arguments for this mutation
        id = graphene.ID()
        first_name = graphene.String(required=True, description="First name")
        last_name = graphene.String(required=True)
        birth_date = graphene.Date()
        phone = graphene.String()
        email = graphene.String()
        city = graphene.String()
        post_code = graphene.Int()
        profession = graphene.String()

    # The class attributes define the response of the mutation
    person = graphene.Field(PersonType)

    @classmethod
    def mutate(cls, root, info, first_name, last_name, birth_date, phone, email, city, post_code, profession, id):
        person = Person.objects.get(pk=id)
        person.first_name = first_name
        person.last_name = last_name
        person.birth_date = birth_date
        person.phone = phone
        person.email = email
        person.city = city
        person.post_code = post_code
        person.profession = profession
        person.save()
        # Notice we return an instance of this mutation
        return UpdatePersonMutation(person=person)


class RemovePersonMutation(graphene.Mutation):
    deleted = graphene.Boolean(default_value=False)

    class Arguments:
        # The input arguments for this mutation
        id = graphene.ID()

    # The class attributes define the response of the mutation
    person = graphene.Field(PersonType)

    @classmethod
    def mutate(cls, root, info, id):
        person = Person.objects.get(pk=id)
        person.delete()
        person.deleted = True
        # Notice we return an instance of this mutation
        # return RemovePersonMutation(person=person)
        return person
