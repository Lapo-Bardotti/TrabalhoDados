import pandas as pd

aluno = 'https://raw.githubusercontent.com/Lapo-Bardotti/TrabalhoDados/master/Base_de_Alunos1.csv'
dengue = 'https://raw.githubusercontent.com/Lapo-Bardotti/TrabalhoDados/master/Base_de_Dengue1.csv'
onibus = 'https://raw.githubusercontent.com/Lapo-Bardotti/TrabalhoDados/master/Base_de_Onibus1.csv'

dadosOnibus = pd.read_csv(onibus)
dadosAluno = pd.read_csv(aluno)
dadosDengue = pd.read_csv(dengue)

listOnibusNome = dadosOnibus['Nome'].tolist()
listAlunos = dadosAluno['Nome'].tolist()
listDengue = dadosDengue['Nome'].tolist()
listDengueDataN = dadosDengue['Data de Nascimento'].tolist()
listDengueID =dadosDengue['ID'].tolist()
listDengueData = dadosDengue['Data da Dengue'].tolist()

print(len(listDengueID))

aux = len(dadosDengue)
i=0
aux3=[0]

while i<aux:
    aux2=len(dadosDengue)
    j=0
    while j<aux2:
      if listDengue[i] == listAlunos[j]:
        if int(aux3[len(aux3)-1]) != i: 
          aux3.append(i)
      j+=1
    i+=1

i=1

while i<len(aux3)-1:
 
 listDengueID.remove(int(aux3[i]))
 i+=1

 aux = len(listDengueID)
i=0
Dengonibus=[0]

while i<aux:
    aux2=len(dadosOnibus)
    j=0
    while j<aux2:
      if listDengue[int(listDengueID[i])] == listOnibusNome[j]:
        if int(Dengonibus[len(Dengonibus)-1]) != int((listDengueID[i])):
          Dengonibus.append(int(listDengueID[i]))
      j+=1
    i+=1

i=1

while i<len(Dengonibus):
 
 listDengueID.remove(int(Dengonibus[i]))
 i+=1
 
i=0
AlunoTxt= open("10questaoNatDis.txt","w+")

while i<len(listDengueID):

  print(str(listDengueID[i])+"-"+listDengue[int(listDengueID[i])] + "//"+listDengueDataN[int(listDengueID[i])] + "//"+listDengueData[int(listDengueID[i])])

  AlunoTxt.write(str(listDengueID[i])+"-"+listDengue[int(listDengueID[i])] + "//"+listDengueDataN[int(listDengueID[i])] + "//"+listDengueData[int(listDengueID[i])]+"\n")
  i+=1


AlunoTxt.close()
