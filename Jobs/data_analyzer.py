import csv

avg_salary = []
data_fp = open("./data.csv", "r")
csv_reader = csv.DictReader(data_fp, fieldnames=("work_experience", "salary_range"))

min_start_year = None
max_end_year = None
min_start_salary = None
max_end_salary = None

next(csv_reader)
for line in csv_reader:
    we, sr = line["work_experience"], line["salary_range"]
    if we in ("不限", "1年以下", "无经验") or sr in ("薪资面议", ):
        continue
    if "以上" in we:
        continue

    assert isinstance(we, str)
    start_year, end_year = we.replace("年", "").split("-")
    start_salary, end_salary = sr.replace("K", "").split("-")

    if min_start_year is None:
        min_start_year = float(start_year)
    if max_end_year is None:
        max_end_year = float(end_year)

    if min_start_salary is None:
        min_start_salary = float(start_salary)
    if max_end_salary is None:
        max_end_salary = float(end_salary)

    min_start_year = min(min_start_year, float(start_year))
    max_end_year = max(max_end_year, float(end_year))
    min_start_salary = min(min_start_salary, float(start_salary))
    max_end_salary = max(max_end_salary, float(end_salary))

avg_salary = (min_start_salary + max_end_salary)/(min_start_year + max_end_year)
import numpy as np
years = np.arange(1, 11)

salarys = (2 + years * avg_salary)

import matplotlib.pyplot as plt

plt.bar(years, salarys)
plt.show()

# print(salarys)
    # x = (float(start_salary) + float(end_salary))/(int(end_year)+int(start_year))
    # print(x)
    # avg_salary.append(x)
    # print(start_year,end_year, start_salary, end_salary)