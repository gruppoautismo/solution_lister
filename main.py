import glob
import os

path = os.path.dirname(os.path.realpath(__file__)) + "\soluzioni"

print("cartella che sta venendo controllata:\n_-_:  " + path)


print("controllando")
files = [f for f in glob.glob(path + "**/*.txt", recursive=True)]

lista = open("lista_sol.lst", 'w')

for f in files:
    
    arr = f.split("\\")
    nome = arr[-1]

    print(nome)

    if(nome != "ignore.txt"):
        lista.write(nome + "\n")
    else:
        print("\n::--------::file da ignorare, non sarà aggiunto alla lista::--------::\n")
lista.close()
    
