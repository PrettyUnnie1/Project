# run.py
import sys
import os
import subprocess
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
from sentiment_analyzer import SentimentAnalyzer  # Import the sentiment analyzer

class ChatBox(QMainWindow):
    def __init__(self):
        super().__init__()

        # Initialize the sentiment analyzer
        self.sentiment_analyzer = SentimentAnalyzer()

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

            # Phân tích cảm xúc của tin nhắn người dùng
            sentiment = self.sentiment_analyzer.analyze(user_message)

            # Tạo phản hồi dựa trên cảm xúc
            bot_reply = self.generate_bot_reply(sentiment)
            self.chat_display.append(f"Bot: {bot_reply}\n")
            self.save_message_to_file("Bot", bot_reply)

    def generate_bot_reply(self, sentiment):
        """Tạo phản hồi của bot dựa trên cảm xúc."""
        if sentiment == "Positive":
            return "Positive! 😊"
        elif sentiment == "Negative":
            return "Negative. 😔"
        elif sentiment == "Mixed":
            return "Mixed! 🤔"
        elif sentiment == "Neutral":
            return "Neutral. 😊"
        else:
            return "I don't understand your emotion. 🤷‍♂️"

    def save_message_to_file(self, sender, message):
        """Lưu tin nhắn vào file txt."""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open("chat_log.txt", "a", encoding="utf-8") as file:
            file.write(f"{timestamp} - {sender}: {message}\n")

def generate_antlr_to_python():
    """Function to generate ANTLR Lexer, Parser, and Listener."""
    # Define paths
    DIR = os.path.dirname(os.path.abspath(__file__))
    ANTLR_JAR = r'D:\antlr\antlr4-4.9.2-complete.jar'
    CPL_Dest = 'CompiledFiles'
    SRC = 'Sample.g4'

    print('Running ANTLR4...')
    cmd = [
        'java',
        '-jar',
        ANTLR_JAR,
        '-o',
        CPL_Dest,
        '-Dlanguage=Python3',
        SRC
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode == 0:
        print('ANTLR4 generated Lexer, Parser, and Listener successfully.')
    else:
        print('Error generating Lexer, Parser, and Listener:')
        print(result.stderr)
    print('-----------------------------------------------')

def main():
    # Check if 'CompiledFiles' directory exists
    if not os.path.exists('CompiledFiles'):
        print("CompiledFiles directory not found. Generating ANTLR files...")
        generate_antlr_to_python()
    
    # Initialize and run the PyQt5 application
    app = QApplication(sys.argv)
    window = ChatBox()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
