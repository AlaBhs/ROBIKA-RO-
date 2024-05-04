import sys
from PyQt5.QtWidgets import QApplication, QMainWindow,QTableWidgetItem,QSpinBox,QLabel
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
import mysql.connector
from ui_main import Ui_MainWindow
from ui_functions import UIFunctions

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        ## TOGGLE/BURGUER MENU
        ########################################################################
        self.ui.Btn_Toggle.clicked.connect(lambda: UIFunctions.toggleMenu(self, 250, True))

        ## PAGES
        ########################################################################

        # PAGE 1
        self.ui.btn_page_1.clicked.connect(self.on_btn_page_clicked)

        # PAGE 2
        self.ui.btn_page_2.clicked.connect(self.on_btn_page_clicked)

        # PAGE 3
        self.ui.btn_page_3.clicked.connect(self.on_btn_page_clicked)
        # Problem 1 Page
        self.ui.btn_problem_1.clicked.connect(self.on_btn_problem_1_clicked)

        # Problem 2 Page
        self.ui.btn_problem_2.clicked.connect(self.on_btn_problem_2_clicked)
        # Solution 1 Page
        self.ui.btn_solution_1.clicked.connect(self.on_btn_solution_1_clicked)

        # Solution 2 Page
        self.ui.btn_solution_2.clicked.connect(self.on_btn_solution_2_clicked)
        # Submit Problem 1 Page
        self.ui.problem1_submit_btn.clicked.connect(self.on_btn_problem_1_submit_clicked)
        # Submit Problem 2 Page
        self.ui.problem2_enter_btn.clicked.connect(self.on_btn_problem2_enter_clicked)
        self.ui.problem2_submit_btn.clicked.connect(self.on_btn_problem_2_submit_clicked)
        # Connect check box signal to slot
        self.ui.checkbox_2.clicked.connect(self.on_checkbox_2_clicked)
        # Connect check box signal to slot
        self.ui.checkbox_1.clicked.connect(self.on_checkbox_1_clicked)
        # Connect check box signal to slot
        self.ui.checkbox_3.clicked.connect(self.on_checkbox_3_clicked)
        # Connect check box signal to slot
        self.ui.checkbox_4.clicked.connect(self.on_checkbox_4_clicked)

        
        ## SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()
    def on_checkbox_4_clicked(self):
            # Show or hide input field based on the check box state
            if self.ui.checkbox_4.isChecked():
                self.ui.input_4_weighting.show()
                self.ui.input_4_weighting_label.show()
                self.ui.input_4_profit_label.show()
                self.ui.input_4_profit.show()
                self.ui.input_4_ovenTime.show()
                self.ui.input_4_ovenTime_label.show()
                self.ui.input_4_flour_blm.show()
                self.ui.input_4_flour_blm_label.show()
                self.ui.input_4_butter_blm.show()
                self.ui.input_4_butter_blm_label.show()
                self.ui.input_4_sugar_blm.show()
                self.ui.input_4_sugar_blm_label.show()
                self.ui.input_4_eggs_blm.show()
                self.ui.input_4_eggs_blm_label.show()

                
            else:
                self.ui.input_4_weighting.hide()
                self.ui.input_4_weighting_label.hide()
                self.ui.input_4_profit_label.hide()
                self.ui.input_4_profit.hide()
                self.ui.input_4_ovenTime.hide()
                self.ui.input_4_ovenTime_label.hide()
                self.ui.input_4_flour_blm.hide()
                self.ui.input_4_flour_blm_label.hide()
                self.ui.input_4_butter_blm.hide()
                self.ui.input_4_butter_blm_label.hide()
                self.ui.input_4_sugar_blm.hide()
                self.ui.input_4_sugar_blm_label.hide()
                self.ui.input_4_eggs_blm.hide()
                self.ui.input_4_eggs_blm_label.hide()
    def on_checkbox_3_clicked(self):
            # Show or hide input field based on the check box state
            if self.ui.checkbox_3.isChecked():
                self.ui.input_3_weighting.show()
                self.ui.input_3_weighting_label.show()
                self.ui.input_3_profit_label.show()
                self.ui.input_3_profit.show()
                self.ui.input_3_ovenTime.show()
                self.ui.input_3_ovenTime_label.show()
                self.ui.input_3_flour_bnm.show()
                self.ui.input_3_flour_bnm_label.show()
                self.ui.input_3_sugar_bnm.show()
                self.ui.input_3_sugar_bnm_label.show()
                self.ui.input_3_butter_bnm.show()
                self.ui.input_3_butter_bnm_label.show()
                self.ui.input_3_eggs_bnm.show()
                self.ui.input_3_eggs_bnm_label.show()
            else:
                self.ui.input_3_weighting.hide()
                self.ui.input_3_weighting_label.hide()
                self.ui.input_3_profit_label.hide()
                self.ui.input_3_profit.hide()
                self.ui.input_3_ovenTime.hide()
                self.ui.input_3_ovenTime_label.hide()
                self.ui.input_3_flour_bnm.hide()
                self.ui.input_3_flour_bnm_label.hide()
                self.ui.input_3_sugar_bnm.hide()
                self.ui.input_3_sugar_bnm_label.hide()
                self.ui.input_3_butter_bnm.hide()
                self.ui.input_3_butter_bnm_label.hide()
                self.ui.input_3_eggs_bnm.hide()
                self.ui.input_3_eggs_bnm_label.hide()
    def on_checkbox_1_clicked(self):
            # Show or hide input field based on the check box state
            if self.ui.checkbox_1.isChecked():
                self.ui.input_1_weighting.show()
                self.ui.input_1_weighting_label.show()
                self.ui.input_1_profit_label.show()
                self.ui.input_1_profit.show()
                self.ui.input_1_ovenTime.show()
                self.ui.input_1_ovenTime_label.show()
                self.ui.input_1_flour_ccc.show()
                self.ui.input_1_flour_ccc_label.show()
                self.ui.input_1_eggs_ccc.show()
                self.ui.input_1_eggs_ccc_label.show()
                self.ui.input_1_butter_ccc.show()
                self.ui.input_1_butter_ccc_label.show()
                self.ui.input_1_sugar_ccc.show()
                self.ui.input_1_sugar_ccc_label.show()
                
            else:
                self.ui.input_1_weighting.hide()
                self.ui.input_1_weighting_label.hide()
                self.ui.input_1_profit_label.hide()
                self.ui.input_1_profit.hide()
                self.ui.input_1_ovenTime.hide()
                self.ui.input_1_ovenTime_label.hide()
                self.ui.input_1_flour_ccc.hide()
                self.ui.input_1_flour_ccc_label.hide()
                self.ui.input_1_eggs_ccc.hide()
                self.ui.input_1_eggs_ccc_label.hide()
                self.ui.input_1_butter_ccc.hide()
                self.ui.input_1_butter_ccc_label.hide()
                self.ui.input_1_sugar_ccc.hide()
                self.ui.input_1_sugar_ccc_label.hide()
    def on_checkbox_2_clicked(self):
            # Show or hide input field based on the check box state
            if self.ui.checkbox_2.isChecked():
                self.ui.input_2_weighting.show()
                self.ui.input_2_weighting_label.show()
                self.ui.input_2_profit_label.show()
                self.ui.input_2_profit.show()
                self.ui.input_2_ovenTime.show()
                self.ui.input_2_ovenTime_label.show()
                self.ui.input_2_flour_orc.show()
                self.ui.input_2_flour_orc_label.show()
                self.ui.input_2_sugar_orc.show()
                self.ui.input_2_sugar_orc_label.show()
                self.ui.input_2_butter_orc.show()
                self.ui.input_2_butter_orc_label.show()
                self.ui.input_2_eggs_orc.show()
                self.ui.input_2_eggs_orc_label.show()
            else:
                self.ui.input_2_weighting.hide()
                self.ui.input_2_weighting_label.hide()
                self.ui.input_2_profit_label.hide()
                self.ui.input_2_profit.hide()
                self.ui.input_2_ovenTime.hide()
                self.ui.input_2_ovenTime_label.hide()
                self.ui.input_2_flour_orc.hide()
                self.ui.input_2_flour_orc_label.hide()
                self.ui.input_2_sugar_orc.hide()
                self.ui.input_2_sugar_orc_label.hide()
                self.ui.input_2_butter_orc.hide()
                self.ui.input_2_butter_orc_label.hide()
                self.ui.input_2_eggs_orc.hide()
                self.ui.input_2_eggs_orc_label.hide()
    def on_btn_page_clicked(self):
        sender = self.sender()
        # Set all button stylesheets to default
        for btn in [self.ui.btn_page_1, self.ui.btn_page_2, self.ui.btn_page_3]:
            btn.setStyleSheet("QPushButton {\n"
                              "    color: rgb(255, 255, 255);\n"
                              "    background-color: rgb(35, 35, 35);\n"
                              "    border: 0px solid;\n"
                              "}\n"
                              "QPushButton:hover {\n"
                              "    background-color: rgb(56, 56, 56);\n"
                              "}")

        # Change the background color of the clicked button to red
        sender.setStyleSheet("QPushButton {\n"
                             "    color: rgb(255, 255, 255);\n"
                             "    background-color: rgb(56, 56, 56);\n"
                             "    border: 0px solid;\n"
                             "}\n"
                             "QPushButton:hover {\n"
                             "    background-color: rgb(56, 56, 56);\n"
                             "}")

        # Set the current widget of stackedWidget
        if sender == self.ui.btn_page_1:
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_1)
        elif sender == self.ui.btn_page_2:
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_2)
        elif sender == self.ui.btn_page_3:
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_3)
            # fetch the data and set the tables here
            self.populate_table1()
            # self.populate_table2()
    # Fetch data from the database
    def fetch_data(self, table, orderby):
        try:
            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="password",
                database="RO_history"
            )
            cursor = connection.cursor()

            query = f"SELECT * FROM {table} ORDER BY {orderby} DESC"
            cursor.execute(query)
            rows = cursor.fetchall()

            return rows

        except mysql.connector.Error as error:
            print("Error fetching data:", error)
            return []

    def populate_table1(self):
        # Fetch data from the database
        rows = self.fetch_data("history","createdIn")
        # Clear existing rows from the table
        self.ui.table.clearContents()
        self.ui.table.setRowCount(0)  # Reset row count

        # Set the number of rows based on the fetched data
        self.ui.table.setRowCount(len(rows))
        # Populate table with fetched data
        for row_num, row_data in enumerate(rows):
            for col_num, col_data in enumerate(row_data):
                item = QTableWidgetItem(str(col_data))
                item.setTextAlignment(Qt.AlignCenter)
                self.ui.table.setItem(row_num, col_num, item)

    def populate_table2(self):
        # Fetch data from the database
        rows = self.fetch_data("history2","created_at")
        # Clear existing rows from the table2
        self.ui.table2.clearContents()
        self.ui.table2.setRowCount(0)  # Reset row count

        # Set the number of rows based on the fetched data
        self.ui.table2.setRowCount(len(rows))
        # Populate table2 with fetched data
        for row_num, row_data in enumerate(rows):
            for col_num, col_data in enumerate(row_data):
                item = QTableWidgetItem(str(col_data))
                item.setTextAlignment(Qt.AlignCenter)
                self.ui.table2.setItem(row_num, col_num, item)


    def on_btn_problem2_enter_clicked(self):
        num_neighborhoods = self.ui.input_1_2.value()
        num_locations = self.ui.input_2_2.value()
        self.ui.input_1_2.hide()
        self.ui.input_2_2.hide()
        self.ui.input_1_label_2.hide()
        self.ui.input_2_label_2.hide()
        self.ui.problem2_submit_btn.show()
        self.ui.problem2_enter_btn.hide()
        font_2 = QFont()
        font_2.setPointSize(13)
        font_1 = QFont()
        font_1.setPointSize(16)

        input_2_label_2 = QLabel("Enter the capacity and the cost of each bakery:")
        input_2_label_2.setFont(font_1)
        input_2_label_2.setStyleSheet("color: #FFF;padding-bottom:5px;")
        self.ui.bottom_layout_2.addWidget(input_2_label_2, 2, 0, 1, 5, alignment=Qt.AlignLeft)


        distance_label = QLabel("Enter the distance between neighborhoods and bakeries:")
        distance_label.setFont(font_1)
        distance_label.setStyleSheet("color: #FFF;padding-bottom:5px;")
        self.ui.bottom_layout_2.addWidget(distance_label, 3+num_locations, 0, 1, 5, alignment=Qt.AlignLeft)

        distance_locations_label = QLabel("Enter the distance between the different bakeries:")
        distance_locations_label.setFont(font_1)
        distance_locations_label.setStyleSheet("color: #FFF;padding-bottom:5px;")
        self.ui.bottom_layout_2.addWidget(distance_locations_label, num_neighborhoods*num_locations + 9, 0, 1, 5, alignment=Qt.AlignLeft)

        for i in range(num_locations):

             # Create and add labels to column 0 and 2
            capacity_label = QLabel(f"Capacity of bakery {i+1}:")
            capacity_label.setFont(font_2)
            capacity_label.setStyleSheet("color: #FFF;padding-bottom:5px;")
            self.ui.bottom_layout_2.addWidget(capacity_label, i+3, 0, alignment=Qt.AlignLeft)

            cost_label = QLabel(f"Cost of bakery {i+1}:")
            cost_label.setFont(font_2)
            cost_label.setStyleSheet("color: #FFF;padding-bottom:5px;")
            self.ui.bottom_layout_2.addWidget(cost_label, i+3, 2, alignment=Qt.AlignLeft)

                    # Create and add capacity spin box
            setattr(self.ui, f"capacity_spinbox_{i+1}", QSpinBox())
            capacity_spinbox = getattr(self.ui, f"capacity_spinbox_{i+1}")
            capacity_spinbox.setObjectName(f"capacity_spinbox_{i}")
            capacity_spinbox.setRange(0, 1000)
            capacity_spinbox.setSuffix(" units")
            capacity_spinbox.setFont(font_2)
            capacity_spinbox.setStyleSheet("background-color: #F0F0F0;padding:5px;")
            capacity_spinbox.setFixedWidth(100)
            self.ui.bottom_layout_2.addWidget(capacity_spinbox, i+3, 1, alignment=Qt.AlignLeft)

            # Create and add cost spin box
            setattr(self.ui, f"cost_spinbox_{i+1}", QSpinBox())
            cost_spinbox = getattr(self.ui, f"cost_spinbox_{i+1}")
            cost_spinbox.setObjectName(f"cost_spinbox_{i}")
            cost_spinbox.setRange(0, 10000)
            cost_spinbox.setSuffix(" $")
            cost_spinbox.setFont(font_2)
            cost_spinbox.setStyleSheet("background-color: #F0F0F0;padding:5px;")
            cost_spinbox.setFixedWidth(100)
            self.ui.bottom_layout_2.addWidget(cost_spinbox, i+3, 3, alignment=Qt.AlignLeft)
        # Assuming num_neighborhoods and num_locations are defined
        for i in range(num_neighborhoods):
            for j in range(num_locations):
                # Create and add labels for distance min and max
                distance_min_label = QLabel(f"D min - N {i+1} to L {j+1}:")
                distance_min_label.setFont(font_2)
                distance_min_label.setStyleSheet("color: #FFF;padding-bottom:5px;")
                distance_min_label.setFixedWidth(240)
                self.ui.bottom_layout_2.addWidget(distance_min_label, i*num_locations+ j + num_locations+ 4, 2, alignment=Qt.AlignLeft)

                distance_max_label = QLabel(f"D max - N {i+1} to L {j+1}:")
                distance_max_label.setFont(font_2)
                distance_max_label.setStyleSheet("color: #FFF;padding-bottom:5px;")
                distance_max_label.setFixedWidth(240)
                self.ui.bottom_layout_2.addWidget(distance_max_label,  i*num_locations+ j + num_locations+ 4, 4, alignment=Qt.AlignLeft)

                distance_label = QLabel(f"Distance - N {i+1} to L {j+1}:")
                distance_label.setFont(font_2)
                distance_label.setStyleSheet("color: #FFF;padding-bottom:5px;")
                distance_label.setFixedWidth(240)
                self.ui.bottom_layout_2.addWidget(distance_label, i*num_locations +  j + num_locations+ 4, 0, alignment=Qt.AlignLeft)

                # Create and add spin boxes for distance
                setattr(self.ui, f"distance_spinbox_{i+1}_{j+1}", QSpinBox())
                distance_spinbox = getattr(self.ui, f"distance_spinbox_{i+1}_{j+1}")
                distance_spinbox.setRange(0, 100)
                distance_spinbox.setSuffix(" km")
                distance_spinbox.setFont(font_2)
                distance_spinbox.setStyleSheet("background-color: #F0F0F0;padding:5px;")
                distance_spinbox.setFixedWidth(100)
                self.ui.bottom_layout_2.addWidget(distance_spinbox, i*num_locations + j + num_locations + 4, 1, alignment=Qt.AlignLeft)

                # Create and add spin boxes for distance min and max
                setattr(self.ui, f"distance_min_spinbox_{i+1}_{j+1}", QSpinBox())
                distance_min_spinbox = getattr(self.ui, f"distance_min_spinbox_{i+1}_{j+1}")
                distance_min_spinbox.setRange(0, 100)
                distance_min_spinbox.setSuffix(" km")
                distance_min_spinbox.setFont(font_2)
                distance_min_spinbox.setStyleSheet("background-color: #F0F0F0;padding:5px;")
                distance_min_spinbox.setFixedWidth(100)
                self.ui.bottom_layout_2.addWidget(distance_min_spinbox, i*num_locations + j + num_locations + 4, 3, alignment=Qt.AlignLeft)

                setattr(self.ui, f"distance_max_spinbox_{i+1}_{j+1}", QSpinBox())
                distance_max_spinbox = getattr(self.ui, f"distance_max_spinbox_{i+1}_{j+1}")
                distance_max_spinbox.setRange(0, 100)
                distance_max_spinbox.setSuffix(" km")
                distance_max_spinbox.setFont(font_2)
                distance_max_spinbox.setStyleSheet("background-color: #F0F0F0;padding:5px;")
                distance_max_spinbox.setFixedWidth(100)
                self.ui.bottom_layout_2.addWidget(distance_max_spinbox, i*num_locations + j + num_locations + 4, 5, alignment=Qt.AlignLeft)
        count=0
        for i in range(num_locations):
            for j in range(num_locations):
                if i != j and i < j:  # Avoid creating spin boxes for distances between the same location
                    # Create and add labels for distance between locations
                    distance_label = QLabel(f"D between (L{i+1},L{j+1}):")
                    distance_label.setFont(font_2)
                    distance_label.setStyleSheet("color: #FFF;padding-bottom:5px;")
                    self.ui.bottom_layout_2.addWidget(distance_label, (num_neighborhoods + 1)*num_locations + j + 9-count, i+count, alignment=Qt.AlignLeft)

                    # Create and add spin boxes for distance between locations
                    setattr(self.ui, f"distance_bakeries_spinbox_{i+1}_{j+1}", QSpinBox())
                    distance_bakeries_spinbox = getattr(self.ui, f"distance_bakeries_spinbox_{i+1}_{j+1}")
                    distance_bakeries_spinbox.setRange(0, 100)
                    distance_bakeries_spinbox.setSuffix(" km")
                    distance_bakeries_spinbox.setFont(font_2)
                    distance_bakeries_spinbox.setStyleSheet("background-color: #F0F0F0;padding:5px;")
                    self.ui.bottom_layout_2.addWidget(distance_bakeries_spinbox, (num_neighborhoods + 1)*num_locations + j + 9-count, i+1+count, alignment=Qt.AlignLeft)
            count=count+1

    def on_btn_problem_1_clicked(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.problem_1_page)

    def on_btn_problem_2_clicked(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.problem_2_page)

    def on_btn_solution_1_clicked(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.solution_1_page)

    def on_btn_solution_2_clicked(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.solution_2_page)

    def on_btn_problem_1_submit_clicked(self):
        input_1_profit = -1
        input_1_weighting = -1
        input_1_flour_ccc = -1
        input_1_butter_ccc = -1
        input_1_sugar_ccc = -1
        input_1_eggs_ccc = -1
        input_1_ovenTime = -1

        input_2_profit = -1
        input_2_weighting = -1
        input_2_flour_orc = -1
        input_2_butter_orc = -1
        input_2_sugar_orc = -1
        input_2_eggs_orc = -1
        input_2_ovenTime = -1

        input_3_profit = -1
        input_3_weighting = -1
        input_3_flour_bnm = -1
        input_3_butter_bnm = -1
        input_3_sugar_bnm = -1
        input_3_eggs_bnm = -1
        input_3_ovenTime = -1

        input_4_profit = -1
        input_4_weighting = -1
        input_4_flour_blm = -1
        input_4_butter_blm = -1
        input_4_sugar_blm = -1
        input_4_eggs_blm = -1
        input_4_ovenTime = -1
        if self.ui.checkbox_1.isChecked():
            input_1_profit = self.ui.input_1_profit.value()
            input_1_weighting = self.ui.input_1_weighting.value()
            input_1_flour_ccc = self.ui.input_1_flour_ccc.value()
            input_1_butter_ccc = self.ui.input_1_butter_ccc.value()
            input_1_sugar_ccc = self.ui.input_1_sugar_ccc.value()
            input_1_eggs_ccc = self.ui.input_1_eggs_ccc.value()
            input_1_ovenTime = self.ui.input_1_ovenTime.value()
        
        if self.ui.checkbox_2.isChecked():
            input_2_profit = self.ui.input_2_profit.value()
            input_2_weighting = self.ui.input_2_weighting.value()
            input_2_flour_orc = self.ui.input_2_flour_orc.value()
            input_2_butter_orc = self.ui.input_2_butter_orc.value()
            input_2_sugar_orc = self.ui.input_2_sugar_orc.value()
            input_2_eggs_orc = self.ui.input_2_eggs_orc.value()
            input_2_ovenTime = self.ui.input_2_ovenTime.value()
        
        if self.ui.checkbox_3.isChecked():
            input_3_profit = self.ui.input_3_profit.value()
            input_3_weighting = self.ui.input_3_weighting.value()
            input_3_flour_bnm = self.ui.input_3_flour_bnm.value()
            input_3_butter_bnm = self.ui.input_3_butter_bnm.value()
            input_3_sugar_bnm = self.ui.input_3_sugar_bnm.value()
            input_3_eggs_bnm = self.ui.input_3_eggs_bnm.value()
            input_3_ovenTime = self.ui.input_3_ovenTime.value()
        
        if self.ui.checkbox_4.isChecked():
            input_4_profit = self.ui.input_4_profit.value()
            input_4_weighting = self.ui.input_4_weighting.value()
            input_4_flour_blm = self.ui.input_4_flour_blm.value()
            input_4_butter_blm = self.ui.input_4_butter_blm.value()
            input_4_sugar_blm = self.ui.input_4_sugar_blm.value()
            input_4_eggs_blm = self.ui.input_4_eggs_blm.value()
            input_4_ovenTime = self.ui.input_4_ovenTime.value()

        input_1_flour = self.ui.input_1_flour.value()
        input_2_sugar = self.ui.input_2_sugar.value()
        input_3_eggs = self.ui.input_3_eggs.value()
        input_4_butter = self.ui.input_4_butter.value()
        input_5_gluten = self.ui.input_5_gluten.value()
        input_6_oven_capacity = self.ui.input_6_oven_capacity.value()

        # Create lists for each input type and append the values
        profit_list = [input_1_profit, input_2_profit, input_3_profit, input_4_profit]
        weighting_list = [input_1_weighting, input_2_weighting, input_3_weighting, input_4_weighting]
        flour_list = [input_1_flour_ccc, input_2_flour_orc, input_3_flour_bnm, input_4_flour_blm]
        butter_list = [input_1_butter_ccc, input_2_butter_orc, input_3_butter_bnm, input_4_butter_blm]
        sugar_list = [input_1_sugar_ccc, input_2_sugar_orc, input_3_sugar_bnm, input_4_sugar_blm]
        eggs_list = [input_1_eggs_ccc, input_2_eggs_orc, input_3_eggs_bnm, input_4_eggs_blm]
        oven_time_list = [input_1_ovenTime, input_2_ovenTime, input_3_ovenTime, input_4_ovenTime]
        global_inputs_list =[input_1_flour,input_2_sugar,input_3_eggs,input_4_butter,input_5_gluten,input_6_oven_capacity]





        
        
        

        # Save the values in a MySQL database
        # self.save_to_database("problem 1", input_1_value, input_2_value, input_3_value, input_4_value, "this is a result")

        # Print the values
        # print("Input 1 problem 1:", input_1_value)
        # print("Input 2 problem 1:", input_2_value)
        # print("Input 3 problem 1:", input_3_value)
        # print("Input 4 problem 1:", input_4_value)

        # Reset input values for product 1
        self.ui.input_1_profit.setValue(0)
        self.ui.input_1_weighting.setValue(0)
        self.ui.input_1_flour_ccc.setValue(0)
        self.ui.input_1_butter_ccc.setValue(0)
        self.ui.input_1_sugar_ccc.setValue(0)
        self.ui.input_1_eggs_ccc.setValue(0)
        self.ui.input_1_ovenTime.setValue(0)

        # Reset input values for product 2
        self.ui.input_2_profit.setValue(0)
        self.ui.input_2_weighting.setValue(0)
        self.ui.input_2_flour_orc.setValue(0)
        self.ui.input_2_butter_orc.setValue(0)
        self.ui.input_2_sugar_orc.setValue(0)
        self.ui.input_2_eggs_orc.setValue(0)
        self.ui.input_2_ovenTime.setValue(0)

        # Reset input values for product 3
        self.ui.input_3_profit.setValue(0)
        self.ui.input_3_weighting.setValue(0)
        self.ui.input_3_flour_bnm.setValue(0)
        self.ui.input_3_butter_bnm.setValue(0)
        self.ui.input_3_sugar_bnm.setValue(0)
        self.ui.input_3_eggs_bnm.setValue(0)
        self.ui.input_3_ovenTime.setValue(0)

        # Reset input values for product 4
        self.ui.input_4_profit.setValue(0)
        self.ui.input_4_weighting.setValue(0)
        self.ui.input_4_flour_blm.setValue(0)
        self.ui.input_4_butter_blm.setValue(0)
        self.ui.input_4_sugar_blm.setValue(0)
        self.ui.input_4_eggs_blm.setValue(0)
        self.ui.input_4_ovenTime.setValue(0)

        # Reset input values for global inputs
        self.ui.input_1_flour.setValue(0)
        self.ui.input_2_sugar.setValue(0)
        self.ui.input_3_eggs.setValue(0)
        self.ui.input_4_butter.setValue(0)
        self.ui.input_5_gluten.setValue(0)
        self.ui.input_6_oven_capacity.setValue(0)

        print("Profit List:", profit_list)
        print("Weighting List:", weighting_list)
        print("Flour List:", flour_list)
        print("Butter List:", butter_list)
        print("Sugar List:", sugar_list)
        print("Eggs List:", eggs_list)
        print("Oven Time List:", oven_time_list)
        print("General List:", global_inputs_list)


        # redirection to result page
        self.ui.stackedWidget.setCurrentWidget(self.ui.gurobi_res1_page)
         # Save the values in a MySQL database
        self.save_to_database("Bakery", profit_list, weighting_list, flour_list, butter_list, sugar_list, eggs_list, oven_time_list, global_inputs_list, "this is a result")


    def on_btn_problem_2_submit_clicked(self):
        # Read the values entered in the input widgets
        num_neighborhoods = self.ui.input_1_2.value()
        num_locations = self.ui.input_2_2.value()


        self.ui.problem2_submit_btn.hide()
        self.ui.problem2_enter_btn.show()
        self.ui.stackedWidget.setCurrentWidget(self.ui.gurobi_res2_page)
        # Save the values in a MySQL database
        # self.save_to_database("problem 2", input_1_value, input_2_value, input_3_value, input_4_value, "this is a result")
        # Define lists to store the values
        capacities = []
        costs = []
        distances = []
        distances_min = []
        distances_max = []
        distance_bakeries = []

        # Collect capacities and costs
        for i in range(num_locations):
            capacity_spinbox = getattr(self.ui, f"capacity_spinbox_{i+1}")
            cost_spinbox = getattr(self.ui, f"cost_spinbox_{i+1}")

            capacities.append(capacity_spinbox.value())
            costs.append(cost_spinbox.value())

        # Collect distances, distances_min, and distances_max
        for i in range(num_neighborhoods):
            for j in range(num_locations):
                distance_spinbox = getattr(self.ui, f"distance_spinbox_{i+1}_{j+1}")
                distance_min_spinbox = getattr(self.ui, f"distance_min_spinbox_{i+1}_{j+1}")
                distance_max_spinbox = getattr(self.ui, f"distance_max_spinbox_{i+1}_{j+1}")

                distances.append(distance_spinbox.value())
                distances_min.append(distance_min_spinbox.value())
                distances_max.append(distance_max_spinbox.value())

        for i in range(num_locations):
            for j in range(num_locations):
                if i != j and i < j:  # Avoid reading spin boxes for distances between the same location
                    distance_bakeries_spinbox = getattr(self.ui, f"distance_bakeries_spinbox_{i+1}_{j+1}")

                    distance_bakeries.append(f"({i+1},{j+1}):{distance_bakeries_spinbox.value()}")



        print("Neighborhoods:", num_neighborhoods)
        print("Bakeries:", num_locations)
        print("Capacities List:", capacities)
        print("Costs List:", costs)
        print("Distances List:", distances)
        print("Distances min List:", distances_min)
        print("Distances max List:", distances_max)
        print("Distances Bakeries List:", distance_bakeries)
        self.save_to_database2("Build Bakeries",num_neighborhoods ,num_locations,capacities, costs, distances, distances_min, distances_max, distance_bakeries, "result problem 2")
        # Now you have all the values collected in lists


    def save_to_database(self, problemName, profit_list, weighting_list, flour_list, butter_list, sugar_list, eggs_list, oven_time_list,general_list, result):
        try:
            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="password",
                database="RO_history"
            )

            cursor = connection.cursor()

            query = "INSERT INTO history (name, profit_list, weighting_list, flour_list, butter_list, sugar_list, eggs_list, oven_time_list, general_list, result) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            values = (problemName, str(profit_list), str(weighting_list), str(flour_list), str(butter_list), str(sugar_list), str(eggs_list), str(oven_time_list), str(general_list), result)

            cursor.execute(query, values)

            connection.commit()

            print("Values saved to database successfully!")

        except mysql.connector.Error as error:
            print("Failed to insert values into MySQL table:", error)

        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
                print("MySQL connection is closed")


    def save_to_database2(self, problemName,num_neighborhoods ,num_locations, capacities_list, costs_list, distances_list, distances_min_list, distances_max_list, distances_bakeries_list, result):
        try:
            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="password",
                database="RO_history"
            )

            cursor = connection.cursor()

            query = "INSERT INTO history2 (name, neighborhoods, bakeries, capacities, costs, distances, distances_min, distances_max, distances_bakeries, result) VALUES (%s, %s, %s, %s,%s, %s, %s, %s, %s, %s)"
            values = (problemName,str(num_neighborhoods), str(num_locations), str(capacities_list), str(costs_list), str(distances_list), str(distances_min_list), str(distances_max_list), str(distances_bakeries_list), result)

            cursor.execute(query, values)

            connection.commit()

            print("Values saved to database successfully!")

        except mysql.connector.Error as error:
            print("Failed to insert values into MySQL table:", error)

        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
                print("MySQL connection is closed")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
