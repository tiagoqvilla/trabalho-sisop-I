import os

class Shell:

    def __init__(self) -> None:
        self.options = {
            "1": "Iniciar sistema",
            "2": "Adicionar programa na memória",
            "3": "Definir o algoritmo de escalonamento",
            "4": "Remover um programa",
            "5": "Resetar configurações",
            "0": "Sair"
        }
        self.selection = "-1"

    def print_menu(self):
        for option in self.options:
            print(f"[{option}] {self.options[option]}")

    def get_input(self):
        return input("> ")

    def run_menu(self):
        self.clean_screen()
        self.print_menu()
        self.selection = self.get_input()
        while(self.selection not in self.options):
            self.clean_screen()
            input("Opção invalida, pressione enter para voltar ao menu.")
            self.clean_screen()
            self.print_menu()
            self.selection = self.get_input()

        return self.selection

    def clean_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')