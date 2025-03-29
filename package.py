import sys
import subprocess
import importlib

def check_and_install(package_name):
    try:
        importlib.import_module(package_name)
        print(package_name, "is already installed.")
    except ImportError:
        print(package_name, "is not installed. Installing...")
        try:
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', package_name])
            print(package_name, "has been successfully installed.")
        except subprocess.CalledProcessError as e:
            print("Error installing", package_name + ":", e)

package_name = input("ENTER PACKAGE NAME (e.g., opencv-python): ")
check_and_install(package_name)
