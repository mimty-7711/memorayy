from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget,  QPushButton, QHBoxLayout, QVBoxLayout, QLabel, QMessageBox, QRadioButton, QButtonGroup, QGroupBox
from random import shuffle, randint

class Question:
    def __init__(self, text, right_answer, wrong1, wrong2, wrong3):
        self.text = text
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

questions_list = []
questions_list.append(Question("whitch one is the cutest?", "ᓚᘏᗢ", "cat", "kitty", "༼ つ ◕_◕ ༽つ"))
questions_list.append(Question("whitch game is the best?", "minecraft", "roblox", "vampy's big day", "catopewpew"))
questions_list.append(Question("whitch one is the best place to eat at?", "that one tasty gas-station", "KFC", "Mc Donalds", "Burger King🍔"))
questions_list.append(Question("whitch meme is the most goated?", "oiai cat", "sad banana cat", "helicopter helicopter", "italian brain-rot"))

app = QApplication([]) 

window = QWidget()
window.resize(400, 200) 
window.setWindowTitle("memorayy")

question = QLabel("which one is the cutest?")
answer1 = QRadioButton("ᓚᘏᗢ")
answer2 = QRadioButton("cat") 
answer3 = QRadioButton("kitty") 
answer4 = QRadioButton("༼ つ ◕_◕ ༽つ")
GroupBox = QGroupBox("NAMA")
Button = QPushButton("Відповідь")

RadioGroup = QButtonGroup()
RadioGroup.addButton(answer1)
RadioGroup.addButton(answer2)
RadioGroup.addButton(answer3)
RadioGroup.addButton(answer4)

RGB = QGroupBox("rebultat")
result = QLabel("tyt rebultat")
correct = QLabel("tyt pravelna vidpovid")
result_V1 =QVBoxLayout()
result_V1.addWidget(result, alignment = Qt.AlignCenter)
result_V1.addWidget(correct, alignment = Qt.AlignCenter)
RGB.setLayout(result_V1)
RGB.hide()

lineH1 = QHBoxLayout()
lineV1 = QVBoxLayout()
lineV2 = QVBoxLayout()

lineV1.addWidget(answer1, alignment=Qt.AlignCenter)
lineV1.addWidget(answer2, alignment=Qt.AlignCenter)
lineV2.addWidget(answer3, alignment=Qt.AlignCenter)
lineV2.addWidget(answer4, alignment=Qt.AlignCenter)

lineH1.addLayout(lineV1)
lineH1.addLayout(lineV2)
RGB

window.setLayout(lineH1)

def show_result():
    GroupBox.hide()
    ResultGroupBox.show()
    Buttom.setText("next question")


def show_question():
    GroupBox.show()
    ResultGroupBox.hide()
    Buttom.setText("answer")
    RadioGroup.setExclusive(False)
    answer1.setChecked(False)
    answer2.setChecked(False)
    answer3.setChecked(False)
    answer4.setChecked(False)
    RadioGroup.setExclusive(True)

def next_question():
    random_question = randint(0, len(questions_list) -1)
    q = questions_list(random_question)
    ask(q)

def ask(text, right_answer, wrong1, wrong2, wrong3):
    shuffle(answers)
    answers[0].setText(right_answer)
    answers[1].setText(wrong1)
    answers[2].setText(wrong2)
    answers[3].setText(wrong3)
    question.setText(text)
    correct.setText("correct A" + right_answer)
    show_question()

def right_wrong():
    window.total += 1
    if RadioGroup.checkedButton() is None:
        return
    if answers[0].isCheked():
        result.setText("correct")
        window.score += 1
    else:
        result.setText("WRONG")
    show_result()
    rating = window.score/window.total * 100
    print("total atempts", window.total)
    print("correct atempts", window.score)
    print("correct in percentage", rating, "%")

def button_OK():
    if Button.text() == "answer":
        show_result()
    else:
        next_question()

Button.clicked.connect(button_OK)
window.score = 0
window.total = 0
window.show()
app.exec_()