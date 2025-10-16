import subprocess
import os
import sys

# Thư mục chứa 2 file code Unity
project_path = r"D:\FPT Polytechnic\NhapMonLTGA\Unity Projects" if sys.platform.startswith("win") else "/Users/username/UnityScripts"
os.chdir(project_path)

# Git pull từ repository để lấy 2 file code mới nhất
subprocess.run(["git", "pull"])

print("Download complete!")
