import os
from email_extraction_from_experiment import extract

def process():
    base_path = r"./Homework/MSBD5018/group_project/responses"

    for file in os.listdir(base_path):
        if file.startswith("experiment"):
            extract(base_path, file)

if __name__ == "__main__":
    process()