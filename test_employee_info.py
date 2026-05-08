import employee_info

print("Test_employee_info")

def test_get_employees_by_age_range():
    expected_result = [
        {"name": "John", "age": 30, "department": "Sales", "salary": 50000},
        {"name": "Jane", "age": 25, "department": "Marketing", "salary": 60000},
        {"name": "Mike", "age": 32, "department": "Engineering", "salary": 65000}
    ]

    result = employee_info.get_employees_by_age_range(23,35)

    assert result == expected_result

def test_calculate_average_salary():
    expected_result = 60166.67
    result = employee_info.calculate_average_salary()
    result == expected_result

def test_get_employees_by_dept():
    expected_result = [
        {"name": "John", "age": 30, "department": "Sales", "salary": 50000},
        {"name": "Peter", "age": 40, "department": "Sales", "salary": 60000}

    ]
    result = employee_info.get_employees_by_dept("Sales")
    assert result == expected_result