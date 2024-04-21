# напиши здесь код основного приложения и первого экрана
from instr.py import *
from second_win import *
class MainWin(QWidget):
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
    def initUI(self):
        self.hello_text = Qlabel(txt_hello)
        self.instruction = Qlabel(txt_instruction)
        self.button = QPushButton(txt_next)
        self.layout = QVBoxLayout
        v_line.addWidget(
    
)
    def connects(self):
        self.btn_next.clicked.connect(self.next_click)
    def next_click(self):
        self.hide
        self.tw = TestWin()