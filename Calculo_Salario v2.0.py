nome = str(input("\nDigite seu nome completo: ").upper().strip())

sb = float(input("\nDigite seu salário bruto: ").replace(",", "."))

dt = int(input("\nDigite a quantidade de dias trabalhados: ").replace(",", "."))

he = float(input("\nDigite seu horário de entrada: ").replace(":", "."))
hs = float(input("\nDigite seu horário de saída: ").replace(":", "."))

ht = (hs - he) * dt
vh = sb / ht

# =====================================================================================================================
# DESCONTOS
# =====================================================================================================================
print("\n")
print("-" * 43)
print("{:^43}".format("DESCONTOS"))
print("-" * 43)

# INSS
verif_inss = True
while verif_inss:
    c_inss = str(input("\nÉ descontado INSS? ('s' ou 'n') ").lower())

    if c_inss == "s" or c_inss == "n":
        if c_inss == "s":
            inss = float(sb * int(input("Qual a porcentagem (%) de desconto? ").replace(",", ".")) / 100)
        else:
            inss = 0

        verif_inss = False
    else:
        print("Nenhuma opção selecionada! Digite novamente.")

# SINDICATO
verif_sind = True
while verif_sind:
    c_sind = str(input("\nÉ descontado sindicato? ('s' ou 'n') ").lower())

    if c_sind == "s" or c_sind == "n":
        if c_sind == "s":
            sind = float(sb * int(input("Qual a porcentagem (%) de desconto? ").replace(",", ".")) / 100)
        else:
            sind = 0

        verif_sind = False
    else:
        print("Nenhuma opção selecionada! Digite novamente.")

# IMPOSTO DE RENDA
verif_ir = True
while verif_ir:
    c_ir = str(input("\nÉ descontado IR? ('s' ou 'n') ").lower())

    if c_ir == "s" or c_ir == "n":
        if c_ir == "s":
            ir = float(sb * int(input("Qual a porcentagem (%) de desconto? ").replace(",", ".")) / 100)
        else:
            ir = 0

        verif_ir = False
    else:
        print("Nenhuma opção selecionada! Digite novamente.")

# VALE TRANSPORTE COM DESCONTO
verif_vt = True
while verif_vt:
    c_vt = str(input("\nÉ descontado vale transporte? ('s' ou 'n') ").lower())

    if c_vt == "s" or c_vt == "n":
        if c_vt == "s":
            vt = float(sb * int(input("Qual a porcentagem (%) de desconto? ").replace(",", ".")) / 100)
        else:
            vt = 0

        verif_vt = False
    else:
        print("Nenhuma opção selecionada! Digite novamente.")

# =====================================================================================================================
# BENEFÍCIOS
# =====================================================================================================================
print("\n")
print("-" * 43)
print("{:^43}".format("BENEFÍCIOS"))
print("-" * 43)

# VALE TRANSPORTE SEM DESCONTO
if c_vt == "n":
    verif_vt_b = True
    while verif_vt_b:
        c_vt_b = input("\nDigite o valor para transporte diário recebido: R$").replace(",", ".")

        if not c_vt_b.isalpha():
            vt_b = int(c_vt_b) * dt
            verif_vt_b = False
        else:
            print("Nenhum valor inserido! Digite novamente.")

# VALE REFEIÇÃO
c_vr = str(input("\nPossui vale refeição? ('s' ou 'n') ").lower())
if c_vr == "s":
    vr = float(input("Digite o valor diário: R$").replace(",", "."))
    vr = vr*dt
else:
    vr = 0

# VALE ALIMENTAÇÃO
c_va = str(input("\nPossui vale alimentação? ('s' ou 'n') ").lower())
if c_va == "s":
    va = float(input("Digite o valor (por dia): R$").replace(",", ".")) * dt

else:
    va = 0

sl = float(sb - (inss + sind + ir + vt))

# =====================================================================================================================
# VERIFICAÇÃO DE SALVAMENTO
# =====================================================================================================================
verif_save = True
while verif_save:
    save = input("\nDeseja salvar o resultado? ('s' ou 'n') ").lower()

    if save == "s" or save == "n":
        verif_save = False
    else:
        print("Nenhuma opção selecionada! Digite novamente.")

if save == "s":
    # SALVAR OS RESULTADOS
    verif_nomearq = True
    while verif_nomearq:
        nome_arq = input("Digite o nome do arquivo: ")

        if nome_arq == "":
            verif_nomenull = True
            while verif_nomenull:
                nome_null = input("\nO nome do arquivo não foi preenchido!\nDeseja continuar mesmo assim? ('s' ou 'n') ")

                if nome_null == "s" or nome_null == "n":
                    verif_nomenull = False
                else:
                    print("Nenhuma opção selecionada! Digite novamente.")

        else:
            nome_arq += ".txt"
            verif_nomearq = False

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

        if c_vt == "n":
            arq.write("\nTotal dos Benefícios: R${:.2f}".format(va + vr + vt_b))
        else:
            arq.write("\nTotal dos Benefícios: R${:.2f}".format(va + vr))

        if c_vt == "n":
            arq.write("\nVale Transporte: R${:.2f}".format(vt_b))

        arq.write("\nVale Refeição: R${:.2f}".format(vr))
        arq.write("\nVale Alimentação: R${:.2f}".format(va))

else:
    # NÃO SALVAR OS RESULTADOS
    print("\n\n")
    print("-" * 43)
    print("{:^43}".format("DADOS"))
    print("-" * 43)

    print("\nNome: {}".format(nome))

    print("\nSalário Bruto: R${:.2f}".format(sb))
    print("Salário Líquido: R${:.2f}".format(sl))
    print("\nSalário Líquido + Benefícios: R${:.2f}".format(sl + va + vr))

    print("\nHoras Trabalhadas: {:.0f}h".format(ht))
    print("Valor Hora: R${:.2f}".format(vh))

    print("\n\nDESCONTOS")
    print("_" * 43)
    print("Valor dos Descontos: R${:.2f}".format(inss + sind + ir + vt))

    print("\nINSS: R${:.2f}".format(inss))
    print("Sindicato: R${:.2f}".format(sind))
    print("IR: R${:.2f}".format(ir))
    print("Vale Transporte: R${:.2f}".format(vt))

    print("\n\nBENEFÍCIOS")
    print("_" * 43)

    if c_vt == "n":
        print("Total dos Benefícios: R${:.2f}".format(va + vr + vt_b))
    else:
        print("Total dos Benefícios: R${:.2f}".format(va + vr))

    if c_vt == "n":
        print("\nVale Transporte: R${:.2f}".format(vt_b))

    print("\nVale Refeição: R${:.2f}".format(vr))
    print("Vale Alimentação: R${:.2f}".format(va))
