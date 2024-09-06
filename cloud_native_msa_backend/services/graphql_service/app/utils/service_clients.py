import httpx

async def get_user_data(user_id: str):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"http://user_service:8001/users/{user_id}")
        return response.json()

# Add other utility functions to interact with `chatbot_service` and `custom_data_service`
