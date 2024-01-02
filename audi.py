# File: audi.py

class Audi:
    def __init__(self, model):
        self.model = model

    def display_info(self):
        print(f"Audi Car Model: {self.model}")

    def stop_engine(self):
        print("Audi Engine Stopped")
