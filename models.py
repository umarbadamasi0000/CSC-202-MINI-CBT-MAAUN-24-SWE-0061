from datetime import datetime

class Patient:
    def __init__(self, name, age, problem):
        self.name = name
        self.age = age
        self.problem = problem
        self.time_registered = datetime.now()

    def get_details(self):
        return f"{self.name} ({self.age}) - {self.problem} - Registered at {self.time_registered.strftime('%Y-%m-%d %H:%M:%S')}"