from datetime import datetime

class Task:
    _id_counter = 0

    def __init__(self, name, description):
        """
        Initializes a Task object with a unique ID, name, description, completion status (False), and creation date (current datetime).

        Args:
            name (str): The name of the task.
            description (str): The description of the task.
        """
        self.id = Task._id_counter
        Task._id_counter += 1
        self.name = name
        self.description = description
        self.completed = False
        self.created_date = datetime.now()

    def mark_completed(self):
        """
        Marks the task as completed by setting the completion status to True.
        """
        self.completed = True

    def __str__(self):
        """
        Returns a string representation of the task, including its ID, name, description, completion status, and creation date.

        Returns:
            str: A formatted string representation of the task.
        """
        status = "Terminée" if self.completed else "Non terminée"
        return f"ID : {self.id}\nTâche : {self.name}\nDescription : {self.description}\nStatut : {status}\nDate de création : {self.created_date}\n"
