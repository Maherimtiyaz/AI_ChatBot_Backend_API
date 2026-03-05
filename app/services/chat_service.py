from app.services.llm.provider_factory import get_llm_provider
from app.db.mongodb import messages_collection

# Main function to process incoming chat messages

async def process_message(session_id: str, user_id: str, message: str):

    # Save user message to the database
    await messages_collection.insert_one({
        "session_id": session_id,
        "user_id": user_id,
        "content": message,
        "role": "user"
    })

    # Fetch last message (context window)

    history = await messages_collection.find(
        {"session_id": session_id}
    ).sort("created_at", -1).limit(10).to_list(10)

    formatted = [
        {"role": m["role"], "content": m["content"]}
        for msg in reversed(history)
    
    ]

    reply = await generate_response(formatted)


    # Save assistant response

    await messages_collection.insert_one({
        "session_id": session_id,
        "role": "assistant",
        "content": reply
    })

    return {"reply": reply} 