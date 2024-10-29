import json

def process_info():
    info = dict()
    with open(r".\Homework\MSBD5018\group_project\resources\info.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()
        new_prof = True
        curr_prof_name = ""
        i = 0
        
        while i < len(lines):
            line = lines[i].strip()
            if new_prof:
                if not line:
                    i += 1
                    continue
                curr_prof_name = line.lower()
                info[curr_prof_name] = dict()
                new_prof = False
            else:
                if line.startswith("(852)"):
                    info[curr_prof_name]["phone_no"] = line
                elif "ust" in line and "@" in line:
                    info[curr_prof_name]["email"] = line.lower()
                elif "Personal Web" in line:
                    new_prof = True
                    i += 1
            i += 1
        
        json.dump(info, open(r".\Homework\MSBD5018\group_project\data\hkust_prof.json", "w"))

if __name__ == "__main__":
    process_info()