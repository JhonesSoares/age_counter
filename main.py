from PySide6.QtWidgets import QMainWindow, QApplication

from src.ui.ui_windown import Ui_MainWindow
from src.date_time import Age
import sys

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setupUi(self)

        self.btnCalc.clicked.connect(self.label_result)

    def label_result(self):
        day_user = int(self.day.text())
        month_user = int(self.month.text()) + 1
        year_user = int(self.year.text())

        age = Age()
        result = age.calculate_age(day_user, month_user, year_user)

        self.labelResult.setText(result)
        print(result)

        self.day.clear()
        self.month.clear()
        self.year.clear()
        





if __name__=='__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()

    #print(idade.calculate_age(1,8+1,1994))