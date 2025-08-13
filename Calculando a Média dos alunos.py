from math import trunc
nome = str(input('Digite o nome do aluno: ')).strip().capitalize()
mat = float(input('Digite a nota do aluno(a) em matemática: '))
port = float(input('Digite a nota do aluno(a) em portugues: '))
bio = float(input('Digite a nota do aluno(a) em bilogia: '))
fis = float(input('Digite a nota do aluno(a) em fisíca: '))
media = (mat + port + bio + fis) /4
total = trunc(media)
print('A nota média do aluno(a) {} é de {:.1f}'.format(nome, total))
