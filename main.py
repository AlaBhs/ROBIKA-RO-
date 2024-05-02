import sys
from PyQt5.QtWidgets import QApplication, QMainWindow,QTableWidgetItem
from PyQt5.QtCore import Qt
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
        # Submit Problem 1 Page
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
            # fetch the data and set the table here
            self.populate_table()
    # Fetch data from the database
    def fetch_data(self):
        try:
            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="password",
                database="RO_history"
            )
            cursor = connection.cursor()

            query = "SELECT * FROM history ORDER BY creation_date DESC"
            cursor.execute(query)
            rows = cursor.fetchall()

            return rows

        except mysql.connector.Error as error:
            print("Error fetching data:", error)
            return []
    def populate_table(self):
        # Fetch data from the database
        rows = self.fetch_data()
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

    def on_btn_problem_2_submit_clicked(self):
        # Read the values entered in the input widgets
        input_1_value = self.ui.input_1_2.value()
        input_2_value = self.ui.input_2_2.value()
        input_3_value = self.ui.input_3_2.value()
        input_4_value = self.ui.input_4_2.value()
        
        self.ui.stackedWidget.setCurrentWidget(self.ui.gurobi_res2_page)
        # Save the values in a MySQL database
        self.save_to_database("problem 2", input_1_value, input_2_value, input_3_value, input_4_value, "this is a result")

        # Print the values
        print("Input 1 problem 2:", input_1_value)
        print("Input 2 problem 2:", input_2_value)
        print("Input 3 problem 2:", input_3_value)
        print("Input 4 problem 2:", input_4_value)

        # Reset the input values
        self.ui.input_1_2.setValue(0)
        self.ui.input_2_2.setValue(0)
        self.ui.input_3_2.setValue(0)
        self.ui.input_4_2.setValue(0)

    def save_to_database(self, problemName, input_1, input_2, input_3, input_4, result):
        # Connect to MySQL database
        try:
            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="password",
                database="RO_history"
            )

            # Create a cursor object
            cursor = connection.cursor()

            # Define the query to insert values into the table
            query = "INSERT INTO history (name, input_1, input_2, input_3, input_4, result) VALUES (%s, %s, %s, %s, %s, %s)"
            values = (problemName, input_1, input_2, input_3, input_4, result)

            # Execute the query
            cursor.execute(query, values)

            # Commit the transaction
            connection.commit()

            print("Values saved to database successfully!")

        except mysql.connector.Error as error:
            print("Failed to insert values into MySQL table:", error)

        finally:
            # Close the cursor and connection
            if connection.is_connected():
                cursor.close()
                connection.close()
                print("MySQL connection is closed")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
