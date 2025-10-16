#!/usr/bin/env python3
import subprocess
import os
import sys

# Kiểm tra readchar, nếu chưa có thì hướng dẫn cài
try:
    import readchar
except ImportError:
    print("Module 'readchar' chưa được cài đặt. Vui lòng chạy:")
    print("pip3 install readchar")
    sys.exit(1)

# --- Thư mục repo ---
repo_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(repo_dir)

print("Đang thực hiện upload...")

try:
    # Thêm tất cả file
    subprocess.run(["git", "add", "."], check=True)
    # Commit với thông báo
    subprocess.run(["git", "commit", "-m", "Auto commit"], check=True)
    # Push lên remote
    subprocess.run(["git", "push"], check=True)
except subprocess.CalledProcessError as e:
    print("Upload thất bại!")
    print(e)
    sys.exit(1)

print("Upload hoàn tất!")

# --- Chờ nhấn bất kỳ phím để thoát ---
print("Nhấn bất kỳ phím nào để thoát...")
readchar.readkey()  # đợi 1 phím
sys.exit(0)
