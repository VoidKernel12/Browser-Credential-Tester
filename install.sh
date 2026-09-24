#!/bin/bash

# ANSI Color Codes for Terminal Output
GOLD="\033[93m"
GREEN="\033[92m"
RED="\033[91m"
RESET="\033[0m"

echo -e "${GOLD}[+] Updating and upgrading system packages...${RESET}"
pkg update -y && pkg upgrade -y 2>/dev/null || sudo apt update && sudo apt upgrade -y

echo -e "${GOLD}[+] Installing Python and Git...${RESET}"
pkg install python git -y 2>/dev/null || sudo apt install python3 python3-pip git -y

echo -e "${GOLD}[+] Upgrading pip to the latest version...${RESET}"
python3 -m pip install --upgrade pip

echo -e "${GOLD}[+] Installing required Python dependencies (Flask, Requests, BeautifulSoup4)...${RESET}"
pip install flask requests beautifulsoup4

echo -e "${GREEN}[+] Installation completed successfully! You can now run the tool using: python main.py${RESET}"
