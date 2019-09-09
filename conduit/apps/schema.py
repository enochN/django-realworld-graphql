import graphene
from graphene_django.types import DjangoObjectType, ObjectType
from conduit.apps.articles.models import Article, Comment, Tag
from conduit.apps.profiles.models import Profile
from conduit.apps.authentication.models import User

class ArticleType(DjangoObjectType):
    class Meta:
        model = Article

class CommentType(DjangoObjectType):
    class Meta:
        model = Comment

class TagType(DjangoObjectType):
    class Meta:
        model = Tag

class ProfileType(DjangoObjectType):
    class Meta:
        model = Profile

class UserType(DjangoObjectType):
    class Meta:
        model = User


class Query(ObjectType):
    article = graphene.Field(ArticleType, slug=graphene.String())
    comment = graphene.Field(CommentType, id=graphene.Int())
    tag = graphene.Field(TagType, id=graphene.Int())
    profile = graphene.Field(ProfileType, id=graphene.Int())
    articles = graphene.List(ArticleType)
    comments = graphene.List(CommentType)
    tags = graphene.List(TagType)
    profiles = graphene.List(ProfileType)

    def resolve_article(self, info, **kwargs):
        slug = kwargs.get('slug')

        if slug is not None:
            return Article.objects.get(slug=slug)

        return None

    def resolve_articles(self, info, *args, **kwargs):
        return Article.objects.all()

    def resolve_comment(self, info, *args, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Comment.objects.get(pk=id)

        return None

class ArticleInput(graphene.InputObjectType):
    id = graphene.ID()
    slug = graphene.String()


schema = graphene.Schema(query=Query)