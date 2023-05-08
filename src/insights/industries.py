from typing import List, Dict
from src.insights.jobs import read


def get_unique_industries(path: str) -> List[str]:
    industries_list = read(path)
    set_unique_industries = set()
    for industries in industries_list:
        if industries["industry"] != "":
            set_unique_industries.add(industries["industry"])
    return set_unique_industries


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    return [job for job in jobs if job["industry"] == industry]
