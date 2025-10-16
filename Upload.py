import subprocess
import datetime
import os
import sys

# Thư mục chứa 2 file code Unity
# Windows: r"D:\FPT Polytechnic\NhapMonLTGA\Unity Projects"
# macOS: "/Users/khangng/Downloads/Hoc FPT/Unity project/Link Projects/Unity-Projects"
project_path = r"D:\FPT Polytechnic\NhapMonLTGA\Unity Projects" if sys.platform.startswith("win") else "/Users/khangng/Downloads/Hoc FPT/Unity project/Link Projects/Unity-Projects"
os.chdir(project_path)

# Git add 2 file code
subprocess.run(["git", "add", "Upload.py", "Clone.py"])

# Git commit với timestamp
subprocess.run(["git", "commit", "-m", f"Auto commit {datetime.datetime.now()}"])

# Git pull trước để tránh xung đột
subprocess.run(["git", "pull", "--rebase"])

# Git push lên repository
subprocess.run(["git", "push"])

print("Upload complete!")
