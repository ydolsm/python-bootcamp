"""
Build a Simple To-Do List with Flask

In this exercise, you will create a simple To-Do list application where users can:
    Add tasks.
    Mark tasks as completed.
    Delete tasks.
    View the current list of tasks.

You will use Flask to build the application. The data will be stored in-memory (no need for a database).
 Tasks will persist for the duration of the session, but once the server is restarted, all tasks will be lost.

Requirements:
    Flask: You will use Flask to build the web application.
    HTML and Forms: Use HTML forms to handle task input and task completion.

Step 1: Setup Flask Application
-------------------------------
Create a Flask app named app.py:

    Initialize a Flask app and set up basic routes (/ for the homepage, /add for adding tasks, /delete for deleting tasks).
    Use an in-memory list to store the tasks (e.g., tasks = []).

Step 2: Display Tasks
---------------------
On the home page, display the current list of tasks in a list format.

    Each task should have a checkbox to mark it as completed.
    Each task should also have a delete button to remove it from the list.

Step 3: Add a New Task
----------------------
Create a form where users can add a new task. When the form is submitted, add the task to the list.

    The form should take a single input (task name).
    After adding the task, redirect the user back to the homepage.

Step 4: Mark Task as Completed
------------------------------
Next to each task, provide a button or checkbox that lets the user mark a task as completed.

    When the checkbox or button is clicked, update the task in the list to mark it as completed.

Step 5: Delete a Task
---------------------
Each task should have a button to delete it. When clicked, remove the task from the list.

Step 6: Basic Styling (Optional)
--------------------------------
Add some simple styling to make the app look clean. You can use an external CSS file or inline styles.

Additional Features (Optional):
-------------------------------
    Allow the user to filter tasks (e.g., show only completed tasks, or show only uncompleted tasks).
    Persist the tasks to a file (e.g., a JSON file) so that tasks are saved even when the app restarts.
"""