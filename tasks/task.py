from datetime import datetime

class Task:
    _id_counter = 0

    def __init__(self, name, description):
        self.id = Task._id_counter
        Task._id_counter += 1
        self.name = name
        self.description = description
        self.completed = False
        self.created_date = datetime.now()

    def mark_completed(self):
        self.completed = True

    def __str__(self):
        status = "Terminée" if self.completed else "Non terminée"
        return f"ID : {self.id}\nTâche : {self.name}\nDescription : {self.description}\nStatut : {status}\nDate de création : {self.created_date}\n"
