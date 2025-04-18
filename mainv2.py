import argparse
import time
# We need the functions from these other files to make our  work!
from validate_tasks import validate_task_list
from calculate_time import calculate_expected_runtime
from run_sequential import run_tasks_sequentially
from run_parallel import run_tasks_parallel

def parse_task_list(file_path):
    """
    This part teaches our  how to read the list of jobs from a file.
    'file_path' is like telling the  the name of the file to open.
    """
    tasks = []  # This is an empty box where we'll store all the jobs.
    try:
        with open(file_path, 'r') as job_file:
            # 'open(... 'r')' opens the file so we can read it. 'as job_file' gives it a nickname.
            for line in job_file:
                # This goes through each line in the file, where each line is a job.
                line = line.strip()  # Remove any extra spaces at the start or end of the line.
                if line and not line.startswith('#'):
                    # If the line is not empty and doesn't start with '#', it's a job!
                    # '#' is used for comments in the file (things the  should ignore).
                    parts = line.split(',')  # Each part of the job info is separated by a comma.
                    name = parts[0].strip()  # The first part is the job's name.
                    duration_str = parts[1].strip() # The second part is how long it takes (as text).
                    dependencies_str = ""
                    if len(parts) > 2:
                        dependencies_str = parts[2].strip() # The third part (if it exists) is the jobs this one waits for.

                    duration = int(duration_str)  # Turn the duration text into a number.
                    dependencies = [dep.strip() for dep in dependencies_str.split(' ') if dep.strip()]
                    # If there are dependencies, split them by spaces and clean them up.

                    # Create a 'job' (which is like a dictionary) to store all the info.
                    job = {'name': name, 'duration': duration, 'dependencies': dependencies, 'status': 'pending'}
                    tasks.append(job)  # Add this job to our list of jobs.
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' with the job list was not found!")
        return None  # Tell the main part that we couldn't find the list.
    except ValueError:
        print("Error: The job list file has a mistake in its format. Each line should be 'name, duration_seconds, job1 job2 ...'")
        return None  # Tell the main part that the list was not written correctly.
    return tasks  # Finally, give back the list of jobs we read.

def main():
    """
    This is the main part of our 's brain. It decides what to do based on our commands.
    """
    parser = argparse.ArgumentParser(description="Run a list of jobs, maybe at the same time!")
    # This sets up a way for us to give commands to our  when we run it.
    parser.add_argument("task_file", help="The file that contains the list of jobs to do.")
    # This says we *must* tell the  which file has the jobs.
    group = parser.add_mutually_exclusive_group(required=True)
    # This creates a group where we can only pick one of these options:
    group.add_argument("--validate", action="store_true", help="Just check if the job list is okay and tell us how long it should take.")
    # This option tells the  to only check the list, not run the jobs.
    group.add_argument("--run", action="store_true", help="Actually run the jobs from the list.")
    # This option tells the  to perform the jobs.
    parser.add_argument("--parallel", action="store_true", help="Try to run jobs at the same time if they don't depend on each other (only works with --run).")
    # This option tells the  to try and do jobs together to finish faster.

    args = parser.parse_args()  # This reads the commands we gave to the .

    task_list = parse_task_list(args.task_file)  # First, read the list of jobs from the file.
    if task_list is None:
        return  # If we couldn't read the list, stop here.

    if args.validate:
        # If we just want to check the list...
        if validate_task_list(task_list):
            # ...check if it's valid (no errors like missing jobs or circular waiting)...
            expected_time = calculate_expected_runtime(task_list)
            # ...and if it is, calculate how long the whole process should take.
            print("Job list is valid!")
            print(f"The expected total time to finish all jobs is: {expected_time:.2f} seconds.")
        else:
            print("The job list has some problems. Please check the errors.")
    elif args.run:
        # If we want to actually run the jobs...
        if not validate_task_list(task_list):
            print("Cannot run jobs because the list has problems. Please fix them first.")
            return

        expected_time = calculate_expected_runtime(task_list)
        print(f"The expected total time to finish all jobs is: {expected_time:.2f} seconds.")

        start_time = time.time()  # Start the timer before running any jobs.
        if args.parallel:
            # If we want to run jobs in parallel...
            print("\nRunning jobs in parallel (trying to do some at the same time)...")
            actual_runtime = run_tasks_parallel(list(task_list)) # Give a copy of the list to the parallel function.
        else:
            # If we want to run jobs one after the other...
            print("\nRunning jobs one after another (sequentially)...")
            actual_runtime = run_tasks_sequentially(task_list)

        end_time = time.time()  # Stop the timer after all jobs are done.
        total_actual_runtime = end_time - start_time
        difference = total_actual_runtime - expected_time

        print(f"\nThe actual time it took to run all jobs was: {total_actual_runtime:.2f} seconds.")
        print(f"The difference between the actual and expected time is: {difference:.2f} seconds.")


if __name__ == "__main__":
    main()
