import sys
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QVBoxLayout,
    QHBoxLayout,
    QTextEdit,
    QLineEdit,
    QPushButton,
    QWidget,
)
from PyQt5.QtCore import Qt
from datetime import datetime


class ChatBox(QMainWindow):
    def __init__(self):
        super().__init__()

        # Thiết lập cửa sổ chính
        self.setWindowTitle("Chat Box")
        self.setGeometry(100, 100, 400, 500)

        # Tạo widget chính
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        # Tạo layout chính
        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        # Khung hiển thị tin nhắn
        self.chat_display = QTextEdit()
        self.chat_display.setReadOnly(True)
        self.layout.addWidget(self.chat_display)

        # Khung nhập liệu và nút gửi
        input_layout = QHBoxLayout()
        self.message_input = QLineEdit()
        self.message_input.setPlaceholderText("Nhập tin nhắn...")
        input_layout.addWidget(self.message_input)

        self.send_button = QPushButton("Gửi")
        input_layout.addWidget(self.send_button)

        self.layout.addLayout(input_layout)

        # Kết nối sự kiện
        self.send_button.clicked.connect(self.send_message)
        self.message_input.returnPressed.connect(self.send_message)

    def send_message(self):
        """Hàm xử lý khi gửi tin nhắn."""
        user_message = self.message_input.text().strip()  # Lấy nội dung trong khung chat
        if user_message:
            # Hiển thị tin nhắn trong khung chat
            self.chat_display.append(f"Bạn: {user_message}")
            # Ghi tin nhắn vào file
            self.save_message_to_file("Bạn", user_message)
            # Xóa nội dung trong khung nhập
            self.message_input.clear()

            # (Tùy chọn) Thêm phản hồi tự động
            #bot_reply = "Tôi đã nhận được tin nhắn của bạn!"
            #self.chat_display.append(f"Bot: {bot_reply}\n")
            #self.save_message_to_file("Bot", bot_reply)

    def save_message_to_file(self, sender, message):
        """Lưu tin nhắn vào file txt trong thư mục text, chỉ ghi phần message."""
        print(message)  # In tin nhắn ra màn hình
        with open("tests/chat_log.txt", "a", encoding="utf-8") as file:
            file.write(f"{message}\n")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ChatBox()
    window.show()
    sys.exit(app.exec_())
