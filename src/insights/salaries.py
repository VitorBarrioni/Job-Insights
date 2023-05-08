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
    try:
        min_salary = int(job["min_salary"])
        max_salary = int(job["max_salary"])
        salary = int((salary))
    except (TypeError, ValueError, KeyError):
        raise ValueError
    if min_salary > max_salary:
        raise ValueError
    return salary in range(min_salary, max_salary)


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
