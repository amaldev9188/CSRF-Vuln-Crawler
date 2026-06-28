# CSRF Vulnerability & Scanning Demo

This project demonstrates a simple web application with a basic login form alongside a crawler script that checks web pages for cross-site request forgery (CSRF) vulnerabilities by auditing HTML forms for CSRF tokens.

## Project Structure

- **[app.py](file:///c:/Users/Amal/Documents/CSRF/app.py)**: A basic Flask web application that serves a login form (without CSRF protection) and a welcome page.
- **[crwaler.py](file:///c:/Users/Amal/Documents/CSRF/crwaler.py)**: A vulnerability scanning script that crawls a target URL, inspects `<form>` tags, and detects if they lack a CSRF/authenticity token.
- **[templates/](file:///c:/Users/Amal/Documents/CSRF/templates)**:
  - **[login.html](file:///c:/Users/Amal/Documents/CSRF/templates/login.html)**: The login interface.
  - **[welcome.html](file:///c:/Users/Amal/Documents/CSRF/templates/welcome.html)**: The landing page after a successful login.

---

## Setup & Installation

### 1. Activate the Virtual Environment

Activate the Python virtual environment based on your operating system and shell:

* **PowerShell**:
  ```powershell
  .\venv\Scripts\Activate.ps1
  ```
  *(If you encounter execution policy issues, run `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process` first)*

* **Command Prompt (CMD)**:
  ```cmd
  venv\Scripts\activate.bat
  ```

* **Bash / Git Bash**:
  ```bash
  source venv/Scripts/activate
  ```

### 2. Install Dependencies

Install the required packages within the activated virtual environment:
```bash
pip install Flask requests beautifulsoup4
```

---

## Usage

### Running the Flask Web App

1. Run the Flask development server:
   ```bash
   python app.py
   ```
2. Open your browser and navigate to `http://127.0.0.1:5000`.
3. Log in using the default credentials:
   - **Username**: `Admin`
   - **Password**: `Password`

### Running the CSRF Crawler/Scanner

1. Keep the Flask web application running.
2. In a separate terminal shell (with the virtual environment activated), run:
   ```bash
   python crwaler.py
   ```
3. Enter the URL of the Flask app when prompted (e.g. `http://127.0.0.1:5000`).
4. The script will analyze the forms on the page and output whether it is vulnerable or secure:
   * **Vulnerable**: If a form lacks a hidden input containing `csrf`, `token`, or `authenticity` in its name.
   * **Secure**: If the form contains a valid token name.
