import sys

flag_a = False
flag_b = False
flag_c = False

option_d = 0
option_e = 0
option_f = 0

files = []


def print_help():
    print('To jest główna pomoc programu')
    print('Opcje do wybrania:')
    print('-a lub -A')
    print('-b lub -B')
    print('-c lub -C')
    print('-d LICZBA lub -D LICZBA')
    print('-e LICZBA lub -E LICZBA')
    print('-f LICZBA lub -F LICZBA')
    print('-file PLIK1 PLIK2 ... lub -FILE PLIK1 PLIK2')


args_count = len(sys.argv[1:])
print('Liczba argumentów:', args_count)
if args_count > 0:
    for x in range(1, args_count):
        # print("Analizuję:", sys.argv[x])
        if sys.argv[x] == '-h' or sys.argv[x] == '-help':
            print_help()
        if sys.argv[x] == '-a' or sys.argv[x] == '-A':
            flag_a = True
            continue
        if sys.argv[x] == '-b' or sys.argv[x] == '-B':
            flag_b = True
            continue
        if sys.argv[x] == '-c' or sys.argv[x] == '-C':
            flag_c = True
            continue
        if sys.argv[x] == '-d' or sys.argv[x] == '-D':
            option_d = int(sys.argv[x+1])
            print('Opcja d:', option_d)
            continue
        if sys.argv[x] == '-e' or sys.argv[x] == '-E':
            option_e = int(sys.argv[x+1])
            print('Opcja e:', option_e)
            continue
        if sys.argv[x] == '-f' or sys.argv[x] == '-F':
            option_f = int(sys.argv[x+1])
            print('Opcja f:', option_f)
            continue
        if sys.argv[x] == '-file' or sys.argv[x] == '-FILE':
            for y in range(x+1, args_count+1):
                files.append(sys.argv[y])
            print(files)
            break
else:
    print('Nie podano argumentów. Pomoc można uzyskać uruchamiając skrypt w następujący sposób:')
    print('python ex4-1.py -help')
