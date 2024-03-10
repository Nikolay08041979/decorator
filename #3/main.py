import profile

import pandas as pd
import math
from datetime import datetime, date, time
from application.db.people import get_employees
from application.salary import calculate_salary
from decorator import logger


@logger('log1.txt')
def company_cost_utd(tax: int):
    salary_month = calculate_salary(1)
    salary_year = calculate_salary(12)
    staff = get_employees(100)
    current_date = date.today()
    total_company_cost = salary_year * staff * tax
    print(f' Monthly salary is {salary_month} by the current day {current_date} for one employee\n'
          f'The total company annual cost is around {math.ceil(total_company_cost/1000000)} mln $ if {tax}% taxes and {staff} employees staff')


@logger('log2.txt')
def company_cost_pd(staff: int):
    salary_year = calculate_salary(12)
    tax = 0.5
    salaries = {staff * salary_year for staff in range(1, staff + 1)}
    staffs = {staff for staff in range(1, staff + 1)}
    taxes = {staff * tax * salary_year for tax in range(1, staff+1)}
    company_pl = zip(staffs, salaries, taxes)
    df = pd.DataFrame.from_dict(company_pl)
    print(df)



if __name__ == '__main__':
    company_cost_utd(15)
    company_cost_pd(10)


