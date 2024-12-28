import threading
import time
import os
import run
from PyQt5.QtWidgets import QApplication
import UI


def start_run():
    """Theo dõi và phân tích dòng mới trong chat_log.txt."""
    chat_log_path = "text/chat_log.txt"
    last_processed_line = ""

    while True:
        if os.path.exists(chat_log_path):
            with open(chat_log_path, "r", encoding="utf-8") as file:
                lines = file.readlines()
                if lines:
                    last_line = lines[-1].strip()
                    if last_line != last_processed_line:
                        print(f"Processing new line: {last_line}")
                        last_processed_line = last_line
                        # Gọi hàm runTest để phân tích dòng mới
                        run.runTest()
        time.sleep(1)  # Kiểm tra file mỗi giây


def main():
    """Chạy giao diện người dùng và luồng phân tích token."""
    # Tạo thread cho việc chạy phân tích token
    run_thread = threading.Thread(target=start_run, daemon=True)
    run_thread.start()

    # Chạy giao diện người dùng trong main thread
    app = QApplication([])
    window = UI.ChatBox()
    window.show()
    app.exec_()


if __name__ == "__main__":
    main()
#Xin chào