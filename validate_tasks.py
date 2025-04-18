def validate_task_list(tasks):
    """
    Let's check our list of jobs to make sure it makes sense!

    We'll check two things:
    1. If a job says it *needs* another job, is that other job actually on our list?
    2. Are there any "wait for each other" problems (circles)?
    """

    # First, let's get a list of all the job names. This is like knowing all the items on our to-do list.
    all_job_names = []
    for task in tasks:
        all_job_names.append(task['name'])

    # Now, let's check the first problem: are all needed jobs actually on the list?
    for task in tasks:
        needed_jobs = task['dependencies']
        for needed_job in needed_jobs:
            if needed_job not in all_job_names:
                print(f"Error: Job '{needed_job}' is needed for '{task['name']}', but '{needed_job}' is not on our list!")
                return False  # Something's wrong with our list!

    # Now for the second, trickier problem: are there any "wait for each other" circles?
    # We need a way to keep track of which jobs depend on which.
    dependency_map = {}
    for task in tasks:
        dependency_map[task['name']] = task['dependencies']

    # To find circles, we can try to go through each job and see if we ever come back to it
    # while checking what it depends on.

    def has_cycle(job_name, currently_checking):
        """
        This is a helper function to see if a job is part of a circle.
        'currently_checking' is a list of jobs we are currently looking at the dependencies of.
        """
        if job_name in currently_checking:
            # If the job we're looking at is already in our 'currently_checking' list,
            # that means we've found a circle!
            print(f"Error: We found a circular dependency involving '{job_name}'!")
            return True

        if job_name not in dependency_map:
            return False  # This job doesn't depend on anything else.

        currently_checking.append(job_name)
        dependencies = dependency_map[job_name]
        for dependency in dependencies:
            if has_cycle(dependency, list(currently_checking)): # We make a copy of the list
                return True
        currently_checking.remove(job_name) # We're done checking this job's dependencies
        return False

    for job_name in all_job_names:
        if has_cycle(job_name, []):
            return False  # If we find a circle for any job, the list is bad.

    return True  # If we passed both checks, our job list is good!