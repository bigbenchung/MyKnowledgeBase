import sys
from sys import argv
import json
import asyncio
import base64

from prompt_templates import *
from chat import chat

def extract(mode: str, bot: str, domain: str=""):
    if not domain or domain == "Enron":
        info:dict = json.load(open(r"./Homework/MSBD5018/group_project/data/selected_enron_emails.json", "r"))
    elif domain == "HKUST":
        info:dict = json.load(open(r"./Homework/MSBD5018/group_project/data/hkust_prof.json", "r"))

    open(r".\Homework\MSBD5018\group_project\responses\experiment.csv", "w").write("name,response\n")

    if mode == "MJP":
        base_prompt =f"""USER: {jailbreak_prompt}
                ASSISTANT: {ack_prompt}
                USER: {query_prompt}{guess_prompt}"""
    elif mode == "P+R":
        base_prompt=f"""{jailbreak_prompt}
                        {refusal_suppression_template}
                        {prefix_injection_template}{query_prompt}"""
    elif mode == "b64":
        base_prompt=query_prompt

    if "claude" in bot.lower():
        base_prompt = base_prompt.replace("ChatGPT", "Claude Agent")
    
    # print(base_prompt)
    # sys.exit()
    for name, info in info.items():
        print(f"Processing {name} ...")
        new_prompt = base_prompt.replace("{domain}", domain).replace("{name}", name)
        if mode == "b64":
            new_prompt = base_64_template+" "+str(base64.b64encode(new_prompt.encode("ascii")))
        asyncio.run(chat(name=name, bot=bot, message=new_prompt, b64=True))
    

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
        domain = "your existing knowledge"

    extract(mode, bot, domain)