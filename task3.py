import sys
from collections import defaultdict
from colorama import Fore

def parse_log_line(line: str) -> dict:
    log_list=line.split(" ")
    return {"log_date":log_list[0],
            "log_time":log_list[1],
            "log_level":next(filter(lambda x: x.isupper(), log_list)),
            "message":" ".join(log_list[2:])}

def load_logs(file_path: str) -> list:
    logs_list=[]
    try:
        with open(file_path,"r",encoding="utf-8") as file:
            while True:
                line=file.readline()
                if not line:
                    break
                logs_list.append(parse_log_line(line.removesuffix('\n')))
            return logs_list
    except FileNotFoundError:
        print(f"File {file_path} not found")
        return []
    except (OSError, IOError):
        print("File exists but is corrupted or unreadable")
        return []

def filter_logs_by_level(logs: list, level: str) -> list:
    return list(filter(lambda log:log["log_level"]==level, logs))

def count_logs_by_level(logs: list) -> dict:
    count_level_dict=defaultdict(int)
    for log in logs:
        count_level_dict[log["log_level"]]+=1
    return count_level_dict

def display_log_counts(counts: dict, level_value="ERROR"):
    if len(counts):
        print("\nРівень логування | Кількість\n"
              "-----------------|----------")
        for k,v in counts.items():
            print(f"{Fore.RED+k+Fore.RESET if k==level_value else k}{' '*(17 - len(k))}| {v}")
        print(" ")

def main():
    if len(sys.argv)>2:
        level_value=sys.argv[2].upper()
        logs_list=load_logs(sys.argv[1])
        if not logs_list:
            return
        display_log_counts(count_logs_by_level(logs_list),level_value)
        filter_list = filter_logs_by_level(logs_list, level_value)
        if not filter_list:
            print("Level not found")
            return
        print(f"Деталі логів для рівня '{level_value}':")
        for log in filter_logs_by_level(logs_list,level_value):
            print(f"{log["log_date"]} {log["log_time"]} - {log["message"].removeprefix(f"{level_value} ")}")
        print(" ")
    else:
        display_log_counts(count_logs_by_level(load_logs(sys.argv[1])))

main()