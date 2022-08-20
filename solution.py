def read_file(file: str) -> dict:
    employee = {}
    with open(file.strip("'")) as f:
        for line in f:
            items = line.rstrip("\n").split("=")
            schedule = items[1].split(",")
            dayTimeList = {}
            for dayTime in schedule:
                day, time = dayTime[:2], dayTime[2:].replace(
                    ":", "").split("-")
                dayTimeList[day] = time
            employee[items[0]] = dayTimeList
    return employee


def calculate_concurrency(employee: dict) -> str:
    employeeName = list(employee.keys())
    coincidences = ""
    for i in range(len(employeeName)-1):
        for j in range(i+1, len(employeeName)):
            counter = 0
            employeeSchedule = employee.get(employeeName[i])
            employeeSchedule2 = employee.get(employeeName[j])
            for day, time in employeeSchedule.items():
                if day in employeeSchedule2:
                    if (int(time[0]) <= int(employeeSchedule2[day][1]) and int(time[0]) >= int(employeeSchedule2[day][0])):
                        counter += 1
            coincidences += f"{employeeName[i]}-{employeeName[j]}: {counter}"
            if (i == len(employeeName)-2):
                return coincidences
            coincidences += "\n"


def main():
    file = input("Ingrese la direccion del archivo o arrastrelo aqui: ")
    print(calculate_concurrency(read_file(file)))


main()
