import graphene
import conduit.apps.schema

class Query(conduit.apps.schema.Query, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query)