import time

def run_tasks_sequentially(tasks):
    """
    Imagine this is like doing your homework one subject at a time.
    We go through our list of 'tasks' (homework subjects) and do each one completely
    before moving to the next.
    """
    print("Starting to do the jobs one by one...")
    start_time = time.time()  # Let's start a clock to see how long it takes in total.

    for task in tasks:
        # This loop goes through each job in our list.
        print(f"Starting job: {task['name']}")
        run_task(task)  # This line actually does the current job.
        print(f"Finished job: {task['name']}")

    end_time = time.time()  # The clock stops when all jobs are done.
    total_time = end_time - start_time  # Let's calculate the total time it took.
    print(f"All jobs finished in {total_time:.2f} seconds.")
    return total_time

def run_task(task):
    """
    This function is like actually doing one specific job.
    The 'task' has a name and a 'duration' (how long it takes).
    We'll pretend to work on it by waiting for that amount of time.
    """
    task_name = task['name']
    duration = task['duration']
    print(f"Working on job '{task_name}' for {duration} seconds...")
    time.sleep(duration)  # This makes the program wait, like we're doing the work.
    task['status'] = 'completed'  # Once the waiting is done, we say the job is 'completed'.