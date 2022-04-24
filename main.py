def main():
    # filename = input("Digite o nome do arquivo: ")
    filename = "prog2.txt"
    with open(filename) as f:
        lines = [" ".join(line.split()) for line in f]

    new_list = []
    for line in lines:
        l = line.split(" ")
        new_list.append(l)

    new_lines = []
    for l in new_list:
        temp = []
        for p in l:
            if p == '#':
                break
            else:
                temp.append(p)
        new_lines.append(temp)

    print(new_lines)


if __name__ == "__main__":
    main()
