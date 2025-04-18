def calculate_expected_runtime(tasks):
    """
    Let's figure out the soonest time all the jobs can be done.
    We need to think about how long each job takes and if some jobs have to wait for others.
    """

    # First, let's make a quick way to find out how long each job takes.
    job_lengths = {}
    for task in tasks:
        job_lengths[task['name']] = task['duration']
    # Now, if we know the job's name, we can easily find its length in 'job_lengths'.

    earliest_start_times = {}
    # This will keep track of the earliest time each job can begin.
    # We'll start by assuming all jobs can start at time 0.

    def get_earliest_start_time(job_name):
        """
        This helps us find out when a specific job can start.
        It has to wait until all the jobs it depends on are finished.
        """
        if job_name in earliest_start_times:
            return earliest_start_times[job_name]  # We've already figured this out!

        start_time = 0  # By default, a job can start at the beginning (time 0).
        current_task_dependencies = []
        # Let's find the dependencies for the current job.
        for task in tasks:
            if task['name'] == job_name:
                current_task_dependencies = task['dependencies']
                break

        for dependency_job_name in current_task_dependencies:
            # For each job that needs to finish before this one...
            dependency_finish_time = get_earliest_start_time(dependency_job_name) + job_lengths[dependency_job_name]
            # ...we find out when that dependency will finish.
            # Our current job can only start *after* all its dependencies are done.
            start_time = max(start_time, dependency_finish_time)
            # We take the latest finish time of all dependencies as the earliest start time for this job.

        earliest_start_times[job_name] = start_time
        return start_time

    total_finish_time = 0
    # We'll keep track of the time when the *very last* job finishes.

    for task in tasks:
        start_time = get_earliest_start_time(task['name'])
        finish_time = start_time + job_lengths[task['name']]
        # The finish time of a job is when it starts plus how long it takes.
        total_finish_time = max(total_finish_time, finish_time)
        # The overall finish time is the latest finish time among all the jobs.

    return total_finish_time