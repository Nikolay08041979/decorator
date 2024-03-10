
def calculate_salary(period_in_months: int):
    fix_salary = 100
    bonus_mounth = 0.5
    bonus_year = 0.3
    salary_mounth_gross = fix_salary + (bonus_mounth * fix_salary)
    return (salary_mounth_gross * period_in_months * (1+bonus_year))