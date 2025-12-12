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


def main():
    
    
    df = carregar_dados()

    while True:
        opcao = menu()

        if opcao == "1":
            df = inserir_aluno(df)
            salvar_dados(df)

        elif opcao == "2":
            
            pass
        elif opcao == "3":
            print("Saindo...")
            salvar_dados(df)
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()
