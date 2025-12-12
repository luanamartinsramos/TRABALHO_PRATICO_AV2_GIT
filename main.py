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

