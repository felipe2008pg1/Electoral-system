# 🗳️ Sistema Eleitoral Web - Eleições 2026

Um sistema de votação interativo e moderno desenvolvido em **Python** utilizando o micro-framework **Flask**, com persistência de dados local em formato **JSON** e interface web limpa (HTML5/CSS3).

> ⚠️ **AVISO DE DESENVOLVIMENTO:** Este projeto está em fase de desenvolvimento. O processo de votação simulado atualmente é baseado no clique direto no candidato exibido na interface de usuário. Futuramente, o sistema será atualizado para refletir o sistema eleitoral real, permitindo a votação através da digitação do número do candidato em uma interface que simula uma urna eletrônica de verdade.

> ⚠️ **Aviso de Isenção de Responsabilidade:** Este projeto foi desenvolvido com fins estritamente acadêmicos e pedagógicos para estudo de arquitetura de software (Flask/Python/JSON). A aplicação não possui qualquer vínculo com partidos políticos, coligações ou candidatos reais, servindo apenas como ferramenta de aprendizado prático de programação.

---

## 🚀 Funcionalidades Atuais

* **Interface Web Responsiva:** Painel escuro (*Dark Mode*) minimalista e intuitivo para computar os votos sem distrações.
* **Arquitetura Back-End:** Servidor web local rodando rotas HTTP de forma limpa, tratando requisições `GET` (exibição) e `POST` (computação de votos).
* **Persistência de Dados:** Os votos são gravados e atualizados em tempo real no arquivo `votos.json`. Se o servidor for desligado, nenhum dado é perdido.
* **Ambiente Isolado:** Configuração pronta para uso com ambiente virtual (`venv`), mantendo as dependências do projeto organizadas.

## 📁 Estrutura do Projeto

```text
sistema-eleitoral-web/
│
├── static/
│   └── style.css       # Estilização e design da página (CSS)
│
├── templates/
│   └── index.html      # Estrutura e interface da urna (HTML)
│
├── app.py              # Servidor principal e rotas da aplicação (Flask)
├── votos.json          # Banco de dados local onde os votos são persistidos
└── .gitignore          # Arquivo para ignorar arquivos locais inúteis no Git
```

## 🛠️ Tecnologias Utilizadas

* **Python 3.x**
* **Flask** (Micro-framework web)
* **JSON** (Armazenamento e persistência de dados)
* **HTML5 e CSS3** (Front-End)

---

## 🔧 Como Executar o Projeto Localmente

Siga os passos abaixo no terminal do seu VS Code para rodar a aplicação:

### 1. Clonar o Repositório
```bash
git clone [https://github.com/felipe2008pg1/sistema-eleitoral.git](https://github.com/felipe2008pg1/sistema-eleitoral.git)
cd sistema-eleitoral
```

### 2. Criar e Ativar o Ambiente Virtual (venv)
* **No Windows (PowerShell):**
  ```powershell
  python -m venv venv
  .\venv\Scripts\Activate.ps1
  ```
* **No Linux/Mac:**
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```

### 3. Instalar as Dependências
Com o `(venv)` ativo no seu terminal, instale o Flask:
```bash
pip install flask
```

### 4. Rodar o Servidor Web
Execute o arquivo principal do projeto:
```bash
python app.py
```

Após executar, abra o seu navegador e acesse o endereço local fornecido pelo terminal (geralmente `http://127.0.0.1:5000`).

---
Desenvolvido com foco em lógica de Back-End por [Felipe de la Vega Gonzalez](https://github.com/felipe2008pg1) 🧑‍💻
