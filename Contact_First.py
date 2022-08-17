from PyQt5.QtWidgets import QMainWindow, QApplication, QListWidget, QPushButton, QLabel, QComboBox, QLineEdit
from PyQt5.QtCore import Qt
from PyQt5 import uic
import numpy as np
from Contact_Third import BatMan

class CHINCHO(QMainWindow):

    def Concrete_Contact_page(self):
        try:
            if len(self.people_list.currentItem().text()) > 0:
                self.window3 = QMainWindow()
                self.bat = BatMan()
                self.close()
            else:
                None
        except AttributeError:
            None

    def __init__(self):
        super(CHINCHO, self).__init__()

        # load ui file:
        uic.loadUi("FIRST.ui", self)

        # DEFINE CONTENT:
        self.add_button = self.findChild(QPushButton, "add_button")
        self.delete_button = self.findChild(QPushButton, "delete_button")
        self.search_button = self.findChild(QPushButton, "search_button")
        self.open_button = self.findChild(QPushButton, "open_button")
        self.refresh_button = self.findChild(QPushButton, "refresh_button")
        self.exit_button = self.findChild(QPushButton, "exit_button")

        self.search_line = self.findChild(QLineEdit, "search_line")

        self.combo_box_1 = self.findChild(QComboBox, "combo_box_1")
        self.people_list = self.findChild(QListWidget, "people_list")

        self.contacts_label = self.findChild(QLabel, "contacts_label")
        self.exam_label = self.findChild(QLabel, "exam_label")

        self.contact_array_1 = np.array([])

#----------------------------------------------------- call --------------------------------------- #
        self.exit_button.clicked.connect(lambda: self.close())
        self.add_button.clicked.connect(self.Write_Forward)
        self.add_button.clicked.connect(lambda: self.close())
        self.delete_button.clicked.connect(self.Delete_From_array)
        self.refresh_button.clicked.connect(self.REFRESH)
        self.search_button.clicked.connect(self.Search_Contact)
        
        self.open_button.clicked.connect(self.Concrete_Contact_page)
        self.open_button.clicked.connect(self.Open_Contact)
        self.open_button.clicked.connect(self.Write_On_Conrete_Contact)

        self.show()
        
#------------------------------------------------------ logic ---------------------------------------- #
    # define method for add button:
    def Write_Forward(self):
        from Contact_Second import SpiderMan
        self.window2 = QMainWindow()
        self.form = SpiderMan() 
        
        if len(self.contact_array_1) == 1:
            variable = self.contact_array_1[-1]
            self.form.contact_array_2 = np.append(self.form.contact_array_2, [variable])
        elif len(self.contact_array_1) > 1:
            for i in self.contact_array_1:
                self.form.contact_array_2 = np.append(self.form.contact_array_2, [i])
        else:
            None
    
    # define method for open button:
    def Write_On_Conrete_Contact(self):
        try:
            if len(self.contact_array_1) == 1:
                variable = self.contact_array_1[-1]
                self.bat.contact_array_3 = np.append(self.bat.contact_array_3, [variable])
            elif len(self.contact_array_1) > 1:
                for i in self.contact_array_1:
                    self.bat.contact_array_3 = np.append(self.bat.contact_array_3, [i])
            else:
                None
        except AttributeError:
            None
    
    # define method for refresh button:
    def REFRESH(self):
        self.people_list.clear()

        bad_array = np.array([])
        for i in self.contact_array_1:
            bad_array = np.append(bad_array, [str(i.keys())])

        for j in bad_array:
            first_position = j.find("'") + 1
            second_position = j.find("'", j.find("'") + 1)
            self.people_list.addItem(f"{j[first_position:second_position:1]}")
        self.people_list.sortItems(Qt.SortOrder.AscendingOrder)

    # define method for search button:
    def Search_Contact(self):
        Entered = self.search_line.text()
        chosen = self.combo_box_1.currentText()

        if len(Entered) > 0:
            if chosen == "with Full Name":
                Items = self.people_list.findItems(f"{Entered}", Qt.MatchExactly)

                answer = np.array([])
                if len(Items) > 0:
                    for j in Items:
                        answer = np.append(answer, [j.text()])

                    self.people_list.clear()
                    for i in answer:
                        self.people_list.addItem(f"{i}")
                    self.search_line.setText("")
                else:
                    self.search_line.setText("Not Found!")
            
            elif chosen == "with First letter" and len(Entered) == 1:
                self.people_list.clear()
                great_array = np.array([])
                for i in self.contact_array_1:
                    great_array = np.append(great_array, [str(i.keys())])
                
                answer_array = np.array([])
                for j in great_array:
                    first_position = j.find("'") + 1
                    second_position = j.find("'", j.find("'") + 1)
                    answer_array = np.append(answer_array, [f"{j[first_position:second_position:1]}"])
                
                for l in answer_array:
                    if l[0] == Entered:
                        self.people_list.addItem(f"{l}")
                
                if self.people_list.count() == 0:
                    self.search_line.setText("Not Found!")
                else:
                    self.search_line.setText("")
        else:
            None
    
    # define method for open button:
    def Open_Contact(self):
        try:
            items = self.people_list.currentItem().text()
            self.exam_label.setText(f"{items}")
            
            name = ''
            control = ''
            for i in self.contact_array_1:
                for j in i.keys():
                    if j == items:
                        name = str(i.keys())
                        control = str(i.values())

            first_position_1 = name.find("'") + 1
            second_position_1 = name.find("'", name.find("'") + 1)

            first_position_2 = control.find("'") + 1
            second_position_2 = control.find("'", control.find("'") + 1)

            key_name = name[first_position_1:second_position_1:1]
            value_items = control[first_position_2:second_position_2:1]
            value_name = value_items.split(",")

            self.bat.name_label.setText(f"{key_name}")
            self.bat.display_lastname.setText(f"{value_name[0]}")
            self.bat.display_number.setText(f"{value_name[1]}")
            self.bat.display_email.setText(f"{value_name[2]}")
        except AttributeError:
            None
    
    # define method for delete button:
    def Delete_From_array(self):
        try:
            items = self.people_list.currentItem().text()
            for i in self.contact_array_1:
                if items in i.keys():
                    position = np.where(self.contact_array_1 == i)
                    self.contact_array_1 = np.delete(self.contact_array_1, position)

            for j in range(0, self.people_list.count() - 1):
                self.people_list.takeItem(j)

            self.REFRESH()
            self.exam_label.setText("")
        except AttributeError:
            None



# ------------------------------------------------- END --------------------------------------------- #


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    ui = CHINCHO()
    sys.exit(app.exec_())