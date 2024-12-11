import os
import psutil
import pyautogui
import subprocess
from datetime import datetime

# Chụp màn hình
def capture_screenshot():
    now = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_path = f"screenshots/screenshot_{now}.png"
    pyautogui.screenshot(file_path)
    return file_path

# Tắt máy tính
def shutdown():
    os.system("shutdown /s /t 1")
    return "Máy tính đang tắt."

# Khởi động lại máy tính
def restart():
    os.system("shutdown /r /t 1")
    return "Máy tính đang khởi động lại."

# Kiểm tra trạng thái CPU và RAM
def get_system_status():
    cpu_percent = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory()
    return f"CPU: {cpu_percent}%\nRAM: {memory.percent}%"

# Mở ứng dụng 
def open_app(app_name):
    try:
        # Xử lý mở app theo tên
        if app_name == "Notepad":
            subprocess.Popen(["notepad.exe"])
        elif app_name == "Calculator":
            subprocess.Popen(["calc.exe"])
        elif app_name == "Chrome":
            subprocess.Popen(["C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"])
        elif app_name == "File Explorer":
            subprocess.Popen(["explorer.exe"])
        else:
            return f"Ứng dụng '{app_name}' không được hỗ trợ."
        
        return f"Đang mở {app_name}..."
    except Exception as e:
        return f"Không thể mở {app_name}. Lỗi: {str(e)}"
    

# Điều khiển media
def control_media(action):
    try:
        if action == "play_pause":
            pyautogui.hotkey('space')  # Play/Pause
            return "Đã thực hiện lệnh Play/Pause."
        
        elif action == "next":
            pyautogui.hotkey('right')  # Next Track
            return "Đã thực hiện lệnh Next."
        
        elif action == "previous":
            pyautogui.hotkey('left')  # Previous Track
            return "Đã thực hiện lệnh Previous."
        
        elif action == "volume_up":
            pyautogui.hotkey('volumeup')  # Volume Up
            return "Đã thực hiện lệnh Volume Up."
        
        elif action == "volume_down":
            pyautogui.hotkey('volumedown')  # Volume Down
            return "Đã thực hiện lệnh Volume Down."
        
        elif action == "mute":
            pyautogui.hotkey('volumemute')  # Mute
            return "Đã thực hiện lệnh Mute."
        
        return "Lệnh không hợp lệ."
    except Exception as e:
        return f"Không thể thực hiện lệnh. Lỗi: {str(e)}"