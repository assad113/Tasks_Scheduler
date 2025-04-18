
import time
import threading

def run_tasks_parallel(tasks):
    """
    This is like having a team of s that can work on different jobs at the same time!
    But, some jobs might need to wait for others to finish first.

    We'll try to start as many jobs as possible at the same time, as long as they don't have to wait.
    """
    print("Trying to run jobs in parallel (at the same time)...")
    start_time = time.time()  # Start the clock for the whole process.

    completed_job_names = set()  # This is like a list of jobs that are already finished.
    all_tasks = {task['name']: task for task in tasks} # Let's easily find tasks by their names.

    while len(completed_job_names) < len(tasks):
        jobs_ready_to_start = []  # These are the jobs we can start right now.

        for task in tasks:
            task_name = task['name']
            dependencies = task['dependencies']
            status = task.get('status', 'pending') # Get the status, default to 'pending' if not set.

            # Can this job start?
            # 1. Has it not been completed yet?
            # 2. Are all the jobs it depends on finished?
            # 3. Has it not started running already?
            if task_name not in completed_job_names and all(dep in completed_job_names for dep in dependencies) and status == 'pending':
                jobs_ready_to_start.append(task)
                task['status'] = 'running' # Mark it as running so we don't start it again.

        threads = []  # We'll put each running job in its own 'thread' (like a 's hand).
        for job_to_run in jobs_ready_to_start:
            # For each job that's ready, let's start it!
            thread = threading.Thread(target=run_task, args=(job_to_run,))
            threads.append(thread)
            thread.start() # Tell this 'hand' to start working.
            print(f"Started job: {job_to_run['name']} in the background.")

        # Wait for all the jobs we just started to finish before checking for more jobs.
        for thread in threads:
            thread.join() # Wait for this 'hand' to finish its work.

        # Now, let's update our list of completed jobs.
        for task in tasks:
            if task.get('status') == 'completed':
                completed_job_names.add(task['name'])

        # If no new jobs started in this round, let's wait a little bit before checking again.
        if not jobs_ready_to_start:
            time.sleep(0.1)

    end_time = time.time() # All jobs are done, stop the clock.
    total_time = end_time - start_time
    print(f"All parallel jobs finished in {total_time:.2f} seconds.")
    return total_time

def run_task(task):
    """
    This is like one  doing its job. It will wait for a specific time.
    """
    task_name = task['name']
    duration = task['duration']
    print(f" started working on '{task_name}' for {duration} seconds...")
    time.sleep(duration) # The  is working (waiting).
    print(f" finished working on '{task_name}'.")
    task['status'] = 'completed' # The job is now done.