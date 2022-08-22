def file_to_dict(path: str) -> dict:
    """A function to convert all of the lines in a file to a dictionary
        Content File Example:
            ASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00
        Output Example:
            {"ASTRID": {"MO": ["1000", "1200"], "TH": ["1200", "1400"], "SU": ["2000", "2100"]}}
    Args:
        file (str): The path of the file to read
    Returns:
        dict: A dictionary with all the processed information ready to be used
    """
    employee = {}
    with open(path.strip("'")) as file:
        for line in file:
            items = line.rstrip("\n").split("=")
            schedule = items[1].split(",")
            dayTimeList = {}
            for dayTime in schedule:
                day, time = dayTime[:2], dayTime[2:].replace(
                    ":", "").split("-")
                dayTimeList[day] = time
            employee[items[0]] = dayTimeList
    return employee


def number_of_coincidences(schedule1: dict, schedule2: dict) -> int:
    """Counts all coincidences between the times of two schedules
        Content File Example:
            schedule1 = {"MO": ["1000", "1200"], "TH": ["1200", "1400"], "SU": ["2000", "2100"]}
            schedule2 = {"MO": ["1130", "1300"], "TH": ["1200", "1400"], "FR": ["1700", "2000"]}
        Output Example: 2
    Args:
        schedule1, schedule2 (dict): A dictionary which contains a day as a key and an array of time as value
    Returns:
        int: A number of all coincidences between the times of the schedules.
    """
    counter = 0
    entry, exit = 0, 1
    for day in schedule1:
        if day in schedule2:
            firstEmployeeEntry, secondEmployeeEntry = int(
                schedule1[day][entry]), int(schedule2[day][entry])
            firstEmployeeExit, secondEmployeeExit = int(
                schedule1[day][exit]), int(schedule2[day][exit])
            if (firstEmployeeEntry >= secondEmployeeEntry and firstEmployeeEntry <= secondEmployeeExit):
                counter += 1
            elif (secondEmployeeEntry >= firstEmployeeEntry and secondEmployeeEntry <= firstEmployeeExit):
                counter += 1
    return counter


def frecuency_meet_employee(employees: dict) -> str:
    """Compare all employees with each other
        Input Example:
            {"ASTRID": {"MO": ["1000", "1200"], "TH": ["1200", "1400"]},
            "RENE": {"MO": ["1115", "1300]", "TU": [1000", "1200"]}
        Output Example:
            ASTRID-RENE: 2
    Args:
        employee (dict): Employee dictionary with name as key and an dictionary of schedule as a value

    Returns:
        str: returns a string with the employees and the times they have met each other
    """
    employeeNames = tuple(employees.keys())
    coincidences = ""
    for i in range(len(employeeNames)-1):
        for j in range(i+1, len(employeeNames)):
            schedule1 = employees.get(employeeNames[i])
            schedule2 = employees.get(employeeNames[j])
            counter = number_of_coincidences(schedule1, schedule2)
            coincidences += f"{employeeNames[i]}-{employeeNames[j]}: {counter}"
            if (i == len(employeeNames)-2):
                return coincidences
            coincidences += "\n"


def main():
    file = input("Ingrese la direccion del archivo o arrastrelo aqui: ")
    print(frecuency_meet_employee(file_to_dict(file)))


main()
