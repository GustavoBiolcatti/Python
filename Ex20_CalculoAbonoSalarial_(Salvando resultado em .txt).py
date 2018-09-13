sal = []
abono = []
col = 0
val_min = 0

print("Projeção de Gastos com Abono")
print("=" * 28)
print("\n\n")

#INSERIR SALÁRIO

verif_sal = True
while verif_sal:
	val = float(input("Salário: R$").replace(",", "."))

	if val == 0:
		verif_sal = False
	else:
		sal += [val]
		col += 1

#CALCULO DO ABONO

i = 1
while i in range(len(sal) + 1):
	abn = sal[i-1] * 0.2
	
	if abn > 100:
		abono.append(abn)
	else:
		abono.append(100)
		val_min += 1

	i += 1

print("\n\n")

verif_save = True
nome_arq = "a"
while verif_save:
	save = input("Deseja salvar os resultados? (s / n) ").lower()

	if save[0] != "":
		if save[0] == "n":
			#NÃO SALVAR OS RESULTADOS

			print("{:^12} - {:^12}".format("Salário", "Abono"))

			i = 1
			for i in range(len(sal)):
				print("Salário: R${:10.2f} - Abono: R${:10.2f}".format(sal[i-1], abono[i-1]))

			print("\n\nForam processados {} colaboradores.".format(col))
			print("Total gasto com abonos: R${:.2f}".format(sum(abono)))
			print("Valor mínimo pago a {} colaboradores".format(val_min))
			print("Maior valor de abono pago: R${:.2f}".format(max(abono)))

			verif_save = False

		if save[0] == "s":
			nome_arq = input("Digite o nome do arquivo: ")
			nome_arq += ".txt"

			#SALVAR OS RESULTADOS

			with open(nome_arq, "w", encoding="utf-8") as arq:
				arq.write("{:^12} - {:^12}\n".format("Salário", "Abono"))

				i = 1
				for i in range(len(sal)):
					arq.write("\nR${:10.2f} - R${:10.2f}".format(sal[i-1], abono[i-1]))

				arq.write("\n\n\nForam processados {} colaboradores".format(col))
				arq.write("\nTotal gasto com abonos: R${:.2f}".format(sum(abono)))
				arq.write("\nValor mínimo pago a {} colaboradores".format(val_min))
				arq.write("\nMaior valor de abono pago: R${:.2f}".format(max(abono)))

			verif_save = False
	else:
		print("Nenhuma opção selecionada!")
