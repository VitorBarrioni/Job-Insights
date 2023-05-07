from typing import Union, List, Dict
from src.insights.jobs import read


def get_max_salary(path: str) -> int:
    jobs_list = read(path)
    return max(
        [
            int(jobs["max_salary"])
            for jobs in jobs_list
            if jobs["max_salary"].isnumeric()
        ]
    )


def get_min_salary(path: str) -> int:
    jobs_list = read(path)
    return min(
        [
            int(jobs["min_salary"])
            for jobs in jobs_list
            if jobs["min_salary"].isnumeric()
        ]
    )


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    if job["min_salary"] > job["max_salary"]:
        raise ValueError("min salary bigger than max salary")
    if not salary.isnumeric():
        raise ValueError("salary is not numeric")
    if not job["min_salary"].isnumeric() or not job["max_salary"].isnumeric():
        raise ValueError("min salary or max salary value is not numerical")

    if int(job["min_salary"]) >= salary and int(job["max_salary"] <= salary):
        return True
    return False


def filter_by_salary_range(
    jobs: List[dict], salary: Union[str, int]
) -> List[Dict]:
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    raise NotImplementedError
