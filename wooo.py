import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox, QButtonGroup
from sasmeli import Ui_Dialog

class DrinkOrderApp(QtWidgets.QMainWindow, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.setStyleSheet("background-color: #d6eeeb")

        self.label_category.setText("კატეგორია😮:")
        self.label_drink.setText("სასმელი😳:")

        self.size_group = QButtonGroup()
        self.size_group.addButton(self.radioButton_small)
        self.size_group.addButton(self.radioButton_medium)
        self.size_group.addButton(self.radioButton_large)
        self.radioButton_medium.setChecked(True)


        self.menu = {
            "ვისკი": {"Jack Daniel's": [18, 28, 38], "Jameson": [17, 27, 37], "Chivas Regal": [20, 30, 40]},
            "არაყი": {"Absolut": [12, 22, 32], "Grey Goose": [20, 30, 40], "Smirnoff": [11, 21, 31]},
            "კონიაკი": {"Sarajishvili": [14, 22, 32], "Hennessy": [20, 32, 45], "Old Kakheti": [13, 21, 31]},
            "ლიქიორი": {"Baileys": [14, 24, 34], "Jägermeister": [15, 25, 35], "Limoncello": [13, 23, 33]},
            "ლუდი": {"Paulaner": [7, 9, 12], "Guinness": [8, 11, 14], "Qarva": [6, 8, 10]},
            "ჭაჭა": {"Sarajishvili Chacha": [22, 32, 42], "Askaneli Chacha": [21, 31, 41]},
            "ლიმონათი": {"მსხალი": [3, 5, 7], "ტარხუნა": [3, 5, 7], "ნაღები": [3, 5, 7], "ლიმონი": [3, 5, 7]},
            "წყალი": {"ბაკურიანი": [1, 2, 3], "სნო": [1, 2, 3], "ბახმარო": [1, 2, 3], "მთის": [1, 2, 3]},
            "ჩაი": {"შავი": [2, 3, 4], "მწვანე": [2, 3, 4], "პიტნის": [2, 3, 4]},
            "ყავა": {"ესპრესო": [3, 4, 5], "ლატე": [4, 5, 6], "კაპუჩინო": [4, 5, 6]},
        }


        self.comboBox_category.addItems(self.menu.keys())


        self.comboBox_category.currentTextChanged.connect(self.update_drinks)
        self.comboBox_drink.currentTextChanged.connect(self.update_price)
        self.size_group.buttonClicked.connect(self.update_price)
        self.pushButton_order.clicked.connect(self.place_order)


        self.update_drinks()

    def update_drinks(self):
        cat = self.comboBox_category.currentText()
        self.comboBox_drink.clear()
        self.comboBox_drink.addItems(self.menu.get(cat, {}).keys())
        self.update_price()

    def update_price(self):
        cat = self.comboBox_category.currentText()
        dr = self.comboBox_drink.currentText()
        if not dr:
            self.label_price.setText("ფასი: ")
            return
        sizes = self.menu[cat][dr]
        if self.radioButton_small.isChecked():
            price = sizes[0]
        elif self.radioButton_medium.isChecked():
            price = sizes[1]
        else:
            price = sizes[2]
        self.label_price.setText(f"ფასი: {price}₾")

    def place_order(self):
        cat = self.comboBox_category.currentText()
        dr = self.comboBox_drink.currentText()
        if not dr:
            QMessageBox.warning(self, "შეცდომა", "გთხოვთ აირჩიოთ სასმელი.") #ყოველი შემთხვევისთვის იყოს
            return
        size = "მცირე" if self.radioButton_small.isChecked() else "საშუალო" if self.radioButton_medium.isChecked() else "დიდი"
        price = self.label_price.text().replace("ფასი: ", "")
        self.label_result.setText(f"შეკვეთა: {cat} - {dr}, ზომა: {size}, ფასი: {price} 😛")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = DrinkOrderApp()
    window.show()
    sys.exit(app.exec_())