@echo off
REM Chuyển đến thư mục chứa game
cd /d "D:\kì5n3\Kì 5\TH - Trí Tuệ Nhân Tạo\Trí Tuệ Nhân Tạo\DOAN_GAME_HILL_CLIMBING\DOAN_TTNT"

REM Chạy game bằng Python trong env envt5
"D:\miniconda_new\envs\envt5\python.exe" main.py

REM Dừng màn hình lại để xem lỗi nếu có
pause
