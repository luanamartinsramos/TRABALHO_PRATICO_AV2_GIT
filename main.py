import pandas as pd
import os
import re

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
    print("2 - PESQUISAR")
    print("3 - SAIR")
    opcao = input("Escolha uma opção: ")
    return opcao

def input_obrigatorio(mensagem):
    while True:
        valor = input(mensagem).strip()
        if valor:
            return valor
        print("ERRO: Este campo não pode ficar vazio! Por favor, preencha.")

def input_numero(mensagem):
    while True:
        valor = input(mensagem).strip()
        if not valor:
            print("ERRO: Este campo não pode ficar vazio! Por favor, preencha.")
            continue
        if valor.isdigit():
            return valor
        print("ERRO: Digite apenas números!")

def input_telefone(mensagem):
    while True:
        valor = input(mensagem).strip()
        if not valor:
            print("ERRO: Este campo não pode ficar vazio! Por favor, preencha.")
            continue
        
        telefone_limpo = re.sub(r'[^\d]', '', valor)
        if not telefone_limpo:
            print("ERRO: Telefone deve conter números!")
            continue
        if len(telefone_limpo) < 8:
            print("ERRO: Telefone deve ter no mínimo 8 dígitos!")
            continue
        if len(telefone_limpo) > 11:
            print("ERRO: Telefone deve ter no máximo 11 dígitos!")
            continue
        return valor  

def input_email(mensagem):
    while True:
        valor = input(mensagem).strip()
        if not valor:
            print("ERRO: Este campo não pode ficar vazio! Por favor, preencha.")
            continue
        
        padrao_email = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if re.match(padrao_email, valor):
            return valor
        print("ERRO: E-mail inválido! Use o formato: exemplo@dominio.com")

def input_uf(mensagem):
    while True:
        valor = input(mensagem).strip().upper()
        if not valor:
            print("ERRO: Este campo não pode ficar vazio! Por favor, preencha.")
            continue
        if len(valor) == 2 and valor.isalpha():
            return valor
        print("ERRO: UF deve ter exatamente 2 letras! (Ex: SP, RJ, MG)")

def input_texto(mensagem):
    while True:
        valor = input(mensagem).strip()
        if not valor:
            print("ERRO: Este campo não pode ficar vazio! Por favor, preencha.")
            continue
        if any(char.isalpha() for char in valor):
            return valor
        print("ERRO: Este campo deve conter pelo menos uma letra!")

def inserir_aluno(df):
    nova_matricula = gerar_matricula(df)
    print(f"\nNova matrícula gerada: {nova_matricula}")

    nome = input_texto("Nome: ")
    rua = input_texto("Rua: ")
    numero = input_numero("Número: ")
    bairro = input_texto("Bairro: ")
    cidade = input_texto("Cidade: ")
    uf = input_uf("UF: ")
    telefone = input_telefone("Telefone: ")
    email = input_email("E-mail: ")

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
            df.at[idx, "nome"] = input_texto("Novo nome: ")
        elif opc == "2":
            df.at[idx, "rua"] = input_texto("Nova rua: ")
        elif opc == "3":
            df.at[idx, "numero"] = input_numero("Novo número: ")
        elif opc == "4":
            df.at[idx, "bairro"] = input_texto("Novo bairro: ")
        elif opc == "5":
            df.at[idx, "cidade"] = input_texto("Nova cidade: ")
        elif opc == "6":
            df.at[idx, "uf"] = input_uf("Nova UF: ")
        elif opc == "7":
            df.at[idx, "telefone"] = input_telefone("Novo telefone: ")
        elif opc == "8":
            df.at[idx, "email"] = input_email("Novo e-mail: ")
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

def menu_aluno(df):
    if df.empty:
        print("Nenhum aluno cadastrado.")
        return df

    idx = buscar_indice_aluno(df)
    if idx is None:
        return df
    
    # Pergunta se deseja editar
    editar = input("\nDeseja EDITAR algum dado deste aluno? (S/N): ")
    if editar.upper() == "S":
        df = editar_aluno(df, idx)
        salvar_dados(df)
        print("\nDados salvos com sucesso!")
        return df
    
    # Pergunta se deseja remover
    remover = input("\nDeseja REMOVER este aluno? (S/N): ")
    if remover.upper() == "S":
        df = remover_aluno(df, idx)
        salvar_dados(df)
        print("\nDados salvos com sucesso!")
    
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

    
