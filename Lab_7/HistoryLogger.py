from typing import List, Dict

class HistoryLogger:

    def __init__(self):
        self.history: List[Dict[str, str]] = []

    def log(self, command: str, result: str) -> None:
        self.history.append({"command": command, "result": result})

    def show_history(self) -> None:
        for record in self.history:
            print(f"Команда: {record['command']}")
            print(f"Результат: {record['result']}")
