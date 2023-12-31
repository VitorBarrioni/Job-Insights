from functools import lru_cache
from typing import List, Dict
import csv


@lru_cache
def read(path: str) -> List[Dict]:
    with open(path) as file:
        content = csv.DictReader(file)
        jobs_list = [jobs for jobs in content]
        print(jobs_list[0])
    return jobs_list


def get_unique_job_types(path: str) -> List[str]:
    jobs_list = read(path)
    set_unique_jobs = set()
    for jobs in jobs_list:
        set_unique_jobs.add(jobs["job_type"])
    return set_unique_jobs


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    return [job for job in jobs if job["job_type"] == job_type]
