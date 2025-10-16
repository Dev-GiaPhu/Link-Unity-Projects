#!/bin/bash
# Chạy Upload.py
python3 "$(dirname "$0")/Upload.py"
# Đợi nhấn phím, rồi tự đóng Terminal
read -n 1 -s -r -p "Hoàn tất! Nhấn phím bất kỳ để thoát..."
exit
