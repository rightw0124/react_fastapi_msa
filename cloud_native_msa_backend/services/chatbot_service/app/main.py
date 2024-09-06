#PORT = 8002
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from pymongo import MongoClient
from app.db.mongo_client import get_mongo_client
from app.schema.chatbot_schema import ChatMessage
import httpx

app = FastAPI()

# Rasa server URL
RASA_SERVER_URL = "http://rasa:5005/webhooks/rest/webhook" # http://localhost:5005/ ?

# MongoDB client
mongo_client = get_mongo_client()
chat_db = mongo_client.chatbot_database

@app.websocket("/ws/chat")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_text()
            user_message = ChatMessage(text=data)
            
            # Log user message to MongoDB
            chat_db.messages.insert_one({"message": user_message.dict(), "sender": "user"})
            
            # Send message to Rasa server
            async with httpx.AsyncClient() as client:
                response = await client.post(RASA_SERVER_URL, json={"sender": "user", "message": user_message.text})
                bot_responses = response.json()

            # Log bot response to MongoDB and send it back to the client
            for bot_response in bot_responses:
                chat_db.messages.insert_one({"message": bot_response, "sender": "bot"})
                await websocket.send_text(bot_response.get("text", ""))
    
    except WebSocketDisconnect:
        print("WebSocket connection closed")


# MongoDB Initialization route (Optional)
@app.on_event("startup")
async def startup_db_client():
    mongo_client = get_mongo_client()
    print("Connected to MongoDB!")
