import graphene
import graphql_jwt

import links.schema
import users.schema
import education.schema
import workexperience.schema
import skills.schema
import certificates.schema
import languages.schema

class Query(languages.schema.Query, certificates.schema.Query, skills.schema.Query, workexperience.schema.Query, education.schema.Query, users.schema.Query, links.schema.Query, graphene.ObjectType):
    pass

class Mutation(languages.schema.Mutation, certificates.schema.Mutation, skills.schema.Mutation, workexperience.schema.Mutation, education.schema.Mutation, users.schema.Mutation, links.schema.Mutation, graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)