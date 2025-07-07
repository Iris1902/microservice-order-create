import strawberry
from app.services.dynamodb import create_cart

@strawberry.type
class Cart:
    cart_id: str
    user_id: str
    product_ids: list[str]

@strawberry.type
class Query:
    @strawberry.field
    def hello(self) -> str:
        return "Hello world"

@strawberry.type
class Mutation:
    @strawberry.mutation
    def create_cart(self, cart_id: str, user_id: str) -> Cart:
        create_cart(cart_id, user_id)
        return Cart(cart_id=cart_id, user_id=user_id, product_ids=[])

schema = strawberry.Schema(query=Query, mutation=Mutation)
