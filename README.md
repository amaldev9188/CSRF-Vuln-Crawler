# CSRF Vulnerability Crawler

A lightweight Python utility designed to scan target web pages, extract HTML forms, and check for the presence of Cross-Site Request Forgery (CSRF) protection tokens.

---

## Table of Contents
1. [Overview](#overview)
2. [Understanding CSRF Vulnerability](#understanding-csrf-vulnerability)
    - [What is CSRF?](#what-is-csrf)
    - [How a CSRF Attack Works](#how-a-csrf-attack-works)
    - [Impact](#impact)
3. [How the Crawler Works](#how-the-crawler-works)
4. [Installation and Requirements](#installation-and-requirements)
5. [Usage](#usage)
6. [Proof of Concept (PoC)](#proof-of-concept-poc)
7. [Mitigation & Prevention](#mitigation--prevention)

---

## Overview
This repository contains a security assessment tool, [crawler.py](file:///c:/Users/Amal/Documents/Crawler/crawler.py), which helps developers and security researchers identify web forms that are susceptible to Cross-Site Request Forgery (CSRF) due to a lack of protection tokens.

---

## Understanding CSRF Vulnerability

### What is CSRF?
**Cross-Site Request Forgery (CSRF)**, also known as one-click attack or session riding, is a web security vulnerability that allows an attacker to induce users to perform actions they do not intend to perform. It bypasses the same-origin policy, which is designed to prevent different websites from interfering with each other.

### How a CSRF Attack Works
1. **Target User Logs In**: A user authenticates to a legitimate web application (e.g., `bank.com`) and establishes an active session (usually stored via session cookies).
2. **Attacker Hosts Malicious Link/Site**: The attacker creates a malicious page containing a forged request targeting `bank.com` (e.g., a hidden form or image source pointing to a money transfer endpoint like `/transfer?amount=1000&to=attacker`).
3. **User Visits Malicious Page**: While still logged into `bank.com`, the user visits the attacker's malicious page.
4. **Forged Request Sent**: The malicious page automatically sends the request to `bank.com`. Because the user is authenticated, the browser automatically attaches the session cookies for `bank.com`, causing the server to process the request as if it were authorized by the user.

### Impact
Depending on the privilege level of the victim, CSRF attacks can lead to:
- Unauthorized state-changing actions (e.g., changing passwords, updating email addresses, deleting accounts).
- Financial transactions (e.g., transferring funds).
- Full application compromise (if the victim is an administrator).

---

## How the Crawler Works
The crawler is a basic static analysis script:
1. It requests the target URL using the `requests` library.
2. It parses the returned HTML response via `BeautifulSoup`.
3. It extracts all `<form>` tags.
4. For each form, it inspects all hidden inputs (`<input type="hidden">`) for common CSRF token parameter names:
   - `csrf_token`
   - `csrfmiddlewaretoken`
   - `authenticity_token`
5. If a form is found without any of these tokens, the script alerts that a CSRF vulnerability is detected.

---

## Installation and Requirements

### Dependencies
The script requires Python 3 and the following external libraries:
- `requests` (for executing HTTP requests)
- `beautifulsoup4` (for parsing HTML structure)

### Installation
You can set up a virtual environment and install the required dependencies:

```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows (PowerShell):
.\venv\Scripts\Activate.ps1
# On Windows (CMD):
.\venv\Scripts\activate.bat
# On Linux/macOS:
source venv/bin/activate

# Install dependencies
pip install requests beautifulsoup4
```

---

## Usage
Run the crawler script and enter the target URL when prompted:

```bash
python crawler.py
```

### Example Input/Output
```text
Enter the URL to crawl: http://example.com/login
Form without CSRF token found:
csrf vulnerability detected
```

---

## Proof of Concept (PoC)
The project includes a file named [poc.html](file:///c:/Users/Amal/Documents/Crawler/poc.html) containing a standard login form:
```html
<form>
    <label for="username">Username:</label>
    <input type="text" id="username" name="username"><br><br>
    <label for="password">Password:</label>
    <input type="password" id="password" name="password"><br><br>
    <input type="submit" value="Sign in">
</form>
```
Since this form does not contain any hidden fields representing a CSRF verification token, running the crawler on a page hosting this form will trigger a vulnerability detection.

---

## Mitigation & Prevention

To secure forms against CSRF attacks, consider implementing the following defense-in-depth measures:

1. **Anti-CSRF Tokens (Synchronizer Token Pattern)**
   - Generate a cryptographically secure, random, and unique token for each user session.
   - Insert this token as a hidden input field in all state-changing forms.
   - Verify that the token submitted with the form matches the token stored in the user's session.

2. **SameSite Cookie Attribute**
   - Configure session cookies with the `SameSite` attribute (`SameSite=Strict` or `SameSite=Lax`).
   - This prevents cookies from being sent along with cross-site requests, mitigating many common CSRF attack vectors.

3. **Custom Headers & Anti-Forgery mechanisms**
   - For AJAX/API calls, use custom request headers (e.g., `X-Requested-With` or `X-CSRF-Token`) as browsers typically don't allow cross-site requests to append custom headers without CORS preflight approvals.
