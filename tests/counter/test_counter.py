from src.pre_built.counter import count_ocurrences


def test_counter():
    count_salary = 598
    count_salary_ocurrences = count_ocurrences("data/jobs.csv", "salary")
    assert count_salary_ocurrences == count_salary
