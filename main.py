from application.salary import calculate_salary
from application.db.people import get_employees
import datetime as dtime

if __name__ == '__main__':
    print(dtime.date.today())
    print(calculate_salary(54000))
    print(get_employees())
