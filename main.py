from solution.functions import frecuency_meet_employee, file_to_dict


def main():
    file = input("Ingrese la direccion del archivo o arrastrelo aqui: ")
    print(frecuency_meet_employee(file_to_dict(file)))


if __name__ == '__main__':
    main()
