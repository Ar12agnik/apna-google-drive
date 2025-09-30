import subprocess
import sys
import os

def setup_venv():
    env_dir = "myenv"
    try:
        subprocess.check_call([sys.executable, "-m", "venv", env_dir])
        print("Successfully set up virtual environment.")
        print(f"To activate it, run:\n")
        if os.name == 'nt':
            print(f"{env_dir}\\Scripts\\activate.bat")
        else:
            print(f"source {env_dir}/bin/activate")
    except subprocess.CalledProcessError as e:
        print(f"Error creating virtual environment: {e}")
setup_venv()
with open(".env","w+") as fp:
    path = input("Please Enter the full path of a folder which will be used to store all items: ")
    fp.write(f"Path = {path}")    

subprocess.call(["cmd.exe", "/c","install_packages.cmd"])
        