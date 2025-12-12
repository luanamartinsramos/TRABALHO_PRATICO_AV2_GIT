# Sistema de Cadastro de Alunos

Desenvolvido por:
- Luana Martins Ramos 06014936
- Arthur Jorge de Godoy Silva 06013964

## Descrição

Este projeto é um sistema simples de cadastro de alunos em Python.

O programa permite:
- Inserir novos alunos com geração automática de matrícula.
- Pesquisar alunos pelo número de matrícula ou pelo nome (sem diferenciar maiúsculas e minúsculas).
- Editar os dados de um aluno já cadastrado (exceto a matrícula).
- Remover um aluno do cadastro com confirmação e excluir seu ID (Número da matrícula) Permanentemente pois cada matrícula é unica.
- Salvar e carregar todos os dados em arquivo `.csv` usando `pandas`, mantendo os cadastros entre as execuções.

Aprendizado:
- Estruturas de dados básicas (listas e dicionários).
- Modularização com funções.
- Manipulação de arquivos com `pandas`.
- Uso de Git e GitHub no controle de versão.

  ## Requisitos

- Python 3 instalado na máquina.
- Biblioteca `pandas` instalada.

Para instalar o `pandas`, use: pip install pandas

## Como executar o projeto

1. Clone este repositório ou faça o download dos arquivos.
2. Abra a pasta do projeto no terminal.
3. Execute o arquivo principal com: python main.py

   
Ao executar o programa, será exibido o menu principal:

- `1 - INSERIR`: cadastra um novo aluno.
- `2 - PESQUISAR `: abre o menu para a pesquisa por nome ou matrícula pnde você terá a opção de editar qualquer dado exceto o número da matrícula.
Caso não queira editar abre a opção de deletar o aluno deletando seus dados e seu número de matrícula permanentemente.
- `3 - SAIR`: salva os dados e encerra o programa.

Sempre que o programa é executado, ele lê os dados existentes do arquivo `alunos.csv`.  
Ao inserir, editar ou remover alunos, o arquivo é atualizado automaticamente.

## Controle de versão (Git e GitHub)

Durante o desenvolvimento foram feitos commits frequentes para registrar a evolução do projeto.

Boas práticas adotadas:
- Commits pequenos e frequentes, sempre após alguma mudança relevante.
- Mensagens de commit claras, explicando o que foi alterado (ex.: `Adiciona função de inserção de alunos`, `Implementa pesquisa por matrícula`, `Ajusta edição de dados`, etc.).
- Uso do repositório remoto no GitHub para manter o histórico do código e facilitar a correção.

<img width="337" height="710" alt="image" src="https://github.com/user-attachments/assets/7ecff529-12e5-480a-92c9-867814c993f8" />
<img width="364" height="563" alt="image" src="https://github.com/user-attachments/assets/78493ef2-0781-4f0b-82ed-8d59850206f6" />
<img width="389" height="407" alt="image" src="https://github.com/user-attachments/assets/ca0c2578-f012-4bc1-bd47-c28e44d0ebf7" />





