from os import walk
import re
import numpy as np

def removetags(s:str):
	new:str = s
	dirty = True
	while dirty:
		start_index = new.find('<')
		end_index = new.find('>')
		if(start_index == -1 or end_index == -1 or end_index < start_index):
			dirty = False
		else:
			new = new.replace(new[start_index:end_index+1], "")
	return new

f = []
for (dirpath, dirnames, filenames) in walk("./emails"):
    f.extend(filenames)
    break

matrix = [['tipo', 'cnpj', 'nome fantasia', 'nome', 'cpf', 'email', 'telefone']]
print("opa:\n")
for(file) in f:
    try:
        text_file = open("./emails/"+file, "r")
        content = text_file.read()
        text_file.close()
        x = re.findall("<td style=\"color:#555555;padding-top:.+</td>", content)
        if(len(x) == 0):
            print("Arquivo com erro: "+file)
        else:
            for(idx, s) in enumerate(x):
                x[idx] = removetags(s)
            matrix.append(x)
    except:
        print("error on file: " + file)

np.savetxt("lista.csv", matrix, delimiter=",", fmt='%s')

