import sys
import requests
from bs4 import BeautifulSoup
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt

class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__() # 呼叫父類別 QtWidgets.QWidget 的 __init__
        self.set_ui()
        self.url = "https://www.taiwanlottery.com.tw/index_new.aspx"
        self.html = requests.get(self.url)
        self.soup = BeautifulSoup(self.html.text, "html.parser")

    def set_ui(self):
        self.setWindowTitle("Taiwan Lottery") # 設置視窗程式標題
        self.resize(640, 640) # 設置視窗程式寬長

        # 台灣彩券標題
        self.label = QtWidgets.QLabel(self)
        self.label.setText("台灣彩券")
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setStyleSheet("font: bold; font-size:50px; color: Red; font-family: 微軟正黑體")
        self.label.setGeometry(0, 30, 640, 120)

        # 選擇欲查詢的彩券號碼
        lottery_name = ["BINGO賓果", "雙贏彩", "威力彩", "38樂合彩", "大樂透", "49樂合彩", "今彩539", "39樂合彩", "3星彩", "4星彩"]
        self.lottery_box = QtWidgets.QComboBox(self)
        self.lottery_box.addItems(lottery_name) # 將串列作為選項
        self.lottery_box.setStyleSheet("font: bold; font-size: 25px; color: Sienna") # CSS 樣式
        self.lottery_box.setCurrentIndex(len(lottery_name)) # 設定預設值，超過串列索引值則顯示為空
        self.lottery_box.setGeometry(45, 150, 350, 50) # 顯示位置，(X, Y, 寬, 高)
        self.lottery_box.setEditable(True) # 設定內容可更改
        line_edit = self.lottery_box.lineEdit()
        line_edit.setAlignment(Qt.AlignCenter) # 文字置中
        line_edit.setReadOnly(True) # 設定僅可閱讀

        # 查詢按鈕
        self.sure_btn = QtWidgets.QPushButton(self)
        self.sure_btn.setText("查詢")
        self.sure_btn.setStyleSheet("font-size: 25px")
        self.sure_btn.setGeometry(395, 150, 200, 50)
        self.sure_btn.clicked.connect(self.reptile) # 呼叫顯示號碼函數

        # 彩券第幾期
        self.lottery_time_label = QtWidgets.QLabel(self)
        self.lottery_time_label.setText("")
        self.lottery_time_label.setStyleSheet("font: bold; font-size: 40px; font-family: 微軟正黑體;")
        self.lottery_time_label.setAlignment(Qt.AlignCenter)
        self.lottery_time_label.setGeometry(0, 210, 640, 200)

        # 彩券號碼
        self.lottery_number_label = QtWidgets.QLabel(self)
        self.lottery_number_label.setText("")
        self.lottery_number_label.setStyleSheet("font-size: 30px; font-family: 微軟正黑體; color: Purple")
        self.lottery_number_label.setAlignment(Qt.AlignCenter)
        self.lottery_number_label.setGeometry(0, 320, 640, 320)

    # 查詢彩券號碼的函式
    def reptile(self):
        choice = self.lottery_box.currentText() # 取得選取的選項
        title = self.soup.find_all("span", class_ = "font_black15")
        red = self.soup.find_all("div", class_ = "ball_red")
        blue = self.soup.find_all("div", class_ = "ball_tx ball_blue")
        green = self.soup.find_all("div", class_ = "ball_tx ball_green")
        lemon = self.soup.find_all("div", class_ = "ball_tx ball_lemon")
        purple = self.soup.find_all("div", class_ = "ball_tx ball_purple")
        yellow = self.soup.find_all("div", class_ = "ball_tx ball_yellow")
        # 根據選取的選項，顯示對應的彩券號碼資料
        if choice == "BINGO賓果":
            number = "開出獎號\n"
            for i in range(0, 10):
                number += f"{yellow[i].text.strip()},"
            number += '\n'
            for i in range(10, 20):
                number += f"{yellow[i].text.strip()},"
            self.lottery_time_label.setText(title[0].text)
            self.lottery_number_label.setText(number)
        elif choice == "雙贏彩":
            number = "開出順序：\n"
            for i in range(0, 12):
                number += f"{blue[i].text.strip()},"
                if i == 5:
                    number += '\n'
            number += "\n大小順序：\n"
            for i in range(12, 24):
                number += f"{blue[i].text.strip()},"
                if i == 17:
                    number += '\n'
            self.lottery_time_label.setText(title[1].text)
            self.lottery_number_label.setText(number)
        elif choice == "威力彩":
            number = "開出順序："
            for i in range(0, 6):
                number += f"{green[i].text.strip()},"
            number += "\n大小順序："
            for i in range(6, 12):
                number += f"{green[i].text.strip()},"
            number += f"\n第二區：{red[1].text}"
            self.lottery_time_label.setText(title[2].text)
            self.lottery_number_label.setText(number)
        elif choice == "38樂合彩":
            number = "開出順序："
            for i in range(12, 18):
                number += f"{green[i].text.strip()},"
            number += "\n大小順序："
            for i in range(18, 24):
                number += f"{green[i].text.strip()},"
            self.lottery_time_label.setText(title[3].text)
            self.lottery_number_label.setText(number)
        elif choice == "大樂透":
            number = "開出順序："
            for i in range(20, 26):
                number += f"{yellow[i].text.strip()},"
            number += "\n大小順序："
            for i in range(26, 32):
                number += f"{yellow[i].text.strip()},"
            number += f"\n特別號：{red[2].text}"
            self.lottery_time_label.setText(title[4].text)
            self.lottery_number_label.setText(number)
        elif choice == "49樂合彩":
            number = "開出順序："
            for i in range(32, 38):
                number += f"{yellow[i].text.strip()},"
            number += "\n大小順序："
            for i in range(38, 44):
                number += f"{yellow[i].text.strip()},"
            self.lottery_time_label.setText(title[5].text)
            self.lottery_number_label.setText(number)
        elif choice == "今彩539":
            number = "開出順序："
            for i in range(0, 5):
                number += f"{lemon[i].text.strip()},"
            number += "\n大小順序："
            for i in range(5, 10):
                number += f"{lemon[i].text.strip()},"
            self.lottery_time_label.setText(title[6].text)
            self.lottery_number_label.setText(number)
        elif choice == "39樂合彩":
            number = "開出順序："
            for i in range(10, 15):
                number += f"{lemon[i].text.strip()},"
            number += "\n大小順序："
            for i in range(15, 20):
                number += f"{lemon[i].text.strip()},"
            self.lottery_time_label.setText(title[7].text)
            self.lottery_number_label.setText(number)
        elif choice == "3星彩":
            number = "中獎號碼："
            for i in range(0, 3):
                number += f"{purple[i].text.strip()},"
            self.lottery_time_label.setText(title[8].text)
            self.lottery_number_label.setText(number)
        elif choice == "4星彩":
            number = "中獎號碼："
            for i in range(3, 7):
                number += f"{purple[i].text.strip()},"
            self.lottery_time_label.setText(title[8].text)
            self.lottery_number_label.setText(number)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv) # 視窗程式開始
    Form = MainWindow() # 放入視窗基底元件
    Form.show() # 顯示元件
    sys.exit(app.exec_()) # 視窗程式結束
