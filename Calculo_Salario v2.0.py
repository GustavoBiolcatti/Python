nome_arq = input("Digite o nome do arquivo: ")
nome_arq += ".txt"

nome = str(input("\nDigite seu nome completo: ").upper().strip())

sb = float(input("\nDigite seu salário bruto: ").replace(",", "."))

dt = int(input("\nDigite a quantidade de dias trabalhados: "))

he = float(input("\nDigite seu horário de entrada: ").replace(":", "."))
hs = float(input("\nDigite seu horário de saída: ").replace(":", "."))

ht = (hs - he) * dt
vh = sb / ht

print("\n")
print("-" * 43)
print("{:^43}".format("DESCONTOS"))
print("-" * 43)

c_inss = str(input("\nÉ descontado INSS? ('s' ou 'n') ").lower())
if c_inss == "s":
    inss = float( sb * int(input("Qual a porcentagem (%) de desconto? ")) / 100)

else:
    inss = 0
    

c_sind = str(input("\nÉ descontado sindicato? ('s' ou 'n') ").lower())
if c_sind == "s":
    sind = float( sb * int(input("Qual a porcentagem (%) de desconto? ")) / 100)

else:
    sind = 0
    

c_ir = str(input("\nÉ descontado IR? ('s' ou 'n') ").lower())
if c_ir == "s":
    ir = float( sb * int(input("Qual a percentagem (%) de desconto? ")) / 100)

else:
    ir = 0


c_vt = str(input("\nÉ descontado vale transporte? ('s' ou 'n') ").lower())
if c_vt == "s":
    vt = float( sb * int(input("Qual a porcentagem (%) de desconto? ")) / 100)

else:
    vt = 0

print("\n")
print("-" * 43)
print("{:^43}".format("BENEFÍCIOS"))
print("-" * 43)

c_vr = str(input("\nPossui vale refeição? ('s' ou 'n') ").lower())
if c_vr == "s":
    vr = float(input("Digite o valor: R$").replace(",", "."))

else:
    vr = 0
    
c_va = str(input("\nPossui vale alimentação? ('s' ou 'n') ").lower())
if c_va == "s":
    va = float(input("Digite o valor (por dia): R$").replace(",", ".")) * dt

else:
    va = 0
    

sl = float(sb - (inss + sind + ir + vt))

with open(nome_arq, 'w', encoding='utf-8') as arq:
    arq.write("-" * 43)
    arq.write("{:^43}".format("\nDADOS"))
    arq.write("\n")
    arq.write("-" * 43)

    arq.write("\n\nNome: {}\n".format(nome))

    arq.write("\nSalário Bruto: R${:.2f}".format(sb))
    arq.write("\nSalário Líquido: R${:.2f}".format(sl))
    arq.write("\nSalário Líquido + Benefícios: R${:.2f}\n".format(sl + va + vr))

    arq.write("\nHoras Trabalhadas: {:.0f}h".format(ht))
    arq.write("\nValor Hora: R${:.2f}".format(vh))

    arq.write("\n\n\nDESCONTOS\n")
    arq.write("_" * 43)
    arq.write("\nValor dos Descontos: R${:.2f}".format(inss + sind + ir + vt))

    arq.write("\nINSS: R${:.2f}".format(inss))
    arq.write("\nSindicato: R${:.2f}".format(sind))
    arq.write("\nIR: R${:.2f}".format(ir))
    arq.write("\nVale Transporte: R${:.2f}".format(vt))

    arq.write("\n\n\nBENEFÍCIOS\n")
    arq.write("_" * 43)
    arq.write("\nTotal dos Benefícios: R${:.2f}".format(va + vr))
    arq.write("\nVale Refeição: R${:.2f}".format(vr))
    arq.write("\nVale Alimentação: R${:.2f}".format(va))
