from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton

class AddressBook(QWidget):
    def __init__(self):
        super().__init__()

        self.title = '주소록'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480

        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # 레이아웃 설정
        vbox = QVBoxLayout()
        hbox = QHBoxLayout()

        # 라벨과 입력창 생성
        name_label = QLabel('이름:')
        name_edit = QLineEdit()

        phone_label = QLabel('전화번호:')
        phone_edit = QLineEdit()

        # 버튼 생성
        add_button = QPushButton('추가')
        del_button = QPushButton('삭제')

        # 레이아웃에 추가
        hbox.addWidget(name_label)
        hbox.addWidget(name_edit)
        hbox.addWidget(phone_label)
        hbox.addWidget(phone_edit)

        vbox.addLayout(hbox)
        vbox.addWidget(add_button)
        vbox.addWidget(del_button)

        self.setLayout(vbox)

if __name__ == '__main__':
    app = QApplication([])
    ex = AddressBook()
    ex.show()
    app.exec_()