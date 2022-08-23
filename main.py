from solution.functions import frecuency_meet_employee, file_to_dict


def main():
    file = input("Enter the file path or drag it here: ")
    print(frecuency_meet_employee(file_to_dict(file)))


if __name__ == '__main__':
    main()
