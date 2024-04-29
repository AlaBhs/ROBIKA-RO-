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
        
        ## SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()

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

            query = "SELECT * FROM history"
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
        # Read the values entered in the input widgets
        input_1_value = self.ui.input_1.value()
        input_2_value = self.ui.input_2.value()
        input_3_value = self.ui.input_3.value()
        input_4_value = self.ui.input_4.value()
        
        # Save the values in a MySQL database
        self.save_to_database(input_1_value, input_2_value, input_3_value, input_4_value)

        # Print the values
        print("Input 1 problem 1:", input_1_value)
        print("Input 2 problem 1:", input_2_value)
        print("Input 3 problem 1:", input_3_value)
        print("Input 4 problem 1:", input_4_value)

        # Reset the input values
        self.ui.input_1.setValue(0)
        self.ui.input_2.setValue(0)
        self.ui.input_3.setValue(0)
        self.ui.input_4.setValue(0)

    def on_btn_problem_2_submit_clicked(self):
        # Read the values entered in the input widgets
        input_1_value = self.ui.input_1_2.value()
        input_2_value = self.ui.input_2_2.value()
        input_3_value = self.ui.input_3_2.value()
        input_4_value = self.ui.input_4_2.value()
        
        # Save the values in a MySQL database
        self.save_to_database(input_1_value, input_2_value, input_3_value, input_4_value)

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

    def save_to_database(self, input_1, input_2, input_3, input_4):
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
            query = "INSERT INTO history (input_1, input_2, input_3, input_4) VALUES (%s, %s, %s, %s)"
            values = (input_1, input_2, input_3, input_4)

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
