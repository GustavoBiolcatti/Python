from tkinter import *


class Application:
    def __init__(self, master=None):
        self.fonteTitulo = ("Arial", "12", "bold")
        self.fonteLabelPadrao = ("Arial", "10", "bold")
        self.fontePadrao = ("Arial", "10")
        self.padxPadrao = 50
        self.widthLabelPadrao = 20
        self.widthEntryPadrao = 30

        # INTERFACE
        self.interface = Frame(master)
        self.interface["padx"] = 20
        self.interface.pack()

        # TÍTULO
        self.tituloContainer = Frame(self.interface)
        self.tituloContainer["pady"] = 5
        self.tituloContainer.pack()

        # INSERIR DADOS
        self.inserirContainer = Frame(self.interface)
        self.inserirContainer.pack()

        # DADOS DO USUÁRIO
        self.dados = Frame(self.inserirContainer)
        self.dados["pady"] = 10
        self.dados.pack()

        # DESCONTOS
        self.desconto = Frame(self.inserirContainer)
        self.desconto.pack()

        # BENEFÍCIOS
        self.beneficio = Frame(self.inserirContainer)
        self.beneficio.pack()

        # BOTÃO
        self.botao = Frame(self.interface)
        self.botao["pady"] = 10
        self.botao.pack()

        # =====================================================================================
        # ======================  CONTEÚDO  ===================================================
        # =====================================================================================

        # TÍTULO
        self.titulo = Label(self.tituloContainer, text="CALCULO SALARIAL", font=self.fonteTitulo)
        self.titulo.pack()

        self.div = Label(self.tituloContainer, text="_" * 90)
        self.div.pack()

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

    # def replacevalores(self):
        # if str(self.salariob).isnumeric():
            # salariob_r = str(self.salariob).replace(",", ".")
        # else:
            # self.salariob["text"] = "Valor inválido"

        self.div = Label(self.dados, text="_" * 90)
        self.div.pack()

        # =====================================================================================
        # ======================  DESCONTOS  ==================================================
        # =====================================================================================

        self.descontoLabel = Label(self.desconto, text="DESCONTOS (%)", font=self.fonteLabelPadrao)
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

        self.beneficioLabel = Label(self.beneficio, text="BENEFÍCIOS", font=self.fonteLabelPadrao)
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
        # ======================  BOTÕES  =====================================================
        # =====================================================================================

        # SAIR
        self.sair = Button(self.botao)
        self.sair["text"] = "Sair"
        self.sair["font"] = self.fonteLabelPadrao
        self.sair["command"] = self.interface.quit
        self.sair.pack(side=LEFT)

        # LIMPAR
        self.limpar = Button(self.botao)
        self.limpar["text"] = "Limpar"
        self.limpar["font"] = self.fonteLabelPadrao
        self.limpar.bind("<Button-1>", self.limparEntry)
        self.limpar.pack(side=LEFT)

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


root = Tk()
Application(root)
root.mainloop()
