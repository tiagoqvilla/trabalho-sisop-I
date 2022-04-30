from FileReader import FileReader
from Shell import Shell
from InputProgram import InputProgram
import os


def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    shell = Shell()
    option = shell.run_menu()
    programs_list = []
    while (option != '1'):
        os.system('cls' if os.name == 'nt' else 'clear')
        if (option == "2"):
            file_reader = FileReader()
            program_data = file_reader.read_file()
            arrival_time = input("Informe o arrival time do programa: ")
            priority = input("Informe a prioridade do programa: ")
            quantum = input("Informe o quantum do programa: ")

            input_program = InputProgram(
                program_data, arrival_time, priority, quantum)
            input_program.processProgramData()
            programs_list.append(input_program)
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
        option = shell.run_menu()

    for program in programs_list:
        print(program.program_data)


if __name__ == "__main__":
    main()
