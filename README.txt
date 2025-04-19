
Termux Setup Instructions for Running ip.py with Serveo
=======================================================

1. Update and Install Required Termux Packages
----------------------------------------------
Run the following commands in Termux:

pkg update -y
pkg upgrade -y
pkg install python -y
pkg install openssh -y
pkg install git -y

2. Install Required Python Modules
----------------------------------
Install Flask using pip:

pip install flask

(Optional)
pip install requests

3. Enable Storage Access (Optional)
-----------------------------------
If you need to save logs or files to shared storage:

termux-setup-storage

(Grant permission when prompted.)

4. Make the Python Script Executable (Optional)
-----------------------------------------------
If you want to make the script executable:

chmod +x ip.py

Then run it with:

python ip.py

5. Using Serveo for Tunneling
-----------------------------
Make sure you're connected to the internet.

The script will automatically start a tunnel using Serveo:

ssh -R 80:localhost:5000 serveo.net

NOTE:
- No installation required for Serveo.
- You must allow SSH access for this to work properly.
- Make sure `openssh` is installed (see step 1).

Once Serveo is running, it will provide you a public link like:

https://yourname.serveo.net

Send this link to your target to capture IP addresses.

Enjoy using IP KILLER!
