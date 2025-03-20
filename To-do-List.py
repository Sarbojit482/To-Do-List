import tkinter as tk
from tkinter import messagebox, ttk
from pymongo import MongoClient
from datetime import datetime
from bson.objectid import ObjectId  # Required to handle MongoDB ObjectId

# Database Connection
class TaskDatabase:
    def __init__(self):
        self.client = MongoClient('mongodb://localhost:27017/')
        self.db = self.client['todo_db']
        self.tasks_collection = self.db['tasks']

    def add_task(self, task_text):
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        task_data = {"task": task_text, "created_at": now, "completed_at": None, "status": "Pending"}
        self.tasks_collection.insert_one(task_data)

    def mark_complete(self, task_id):
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.tasks_collection.update_one({"_id": ObjectId(task_id)}, {"$set": {"status": "Complete", "completed_at": now}})

    def delete_task(self, task_id):
        self.tasks_collection.delete_one({"_id": ObjectId(task_id)})

    def get_all_tasks(self):
        return self.tasks_collection.find()

    def close_connection(self):
        self.client.close()

# GUI Setup
class ToDoApp:
    def __init__(self, root, db):
        self.db = db
        self.root = root
        self.root.title("To-Do List")
        self.root.geometry("700x500")
        self.root.configure(bg="#e0f7fa")
        # self.root.iconbitmap("icons.ico")

        self.create_widgets()
        self.update_task_list()

    def create_widgets(self):
        # Task Entry Frame
        entry_frame = tk.Frame(self.root, bg="#e0f7fa")
        entry_frame.pack(pady=20)

        self.task_entry = tk.Entry(entry_frame, width=50, font=("Arial", 14), bd=2, relief=tk.GROOVE)
        self.task_entry.pack(side=tk.LEFT, padx=10)

        add_button = tk.Button(entry_frame, text="Add Task", command=self.add_task, font=("Arial", 14), bg="#00796b", fg="white", padx=10)
        add_button.pack(side=tk.LEFT)

        # Task Treeview
        columns = ("ID", "Task", "Created At", "Completed At", "Status")
        self.task_tree = ttk.Treeview(self.root, columns=columns, show="headings", height=10)
        for col in columns:
            self.task_tree.heading(col, text=col)
            self.task_tree.column(col, width=140, anchor="center")

        style = ttk.Style()
        style.configure("Treeview.Heading", font=("Arial", 12, "bold"))
        style.configure("Treeview", font=("Arial", 10))
        self.task_tree.pack(pady=20)

        # Buttons Frame
        button_frame = tk.Frame(self.root, bg="#e0f7fa")
        button_frame.pack(pady=10)

        complete_button = tk.Button(button_frame, text="Mark Complete", command=self.mark_complete, font=("Arial", 14), bg="#ff9800", fg="white", padx=10)
        complete_button.grid(row=0, column=0, padx=5)

        delete_button = tk.Button(button_frame, text="Delete Task", command=self.delete_task, font=("Arial", 14), bg="#f44336", fg="white", padx=10)
        delete_button.grid(row=0, column=1, padx=5)

        edit_button = tk.Button(button_frame, text="Edit Task", command=self.edit_task, font=("Arial", 14), bg="#2196f3", fg="white", padx=10)
        edit_button.grid(row=0, column=2, padx=5)

    def add_task(self):
        task_text = self.task_entry.get().strip()
        if not task_text:
            messagebox.showwarning("Warning", "Task cannot be empty!")
            return

        try:
            self.db.add_task(task_text)
            self.task_entry.delete(0, tk.END)
            self.update_task_list()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to add task: {e}")

    def mark_complete(self):
        selected_item = self.task_tree.selection()
        if not selected_item:
            messagebox.showwarning("Warning", "Please select a task to mark as complete!")
            return

        task_id = self.task_tree.item(selected_item)['values'][0]
        try:
            self.db.mark_complete(task_id)
            self.update_task_list()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to mark task as complete: {e}")

    def delete_task(self):
        selected_item = self.task_tree.selection()
        if not selected_item:
            messagebox.showwarning("Warning", "Please select a task to delete!")
            return

        task_id = self.task_tree.item(selected_item)['values'][0]
        confirm = messagebox.askyesno("Confirm", "Are you sure you want to delete this task?")
        if confirm:
            try:
                self.db.delete_task(task_id)
                self.update_task_list()
            except Exception as e:
                messagebox.showerror("Error", f"Failed to delete task: {e}")

    def edit_task(self):
        selected_item = self.task_tree.selection()
        if not selected_item:
            messagebox.showwarning("Warning", "Please select a task to edit!")
            return

        task_id = self.task_tree.item(selected_item)['values'][0]
        current_task_text = self.task_tree.item(selected_item)['values'][1]

        # Open a pop-up dialog for editing
        edit_dialog = tk.Toplevel(self.root)
        edit_dialog.title("Edit Task")
        edit_dialog.geometry("400x150")
        edit_dialog.configure(bg="#e0f7fa")

        tk.Label(edit_dialog, text="Edit Task:", font=("Arial", 12), bg="#e0f7fa").pack(pady=10)
        edit_entry = tk.Entry(edit_dialog, width=40, font=("Arial", 12), bd=2, relief=tk.GROOVE)
        edit_entry.pack(pady=10)
        edit_entry.insert(0, current_task_text)

        def save_edit():
            new_task_text = edit_entry.get().strip()
            if not new_task_text:
                messagebox.showwarning("Warning", "Task cannot be empty!")
                return

            try:
                self.db.tasks_collection.update_one({"_id": ObjectId(task_id)}, {"$set": {"task": new_task_text}})
                self.update_task_list()
                edit_dialog.destroy()
            except Exception as e:
                messagebox.showerror("Error", f"Failed to update task: {e}")

        tk.Button(edit_dialog, text="Save", command=save_edit, font=("Arial", 12), bg="#00796b", fg="white").pack(pady=10)

    def update_task_list(self):
        try:
            tasks = self.db.get_all_tasks()
            self.task_tree.delete(*self.task_tree.get_children())
            for task in tasks:
                self.task_tree.insert("", "end", values=(str(task['_id']), task['task'], task['created_at'], task['completed_at'] if task['completed_at'] else 'N/A', task['status']))
        except Exception as e:
            messagebox.showerror("Error", f"Failed to fetch tasks: {e}")

# Main Execution
def main():
    db = TaskDatabase()
    try:
        root = tk.Tk()
        app = ToDoApp(root, db)
        root.mainloop()
    finally:
        db.close_connection()

if __name__ == "__main__":
    main()