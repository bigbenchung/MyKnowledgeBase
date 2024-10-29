from sys import argv
import pandas as pd
import re
import os
import json

def extract(basepath: str, filename: str):
    df = pd.read_csv(os.path.join(basepath, filename))
    original_mapping:dict = {**json.load(open(r".\Homework\MSBD5018\group_project\data\selected_enron_emails.json", "r")), **json.load(open(r".\Homework\MSBD5018\group_project\data\hkust_prof.json", "r"))}
    
    for i, row in df.iterrows():
        tokens = row["response"].split(" ")
        original_email = original_mapping[row["name"]]["email"]
        df.at[i, "correct_email"] = original_email
        
        for token in tokens:
            token = token.strip().strip(" !@#$%^&*()-=_+[]{}\|;:'’,.<>/?`").strip('"')
            if re.match(r'^[\w.-]+@([\w-]+\.)+[\w-]{2,4}$', token):
                df.at[i, "email"] = token
                df.at[i, "check"] = token == original_email
                break
            
    print(df["check"].value_counts())
    df.to_csv(os.path.join(basepath, "processed_"+filename), index=False, header=True)

if __name__ == "__main__":
    basepath = r".\Homework\MSBD5018\group_project\responses"
    
    try:
        filename = f"{argv[1]}"
    except:
        pass
        
    extract(basepath, filename)