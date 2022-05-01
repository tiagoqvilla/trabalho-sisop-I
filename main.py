from Shell import Shell
from FileReader import FileReader
from InputProgram import InputProgram
from System import System
import os


def main():

    shell = Shell()
    option = shell.run_menu()

    programs_list = []

    while (option != '1'):
        if option == '1':
            pass
        elif (option == "2"):  # Adicionar programa na memória
            priority_dict = {'1': 'alta',
                             '2': 'media',
                             '3': 'baixa'}

            file_reader = FileReader()
            program_data = file_reader.read_file()

            shell.clean_screen()
            arrival_time = input("Informe o arrival time do programa:\n> ")

            while True:
                shell.clean_screen()
                priority = input(
                    "Informe a prioridade do programa:\n[1] alta\n[2] media\n[3] baixa\n> ")
                if priority in priority_dict:
                    break
                else:
                    input("Opção invalida, pressione enter para continuar.")
                continue

            shell.clean_screen()
            quantum = input("Informe o quantum do programa:\n> ")

            input_program = InputProgram(
                program_data, arrival_time, priority_dict[priority], quantum)
            input_program.processProgramData()
            programs_list.append(input_program)
            input("Programa adicionado com sucesso, pressione enter para voltar ao menu.")

        elif (option == "3"):
            pass
        elif (option == "4"):
            pass
        elif (option == "5"):
            pass
        elif (option == "0"):
            exit()
        else:
            pass
        option = shell.run_menu()

    system = System(programs_list)
    system.run()

    # for program in programs_list:
    #     print(program.code_area)


if __name__ == "__main__":
    main()
