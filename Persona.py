import os

class Personagem():
    def __init__(self, nome, descricao, imglink, programa, animador):
        self.nome = nome
        self.descricao = descricao
        self.imglink = imglink
        self.programa = programa
        self.animador = animador

class Programa():
    def __init__(self, nome):
        self.nome = nome

class Animador():
    def __init__(self, nome):
        self.nome = nome

lista_personagens=[]
lista_programas=[]
lista_animadores=[]
lista_nomes=[]

def menu():
    os.system('cls')
    print("Menu\n\nO que deseja fazer:\n")
    print("1 - Cadastrar personagem")
    print("2 - Cadastrar programa")
    print("3 - Cadastrar animador(a)")
    print("4 - Listas")
    print("0 - Sair")
    
    try:
        acao = int(input("\nDigite a ação aqui:")) 
    except ValueError:
        os.system('cls')
        input("Entrada inválida. Pressione ENTER para tentar novamente.")
        menu()
    if acao == "":
        os.system('cls')
        input("Entrada inválida. Pressione ENTER para tentar novamente.")
        menu()
        
    if acao == 1 and len(lista_animadores) <= 0 and len(lista_programas) <= 0:
        os.system('cls')
        print("Não é possivel cadastrar personagens sem antes cadastrar um(a) animador(a) e um programa.")
        input("\n" + "Pressione ENTER para voltar ao Menu.")
        menu()
    elif acao == 1 and len(lista_animadores) <= 0:
        os.system('cls')
        print("Não é possivel cadastrar personagens sem antes cadastrar um(a) animador(a).")
        input("\n" + "Pressione ENTER para voltar ao Menu.")
        menu()
    elif acao == 1 and len(lista_programas) <= 0:
        os.system('cls')
        print("Não é possivel cadastrar personagens sem antes cadastrar um programa.")
        input("\n" + "Pressione ENTER para voltar ao Menu.")
        menu()
    

    if acao == 1:
        cadastro_personagem()
    elif acao == 2:
        cadastro_programa()
    elif acao == 3:
        cadastro_animador()
    elif acao == 4:
        exibir_listas()
    elif acao == 0:
        print("\nSessão encerrada.\n")
        exit()

def cadastro_personagem():
    os.system('cls')
    
    print("Cadastro De Personagens")
    nome = input("\n0 - cancelar e voltar ao Menu.\nDigite o nome do personagem:\n")
    
    if nome in lista_nomes:
        os.system('cls')
        print("Personagem já cadastrado.")
        input("Pressione ENTER para voltar ao Menu.")
        menu()
            
    if nome == "0":
            menu()
    
    descricao = input("\n0 - cancelar e voltar ao Menu.\nDigite a descrição do personagem:\n")
    if descricao == "0":
            menu()
    
    imglink = input("\n0 - cancelar e voltar ao Menu.\nInsira um link de imagem do personagem:\n")
    if imglink == "0":
            menu()
    
    print("\n"+"Programas cadastrados: ",lista_programas)
    programa = input("\n0 - cancelar e voltar ao Menu.\nDigite o nome do programa do personagem:\n")
    
    while True:
        if programa == "0":
            menu()
            break
        
        if programa in lista_programas:
            break
        else:
            print("\nO programa informado não está cadastrado. Tente novamente.")
            print("0 - Cancelar e voltar ao Menu.")
            programa = input("\nDigite o nome do programa:\n")
    
    print("\n"+"Animadores cadastrados: ",lista_animadores)
    animador = input("\n0 - cancelar e voltar ao Menu.\nDigite o nome do animador(a):\n")
    
    while True:
        if animador == "0":
            menu()
            break
        
        if animador in lista_animadores:
            break
        
        else:
            print("\nO(A) animador(a) informado(a) não está cadastrado(a). Tente novamente.")
            print("0 - Cancelar e voltar ao Menu.")
            animador = input("\nDigite o nome do animador(a):\n")
            
    personagem = Personagem(nome, descricao, imglink, programa, animador)
    lista_personagens.append(personagem)
    lista_nomes.append(personagem.nome)
    
    
    print("\nPersonagem cadastrado com sucesso!")
    input("Pressione ENTER para voltar ao Menu.")
    menu()

def cadastro_programa():
    
    os.system('cls')
    print("Cadastro De Programas\n")

    nome = input("0 - cancelar e voltar ao Menu.\nDigite o nome do programa:\n")
    
    if nome == "":
        os.system('cls')
        input("Entrada inválida. Pressione ENTER para tentar novamente.")
        cadastro_programa()

    if nome in lista_programas:
        os.system('cls')
        print("Programa já cadastrado.")
        input("Pressione ENTER para voltar ao Menu.")
        menu()
    
    if nome == "0":
            menu()
    
    programa = Programa(nome)
    
    lista_programas.append(programa.nome)
    
    print("\nPrograma cadastrado com sucesso!")
    input("Pressione ENTER para voltar ao Menu.")
    menu()

def cadastro_animador():
    
    os.system('cls')
    
    print("Cadastro De Animadores\n")
    
    nome = input("0 - cancelar e voltar ao Menu.\nDigite o nome do animador(a):\n")

    if nome == "":
        os.system('cls')
        input("Entrada inválida. Pressione ENTER para tentar novamente.")
        cadastro_animador()
    
    if nome in lista_animadores:
        os.system('cls')
        print("Animador(a) já cadastrado(a).")
        input("Pressione ENTER para voltar ao Menu.")
        menu()
    
    if nome == "0":
            menu()
    
    animador = Animador(nome)
    
    lista_animadores.append(animador.nome)
    
    print("\nAnimador(a) cadastrado com sucesso!")
    input("Pressione ENTER para voltar ao Menu.")
    menu()

def exibir_listas():
    os.system('cls')
    print("Listas\n")
    print("1 - Lista de personagens")
    print("2 - Lista de programas")
    print("3 - Lista de animadores")
    print("0 - Voltar ao Menu.")
    
    try:
        acao= int(input("\nDigite a ação aqui:"))
    except ValueError:
        os.system('cls')
        input("Entrada inválida. Pressione ENTER para tentar novamente.")
        exibir_listas()
    if acao == "":
        os.system('cls')
        input("Entrada inválida. Pressione ENTER para tentar novamente.")
        exibir_listas()

    if acao == 1 and len(lista_personagens) <= 0:
        os.system('cls')
        print("Nenhum personagem cadastrado.")
        input("\n" + "Pressione ENTER para voltar para Listas.")
        exibir_listas()
    elif acao == 2 and len(lista_programas) <= 0:
        os.system('cls')
        print("Nenhum programa cadastrado.")
        input("\n" + "Pressione ENTER para voltar para Listas.")
        exibir_listas()
    elif acao == 3 and len(lista_animadores) <= 0:
        os.system('cls')
        print("Nenhum animador(a) cadastrado(a).")
        input("\n" + "Pressione ENTER para voltar para Listas.")
        exibir_listas()

    if acao == 1:
        os.system('cls')
        lista_exibida = [f"{i + 1} - {x}" for (i, x) in enumerate(lista_nomes)]
        print("Lista de personagens\n")
        print(lista_exibida)
        try:
            posicao = int(input("\n0 - Voltar para Listas.\nDigite a posição do personagem para mais informações:\n")) - 1
        except ValueError:
            os.system('cls')
            input("Entrada inválida. Pressione ENTER para tentar novamente.")
            exibir_listas()
        
        if posicao == "":
            os.system('cls')
            input("Entrada inválida. Pressione ENTER para tentar novamente.")
            exibir_listas()
        
        if posicao == -1:
            exibir_listas()
       
        personagem = lista_personagens[posicao]
        if personagem in lista_personagens:
            os.system('cls')
            print("\n Nome:", personagem.nome, "\n",
            "Descrição: ", personagem.descricao,"\n",
            "Imagem (link): ", personagem.imglink,"\n",
            "Programa: ", personagem.programa,"\n",
            "Animador(a): ", personagem.animador)

        input("\n" + "Pressione ENTER para voltar para Listas.")
        exibir_listas()            
        
    elif acao == 2:
        os.system('cls')
        print("Lista de programas\n")
        print(lista_programas)
        input("\n" + "Pressione ENTER para voltar para Listas.")
        exibir_listas()
    elif acao == 3:
        os.system('cls')
        print("Lista de animadores\n")
        print(lista_animadores)
        input("\n" + "Pressione ENTER para voltar para Listas.")
        exibir_listas()
    elif acao == 0:
        menu()


menu()