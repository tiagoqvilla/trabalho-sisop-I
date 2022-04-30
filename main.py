from FileReader import FileReader
from Shell import Shell


def main():
    file_reader = FileReader()
    # file_reader.read_file()
    # print(file_reader.file_data)
    shell = Shell()
    option = shell.run_menu()

    programs_list = []

    if (option == "1"):
        pass
    elif (option == "2"):
        program_data = file_reader.read_file()
        arrival_time = input("Informe o arrival time do programa: ")
        priority = input("Informe a prioridade do programa: ")
        quantum = input("Informe o quantum do programa: ")
        program = {
            "program_data": program_data,
            "arrival_time": arrival_time,
            "priority": priority,
            "quantum": quantum
        }

        # programs_list.append(program + list(arrival_time) +
        #                      list(priority) + list(quantum))
        programs_list.append(program)
        print(programs_list)
    elif (option == "3"):
        pass
    elif (option == "4"):
        pass
    elif (option == "5"):
        pass
    elif (option == "6"):
        pass
    else:
        pass


if __name__ == "__main__":
    main()
