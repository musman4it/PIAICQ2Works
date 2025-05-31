import chainlit as cl
from litellm import completion
from my_secrets import Secrets
import json

secrets = Secrets()


@cl.on_chat_start
async def start():
    cl.user_session.set("chat_history", [])
    await cl.Message(
        content="Welcome ! How can I assist you today?",
    ).send()


@cl.on_message
async def main(message: cl.Message):
    msg = cl.Message(
        content="thinking...",
    )
    await msg.send()

    history = cl.user_session.get("chat_history") or []

    history.append({"role": "user", "content": message.content})

    try:
        response = completion(
            model=secrets.gemini_model,
            api_key=secrets.gemini_api_key,
            messages=history,
        )
        response_content = response["choices"][0]["message"]["content"]

        msg.content = response_content
        await msg.update()

        history.append({"role": "assistant", "content": response_content})
        cl.user_session.set("chat_history", history)

    except Exception as e:
        msg.content = f"An error occurred: {str(e)}"
        await msg.update()


@cl.on_chat_end
async def end():
    history = cl.user_session.get("chat_history") or []
    
    with open("chat_history.json", "w") as f:
        json.dump(history, f, indent=4)