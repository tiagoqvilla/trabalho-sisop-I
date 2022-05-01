import os

class FileReader:

    def __init__(self) -> None:
        self.name = ""
        self.file_data = []

    def read_file(self):
        #self.name = input("Digite o nome do arquivo:\n> ")
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            self.name = input("Digite o nome do arquivo:\n> ")
            if os.path.isfile(self.name):
                break
            else:
                input("Arquivo não encontrado, pressione enter para continuar.")
                continue

        
        with open(self.name) as f:
            lines = [" ".join(line.split()) for line in f]

        new_list = []
        for line in lines:
            l = line.split(" ")
            new_list.append(l)

        for l in new_list:
            temp = []
            for p in l:
                if p == '#':
                    break
                else:
                    temp.append(p)
            self.file_data.append(temp)

        return self.file_data

        # print(self.file_data)
