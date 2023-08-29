import tkinter as tk
from tkinter import messagebox

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")

        self.task_list = []

        # Create UI elements
        self.task_entry = tk.Entry(root)
        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.task_listbox = tk.Listbox(root)
        self.update_button = tk.Button(root, text="Update Task", command=self.update_task)
        self.delete_button = tk.Button(root, text="Delete Task", command=self.delete_task)

        # Place UI elements using grid layout manager
        self.task_entry.grid(row=0, column=0, padx=10, pady=10)
        self.add_button.grid(row=0, column=1, padx=10, pady=10)
        self.task_listbox.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
        self.update_button.grid(row=2, column=0, padx=10, pady=10)
        self.delete_button.grid(row=2, column=1, padx=10, pady=10)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.task_list.append(task)
            self.update_task_listbox()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Task cannot be empty.")

    def update_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            task = self.task_entry.get()
            if task:
                index = selected_index[0]
                self.task_list[index] = task
                self.update_task_listbox()
                self.task_entry.delete(0, tk.END)
            else:
                messagebox.showwarning("Warning", "Task cannot be empty.")

    def delete_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            del self.task_list[index]
            self.update_task_listbox()

    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.task_list:
            self.task_listbox.insert(tk.END, task)

def main():
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
