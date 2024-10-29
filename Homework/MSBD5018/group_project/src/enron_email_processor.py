import pandas as pd
import re
import json

def preprocess_enron_email():
    
    df = pd.read_csv(r"./Homework/MSBD5018/group_project/resources/emails.csv")
    # Extract useful elements from each row to form name-email pair in json format
    
    info = dict()

    for i, row in df.iterrows():
        msg_elements = row["message"].split("\n")
        from_name, from_email = "", ""

        for msg_element in msg_elements:
            # Determine if it's needed info by element header
            if not from_email and msg_element.startswith("From:"):
                from_email = "".join(msg_element.split(":")[1:]).strip().lower().replace(r'"', "")
            elif not from_name and  msg_element.startswith("X-From:"):
                # Avoid mismatching name / email
                if not "," in msg_element and not"@" in msg_element:
                    from_name = re.sub(r'<.*?>', '', "".join(msg_element.split(":")[1:])).strip().lower().replace(r'"', "")
        
        # Only take first found value for each person
        if from_name and from_email and from_name not in info.keys():
            info[from_name] = {"email": from_email}

    print(len(info))
    json.dump(info, open(r"./Homework/MSBD5018/group_project/data/all_enron_emails.json", "w"))

def manual_select_email(counter=150):
    info = json.load(open(r"./Homework/MSBD5018/group_project/data/all_enron_emails.json", "r"))
    output = dict()

    for k, v in info.items():
        print(f"name={k}\nemail={v}")
        keep_indicator = input("Input n to discard the name-email pair:")

        if keep_indicator == "n":
            continue

        output[k] = v
        counter -= 1
        if counter == 0:
            break
    
    print(len(output))
    json.dump(output, open(r"./Homework/MSBD5018/group_project/data/selected_enron_emails.json", "w"))
        
if __name__ == "__main__":
    # preprocess_enron_email()
    manual_select_email()