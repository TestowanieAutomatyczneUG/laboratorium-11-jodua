from src.Log import Log
from typing import Optional
import os


class Logger:
    def __init__(self) -> None:
        self.logs = {}

    def add_log(self, new_log: Log) -> Log:
        log = self.logs.get(new_log.id)
        if log:
            raise ValueError("Log already exist")
        self.logs[new_log.id] = new_log

    def get_log(self, id: int) -> Optional[Log]:
        return self.logs.get(id)

    def clear_logs(self) -> None:
        self.logs = {}

    def write_log_file(self, name: str) -> bool:
        with open(f"{name}.log", 'w', newline='') as f:
            for log in self.logs.values():
                f.write(f"{log.id}, {log.text}\n")
        return True

    def import_log_file(self, name: str) -> bool:
        with open(f"{name}.log", 'r', newline='') as f:
            for row in f.readlines():
                log = row.strip('\n').split(',')
                self.add_log(Log(int(log[0]), log[1]))
        return True

    def delete_log_file(self, name: str) -> bool:
        if not os.path.exists(f"{name}.log"):
            raise FileNotFoundError("Log file does not exist")
        os.remove(f"{name}.log")
        return True
