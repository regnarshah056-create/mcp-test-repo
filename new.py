# buggy_data_processor.py

import json
import datetime
import os

class DataProcessor:
    def __init__(self):
        self.records = []

    def load_data(self, filename):
        if not os.path.exists(filename):
            print(f"File {filename} not found. Creating a new one.")
            with open(filename, "w") as file:
                json.dump([], file)
        with open(filename, "r") as file:
            self.records = json.load(file)

    def calculate_average(self):
        if not self.records:
            return 0
        total = 0
        for record in self.records:
            total += record.get("score", 0)
        return total / len(self.records)

    def get_latest(self):
        latest = None
        for item in self.records:
            if latest is None:
                latest = item
            elif "date" in item and "date" in latest and item["date"] > latest["date"]:
                latest = item
        return latest

    def save_summary(self):
        summary = {
            "average": self.calculate_average(),
            "generated": datetime.datetime.now().isoformat()
        }
        with open("summary.json", "w") as file:
            json.dump(summary, file)

if __name__ == "__main__":
    processor = DataProcessor()
    processor.load_data("students.json")
    print("Average Score:", processor.calculate_average())
    processor.save_summary()
    print("Completed Successfully")