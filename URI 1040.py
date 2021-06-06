
N1,N2,N3,N4 = list(map(float,input().split()))

media = (N1*2+N2*3+N3*4+N4*1)/10
print("Media: %.1f" %media)
if media >=7:
    print("Aluno aprovado.")
elif media < 5:
    print("Aluno reprovado.")
elif media >= 5 and media <6.9:
    print("Aluno em exame.")

exam = float(input())
print("Nota do exame: %.1f" %exam)
avg = (media + exam)/2
if avg >= 5 :
    print("Aluno aprovado.")
else :
    print("Aluno reprovado.")

print("Media final: %.1f" %avg)