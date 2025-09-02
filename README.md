# 🧮 Calculadora de IMC (Flet)

Este projeto é uma **aplicação gráfica em Python** desenvolvida com o [Flet](https://flet.dev/), que permite calcular o **Índice de Massa Corporal (IMC)** a partir do peso e altura informados pelo usuário.  
O app também classifica o resultado em **baixo peso, peso normal, sobrepeso ou obesidade**, com cores e mensagens diferentes.

---

## 🚀 Funcionalidades

- Inserir **peso (kg)** e **altura (m)**.  
- Calcular o **IMC = Peso / (Altura × Altura)**.  
- Exibir a **classificação**:  
  - **Baixo peso**: IMC < 18,5  
  - **Peso normal**: 18,5 ≤ IMC < 25  
  - **Sobrepeso**: 25 ≤ IMC < 30  
  - **Obesidade**: IMC ≥ 30  
- Botão para **limpar** os campos.  
- **Tema claro e escuro** com botão na AppBar.  
- Ajuste automático da **cor da AppBar** para manter contraste no título e ícones.

---

## 🛠️ Tecnologias Utilizadas

* **Python** → linguagem principal usada no desenvolvimento.

* **Flet** → framework para criação da interface gráfica (apps web e mobile com Python).

* **Visual Studio Code** → editor de código utilizado para escrever e organizar o projeto.

* **Git/GitHub** → versionamento e hospedagem do repositório.


<br> 

## 💻 Comandos Utilizados no Terminal

### 🔹 Ambiente Virtual
```bash
python -m venv .venv
.venv\Scripts\activate
```

### 🔹 Instalação de Dependências
```bash
pip install flet-desktop
pip show flet
```

### 🔹 Execução do Projeto
```bash
flet run --web nomeprojeto.py
```

<br>

## 🌆 Imagens da Tela
<img width="751" height="877" alt="Captura de tela 2025-09-02 141134" src="https://github.com/user-attachments/assets/797584c3-f978-4c8f-acf6-5d407635fb12" />

<img width="751" height="870" alt="Captura de tela 2025-09-02 141236" src="https://github.com/user-attachments/assets/83fb1ee0-f40f-421c-a582-e8d4f3d5e2dc" />

<img width="752" height="870" alt="Captura de tela 2025-09-02 141310" src="https://github.com/user-attachments/assets/91f6b91f-3a33-46c8-93ca-413b61dd47dc" />


