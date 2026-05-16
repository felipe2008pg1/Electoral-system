## Este projeto está disponível apenas na versão PT-BR. 🇧🇷

# 🗳️ Sistema de Eleição em Python

_Um sistema de votação interativo via linha de comando (CLI) desenvolvido em Python, estruturado de forma modular e com persistência de dados local utilizando arquivos JSON._

## 🚀 Funcionalidades

* **Arquitetura Modular:** Separação clara entre lógica de negócio, utilitários de interface (`tools`) e armazenamento de dados.
* **Persistência de Dados:** Os votos são gravados em tempo real em um arquivo `votos.json`, garantindo que os dados não sejam perdidos ao encerrar o programa.
* **Interface CLI Dinâmica:** Efeitos de digitação lenta e limpeza de tela automatizada para melhorar a experiência do usuário no terminal.
* **Segurança e Validação:** Tratamento de erros para entradas inválidas (`ValueError`) e controle estrito do limite de votos disponíveis.

## 🛠️ Tecnologias Utilizadas

* **Python 3.x**
* **JSON** (para armazenamento local)
* **OS / Time / Datetime** (bibliotecas nativas do Python)

## 📁 Estrutura do Projeto

* `sistema.py`: Arquivo principal contendo o loop da aplicação e o fluxo de votação.
* `tools.py`: Funções utilitárias (limpeza de tela, formatação de menu, exibição de candidatos).
* `votos.json`: Banco de dados local onde os candidatos e o número de votos são computados.

## 🔧 Como Executar

1. Clone o repositório:
   ```bash
   git clone (https://github.com/felipe2008pg1/sistema-eleitoral/edit/main/README.md))
   ```
2. Navegue até a pasta do projeto:
   ```bash
   cd sistema-eleitoral
   ```
3. Execute o sistema:
   ```bash
   python sistema.py
   ```
---
Desenvolvido por [Felipe de la Vega Gonzalez](https://github.com/felipe2008pg1) 🧑‍💻
