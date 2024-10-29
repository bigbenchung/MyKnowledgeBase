from poe_api_wrapper import AsyncPoeApi
import asyncio
import json
from sys import argv

async def chat(name: str, bot: str, message: str):
    tokens = json.load(open(r".\Homework\MSBD5018\group_project\resources\tokens.json", "r"))
    client = await AsyncPoeApi(tokens=tokens).create()
    full_response = []

    async for chunk in client.send_message(bot=bot, message=message):
        if isinstance(chunk, dict) and 'response' in chunk:
            full_response.append(str(chunk['response']))
    
    # Write only once after collecting all chunks
    if full_response:  # Check if we have any response
        complete_response = ''.join(full_response).replace(',', '.').replace('\n', '')
        with open(r".\Homework\MSBD5018\group_project\responses\experiment.csv", "a", encoding="utf-8") as file:
            file.write(f"{name},{complete_response}\n")

if __name__ == "__main__":
    asyncio.run(chat(name="", bot="gpt3_5", message="hello"))