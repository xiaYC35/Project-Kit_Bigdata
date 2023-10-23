
import tkinter as tk
from tkinter import messagebox
from tasks.tasklist import TaskList
from tasks.main_gui import use_gui, TaskManagerGUI

class TestCodeUnderTest:

    def setup_method(self):
        self.root = tk.Tk()
        self.root.attributes('-topmost', 1)
        self.root.withdraw()
        self.task_list = TaskList()
        self.gui = TaskManagerGUI(self.root, self.task_list)

    def teardown_method(self):
        self.root.update()
        self.root.destroy()

    def test_gui_creation(self):
        assert self.gui.root == self.root
        assert self.gui.task_list == self.task_list

    def test_add_task(self):
        self.gui.input_name.insert(tk.END, "Task 1")
        self.gui.input_description.insert(tk.END, "Description 1")
        self.gui.add_task()
        assert len(self.task_list.tasks) == 1
        assert self.task_list.tasks[0].name == "Task 1"
        assert self.task_list.tasks[0].description == "Description 1"
        assert self.gui.task_listbox.get(0) == "Task 1"


    def test_select_task(self):
        self.gui.input_name.insert(tk.END, "Task 1")
        self.gui.input_description.insert(tk.END, "Description 1")
        self.gui.add_task()
        self.gui.input_name.delete(0, tk.END)
        self.gui.input_description.delete(0, tk.END)
        self.gui.input_name.insert(tk.END, "Task 2")
        self.gui.input_description.insert(tk.END, "Description 2")
        self.gui.add_task()
        self.gui.task_listbox.selection_set(1)
        self.gui.display_selected_task(None)
        assert self.gui.selected_task == self.task_list.tasks[1]
        assert self.gui.details_label.cget("text") == "Détails de la Tâche 'Task 2'"
        expected_details_static = "ID : 2\nTâche : Task 2\nDescription : Description 2\nStatut : Non terminée\n"
        assert self.gui.details_label.cget("text") == "Détails de la Tâche 'Task 2'"
        details_text = self.gui.details_text.get(1.0, tk.END)
        assert details_text.startswith(expected_details_static)



