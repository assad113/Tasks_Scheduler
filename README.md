What does it do?

This program uses a simple text file to understand your tasks. For each task, you tell it:

 What the task is called.
 How long it takes.
 If it needs other tasks to finish first.

Here's what the program can do:

1.  Check your task list: It reads your list and finds any mistakes. For example, it checks if you mention a task that doesn't exist or if tasks are waiting for each other in a loop.
2.  Guess the total time: It tries to predict the earliest time all your tasks can be done. It looks at how long each task takes and which tasks have to wait.
3.  Run tasks one by one: It can go through your list and "do" each task in order. It waits for the specified time for each task.
4.  Run tasks at the same time: If some tasks don't depend on each other, it can do them together. Think of it like having extra helpers!
5.  Compare guess to reality: When running the tasks, it tracks the actual time taken and compares it to its initial guess.


Here's how to use it:

1.  Save the code: You'll have several Python files (`mainv2.py`, `validate_tasks.py`, `calculate_time.py`, `run_sequential.py`, `run_parallel.py`). Put all of them in the same folder.
2.  Make a task list: Create a text file (like `my_tasks.txt`) in the same folder. List your tasks like this:

    ```
    TaskName1, DurationInSeconds, Dependency1 Dependency2
    AnotherTask, 10, TaskName1
    DoLaundry, 30,
    CookDinner, 45, GoGroceryShopping
    GoGroceryShopping, 60,
    ```

     Put each task on a new line.
     Write the task's name (e.g., `TaskName1`).
     Add a comma `,`.
     Write how long it takes in seconds (e.g., `10`).
     Add another comma `,`.
     List any tasks that must finish first. Use spaces to separate them (e.g., `TaskName1 AnotherTask`). If no tasks need to finish first, leave this part empty.
     Lines starting with `#` are ignored (for your notes).

3.  Run the program: Open your computer's command line (or terminal). Go to the folder where you saved the files. Use these commands:

     To check your task list:

        ```cmd
        python mainv2.py my_tasks.txt --validate
        ```

        Replace `my_tasks.txt` with your file's name. This checks for errors and tells you the estimated time.
     To run tasks one after the other:

        ```cmd
        python mainv2.py my_tasks.txt --run
        ```

        This runs the tasks in order and shows the expected and actual times.
     To run tasks at the same time (if possible):

        ```cmd
        python mainv2.py my_tasks.txt --run --parallel
        ```

        This tries to run independent tasks together. It also shows the expected and actual times.


Reading files: How to open and get information from text files.
Organizing data: How to store task information so the program can use it (with dictionaries).
Finding errors: How to check for problems in the task list, like missing or circular dependencies.
Estimating time: How to guess the total time, considering task order.
Running tasks in order: How to do tasks one after another.
Running tasks together: How to use "threads" in Python to do multiple tasks at the same time. It's like having multiple helpers.
Comparing predictions: How to see if my time guess was correct.
Using commands: How to tell the program what to do using words after `python mainv2.py`.
