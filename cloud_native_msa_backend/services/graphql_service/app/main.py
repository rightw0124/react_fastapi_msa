
from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter
from app.schema.graphql_schema import schema  # Import the schema from graphql_schema.py

# Create a FastAPI instance
app = FastAPI()

# Create a GraphQL router using Strawberry
graphql_app = GraphQLRouter(schema)

# Include the GraphQL router with the prefix "/graphql"
app.include_router(graphql_app, prefix="/graphql")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
