import random
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox, QPushButton, QVBoxLayout, QLabel, QHBoxLayout, QLineEdit

def to_no_ss():
    btn_no_mode.hide()
    button1.hide()
    button2.hide()
    button3.hide()
    button4.hide()
    
    btn_yes_mode.show()
    button1_x.show()
    button2_x.show()
    button3_x.show()
    button4_x.show()

def to_yes_ss():
    btn_no_mode.show()
    button1_x.hide()
    button2_x.hide()
    button3_x.hide()
    button4_x.hide()
    
    btn_yes_mode.hide()
    button1.show()
    button2.show()
    button3.show()
    button4.show()

def gen6():
    chars = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM12345678890!@#$%^&*()_+-="
    passwords = ''
    for n in range(6):
        passwords += random.choice(chars)
    pasw_text.setText(passwords)
    winpass = QMessageBox()
    winpass.setText('Успешно!')
    winpass.exec_()

def gen8():
    chars = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM12345678890!@#$%^&*()_+-="
    passwords = ''
    for n in range(8):
        passwords += random.choice(chars)
    pasw_text.setText(passwords)
    winpass = QMessageBox()
    winpass.setText('Успешно!')
    winpass.exec_()

def gen10():
    chars = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM12345678890!@#$%^&*()_+-="
    passwords = ''
    for n in range(10):
        passwords += random.choice(chars)
    pasw_text.setText(passwords)
    winpass = QMessageBox()
    winpass.setText('Успешно!')
    winpass.exec_()

def gen12():
    chars = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM12345678890!@#$%^&*()_+-="
    passwords = ''
    for n in range(12):
        passwords += random.choice(chars)
    pasw_text.setText(passwords)
    winpass = QMessageBox()
    winpass.setText('Успешно!')
    winpass.exec_()
    
def gen6_x():
    chars = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM12345678890"
    passwords = ''
    for n in range(6):
        passwords += random.choice(chars)
    pasw_text.setText(passwords)
    winpass = QMessageBox()
    winpass.setText('Успешно!')
    winpass.exec_()

def gen8_x():
    chars = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM12345678890"
    passwords = ''
    for n in range(8):
        passwords += random.choice(chars)
    pasw_text.setText(passwords)
    winpass = QMessageBox()
    winpass.setText('Успешно!')
    winpass.exec_()

def gen10_x():
    chars = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM12345678890"
    passwords = ''
    for n in range(10):
        passwords += random.choice(chars)
    pasw_text.setText(passwords)
    winpass = QMessageBox()
    winpass.setText('Успешно!')
    winpass.exec_()

def gen12_x():
    chars = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM12345678890"
    passwords = ''
    for n in range(12):
        passwords += random.choice(chars)
    pasw_text.setText(passwords)
    winpass = QMessageBox()
    winpass.setText('Успешно!')
    winpass.exec_()





app = QApplication([])
win = QWidget()
win.setWindowTitle('Генератор паролей')
win.resize(300,400)
label1 = QLabel('Выбери длину пароля')
label1.setAlignment(Qt.AlignCenter)
button1 = QPushButton('8 символов')
button2 = QPushButton('6 символов')
button3 = QPushButton('10 символов')
button4 = QPushButton('12 символов')

button1_x = QPushButton('8 символов')
button2_x = QPushButton('6 символов')
button3_x = QPushButton('10 символов')
button4_x = QPushButton('12 символов')

button1_x.hide()
button2_x.hide()
button3_x.hide()
button4_x.hide()

btn_no_mode = QPushButton('Режим без спец. символов')
btn_yes_mode = QPushButton('Обычный режим')
btn_yes_mode.hide()
pasw_text = QLineEdit()
pasw_text.setPlaceholderText('Тут будет ваш пароль...')
main_lay = QVBoxLayout()

lv1 = QVBoxLayout()
lv2 = QVBoxLayout()
h1 = QHBoxLayout()
h2 = QHBoxLayout()
h3 = QHBoxLayout()
h4 = QHBoxLayout()

lv1.addWidget(button1)
lv1.addWidget(button2)
lv2.addWidget(button3)
lv2.addWidget(button4)

lv1.addWidget(button1_x)
lv1.addWidget(button2_x)
lv2.addWidget(button3_x)
lv2.addWidget(button4_x)

h3.addWidget(btn_no_mode)
h3.addWidget(btn_yes_mode)
h4.addWidget(pasw_text)

h1.addWidget(label1)
h2.addLayout(lv1)
h2.addLayout(lv2)
main_lay.addLayout(h1)
main_lay.addLayout(h2)
main_lay.addLayout(h3)
main_lay.addLayout(h4)

win.setLayout(main_lay)
button1.clicked.connect(gen8)
button2.clicked.connect(gen6)
button3.clicked.connect(gen10)
button4.clicked.connect(gen12)

button1_x.clicked.connect(gen8_x)
button2_x.clicked.connect(gen6_x)
button3_x.clicked.connect(gen10_x)
button4_x.clicked.connect(gen12_x)

btn_no_mode.clicked.connect(to_no_ss)
btn_yes_mode.clicked.connect(to_yes_ss)
win.show()
app.exec_()