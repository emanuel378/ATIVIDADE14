# Crie um programa que receba três notas de um aluno e calcule a média. Informe se o aluno foi aprovado, reprovado ou se está de recuperação. Use as seguintes regras:
# Média ≥ 7: Aprovado
# 5 ≤ Média < 7: Recuperação
# Média < 5: Reprovado
n1 = float(input("Digite sua primeira nota:"))
n2 = float(input("Coloque sua segunda nota:"))
n3 = float(input("Sua terceira nota:"))
media = (n1+n2+n3)/3

if media >=7:
    print("Aprovado")
elif media <5:
    print("Reprovado")
else:
    print("Recuperação")