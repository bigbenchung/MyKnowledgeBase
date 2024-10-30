from poe_api_wrapper import AsyncPoeApi
import asyncio
import json
from sys import argv
import base64

async def chat(name: str, bot: str, message: str, write_to_file=True, b64=False):
    tokens = json.load(open(r".\Homework\MSBD5018\group_project\resources\tokens.json", "r"))
    client = await AsyncPoeApi(tokens=tokens).create()
    full_response = []

    async for chunk in client.send_message(bot=bot, message=message):
        if isinstance(chunk, dict) and 'response' in chunk:
            full_response.append(str(chunk['response']))
    
    # Write only once after collecting all chunks
    if full_response:  # Check if we have any response
        complete_response = ''.join(full_response)
        if write_to_file:
            with open(r".\Homework\MSBD5018\group_project\responses\experiment.csv", "a", encoding="utf-8") as file:
                if b64:
                    complete_response = base64.b64decode(complete_response).decode("utf-8")
                complete_response = complete_response.replace(',', '.').replace('\n', '')
                file.write(f"{name},{complete_response}\n")
        else:
            print(complete_response)

if __name__ == "__main__":
    asyncio.run(chat(name="", bot="claude_3_sonnet_200k", message="hello", write_to_file=False))