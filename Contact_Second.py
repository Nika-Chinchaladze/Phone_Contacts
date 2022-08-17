from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel, QLineEdit
from PyQt5.QtCore import Qt
from PyQt5 import uic
import numpy as np
from Contact_First import CHINCHO

class SpiderMan(QMainWindow):

    def Previous_Page(self):
        firstname = self.name_line.text()
        lastname = self.surname_line.text()
        phone = self.number_line.text()
        emails = self.email_line.text()

        if len(firstname) > 0 and len(lastname) > 0 and len(phone) > 0 and len(emails) > 0:
            self.window2 = QMainWindow()
            self.ui = CHINCHO()

            self.close()
        else:
            None

    def __init__(self):
        super(SpiderMan, self).__init__()

        # load ui file:
        uic.loadUi("SECOND.ui", self)

        # DEFINE CONTENT:
        self.back_button = self.findChild(QPushButton, "back_button")

        self.name_line = self.findChild(QLineEdit, "name_line")
        self.surname_line = self.findChild(QLineEdit, "surname_line")
        self.number_line = self.findChild(QLineEdit, "number_line")
        self.email_line = self.findChild(QLineEdit, "email_line")

        self.add_label = self.findChild(QLabel, "add_label")
        self.firstname_label = self.findChild(QLabel, "firstname_label")
        self.lastname_label = self.findChild(QLabel, "lastname_label")
        self.number_label = self.findChild(QLabel, "number_label")
        self.email_label = self.findChild(QLabel, "email_label")
        self.photo_label = self.findChild(QLabel, "photo_label")

        self.contact_array_2 = np.array([])

#----------------------------------------------------- call --------------------------------------- #
        self.back_button.clicked.connect(self.Previous_Page)
        self.back_button.clicked.connect(self.Write_Back)

        self.show()

#----------------------------------------------------- logic --------------------------------------- #  
    # define method for back button:
    def Write_Back(self):
        firstname = self.name_line.text()
        lastname = self.surname_line.text()
        phone = self.number_line.text()
        emails = self.email_line.text()

        if len(firstname) > 0 and len(lastname) > 0 and len(phone) > 0 and len(emails) > 0:
            dictionary = {f"{firstname}":f"{lastname}, {phone}, {emails}"}

            if len(self.contact_array_2) > 0:
                for i in self.contact_array_2:
                    self.ui.contact_array_1 = np.append(self.ui.contact_array_1, [i])
            self.ui.contact_array_1 = np.append(self.ui.contact_array_1, [dictionary])

            good_array = np.array([])
            for i in self.ui.contact_array_1:
                good_array = np.append(good_array, [str(i.keys())])

            for j in good_array:
                first_position = j.find("'") + 1
                second_position = j.find("'", j.find("'") + 1)
                self.ui.people_list.addItem(f"{j[first_position:second_position:1]}")
            self.ui.people_list.sortItems(Qt.SortOrder.AscendingOrder)
        else:
            None

#------------------------------------------------------ end ---------------------------------------- #    

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    form = SpiderMan()
    sys.exit(app.exec_())