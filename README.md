## This project was originally written in Portuguese and then translated into English. 🇧🇷 🇺🇸

# 🗳️ Web-based Electoral System - 2026 Elections

An interactive and modern voting system developed in **Python** using the **Flask** micro-framework, with local data persistence in *JSON* format and a clean web interface (HTML5/CSS3).

> ⚠️ **DEVELOPMENT NOTICE:** This project is under development. The simulated voting process is currently based on a direct click on the candidate displayed in the user interface. In the future, the system will be updated to reflect the real electoral system, allowing a single vote by typing the candidate's number into an interface that simulates a real electronic voting machine.

> ⚠️ **Disclaimer:** This project was developed for strictly academic and educational purposes for the study of software architecture (Flask/Python/JSON). The application has no connection whatsoever with political parties, coalitions, or real candidates, serving only as a practical programming learning tool.
---

## 🚀 Current Features

* **Responsive Web Interface:** Minimalist and intuitive dark mode panel for counting votes without distractions.
* **Back-End Architecture:** Local web server running clean HTTP routes, handling `GET` (display) and `POST` (vote counting) requests.
* **Data Persistence:** Votes are recorded and updated in real time in the `votes.json` file. If the server is shut down, no data is lost.
* **Isolated Environment:** Ready-to-use configuration with a virtual environment (`venv`), keeping project dependencies organized.

## 📁 Project Structure

```text
sistema-eleitoral-web/
│
├── static/
│   └── style.css       # Page styling and design (CSS)
│
├── templates/
│   └── index.html      # Ballot box structure and interface (HTML)
│
├── app.py              # Main server and application routes (Flask)
├── votos.json          # Local database where votes are stored.
└── .gitignore          # File to ignore useless local files in Git
```

## 🛠️ Technologies Used

* **Python 3.x**
* **Flask** (Micro-framework web)
* **JSON** (Data storage and persistence)
* **HTML5 e CSS3** (Front-End)

---

## 🔧 How to Run the Project Locally

Follow the steps below in your VS Code terminal to run the application:

### 1. Clone the Repository
```bash
git clone [https://github.com/felipe2008pg1/sistema-eleitoral.git](https://github.com/felipe2008pg1/sistema-eleitoral.git)
cd sistema-eleitoral
```

### 2. Create and Activate the Virtual Environment (venv)
* **In Windows (PowerShell):**
  ```powershell
  python -m venv venv
  .\venv\Scripts\Activate.ps1
  ```
* **No Linux/Mac:**
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```

### 3. Install the dependences
With `(venv)` active in your terminal, install Flask.:
```bash
pip install flask
```

### 4. Run the Web Server
Run the main project file:
```bash
python app.py
```

After running the program, open your browser and access the local address provided by the terminal (usually `http://127.0.0.1:5000`).

---
Developed with a focus on back-end logic by [Felipe de la Vega Gonzalez](https://github.com/felipe2008pg1) 🧑‍💻
