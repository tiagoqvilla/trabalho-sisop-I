from Shell import Shell
from FileReader import FileReader
from InputProgram import InputProgram
from System import System
import os

'''
    Trabalho de Sistemas Operacionais - 2022/1
    Prof. Fabiano Passuelo Hessel
    Autores: Henrique Brauveres, Lucas Pescador, Tiago Villa
'''


def main():

    shell = Shell()
    option = shell.run_menu()

    programs_list = []

    while (option != '1'):
        if option == '1':  # Inicia o sistema
            pass
        elif (option == "2"):  # Adicionar programa na memória
            priority_dict = {'0': 'alta',
                             '1': 'media',
                             '2': 'baixa'}

            file_reader = FileReader()
            program_data = file_reader.read_file()

            shell.clean_screen()

            program_name = file_reader.name.replace(".txt", "")

            arrival_time = int(
                input("Informe o arrival time do programa:\n> "))

            while True:
                shell.clean_screen()
                priority = input(
                    "Informe a prioridade do programa:\n[0] alta\n[1] media\n[2] baixa\n> ")
                if priority in priority_dict:
                    break
                else:
                    input("Opção invalida, pressione enter para continuar.")
                continue

            shell.clean_screen()
            quantum = input("Informe o quantum do programa:\n> ")

            input_program = InputProgram(
                program_name, program_data, arrival_time, priority_dict[priority], quantum)
            input_program.processProgramData()
            programs_list.append(input_program)
            input("Programa adicionado com sucesso, pressione enter para voltar ao menu.")

        elif (option == "3"):  # Define o algoritmo de escalonamento
            scheduling_algorithm_dict = {
                '1': 'prioridade sem preempção',
                '2': 'prioridade com preempção',
                '3': 'round robin'
            }
            while True:
                shell.clean_screen()
                scheduling_algorithm = input(
                    "Informe o algoritmo de escalonamento do programa:\n[1] prioridade sem preempção\n[2] prioridade com preempção\n[3] round robin\n> ")
                if scheduling_algorithm in scheduling_algorithm_dict:
                    input(
                        f"Algoritmo de escalonamento {scheduling_algorithm_dict[scheduling_algorithm]} definido com sucesso! Pressione enter para continuar")
                    break
                else:
                    input("Opção invalida, pressione enter para continuar.")
                continue
            pass
        elif (option == "4"):  # Remove um programa da lista
            pass
        elif (option == "5"):  # Reseta as configurações
            shell.clean_screen()
            programs_list.clear()
            input(
                'A lista de programas foi resetada. Pressione qualquer tecla para voltar ao menu.')
        elif (option == "0"):
            exit()
        else:
            pass
        option = shell.run_menu()

    system = System(programs_list)

    if not programs_list:
        shell.clean_screen()
        input('Voce deve adicionar um programa na memória para poder iniciar o sistema. Pressione qualquer tecla para voltar o menu.')
        option = shell.run_menu()
    else:
        system.run()


if __name__ == "__main__":
    main()
