# To-Do List Application with Tkinter and MongoDB
A simple, user-friendly To-Do List desktop application built with Python's Tkinter GUI toolkit and MongoDB for persistent task storage. The app allows users to add, edit, mark complete, and delete tasks, with task status and timestamps tracked and stored in a MongoDB database.

# Project Description
This To-Do List application provides an intuitive interface to manage daily tasks. It integrates Python’s Tkinter for the graphical interface and MongoDB for data persistence, enabling CRUD (Create, Read, Update, Delete) operations on tasks stored in a local MongoDB instance.

# Features
Add Tasks: Enter a new task and save it to the database with a timestamp.

Edit Tasks: Modify existing task text through a popup dialog.

Mark Complete: Update task status to "Complete" along with completion timestamp.

Delete Tasks: Remove tasks permanently from the database.

Task Listing: View all tasks with their ID, description, creation date, completion date, and status in a sortable tree view.

Error Handling: Friendly error messages and warnings for invalid operations.

Clean UI: Simple and visually appealing layout with color-coded buttons and styled tree view.

# Technologies Used
Python 3.x

Tkinter — for GUI components.

pymongo — to connect and interact with MongoDB.

MongoDB — NoSQL database for storing tasks.

bson — to handle MongoDB ObjectIds.

datetime — for timestamping tasks.

# Installation & Setup
1.Install Python 3
Download and install from python.org.

2.Install MongoDB
Download and install from mongodb.com.
Make sure MongoDB server is running locally on the default port.

3.Install Required Python Packages
Run this command in your terminal or command prompt:
![Screenshot 2025-06-06 083749](https://github.com/user-attachments/assets/d59d7e29-30b2-4248-b994-ce2df98b6683)

4.Run the Application
Save the source code into a .py file (e.g., todo_app.py) and run:
![Screenshot 2025-06-06 083949](https://github.com/user-attachments/assets/5c868aaf-dd37-40b5-8bbc-c7dccc97dd1c)

# Usage
Add a Task: Type your task in the input box and click "Add Task".

Edit a Task: Select a task from the list and click "Edit Task" to modify it.

Mark Complete: Select a task and click "Mark Complete" to mark it done.

Delete a Task: Select a task and click "Delete Task" to remove it.

The task list updates automatically to reflect changes.

# Code Structure Overview
TaskDatabase Class: Handles all MongoDB interactions (CRUD operations).

ToDoApp Class: Manages the Tkinter GUI, user interactions, and updates the UI.

Main function: Initializes database connection, runs the Tkinter main loop, and closes DB connection on exit.

# Screenshots
![Screenshot 2025-06-06 084241](https://github.com/user-attachments/assets/0d9bff28-5764-414f-a156-bbd8f3fa6a38)
![Screenshot 2025-06-06 084327](https://github.com/user-attachments/assets/37f9d487-3ef8-43ee-be51-eb1df2f13631)
![Screenshot 2025-06-06 084347](https://github.com/user-attachments/assets/bddde559-9744-4ed5-ac77-a350fcd19d79)
![Screenshot 2025-06-06 084413](https://github.com/user-attachments/assets/abebf82c-8f7d-4fe7-9f3e-3191c7d32d98)
![Screenshot 2025-06-06 084437](https://github.com/user-attachments/assets/b0e6a4c2-ef19-45e1-9de0-27d0404cf643)
![Screenshot 2025-06-06 084509](https://github.com/user-attachments/assets/ed789455-b6cb-42c3-8e88-41b7ed7009b7)


# Future Improvements
User authentication for multiple users.

Due dates and task priorities.

Task filtering and search functionality.

Sync with online MongoDB or cloud database.

Export tasks to CSV or PDF reports.

# License
This project is open-source and free to use for educational and personal purposes.
