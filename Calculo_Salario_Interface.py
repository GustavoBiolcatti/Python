from tkinter import *


class Application:
    def __init__(self, master=None):
        self.fonteTitulo = ("Arial", "12", "bold")
        self.fonteLabelPadrao = ("Arial", "10", "bold")
        self.fontePadrao = ("Arial", "10")
        self.padxPadrao = 50
        self.widthLabelPadrao = 25
        self.widthEntryPadrao = 30
        self.tamanhoBotaoPadrao = 10

        # INTERFACE
        self.interface = Frame(master)
        self.interface["padx"] = 20
        self.interface.pack()

        # TÍTULO
        self.tituloContainer = Frame(self.interface)
        self.tituloContainer["pady"] = 5
        self.tituloContainer.pack()

        self.titulo = Label(self.tituloContainer, text="CALCULO SALARIAL", font=self.fonteTitulo)
        self.titulo.pack()

        # =====================================================================================
        # ======================  CONTEÚDO  ===================================================
        # =====================================================================================

        # INSERIR DADOS
        self.inserirContainer = Frame(self.interface)
        self.inserirContainer.pack()

        self.div = Label(self.tituloContainer, text="_" * 90)
        self.div.pack()

        # --------------------------------------------------------
        # DADOS DO USUÁRIO
        self.dados = Frame(self.inserirContainer)
        self.dados["pady"] = 10
        self.dados.pack()

        self.dadosLabel = Label(self.dados, text="DADOS", font=self.fonteTitulo)
        self.dadosLabel["pady"] = 10
        self.dadosLabel.pack()

        # --------------------------------------------------------
        # NOME
        self.dadosNome = Frame(self.dados)
        self.dadosNome.pack()

        self.nomeLabel = Label(self.dadosNome, text="NOME:", font=self.fonteLabelPadrao)
        self.nomeLabel["width"] = self.widthLabelPadrao
        self.nomeLabel.pack(side=LEFT)

        self.nome = Entry(self.dadosNome)
        self.nome["font"] = self.fontePadrao
        self.nome["width"] = self.widthEntryPadrao
        # self.nome["command"] = self.replacestring
        self.nome.pack(side=RIGHT)

        # --------------------------------------------------------
        # SALÁRIO BRUTO
        self.dadosSalariob = Frame(self.dados)
        self.dadosSalariob["padx"] = self.padxPadrao
        self.dadosSalariob.pack()

        self.salariobLabel = Label(self.dadosSalariob, text="SALÁRIO BRUTO:", font=self.fonteLabelPadrao)
        self.salariobLabel["width"] = self.widthLabelPadrao
        self.salariobLabel.pack(side=LEFT)

        self.salariob = Entry(self.dadosSalariob)
        self.salariob["font"] = self.fontePadrao
        self.salariob["width"] = self.widthEntryPadrao
        # self.salariob["command"] = self.replacevalor
        self.salariob.pack(side=RIGHT)

        # --------------------------------------------------------
        # DIAS TRABALHADOS
        self.dadosDiat = Frame(self.dados)
        self.dadosDiat.pack()

        self.diatLabel = Label(self.dadosDiat, text="DIAS TRABALHADOS:", font=self.fonteLabelPadrao)
        self.diatLabel["width"] = self.widthLabelPadrao
        self.diatLabel.pack(side=LEFT)

        self.diat = Entry(self.dadosDiat)
        self.diat["font"] = self.fontePadrao
        self.diat["width"] = self.widthEntryPadrao
        self.diat.pack(side=RIGHT)

        # --------------------------------------------------------
        # HORÁRIO ENTRADA
        self.dadosHorae = Frame(self.dados)
        self.dadosHorae.pack()

        self.horaeLabel = Label(self.dadosHorae, text="HORA DE ENTRADA:", font=self.fonteLabelPadrao)
        self.horaeLabel["width"] = self.widthLabelPadrao
        self.horaeLabel.pack(side=LEFT)

        self.horae = Entry(self.dadosHorae)
        self.horae["font"] = self.fontePadrao
        self.horae["width"] = self.widthEntryPadrao
        self.horae.pack(side=RIGHT)

        # --------------------------------------------------------
        # HORÁRIO SAÍDA
        self.dadosHoras = Frame(self.dados)
        self.dadosHoras.pack()

        self.horasLabel = Label(self.dadosHoras, text="HORA DE SAÍDA:", font=self.fonteLabelPadrao)
        self.horasLabel["width"] = self.widthLabelPadrao
        self.horasLabel.pack(side=LEFT)

        self.horas = Entry(self.dadosHoras)
        self.horas["font"] = self.fontePadrao
        self.horas["width"] = self.widthEntryPadrao
        self.horas.pack(side=RIGHT)

        self.div = Label(self.dados, text="_" * 90)
        self.div.pack()

        # =====================================================================================
        # ======================  DESCONTOS  ==================================================
        # =====================================================================================

        # DESCONTOS
        self.desconto = Frame(self.inserirContainer)
        self.desconto.pack()

        # --------------------------------------------------------

        self.descontoLabel = Label(self.desconto, text="DESCONTOS (%)", font=self.fonteTitulo)
        self.descontoLabel["pady"] = 10
        self.descontoLabel.pack()

        # --------------------------------------------------------
        # INSS
        self.descontoInss = Frame(self.desconto)
        self.descontoInss.pack()

        self.inssLabel = Label(self.descontoInss, text="INSS:", font=self.fonteLabelPadrao)
        self.inssLabel["width"] = self.widthLabelPadrao
        self.inssLabel.pack(side=LEFT)

        self.inss = Entry(self.descontoInss)
        self.inss["font"] = self.fontePadrao
        self.inss["width"] = self.widthEntryPadrao
        self.inss.pack(side=RIGHT)

        # --------------------------------------------------------
        # SINDICATO
        self.descontoSindicato = Frame(self.desconto)
        self.descontoSindicato.pack()

        self.sindicatoLabel = Label(self.descontoSindicato, text="SINDICATO", font=self.fonteLabelPadrao)
        self.sindicatoLabel["width"] = self.widthLabelPadrao
        self.sindicatoLabel.pack(side=LEFT)

        self.sindicato = Entry(self.descontoSindicato)
        self.sindicato["font"] = self.fontePadrao
        self.sindicato["width"] = self.widthEntryPadrao
        self.sindicato.pack(side=RIGHT)

        # --------------------------------------------------------
        # IMPOSTO DE RENDA
        self.descontoImp = Frame(self.desconto)
        self.descontoImp.pack()

        self.impLabel = Label(self.descontoImp, text="IMPOSTO DE RENDA:", font=self.fonteLabelPadrao)
        self.impLabel["width"] = self.widthLabelPadrao
        self.impLabel.pack(side=LEFT)

        self.imp = Entry(self.descontoImp)
        self.imp["font"] = self.fontePadrao
        self.imp["width"] = self.widthEntryPadrao
        self.imp.pack(side=RIGHT)

        # --------------------------------------------------------
        # VALE TRANSPORTE

        self.descontoVt = Frame(self.desconto)
        self.descontoVt.pack()

        self.vtLabel = Label(self.descontoVt, text="VALE TRANSPORTE:", font=self.fonteLabelPadrao)
        self.vtLabel["width"] = self.widthLabelPadrao
        self.vtLabel.pack(side=LEFT)

        self.vt = Entry(self.descontoVt)
        self.vt["font"] = self.fontePadrao
        self.vt["width"] = self.widthEntryPadrao
        self.vt.pack(side=RIGHT)

        self.div = Label(self.desconto, text="_" * 90)
        self.div.pack()

        # =====================================================================================
        # ======================  BENEFÍCIOS  =================================================
        # =====================================================================================

        # BENEFÍCIOS
        self.beneficio = Frame(self.inserirContainer)
        self.beneficio.pack()

        # --------------------------------------------------------

        self.beneficioLabel = Label(self.beneficio, text="BENEFÍCIOS", font=self.fonteTitulo)
        self.beneficioLabel["pady"] = 10
        self.beneficioLabel.pack()

        # --------------------------------------------------------
        # VALE REFEIÇÃO
        self.beneficioVr = Frame(self.beneficio)
        self.beneficioVr.pack()

        self.vrLabel = Label(self.beneficioVr, text="VALE REFEIÇÃO (DIA):", font=self.fonteLabelPadrao)
        self.vrLabel["width"] = self.widthLabelPadrao
        self.vrLabel.pack(side=LEFT)

        self.vr = Entry(self.beneficioVr)
        self.vr["font"] = self.fontePadrao
        self.vr["width"] = self.widthEntryPadrao
        self.vr.pack(side=RIGHT)

        # --------------------------------------------------------
        # VALE ALIMENTAÇÃO
        self.beneficioVa = Frame(self.beneficio)
        self.beneficioVa.pack()

        self.vaLabel = Label(self.beneficioVa, text="VALE ALIMENTAÇÃO:", font=self.fonteLabelPadrao)
        self.vaLabel["width"] = self.widthLabelPadrao
        self.vaLabel.pack(side=LEFT)

        self.va = Entry(self.beneficioVa)
        self.va["font"] = self.fontePadrao
        self.va["width"] = self.widthEntryPadrao
        self.va.pack(side=RIGHT)

        self.div = Label(self.beneficio, text="_" * 90)
        self.div.pack()

        # =====================================================================================
        # ======================  SALVAR  =====================================================
        # =====================================================================================

        # SALVAR
        self.salvar = Frame(self.interface)
        self.salvar["pady"] = 10
        self.salvar.pack()

        # --------------------------------------------------------
        self.salvarNome = Frame(self.salvar)
        self.salvarNome.pack()

        self.salvarLabel = Label(self.salvarNome, text="SALVAR", font=self.fonteTitulo)
        self.salvarLabel["pady"] = 10
        self.salvarLabel.pack()

        self.nomeLabel = Label(self.salvarNome, text="NOME DO ARQUIVO (.TXT):", font=self.fonteLabelPadrao)
        self.nomeLabel["width"] = self.widthLabelPadrao
        self.nomeLabel.pack(side=LEFT)

        self.nomeArq = Entry(self.salvarNome)
        self.nomeArq["font"] = self.fontePadrao
        self.nomeArq["width"] = self.widthEntryPadrao
        self.nomeArq.pack(side=RIGHT)

        self.div = Label(self.salvar, text="_" * 90)
        self.div.pack()

        # =====================================================================================
        # ======================  BOTÕES  =====================================================
        # =====================================================================================

        # BOTÃO
        self.botao = Frame(self.interface)
        self.botao["pady"] = 10
        self.botao.pack()

        # --------------------------------------------------------
        # B - SAIR
        self.bSair = Button(self.botao)
        self.bSair["width"] = self.tamanhoBotaoPadrao
        self.bSair["text"] = "Sair"
        self.bSair["font"] = self.fonteLabelPadrao
        self.bSair["command"] = self.interface.quit
        self.bSair.pack(side=LEFT)

        # B - LIMPAR
        self.bLimpar = Button(self.botao)
        self.bLimpar["width"] = self.tamanhoBotaoPadrao
        self.bLimpar["text"] = "Limpar"
        self.bLimpar["font"] = self.fonteLabelPadrao
        self.bLimpar.bind("<Button-1>", self.limparEntry)
        self.bLimpar.pack(side=LEFT)

        # B - SALVAR
        self.bSalvar = Button(self.botao)
        self.bSalvar["width"] = self.tamanhoBotaoPadrao
        self.bSalvar["text"] = "Salvar"
        self.bSalvar["font"] = self.fonteLabelPadrao
        self.bSalvar.bind("<Button-1>", self.salvarRes)
        self.bSalvar.pack(side=LEFT)

    def limparEntry(self, event):
        self.nome.delete(0, 'end')
        self.salariob.delete(0, 'end')
        self.diat.delete(0, 'end')
        self.horae.delete(0, 'end')
        self.horas.delete(0, 'end')
        self.inss.delete(0, 'end')
        self.sindicato.delete(0, 'end')
        self.imp.delete(0, 'end')
        self.vt.delete(0, 'end')
        self.vr.delete(0, 'end')
        self.va.delete(0, 'end')
        self.nomeArq.delete(0, 'end')

    def salvarRes(self, event):
        inss = int(str(self.inss.get()).replace(",", ".").strip())
        sind = int(str(self.sindicato.get()).replace(",", ".").strip())
        ir = int(str(self.imp.get()).replace(",", ".").strip())
        vt = int(str(self.vt.get()).replace(",", ".").strip())

        diat = int(str(self.diat.get()).replace(",", ".").strip())

        vr = float(str(self.vr.get()).replace(",", ".").strip()) * diat
        va = float(str(self.va.get()).replace(",", ".").strip())

        nome_arq = str(self.nomeArq.get()).strip()
        nome_arq += ".txt"

        nome = str(self.nome.get()).strip().upper()

        sb = float(str(self.salariob.get()).replace(",", ".").strip())

        desc = inss + sind + ir + vt
        sl = sb - desc

        he = float(str(self.horae.get()).replace(":", ".").strip())
        hs = float(str(self.horas.get()).replace(":", ".").strip())

        ht = (hs - he) * diat

        if ht == 220:
            vh = sb / 220
        else:
            vh = sb / 180

        with open(nome_arq, 'w', encoding='utf-8') as arq:
            arq.write("\n")
            arq.write("{:^43}".format("\nDADOS"))
            arq.write("\n")
            arq.write("_" * 43)

            arq.write("\n\nNome: {}\n".format(nome))

            arq.write("\nSalário Bruto: R${:.2f}".format(sb))
            arq.write("\nSalário Líquido: R${:.2f}".format(sl))
            arq.write("\nSalário Líquido + Benefícios: R${:.2f}\n".format(sl + va + vr))

            arq.write("\nHoras Trabalhadas: {:.0f}h".format(ht))
            arq.write("\nValor Hora: R${:.2f}".format(vh))

            arq.write("\n\n\nDESCONTOS\n")
            arq.write("_" * 43)
            arq.write("\nValor dos Descontos: R${:.2f}".format(desc))

            arq.write("\n\nINSS: R${:.2f}".format(inss))
            arq.write("\nSindicato: R${:.2f}".format(sind))
            arq.write("\nIR: R${:.2f}".format(ir))
            arq.write("\nVale Transporte: R${:.2f}".format(vt))

            arq.write("\n\n\nBENEFÍCIOS\n")
            arq.write("_" * 43)
            arq.write("\nValor dos Benefícios: R${:.2f}".format(vr + va))

            arq.write("\n\nVale Refeição: R${:.2f}".format(vr))
            arq.write("\nVale Alimentação: R${:.2f}".format(va))


root = Tk()
Application(root)
root.mainloop()
