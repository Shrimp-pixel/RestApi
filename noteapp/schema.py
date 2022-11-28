import graphene
from graphene import ObjectType
from graphene_django import DjangoObjectType

from userapp.models import User
from todo.models import Project, Todo


class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = '__all__'


class ProjectType(DjangoObjectType):
    class Meta:
        model = Project
        fields = '__all__'


class TodoType(DjangoObjectType):
    class Meta:
        model = Todo
        fields = '__all__'


class Query(ObjectType):
    user_by_id = graphene.List(UserType, id=graphene.Int(required=False))

    def resolve_user_by_id(root, info, id=None):
        if id:
            return User.objects.get(id=id)
        return User.objects.all()

    all_users = graphene.List(UserType)

    def resolve_all_users(root, info):
        return User.objects.all()

    all_projects = graphene.List(ProjectType)

    def resolve_all_projects(root, info):
        return Project.objects.all()

    all_todo = graphene.List(TodoType)

    def resolve_all_todo(root, info):
        return Todo.objects.all()

    todo_by_user = graphene.List(TodoType, first_name=graphene.String(required=False))

    def resolve_todo_by_user(root, info, first_name=None):
        if first_name:
            return Todo.objects.filter(creator__first_name=first_name)
        return Todo.objects.all()


class UserUpdaterMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
        first_name = graphene.String()

    user = graphene.Field(UserType)

    @classmethod
    def mutate(cls, root, info, **kwargs):
        user = User.objects.get(id=kwargs.get('id'))
        user.first_name = kwargs.get('first_name')
        user.save()
        return UserUpdaterMutation(user=user)


class UserCreateMutation(graphene.Mutation):
    class Arguments:
        username = graphene.String()
        first_name = graphene.String()
        last_name = graphene.String()
        email = graphene.String()

    user = graphene.Field(UserType)

    @classmethod
    def mutate(cls, root, info, **kwargs):
        user = User.objects.create(**kwargs)
        return UserCreateMutation(user=user)


class UserDeleteMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID()

    user = graphene.Field(UserType)

    @classmethod
    def mutate(cls, root, info, **kwargs):
        user = User.objects.get(id=kwargs.get('id')).delete()
        return UserDeleteMutation(users=User.objects.all())


class Mutation(ObjectType):
    update_user = UserUpdaterMutation.Field()
    create_user = UserCreateMutation.Field()
    delete_user = UserDeleteMutation.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
