from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel
from PyQt5.QtCore import Qt
from PyQt5 import uic
import numpy as np

class BatMan(QMainWindow):
    def __init__(self):
        super(BatMan, self).__init__()

        # load ui file:
        uic.loadUi("THIRD.ui", self)

        # Define Content:
        self.picture_label = self.findChild(QLabel, "picture_label")
        self.name_label = self.findChild(QLabel, "name_label")
        self.message_label = self.findChild(QLabel, "message_label")
        self.call_label = self.findChild(QLabel, "call_label")
        self.viber_label = self.findChild(QLabel, "viber_label")
        self.mail_label = self.findChild(QLabel, "mail_label")
        self.lastname_label = self.findChild(QLabel, "lastname_label")
        self.phone_label = self.findChild(QLabel, "phone_label")
        self.email_label = self.findChild(QLabel, "email_label")
        self.display_lastname = self.findChild(QLabel, "display_lastname")
        self.display_number = self.findChild(QLabel, "display_number")
        self.display_email = self.findChild(QLabel, "display_email")

        self.edit_button = self.findChild(QPushButton, "edit_button")
        self.return_button = self.findChild(QPushButton, "return_button")

        self.contact_array_3 = np.array([])

        self.return_button.clicked.connect(self.Write_Back_On_First)
        self.return_button.clicked.connect(lambda: self.close())
        self.edit_button.clicked.connect(self.Edit_Contact)
        self.edit_button.clicked.connect(lambda: self.close())

        self.show()

# ------------------------------------------------- logic ----------------------------------------- #
    # define method for return button:
    def Write_Back_On_First(self):
        from Contact_First import CHINCHO
        self.window1 = QMainWindow()
        self.ui = CHINCHO() 

        if len(self.contact_array_3) > 0:
            for i in self.contact_array_3:
                self.ui.contact_array_1 = np.append(self.ui.contact_array_1, [i])
        
        big_array = np.array([])
        for i in self.ui.contact_array_1:
            big_array = np.append(big_array, [str(i.keys())])

        for j in big_array:
            first_position = j.find("'") + 1
            second_position = j.find("'", j.find("'") + 1)
            self.ui.people_list.addItem(f"{j[first_position:second_position:1]}")
        self.ui.people_list.sortItems(Qt.SortOrder.AscendingOrder)
    
    def Edit_Contact(self):
        from Contact_Second import SpiderMan
        self.window2 = QMainWindow()
        self.form = SpiderMan()

        if len(self.contact_array_3) > 0:
            for i in self.contact_array_3:
                self.form.contact_array_2 = np.append(self.form.contact_array_2, [i])
        
        firstname = self.name_label.text()
        lastname = self.display_lastname.text()
        phone_number = self.display_number.text()
        gmail = self.display_email.text()

        self.form.name_line.setText(f"{firstname}")
        self.form.surname_line.setText(f"{lastname}")
        self.form.number_line.setText(f"{phone_number}")
        self.form.email_line.setText(f"{gmail}")

        for j in self.form.contact_array_2:
            if firstname in j.keys():
                position = np.where(self.form.contact_array_2 == j)
                self.form.contact_array_2 = np.delete(self.form.contact_array_2, position)

# -------------------------------------------------- end ----------------------------------------- #

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    bat = BatMan()
    sys.exit(app.exec_())