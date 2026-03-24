from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QPushButton, QGroupBox, QRadioButton, QVBoxLayout,QHBoxLayout)

app = QApplication ([])
main_window = QWidget()
main_window.setWindowTitle('Memory App')
main_window.resize(640, 480)

#Widgets
question = QLabel('Pregunta')
start_btn = QPushButton('Siguiente')

#Grupo de botones de radio
button_group = QGroupBox('Seleccione una respuesta')
radiobut_1 = QRadioButton('1')
radiobut_2 = QRadioButton('2')
radiobut_3 = QRadioButton('3')
radiobut_4 = QRadioButton('4')

#Layout de botones
answer_layout = QHBoxLayout()
col_1 = QVBoxLayout()
col_2 = QVBoxLayout()

col_1.addWidget(radiobut_1)
col_1.addWidget(radiobut_2)
col_2.addWidget(radiobut_3)
col_2.addWidget(radiobut_4)

answer_layout.addLayout(col_1)
answer_layout.addLayout(col_2)

button_group.setLayout(answer_layout)

#Layout Principal:
main_layout = QVBoxLayout()
line_1 = QHBoxLayout()
line_2 = QHBoxLayout()
line_3 = QHBoxLayout()

line_1.addWidget(question, alignment= (Qt.AlignHCenter | Qt.AlignVCenter))
line_2.addWidget(button_group)
line_3.addWidget(start_btn)


main_window.addLayout(line_1)
main_window.addLayout(line_2)
main_window.addLayout(line_3)
main_window.setLayout(main_layout)

