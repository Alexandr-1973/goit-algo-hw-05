import sys


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
    pass

def display_log_counts(counts: dict):
    pass


def main():
    print(filter_logs_by_level(load_logs("log.txt"), "INFO"))
    # print(sys.argv)

main()