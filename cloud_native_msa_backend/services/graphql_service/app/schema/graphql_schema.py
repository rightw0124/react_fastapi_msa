import strawberry

# Define a basic User type for demonstration
@strawberry.type
class User:
    id: int
    name: str
    email: str

# Define a Query type with basic fields
@strawberry.type
class Query:
    @strawberry.field
    def hello(self) -> str:
        return "Hello from the GraphQL Service!"

    @strawberry.field
    def get_user(self, id: int) -> User:
        # In a real application, you would fetch this from your database or another service
        return User(id=id, name="John Doe", email="john.doe@example.com")

# Create the schema
schema = strawberry.Schema(query=Query)
