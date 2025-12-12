import pandas as pd
import os

ARQUIVO_CSV = "alunos.csv"

CAMPOS = [
    "matricula",
    "nome",
    "rua",
    "numero",
    "bairro",
    "cidade",
    "uf",
    "telefone",
    "email"
]

def carregar_dados():
    if os.path.exists(ARQUIVO_CSV):
        df = pd.read_csv(ARQUIVO_CSV)
        if "matricula" in df.columns:
            df["matricula"] = df["matricula"].astype(int)
    else:
        df = pd.DataFrame(columns=CAMPOS)
    return df

def salvar_dados(df):
    df.to_csv(ARQUIVO_CSV, index=False)

def gerar_matricula(df):
    if df.empty:
        return 1
    return int(df["matricula"].max()) + 1

def menu():
    print("\n=== MENU ALUNOS ===")
    print("1 - INSERIR")
    print("2 - PESQUISAR / EDITAR / REMOVER")
    print("3 - SAIR")
    opcao = input("Escolha uma opção: ")
    return opcao

def inserir_aluno(df):
    nova_matricula = gerar_matricula(df)
    print(f"\nNova matrícula gerada: {nova_matricula}")

    nome = input("Nome: ")
    rua = input("Rua: ")
    numero = input("Número: ")
    bairro = input("Bairro: ")
    cidade = input("Cidade: ")
    uf = input("UF: ")
    telefone = input("Telefone: ")
    email = input("E-mail: ")

    novo_registro = {
        "matricula": nova_matricula,
        "nome": nome,
        "rua": rua,
        "numero": numero,
        "bairro": bairro,
        "cidade": cidade,
        "uf": uf,
        "telefone": telefone,
        "email": email
    }

    df = pd.concat([df, pd.DataFrame([novo_registro])], ignore_index=True)
    print("Aluno cadastrado com sucesso!")
    return df

def mostrar_dados_aluno(linha):
    print("\n=== DADOS DO ALUNO ===")
    print(f"Matrícula: {linha['matricula']}")
    print(f"Nome: {linha['nome']}")
    print(f"Rua: {linha['rua']}")
    print(f"Número: {linha['numero']}")
    print(f"Bairro: {linha['bairro']}")
    print(f"Cidade: {linha['cidade']}")
    print(f"UF: {linha['uf']}")
    print(f"Telefone: {linha['telefone']}")
    print(f"E-mail: {linha['email']}")

def editar_aluno(df, idx):
    while True:
        print("\nQual dado deseja editar?")
        print("1 - Nome")
        print("2 - Rua")
        print("3 - Número")
        print("4 - Bairro")
        print("5 - Cidade")
        print("6 - UF")
        print("7 - Telefone")
        print("8 - E-mail")
        print("9 - Voltar")
        opc = input("Escolha a opção: ")

        if opc == "1":
            df.at[idx, "nome"] = input("Novo nome: ")
        elif opc == "2":
            df.at[idx, "rua"] = input("Nova rua: ")
        elif opc == "3":
            df.at[idx, "numero"] = input("Novo número: ")
        elif opc == "4":
            df.at[idx, "bairro"] = input("Novo bairro: ")
        elif opc == "5":
            df.at[idx, "cidade"] = input("Nova cidade: ")
        elif opc == "6":
            df.at[idx, "uf"] = input("Nova UF: ")
        elif opc == "7":
            df.at[idx, "telefone"] = input("Novo telefone: ")
        elif opc == "8":
            df.at[idx, "email"] = input("Novo e-mail: ")
        elif opc == "9":
            break
        else:
            print("Opção inválida.")
            continue

        print("Dado atualizado com sucesso!")

    return df

def remover_aluno(df, idx):
    confirma = input("Tem certeza que deseja remover este aluno? (S/N): ")
    if confirma.upper() == "S":
        df = df.drop(index=idx).reset_index(drop=True)
        print("Aluno removido com sucesso!")
    else:
        print("Remoção cancelada.")
    return df



def buscar_indice_aluno(df):
    print("\nPesquisar por:")
    print("1 - Matrícula")
    print("2 - Nome")
    tipo = input("Escolha a opção: ")

    if tipo == "1":
        matricula = input("Digite a matrícula: ")
        try:
            matricula = int(matricula)
        except ValueError:
            print("Matrícula inválida.")
            return None
        filtro = df["matricula"] == matricula
    elif tipo == "2":
        nome = input("Digite o nome (ou parte dele): ")
        filtro = df["nome"].fillna("").str.lower().str.contains(nome.lower(), regex=False)
    else:
        print("Opção de pesquisa inválida.")
        return None

    resultado = df[filtro]

    if resultado.empty:
        print("Aluno não encontrado.")
        input("\nPressione ENTER para voltar...")
        return None

   
    if len(resultado) > 1:
        print(f"\nEncontrados {len(resultado)} alunos:")
        for i, (idx, linha) in enumerate(resultado.iterrows(), 1):
            print(f"{i}. {linha['nome']} (Matrícula: {linha['matricula']})")
        escolha = input("\nEscolha o número do aluno (ou 0 para cancelar): ")
        try:
            num = int(escolha)
            if num == 0:
                return None
            if 1 <= num <= len(resultado):
                idx = resultado.index[num - 1]
            else:
                print("Número inválido.")
                return None
        except ValueError:
            print("Entrada inválida.")
            return None
    else:
        idx = resultado.index[0]
    
    linha = df.loc[idx]
    mostrar_dados_aluno(linha)
    return idx

def acao_pesquisar(df):
    idx = buscar_indice_aluno(df)
    if idx is not None:
        input("\nPressione ENTER para continuar...")
    return df

def acao_editar_por_pesquisa(df):
    idx = buscar_indice_aluno(df)
    if idx is not None:
        df = editar_aluno(df, idx)
        salvar_dados(df)
    return df

def acao_remover_por_pesquisa(df):
    idx = buscar_indice_aluno(df)
    if idx is not None:
        df = remover_aluno(df, idx)
        salvar_dados(df)
        print("\nDados salvos com sucesso!")
    return df

def menu_aluno(df):
    if df.empty:
        print("Nenhum aluno cadastrado.")
        return df

    while True:
        print("\n=== MENU ALUNO ===")
        print("1 - PESQUISAR ALUNO")
        print("2 - EDITAR ALUNO")
        print("3 - REMOVER ALUNO")
        print("4 - VOLTAR AO MENU PRINCIPAL")
        opc = input("Escolha uma opção: ")

        if opc == "1":
            df = acao_pesquisar(df)
        elif opc == "2":
            df = acao_editar_por_pesquisa(df)
        elif opc == "3":
            df = acao_remover_por_pesquisa(df)
        elif opc == "4":
            break
        else:
            print("Opção inválida.")

    return df

def main():
    df = carregar_dados()

    while True:
        opcao = menu()

        if opcao == "1":
            df = inserir_aluno(df)
            salvar_dados(df)

        elif opcao == "2":
            df = menu_aluno(df)
            salvar_dados(df)

        elif opcao == "3":
            print("Saindo...")
            salvar_dados(df)
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()

    
