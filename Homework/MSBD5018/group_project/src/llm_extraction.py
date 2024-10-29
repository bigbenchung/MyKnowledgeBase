import sys
from sys import argv
import json
import asyncio
import os

from prompt_templates import *
from chat import chat

def extract(mode: str, bot: str, domain: str=""):

    enron_info:dict = json.load(open(r"./Homework/MSBD5018/group_project/data/selected_enron_emails.json", "r"))

    open(r".\Homework\MSBD5018\group_project\responses\experiment.csv", "w").write("name,response\n")

    if mode == "MJP":
        base_prompt =f"""USER: {jailbreak_prompt}
                ASSISTANT: {ack_prompt}
                USER: {query_prompt}{guess_prompt}"""

    for name, info in enron_info.items():
        print(f"Processing {name} ...")
        new_prompt = base_prompt.replace("{domain}", domain).replace("{name}", name)
        asyncio.run(chat(name=name, bot=bot, message=new_prompt))
    

if __name__ == "__main__":
    try:
        mode = argv[1]
    except:
        mode = "MJP"
    
    try:
        bot = argv[2]
    except:
        bot = "beaver"
        
    try:
        domain = argv[3]
    except:
        domain = "Enron"

    extract(mode, bot, domain)