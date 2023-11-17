# Визначення класу для співробітників
class Employee:
    def __init__(self, last_name, salary, gender):
        self.last_name = last_name
        self.salary = salary
        self.gender = gender

# Функція для знаходження прізвища особи з найбільшою зарплатою
def find_highest_salary(employee_list):
    highest_salary_employee = max(employee_list, key=lambda x: x.salary)
    return highest_salary_employee.last_name

# Функція для знаходження прізвищ чоловіка і жінки з найменшою зарплатою
def find_lowest_salary_names(employee_list):
    # Розділення співробітників за статтю
    male_employees = [employee for employee in employee_list if employee.gender == 'Male']
    female_employees = [employee for employee in employee_list if employee.gender == 'Female']

    # Знаходження прізвищ з найменшою зарплатою у чоловіків і жінок
    lowest_salary_male = min(male_employees, key=lambda x: x.salary).last_name
    lowest_salary_female = min(female_employees, key=lambda x: x.salary).last_name

    return lowest_salary_male, lowest_salary_female

# Основна частина програми
if __name__ == "__main__":
    # Задання даних про співробітників
    employees_data = [
        {"last_name": "Ivanov", "salary": 49000, "gender": "Male"},
        {"last_name": "Petrov", "salary": 60000, "gender": "Male"},
        {"last_name": "Sidorovna", "salary": 45000, "gender": "Female"},
        {"last_name": "Sidorov", "salary": 47500, "gender": "Male"},
        {"last_name": "Prikhodko", "salary": 55500, "gender": "Male"},
        {"last_name": "Miroshnichenko", "salary": 60500, "gender": "Male"},
        {"last_name": "Skochenko", "salary": 30000, "gender": "Female"},
        {"last_name": "Ponomarenko", "salary": 52000, "gender": "Male"},
        {"last_name": "Taran", "salary": 51200, "gender": "Male"},
        {"last_name": "Rovna", "salary": 53000, "gender": "Female"}
    ]

    # Створення об'єктів співробітників
    employees = [Employee(data["last_name"], data["salary"], data["gender"]) for data in employees_data]

    # Знаходження результатів
    highest_salary_last_name = find_highest_salary(employees)
    lowest_salary_male, lowest_salary_female = find_lowest_salary_names(employees)

    # Виведення результатів
    print(f"Прізвище особи з найбільшою зарплатою: {highest_salary_last_name}")
    print(f"Прізвище чоловіка з найменшою зарплатою: {lowest_salary_male}")
    print(f"Прізвище жінки з найменшою зарплатою: {lowest_salary_female}")