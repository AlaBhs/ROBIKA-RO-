from PyQt5.QtCore import Qt,QSize
from PyQt5.QtWidgets import QApplication, QMainWindow,QSpinBox,QGridLayout, QScrollArea, QWidget,QTableWidget,QTableWidgetItem, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QFrame, QStackedWidget, QSizePolicy ,QSpacerItem
from PyQt5.QtGui import QFont,QIcon,QPixmap

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName("ROBIKA.inc")
        MainWindow.resize(1245, 600)
        MainWindow.setMinimumSize(1245, 600)
        MainWindow.setStyleSheet("background-color: rgb(45, 45, 45);")
         # Set window icon
        icon = QIcon("Assets/ROBIKA_ICON.ico")  # Specify the path to your icon file
        MainWindow.setWindowIcon(icon)

        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.Top_Bar = QFrame(self.centralwidget)
        self.Top_Bar.setObjectName("Top_Bar")
        self.Top_Bar.setMaximumSize(16777215, 40)
        self.Top_Bar.setStyleSheet("background-color: rgb(35, 35, 35);")
        self.Top_Bar.setFrameShape(QFrame.NoFrame)
        self.Top_Bar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.Top_Bar)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_toggle = QFrame(self.Top_Bar)
        self.frame_toggle.setObjectName("frame_toggle")
        self.frame_toggle.setMaximumSize(70, 40)
        self.frame_toggle.setStyleSheet("background-color: rgb(35, 35, 35);")
        self.frame_toggle.setFrameShape(QFrame.StyledPanel)
        self.frame_toggle.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_toggle)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        
        self.horizontalLayout.addWidget(self.frame_toggle)
        self.frame_top = QFrame(self.Top_Bar)
        self.frame_top.setObjectName("frame_top")
        self.frame_top.setFrameShape(QFrame.StyledPanel)
        self.frame_top.setFrameShadow(QFrame.Raised)
        self.horizontalLayout.addWidget(self.frame_top)
        self.verticalLayout.addWidget(self.Top_Bar)
        self.Content = QFrame(self.centralwidget)
        self.Content.setObjectName("Content")
        self.Content.setFrameShape(QFrame.NoFrame)
        self.Content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.Content)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_left_menu = QFrame(self.Content)
        self.frame_left_menu.setObjectName("frame_left_menu")
        self.frame_left_menu.setMinimumSize(70, 0)
        self.frame_left_menu.setMaximumSize(70, 16777215)
        self.frame_left_menu.setStyleSheet("background-color: rgb(35, 35, 35);")
        self.frame_left_menu.setFrameShape(QFrame.StyledPanel)
        self.frame_left_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_left_menu)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_top_menus = QFrame(self.frame_left_menu)
        self.frame_top_menus.setObjectName("frame_top_menus")
        self.frame_top_menus.setFrameShape(QFrame.NoFrame)
        self.frame_top_menus.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_top_menus)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.Btn_Toggle = QPushButton(self.frame_top_menus)
        self.Btn_Toggle.setObjectName("Btn_Toggle")
        self.Btn_Toggle.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.Btn_Toggle.setStyleSheet("color: rgb(255, 255, 255);\n"
                                       "border: 0px solid;")
        self.Btn_Toggle.setCursor(Qt.PointingHandCursor)
        # Create a QIcon object with the desired icon
        icon = QIcon("Assets/menu.png")

        # Set the icon for the toggle button
        self.Btn_Toggle.setIcon(icon)
        self.Btn_Toggle.setIconSize(QSize(24, 24))  # Optionally, set the size of the icon
        self.verticalLayout_4.addWidget(self.Btn_Toggle)

        self.Btn_space = QPushButton(self.frame_top_menus)
        self.Btn_space.setObjectName("Btn_space")
        self.Btn_space.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.Btn_space.setStyleSheet("color: rgb(255, 255, 255);\n"
                                       "border: 0px solid;")
        self.verticalLayout_2.addWidget(self.Btn_space)

        self.btn_page_1 = QPushButton(self.frame_top_menus)
        self.btn_page_1.setObjectName("btn_page_1")
        self.btn_page_1.setMinimumSize(0, 40)
        self.btn_page_1.setStyleSheet("QPushButton {\n"
                                "    color: rgb(255, 255, 255);\n"
                                "    background-color: rgb(35, 35, 35);\n"
                                "    border: 0px solid;\n"
                                "}\n"
                                "QPushButton:hover {\n"
                                "    background-color: rgb(56, 56, 56);\n"
                                "}")
        self.btn_page_1.setCursor(Qt.PointingHandCursor)
        # Create a QIcon object with the desired icon
        icon_btn_page_1 = QIcon("Assets/puzzle.png")

        self.btn_page_1.setIcon(icon_btn_page_1)
        self.btn_page_1.setIconSize(QSize(20, 20))  # Optionally, set the size of the icon
        self.verticalLayout_4.addWidget(self.btn_page_1)
        self.btn_page_2 = QPushButton(self.frame_top_menus)
        self.btn_page_2.setObjectName("btn_page_2")
        self.btn_page_2.setMinimumSize(0, 40)
        self.btn_page_2.setStyleSheet("QPushButton {\n"
                                      "	color: rgb(255, 255, 255);\n"
                                      "	background-color: rgb(35, 35, 35);\n"
                                      "	border: 0px solid;\n"
                                      "}\n"
                                      "QPushButton:hover {\n"
                                      "	background-color: rgb(56, 56, 56);\n"
                                      "}")
        self.btn_page_2.setCursor(Qt.PointingHandCursor)
        # Create a QIcon object with the desired icon
        icon_btn_page_2 = QIcon("Assets/solutions.png")

        self.btn_page_2.setIcon(icon_btn_page_2)
        self.btn_page_2.setIconSize(QSize(24, 24))  # Optionally, set the size of the icon
        self.verticalLayout_4.addWidget(self.btn_page_2)
        self.btn_page_3 = QPushButton(self.frame_top_menus)
        self.btn_page_3.setObjectName("btn_page_3")
        self.btn_page_3.setMinimumSize(0, 40)
        self.btn_page_3.setStyleSheet("QPushButton {\n"
                                      "	color: rgb(255, 255, 255);\n"
                                      "	background-color: rgb(35, 35, 35);\n"
                                      "	border: 0px solid;\n"
                                      "}\n"
                                      "QPushButton:hover {\n"
                                      "	background-color: rgb(56, 56, 56);\n"
                                      "}")
        self.btn_page_3.setCursor(Qt.PointingHandCursor)
        # Create a QIcon object with the desired icon
        icon_btn_page_3 = QIcon("Assets/file.png")

        self.btn_page_3.setIcon(icon_btn_page_3)
        self.btn_page_3.setIconSize(QSize(20, 20))  # Optionally, set the size of the icon
        self.verticalLayout_4.addWidget(self.btn_page_3)
        self.verticalLayout_3.addWidget(self.frame_top_menus, 0, Qt.AlignTop)
        self.horizontalLayout_2.addWidget(self.frame_left_menu)
        self.frame_pages = QFrame(self.Content)
        self.frame_pages.setObjectName("frame_pages")
        self.frame_pages.setFrameShape(QFrame.StyledPanel)
        self.frame_pages.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_pages)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.stackedWidget = QStackedWidget(self.frame_pages)
        self.stackedWidget.setObjectName("stackedWidget")
        
        self.page_welcome = QWidget()
        self.page_welcome.setObjectName("page_welcome")

        # Layout for page_welcome
        self.verticalLayout_7 = QVBoxLayout(self.page_welcome)
        self.verticalLayout_7.setObjectName("verticalLayout_7")

        # Welcome label
        self.label_welcome = QLabel(self.page_welcome)
        self.label_welcome.setObjectName("label_welcome")
        font = QFont()
        font.setPointSize(70)
        self.label_welcome.setFont(font)
        self.label_welcome.setStyleSheet("color: #FFF;")
        self.label_welcome.setAlignment(Qt.AlignCenter)
        self.verticalLayout_7.addWidget(self.label_welcome)
        font1 = QFont()      
        font1.setPointSize(40)
        # Text label
        self.label_instruction = QLabel(self.page_welcome)
        self.label_instruction.setObjectName("label_instruction")
        self.label_instruction.setText("To start<br>Click on the button <img src='Assets/puzzle.png'><br> in the sidebar")
        self.label_instruction.setAlignment(Qt.AlignCenter)
        self.label_instruction.setFont(font1)
        self.label_instruction.setStyleSheet("color: #FFF;margin-bottom: 50px;")
        self.verticalLayout_7.addWidget(self.label_instruction)

        self.stackedWidget.addWidget(self.page_welcome)

        self.page_1 = QWidget()
        self.page_1.setObjectName("page_1")
        self.verticalLayout_7 = QVBoxLayout(self.page_1)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.verticalLayout_7.setSpacing(10)  # Set vertical spacing between widgets
        # self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)  # Remove margins

        # Label "Select a problem"
        label_select_problem = QLabel("Select a problem <br/> to solve:")
        label_select_problem.setObjectName("label_select_problem")
        font = QFont()
        font.setPointSize(55)
        label_select_problem.setFont(font)
        label_select_problem.setStyleSheet("color: #FFF; text-align: center;")
        label_select_problem.setAlignment(Qt.AlignCenter)
        self.verticalLayout_7.addWidget(label_select_problem)

        # Button "Problem 1"
        self.btn_problem_1 = QPushButton("Problem 1")
        self.btn_problem_1.setObjectName("btn_problem_1")
        self.btn_problem_1.setFixedWidth(160)  # Set width
        self.btn_problem_1.setStyleSheet("""
            QPushButton {
                color: #FFF;
                background-color: #DB2B39; /* Set background color */
                padding: 10px; /* Set padding */
                border-radius: 10px;
            }

            QPushButton:hover {
                background-color: #D6404D; /* Change background color on hover */
            }

            QPushButton:pressed {
                border: 2px solid rgba(0, 0, 0, 0.5); /* Add shadow effect when pressed */
            }
        """)
        self.btn_problem_1.setCursor(Qt.PointingHandCursor)

        # Add the button to the layout
        self.verticalLayout_7.addWidget(self.btn_problem_1, alignment=Qt.AlignHCenter)



        # Button "Problem 2"
        self.btn_problem_2 = QPushButton("Problem 2")
        self.btn_problem_2.setObjectName("btn_problem_2")
        self.btn_problem_2.setFixedWidth(160)  # Set width
        self.btn_problem_2.setStyleSheet("""
            QPushButton {
                color: #FFF;
                background-color: #DB2B39; /* Set background color */
                padding: 10px; /* Set padding */
                border-radius: 10px;
            }

            QPushButton:hover {
                background-color: #D6404D; /* Change background color on hover */
            }

            QPushButton:pressed {
                border: 2px solid rgba(0, 0, 0, 0.5); /* Add shadow effect when pressed */
            }
        """)
        self.btn_problem_2.setCursor(Qt.PointingHandCursor)

        # Add the button to the layout
        self.verticalLayout_7.addWidget(self.btn_problem_2, alignment=Qt.AlignHCenter)
        spacer_item = QSpacerItem(20, 65, QSizePolicy.Minimum, QSizePolicy.Fixed)
        self.verticalLayout_7.addItem(spacer_item)
        self.stackedWidget.addWidget(self.page_1)



        # Problem 1 Page
        self.problem_1_page = QWidget()
        self.problem_1_page.setObjectName("problem_1_page")
        self.verticalLayout_6 = QVBoxLayout(self.problem_1_page)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout_6.setSpacing(10)  # Set vertical spacing between widgets
       # Create a QLabel widget to display the image
        image_label = QLabel()

        # Load the image from file
        pixmap = QPixmap("Assets/problem1_bakery.png")

        # Set the pixmap to the label
        image_label.setPixmap(pixmap)

        # Create a scroll area
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        # Create a layout for the scroll area
        scroll_layout = QVBoxLayout()
        scroll_layout.addWidget(image_label)

        # Create a widget to contain the layout
        scroll_widget = QWidget()
        scroll_widget.setLayout(scroll_layout)

        # Set the widget to the scroll area
        scroll_area.setWidget(scroll_widget)

        # Add the scroll area to the vertical layout of problem_1_page
        self.verticalLayout_6.addWidget(scroll_area)

        # Create a bottom widget to contain input widgets
        bottom_widget = QWidget()

        # Create a layout for the bottom widget
        bottom_layout = QGridLayout(bottom_widget)

        # Input 1
        input_1_label = QLabel("Input 1:")
        font_input = QFont()
        font_input.setPointSize(17)
        font = QFont()
        font.setPointSize(25)
        input_1_label.setFont(font)
        input_1_label.setStyleSheet("color: #FFF;padding-bottom:5px;")  # Set label text color
        self.input_1 = QSpinBox()
        self.input_1.setFont(font_input)
        self.input_1.setStyleSheet("background-color: #F0F0F0;padding:5px;")
        self.input_1.setFixedWidth(100)
        self.input_1.setFixedHeight(40)
        bottom_layout.addWidget(input_1_label, 0, 0, alignment=Qt.AlignRight)
        bottom_layout.addWidget(self.input_1, 0, 1, alignment=Qt.AlignLeft)

        # Input 2
        input_2_label = QLabel("Input 2:")
        self.input_2 = QSpinBox()
        self.input_2.setFont(font_input)
        input_2_label.setFont(font)
        input_2_label.setStyleSheet("color: #FFF;padding-bottom:5px;")
        self.input_2.setStyleSheet("background-color: #F0F0F0;padding:5px;")
        self.input_2.setFixedWidth(100)
        self.input_2.setFixedHeight(40)
        bottom_layout.addWidget(input_2_label, 0, 2, alignment=Qt.AlignRight)
        bottom_layout.addWidget(self.input_2, 0, 3, alignment=Qt.AlignLeft)

        # Input 3
        input_3_label = QLabel("Input 3:")
        self.input_3 = QSpinBox()
        self.input_3.setFont(font_input)
        input_3_label.setFont(font)
        input_3_label.setStyleSheet("color: #FFF;padding-bottom:5px;")
        self.input_3.setStyleSheet("background-color: #F0F0F0;padding:5px;")
        self.input_3.setFixedWidth(100)
        self.input_3.setFixedHeight(40)
        bottom_layout.addWidget(input_3_label, 1, 0, alignment=Qt.AlignRight)
        bottom_layout.addWidget(self.input_3, 1, 1, alignment=Qt.AlignLeft)

        # Input 4
        input_4_label = QLabel("Input 4:")
        self.input_4 = QSpinBox()
        self.input_4.setFont(font_input)
        input_4_label.setFont(font)
        input_4_label.setStyleSheet("color: #FFF;padding-bottom:5px;")
        self.input_4.setStyleSheet("background-color: #F0F0F0;padding:5px;")
        self.input_4.setFixedWidth(100)
        self.input_4.setFixedHeight(40)
        bottom_layout.addWidget(input_4_label, 1, 2, alignment=Qt.AlignRight)
        bottom_layout.addWidget(self.input_4, 1, 3, alignment=Qt.AlignLeft)

        # Submit button
        self.problem1_submit_btn = QPushButton("Submit")
        self.problem1_submit_btn.setStyleSheet("background-color: #F0F0F0;")
        self.problem1_submit_btn.setFixedWidth(100)
        self.problem1_submit_btn.setFixedHeight(40)
        self.problem1_submit_btn.setStyleSheet("""
            QPushButton {
                color: #FFF;
                background-color: #DB2B39; /* Set background color */
                padding: 10px; /* Set padding */
                border-radius: 10px;
            }

            QPushButton:hover {
                background-color: #D6404D; /* Change background color on hover */
            }

            QPushButton:pressed {
                border: 2px solid rgba(0, 0, 0, 0.5); /* Add shadow effect when pressed */
            }
        """)
        self.problem1_submit_btn.setCursor(Qt.PointingHandCursor)
        bottom_layout.addWidget(self.problem1_submit_btn, 2, 3, alignment=Qt.AlignRight)
        # Add the bottom widget to the problem_1_page layout
        scroll_layout.addWidget(bottom_widget)
        self.stackedWidget.addWidget(self.problem_1_page)
        


        # Problem 2 Page
        self.problem_2_page = QWidget()
        self.problem_2_page.setObjectName("problem_2_page")
        self.verticalLayout_7 = QVBoxLayout(self.problem_2_page)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.verticalLayout_7.setSpacing(10)  # Set vertical spacing between widgets
        # Create a QLabel widget to display the image
        image_label_2 = QLabel()

        # Load the image from file
        pixmap_2 = QPixmap("Assets/problem1.png")

        # Set the pixmap to the label
        image_label_2.setPixmap(pixmap_2)

        # Create a scroll area
        scroll_area_2 = QScrollArea()
        scroll_area_2.setWidgetResizable(True)
        scroll_area_2.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        # Create a layout for the scroll area
        scroll_layout_2 = QVBoxLayout()
        scroll_layout_2.addWidget(image_label_2)

        # Create a widget to contain the layout
        scroll_widget_2 = QWidget()
        scroll_widget_2.setLayout(scroll_layout_2)

        # Set the widget to the scroll area
        scroll_area_2.setWidget(scroll_widget_2)

        # Add the scroll area to the vertical layout of problem_2_page
        self.verticalLayout_7.addWidget(scroll_area_2)

        # Create a bottom widget to contain input widgets
        bottom_widget_2 = QWidget()

        # Create a layout for the bottom widget
        bottom_layout_2 = QGridLayout(bottom_widget_2)

        # Input 1
        input_1_label_2 = QLabel("Input 1:")
        font_input_2 = QFont()
        font_input_2.setPointSize(17)
        font_2 = QFont()
        font_2.setPointSize(25)
        input_1_label_2.setFont(font_2)
        input_1_label_2.setStyleSheet("color: #FFF;padding-bottom:5px;")  # Set label text color
        self.input_1_2 = QSpinBox()
        self.input_1_2.setFont(font_input_2)
        self.input_1_2.setStyleSheet("background-color: #F0F0F0;padding:5px;")
        self.input_1_2.setFixedWidth(100)
        self.input_1_2.setFixedHeight(40)
        bottom_layout_2.addWidget(input_1_label_2, 0, 0, alignment=Qt.AlignRight)
        bottom_layout_2.addWidget(self.input_1_2, 0, 1, alignment=Qt.AlignLeft)

        # Input 2
        input_2_label_2 = QLabel("Input 2:")
        self.input_2_2 = QSpinBox()
        self.input_2_2.setFont(font_input_2)
        input_2_label_2.setFont(font_2)
        input_2_label_2.setStyleSheet("color: #FFF;padding-bottom:5px;")
        self.input_2_2.setStyleSheet("background-color: #F0F0F0;padding:5px;")
        self.input_2_2.setFixedWidth(100)
        self.input_2_2.setFixedHeight(40)
        bottom_layout_2.addWidget(input_2_label_2, 0, 2, alignment=Qt.AlignRight)
        bottom_layout_2.addWidget(self.input_2_2, 0, 3, alignment=Qt.AlignLeft)

        # Input 3
        input_3_label_2 = QLabel("Input 3:")
        self.input_3_2 = QSpinBox()
        self.input_3_2.setFont(font_input_2)
        input_3_label_2.setFont(font_2)
        input_3_label_2.setStyleSheet("color: #FFF;padding-bottom:5px;")
        self.input_3_2.setStyleSheet("background-color: #F0F0F0;padding:5px;")
        self.input_3_2.setFixedWidth(100)
        self.input_3_2.setFixedHeight(40)
        bottom_layout_2.addWidget(input_3_label_2, 1, 0, alignment=Qt.AlignRight)
        bottom_layout_2.addWidget(self.input_3_2, 1, 1, alignment=Qt.AlignLeft)

        # Input 4
        input_4_label_2 = QLabel("Input 4:")
        self.input_4_2 = QSpinBox()
        self.input_4_2.setFont(font_input_2)
        input_4_label_2.setFont(font_2)
        input_4_label_2.setStyleSheet("color: #FFF;padding-bottom:5px;")
        self.input_4_2.setStyleSheet("background-color: #F0F0F0;padding:5px;")
        self.input_4_2.setFixedWidth(100)
        self.input_4_2.setFixedHeight(40)
        bottom_layout_2.addWidget(input_4_label_2, 1, 2, alignment=Qt.AlignRight)
        bottom_layout_2.addWidget(self.input_4_2, 1, 3, alignment=Qt.AlignLeft)

        # Submit button
        self.problem2_submit_btn = QPushButton("Submit")
        self.problem2_submit_btn.setStyleSheet("background-color: #F0F0F0;")
        self.problem2_submit_btn.setFixedWidth(100)
        self.problem2_submit_btn.setFixedHeight(40)
        self.problem2_submit_btn.setStyleSheet("""
            QPushButton {
                color: #FFF;
                background-color: #DB2B39; /* Set background color */
                padding: 10px; /* Set padding */
                border-radius: 10px;
            }

            QPushButton:hover {
                background-color: #D6404D; /* Change background color on hover */
            }

            QPushButton:pressed {
                border: 2px solid rgba(0, 0, 0, 0.5); /* Add shadow effect when pressed */
            }
        """)
        self.problem2_submit_btn.setCursor(Qt.PointingHandCursor)
        bottom_layout_2.addWidget(self.problem2_submit_btn, 2, 3, alignment=Qt.AlignRight)
        # Add the bottom widget to the problem_2_page layout
        scroll_layout_2.addWidget(bottom_widget_2)
        self.stackedWidget.addWidget(self.problem_2_page)


         
        self.page_2 = QWidget()
        self.page_2.setObjectName("page_2")
        self.verticalLayout_7 = QVBoxLayout(self.page_2)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.verticalLayout_7.setSpacing(10)  # Set vertical spacing between widgets
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)  # Remove margins

        # Label "Select a problem"
        label_select_problem = QLabel("You can find here <br/>the solutions :")
        label_select_problem.setObjectName("label_select_problem")
        font = QFont()
        font.setPointSize(55)
        label_select_problem.setFont(font)
        label_select_problem.setStyleSheet("color: #FFF; text-align: center;")
        label_select_problem.setAlignment(Qt.AlignCenter)
        self.verticalLayout_7.addWidget(label_select_problem)

        # Button "Solution 1"
        self.btn_solution_1 = QPushButton("Solution 1")
        self.btn_solution_1.setObjectName("btn_solution_1")
        self.btn_solution_1.setFixedWidth(160)  # Set width
        self.btn_solution_1.setStyleSheet("""
            QPushButton {
                color: #FFF;
                background-color: #DB2B39; /* Set background color */
                padding: 10px; /* Set padding */
                border-radius: 10px;
            }

            QPushButton:hover {
                background-color: #D6404D; /* Change background color on hover */
            }

            QPushButton:pressed {
                border: 2px solid rgba(0, 0, 0, 0.5); /* Add shadow effect when pressed */
            }
        """)
        self.btn_solution_1.setCursor(Qt.PointingHandCursor)

        # Add the button to the layout
        self.verticalLayout_7.addWidget(self.btn_solution_1, alignment=Qt.AlignHCenter)



        # Button "Solution 2"
        self.btn_solution_2 = QPushButton("Solution 2")
        self.btn_solution_2.setObjectName("btn_solution_2")
        self.btn_solution_2.setFixedWidth(160)  # Set width
        self.btn_solution_2.setStyleSheet("""
            QPushButton {
                color: #FFF;
                background-color: #DB2B39; /* Set background color */
                padding: 10px; /* Set padding */
                border-radius: 10px;
            }

            QPushButton:hover {
                background-color: #D6404D; /* Change background color on hover */
            }

            QPushButton:pressed {
                border: 2px solid rgba(0, 0, 0, 0.5); /* Add shadow effect when pressed */
            }
        """)
        self.btn_solution_2.setCursor(Qt.PointingHandCursor)

        # Add the button to the layout
        self.verticalLayout_7.addWidget(self.btn_solution_2, alignment=Qt.AlignHCenter)
        spacer_item = QSpacerItem(20, 65, QSizePolicy.Minimum, QSizePolicy.Fixed)
        self.verticalLayout_7.addItem(spacer_item)
        self.stackedWidget.addWidget(self.page_2)

        self.solution_1_page = QWidget()
        self.solution_1_page.setObjectName("solution_1_page")
        self.verticalLayout_6 = QVBoxLayout(self.solution_1_page)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_solution_1 = QLabel(self.solution_1_page)
        self.label_solution_1.setObjectName("label_solution_1")
        self.label_solution_1.setText("This is solution 1")
        self.label_solution_1.setAlignment(Qt.AlignCenter)
        self.label_solution_1.setFont(font1)
        self.label_solution_1.setStyleSheet("color: #FFF;")
        self.verticalLayout_6.addWidget(self.label_solution_1)
        self.stackedWidget.addWidget(self.solution_1_page)

        self.solution_2_page = QWidget()
        self.solution_2_page.setObjectName("solution_2_page")
        self.verticalLayout_6 = QVBoxLayout(self.solution_2_page)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_solution_2 = QLabel(self.solution_2_page)
        self.label_solution_2.setObjectName("label_solution_2")
        self.label_solution_2.setText("This is solution 2")
        self.label_solution_2.setAlignment(Qt.AlignCenter)
        self.label_solution_2.setFont(font1)
        self.label_solution_2.setStyleSheet("color: #FFF;")
        self.verticalLayout_6.addWidget(self.label_solution_2)
        self.stackedWidget.addWidget(self.solution_2_page)

        #Gurobi result problem 1
        self.gurobi_res1_page = QWidget()
        self.gurobi_res1_page.setObjectName("gurobi_res1_page")
        self.verticalLayout_6 = QVBoxLayout(self.gurobi_res1_page)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_gurobi_res1 = QLabel(self.gurobi_res1_page)
        self.label_gurobi_res1.setObjectName("label_gurobi_res1")
        self.label_gurobi_res1.setText("This is Gurobi result 1")
        self.label_gurobi_res1.setAlignment(Qt.AlignCenter)
        self.label_gurobi_res1.setFont(font1)
        self.label_gurobi_res1.setStyleSheet("color: #FFF;")
        self.verticalLayout_6.addWidget(self.label_gurobi_res1)
        self.stackedWidget.addWidget(self.gurobi_res1_page)




        #Gurobi result problem 2 
        self.gurobi_res2_page = QWidget()
        self.gurobi_res2_page.setObjectName("gurobi_res2_page")
        self.verticalLayout_6 = QVBoxLayout(self.gurobi_res2_page)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_gurobi_res2 = QLabel(self.gurobi_res2_page)
        self.label_gurobi_res2.setObjectName("label_gurobi_res2")
        self.label_gurobi_res2.setText("This is Gurobi result 2")
        self.label_gurobi_res2.setAlignment(Qt.AlignCenter)
        self.label_gurobi_res2.setFont(font1)
        self.label_gurobi_res2.setStyleSheet("color: #FFF;")
        self.verticalLayout_6.addWidget(self.label_gurobi_res2)
        self.stackedWidget.addWidget(self.gurobi_res2_page)


        self.page_3 = QWidget()
        self.page_3.setObjectName("page_3")
        self.verticalLayout_8 = QVBoxLayout(self.page_3)
        self.verticalLayout_8.setObjectName("verticalLayout_8")

        # Label
        label = QLabel(self.page_3)
        label.setObjectName("label")
        label.setText("Your history:")
        font = QFont()
        font.setPointSize(20)  # Set font size to 10 points
        label.setFont(font)
        label.setStyleSheet("color: #FFF;")
        label.setAlignment(Qt.AlignLeft)
        self.verticalLayout_8.addWidget(label)

        # Table
        self.table = QTableWidget(self.page_3)
        self.table.setColumnCount(8) 
        # Set column widths
        self.table.setColumnWidth(0, 50)  # ID column
        self.table.setColumnWidth(1, 130)  # Problem name column
        self.table.setColumnWidth(2, 70)  # Input 1 column
        self.table.setColumnWidth(3, 70)  # Input 2 column
        self.table.setColumnWidth(4, 70)  # Input 3 column
        self.table.setColumnWidth(5, 70)  # Input 4 column
        self.table.setColumnWidth(6, 460)  # Result column
        self.table.setColumnWidth(7, 200)  # Created In column
        # Set font size for table
        font = QFont()
        font.setPointSize(15)  # Set font size to 10 points
        self.table.setFont(font)

        # Set background color for cells
        self.table.setStyleSheet(
                                "QTableWidget::item { background-color: #ffffff; }"  # Set background color for cells
                                "QTableWidget::item:selected { background-color: #a6a6a6; }")  # Set background color for selected cells

        # Set row heights
        for row in range(self.table.rowCount()):
            self.table.setRowHeight(row, 60)  # Set height for each row
        # Set column headers
        self.table.setHorizontalHeaderLabels(["ID","Problem Name", "Input 1", "Input 2", "Input 3", "Input 4","Gurobi Result","Created In"])


        self.verticalLayout_8.addWidget(self.table)

        self.stackedWidget.addWidget(self.page_3)





        self.verticalLayout_5.addWidget(self.stackedWidget)
        self.horizontalLayout_2.addWidget(self.frame_pages)
        self.verticalLayout.addWidget(self.Content)
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        # QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        # Set window title
        MainWindow.setWindowTitle("ROBIKA.inc")
        # self.Btn_Toggle.setText("TOGGLE")
        # self.ui.btn_page_1.setText("Problems")
        # self.ui.btn_page_2.setText("Solutions")
        # self.ui.btn_page_3.setText("History")
        self.label_welcome.setText("Welcome !")
    # retranslateUi

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
