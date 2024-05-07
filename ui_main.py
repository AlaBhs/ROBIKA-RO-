from PyQt5.QtCore import Qt,QSize
from PyQt5.QtWidgets import QApplication, QMainWindow,QDoubleSpinBox,QSpinBox,QCheckBox,QGridLayout, QScrollArea, QWidget,QTableWidget,QTableWidgetItem, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QFrame, QStackedWidget, QSizePolicy ,QSpacerItem
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
        font.setPointSize(60)
        self.label_welcome.setFont(font)
        self.label_welcome.setStyleSheet("color: #FFF;")
        self.label_welcome.setAlignment(Qt.AlignCenter)
        self.verticalLayout_7.addWidget(self.label_welcome)
        font1 = QFont()      
        font1.setPointSize(21)
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

        bottom_widget = QWidget()

        # Create a layout for the bottom widget
        bottom_layout = QGridLayout(bottom_widget)

        checkbox_widget = QWidget()

        # Create a layout for the checkbox widget
        checkbox_layout = QGridLayout(checkbox_widget)

        

        checkbox_font = QFont()
        checkbox_font.setPointSize(20)


        check_ccc_label = QLabel("Chocolate chip cookies: ")
        
        check_ccc_label.setFont(checkbox_font)
        check_ccc_label.setStyleSheet("color: #DB2B39;padding-bottom:5px;")  # Set label text color
        checkbox_layout.addWidget(check_ccc_label, 0, 0, alignment=Qt.AlignLeft)


        check_orc_label = QLabel("Oatmeal raisin cookies: ")
        check_orc_label.setFont(checkbox_font)
        check_orc_label.setStyleSheet("color: #DB2B39;padding-bottom:5px;")  # Set label text color
        checkbox_layout.addWidget(check_orc_label, 0, 2, alignment=Qt.AlignLeft)

        check_bnm_label = QLabel("Banana nut muffins: ")
        check_bnm_label.setFont(checkbox_font)
        check_bnm_label.setStyleSheet("color: #DB2B39;padding-bottom:5px;")  # Set label text color
        checkbox_layout.addWidget(check_bnm_label, 1, 0, alignment=Qt.AlignLeft)

        check_blm_label = QLabel("Blueberry muffins: ")
        check_blm_label.setFont(checkbox_font)
        check_blm_label.setStyleSheet("color: #DB2B39;padding-bottom:5px;")  # Set label text color
        checkbox_layout.addWidget(check_blm_label, 1, 2, alignment=Qt.AlignLeft)
        # Create check boxes
        self.checkbox_1 = QCheckBox()
        self.checkbox_2 = QCheckBox()
        self.checkbox_3 = QCheckBox()
        self.checkbox_4 = QCheckBox()

        self.checkbox_1.setFont(font)
        self.checkbox_2.setFont(font)
        self.checkbox_3.setFont(font)
        self.checkbox_4.setFont(font)
        # the first product is checked by default
        self.checkbox_1.setChecked(True)
        # Add check boxes to layout
        checkbox_layout.addWidget(self.checkbox_1, 0, 1)
        checkbox_layout.addWidget(self.checkbox_2, 0, 3)
        checkbox_layout.addWidget(self.checkbox_3, 1, 1)
        checkbox_layout.addWidget(self.checkbox_4, 1, 3)
        # Create a bottom widget to contain input widgets
        
        # Profit list
        profit_list_label = QLabel("Profit: ")
        font = QFont()
        font.setPointSize(20)
        profit_list_label.setFont(font)
        profit_list_label.setStyleSheet("color: #FFF;padding-bottom:5px;")  # Set label text color
        bottom_layout.addWidget(profit_list_label, 0, 0, alignment=Qt.AlignLeft)
        # Input 1
        self.input_1_profit_label = QLabel("Chocolate chip cookies:")
        font_input = QFont()
        font_input.setPointSize(12)
        font_input_label = QFont()
        font_input_label.setPointSize(14)
        self.input_1_profit_label.setFont(font_input_label)
        self.input_1_profit_label.setStyleSheet("color: #FFF;padding-bottom:5px;")  # Set label text color
        self.input_1_profit = QDoubleSpinBox()
        self.input_1_profit.setFont(font_input)
        self.input_1_profit.setStyleSheet("background-color: #F0F0F0;padding:5px;")
        self.input_1_profit.setRange(0.0, 100000.0)  # Set the range of values as needed
        self.input_1_profit.setSingleStep(0.1)  # Set the step size
        self.input_1_profit.setSuffix(" dt")
        self.input_1_profit.setFixedWidth(150)
        self.input_1_profit.setFixedHeight(40)
        bottom_layout.addWidget(self.input_1_profit_label, 1, 1, )
        bottom_layout.addWidget(self.input_1_profit, 1, 2, alignment=Qt.AlignLeft)

        # Input 2
        self.input_2_profit_label = QLabel("Oatmeal raisin cookies:")
        self.input_2_profit = QDoubleSpinBox()
        self.input_2_profit.setFont(font_input)
        self.input_2_profit_label.setFont(font_input_label)
        self.input_2_profit_label.setStyleSheet("color: #FFF;padding-bottom:5px;")
        self.input_2_profit.setStyleSheet("background-color: #F0F0F0;padding:5px;")
        self.input_2_profit.setRange(0.0, 100000.0)  # Set the range of values as needed
        self.input_2_profit.setSingleStep(0.1)  # Set the step size
        self.input_2_profit.setSuffix(" dt")
        self.input_2_profit.setFixedWidth(150)
        self.input_2_profit.setFixedHeight(40)
        self.input_2_profit_label.hide()
        self.input_2_profit.hide()
        bottom_layout.addWidget(self.input_2_profit_label, 1, 3, )
        bottom_layout.addWidget(self.input_2_profit, 1, 4, alignment=Qt.AlignLeft)

        # Input 3
        self.input_3_profit_label = QLabel("Banana nut muffins:")
        self.input_3_profit = QDoubleSpinBox()
        self.input_3_profit.setFont(font_input)
        self.input_3_profit_label.setFont(font_input_label)
        self.input_3_profit_label.setStyleSheet("color: #FFF;padding-bottom:5px;")
        self.input_3_profit.setStyleSheet("background-color: #F0F0F0;padding:5px;")
        self.input_3_profit.setRange(0.0, 100000.0)  # Set the range of values as needed
        self.input_3_profit.setSingleStep(0.1)  # Set the step size
        self.input_3_profit.setSuffix(" dt")
        self.input_3_profit.setFixedWidth(150)
        self.input_3_profit.setFixedHeight(40)
        self.input_3_profit_label.hide()
        self.input_3_profit.hide()
        bottom_layout.addWidget(self.input_3_profit_label, 2, 1, )
        bottom_layout.addWidget(self.input_3_profit, 2, 2, alignment=Qt.AlignLeft)

        # Input 4
        self.input_4_profit_label = QLabel("Blueberry muffins:")
        self.input_4_profit = QDoubleSpinBox()
        self.input_4_profit.setFont(font_input)
        self.input_4_profit_label.setFont(font_input_label)
        self.input_4_profit_label.setStyleSheet("color: #FFF;padding-bottom:5px;")
        self.input_4_profit.setStyleSheet("background-color: #F0F0F0;padding:5px;")
        self.input_4_profit.setRange(0.0, 100000.0)  # Set the range of values as needed
        self.input_4_profit.setSingleStep(0.1)  # Set the step size
        self.input_4_profit.setSuffix(" dt")
        self.input_4_profit.setFixedWidth(150)
        self.input_4_profit.setFixedHeight(40)
        self.input_4_profit_label.hide()
        self.input_4_profit.hide()
        bottom_layout.addWidget(self.input_4_profit_label, 2, 3, )
        bottom_layout.addWidget(self.input_4_profit, 2, 4, alignment=Qt.AlignLeft)


        # Weighting list
        weighting_list_label = QLabel("Weighting: ")
        font = QFont()
        font.setPointSize(20)
        weighting_list_label.setFont(font)
        weighting_list_label.setStyleSheet("color: #FFF;padding-bottom:5px;")  # Set label text color
        bottom_layout.addWidget(weighting_list_label, 3, 0, alignment=Qt.AlignLeft)
        # Input 1
        self.input_1_weighting_label = QLabel("Chocolate chip cookies:")
        font_input = QFont()
        font_input.setPointSize(12)
        font = QFont()
        font.setPointSize(14)
        self.input_1_weighting_label.setFont(font_input_label)
        self.input_1_weighting_label.setStyleSheet("color: #FFF;padding-bottom:5px;")  # Set label text color
        self.input_1_weighting = QDoubleSpinBox()
        self.input_1_weighting.setFont(font_input)
        self.input_1_weighting.setStyleSheet("background-color: #F0F0F0;padding:5px;")
        self.input_1_weighting.setRange(0.0, 1000.0)  # Set the range of values as needed
        self.input_1_weighting.setSingleStep(0.1)  # Set the step size
        self.input_1_weighting.setSuffix(" kg")
        self.input_1_weighting.setFixedWidth(150)
        self.input_1_weighting.setFixedHeight(40)
        bottom_layout.addWidget(self.input_1_weighting_label, 4, 1, )
        bottom_layout.addWidget(self.input_1_weighting, 4, 2, alignment=Qt.AlignLeft)

        # Input 2
        self.input_2_weighting_label = QLabel("Oatmeal raisin cookies:")
        self.input_2_weighting = QDoubleSpinBox()
        self.input_2_weighting.setFont(font_input)
        self.input_2_weighting_label.setFont(font_input_label)
        self.input_2_weighting_label.setStyleSheet("color: #FFF;padding-bottom:5px;")
        self.input_2_weighting.setStyleSheet("background-color: #F0F0F0;padding:5px;")
        self.input_2_weighting.setRange(0.0, 1000.0)  # Set the range of values as needed
        self.input_2_weighting.setSingleStep(0.1)  # Set the step size
        self.input_2_weighting.setSuffix(" kg")
        self.input_2_weighting.setFixedWidth(150)
        self.input_2_weighting.setFixedHeight(40)
        self.input_2_weighting_label.hide()
        self.input_2_weighting.hide()
        bottom_layout.addWidget(self.input_2_weighting_label, 4, 3, )
        bottom_layout.addWidget(self.input_2_weighting, 4, 4, alignment=Qt.AlignLeft)

        # Input 3
        self.input_3_weighting_label = QLabel("Banana nut muffins:")
        self.input_3_weighting = QDoubleSpinBox()
        self.input_3_weighting.setFont(font_input)
        self.input_3_weighting_label.setFont(font_input_label)
        self.input_3_weighting_label.setStyleSheet("color: #FFF;padding-bottom:5px;")
        self.input_3_weighting.setStyleSheet("background-color: #F0F0F0;padding:5px;")
        self.input_3_weighting.setRange(0.0, 1000.0)  # Set the range of values as needed
        self.input_3_weighting.setSingleStep(0.1)  # Set the step size
        self.input_3_weighting.setSuffix(" kg")
        self.input_3_weighting.setFixedWidth(150)
        self.input_3_weighting.setFixedHeight(40)
        self.input_3_weighting_label.hide()
        self.input_3_weighting.hide()
        bottom_layout.addWidget(self.input_3_weighting_label, 5, 1, )
        bottom_layout.addWidget(self.input_3_weighting, 5, 2, alignment=Qt.AlignLeft)

        # Input 4
        self.input_4_weighting_label = QLabel("Blueberry muffins:")
        self.input_4_weighting = QDoubleSpinBox()
        self.input_4_weighting.setFont(font_input)
        self.input_4_weighting_label.setFont(font_input_label)
        self.input_4_weighting_label.setStyleSheet("color: #FFF;padding-bottom:5px;")
        self.input_4_weighting.setStyleSheet("background-color: #F0F0F0;padding:5px;")
        self.input_4_weighting.setRange(0.0, 1000.0)  # Set the range of values as needed
        self.input_4_weighting.setSingleStep(0.1)  # Set the step size
        self.input_4_weighting.setSuffix(" kg")
        self.input_4_weighting.setFixedWidth(150)
        self.input_4_weighting.setFixedHeight(40)
        self.input_4_weighting_label.hide()
        self.input_4_weighting.hide()
        bottom_layout.addWidget(self.input_4_weighting_label, 5, 3, )
        bottom_layout.addWidget(self.input_4_weighting, 5, 4, alignment=Qt.AlignLeft)

        # Ingredients list
        ingredients_list_label = QLabel("Ingredients: ")
        font = QFont()
        font.setPointSize(20)
        ingredients_list_label.setFont(font)
        ingredients_list_label.setStyleSheet("color: #FFF;padding-bottom:5px;")  # Set label text color
        bottom_layout.addWidget(ingredients_list_label, 6, 0, alignment=Qt.AlignLeft)
        # Input 1
        input_1_ingredients_label = QLabel("Flour:")
        font_input = QFont()
        font_input.setPointSize(12)
        input_1_ingredients_label.setFont(font_input_label)
        input_1_ingredients_label.setStyleSheet("color: #FFF;padding-bottom:5px;")  # Set label text color
        bottom_layout.addWidget(input_1_ingredients_label, 7, 1, )
        # Input 1
        self.input_1_flour_ccc_label = QLabel("Chocolate chip cookies:")
        font_input = QFont()
        font_input.setPointSize(12)

        self.input_1_flour_ccc_label.setFont(font_input_label)
        self.input_1_flour_ccc_label.setStyleSheet("color: #FFF;padding-bottom:5px;")  # Set label text color
        self.input_1_flour_ccc = QDoubleSpinBox()
        self.input_1_flour_ccc.setFont(font_input)
        self.input_1_flour_ccc.setStyleSheet("background-color: #F0F0F0;padding:5px;")
        self.input_1_flour_ccc.setRange(0.0, 1000.0)  # Set the range of values as needed
        self.input_1_flour_ccc.setSingleStep(0.1)  # Set the step size
        self.input_1_flour_ccc.setSuffix(" kg")
        self.input_1_flour_ccc.setFixedWidth(150)
        self.input_1_flour_ccc.setFixedHeight(40)
        bottom_layout.addWidget(self.input_1_flour_ccc_label, 8, 1, )
        bottom_layout.addWidget(self.input_1_flour_ccc, 8, 2, alignment=Qt.AlignLeft)

        # Input 2
        self.input_2_flour_orc_label = QLabel("Oatmeal raisin cookies:")
        self.input_2_flour_orc = QDoubleSpinBox()
        self.input_2_flour_orc.setFont(font_input)
        self.input_2_flour_orc_label.setFont(font_input_label)
        self.input_2_flour_orc_label.setStyleSheet("color: #FFF;padding-bottom:5px;")
        self.input_2_flour_orc.setStyleSheet("background-color: #F0F0F0;padding:5px;")
        self.input_2_flour_orc.setRange(0.0, 1000.0)  # Set the range of values as needed
        self.input_2_flour_orc.setSingleStep(0.1)  # Set the step size
        self.input_2_flour_orc.setSuffix(" kg")
        self.input_2_flour_orc.setFixedWidth(150)
        self.input_2_flour_orc.setFixedHeight(40)
        self.input_2_flour_orc.hide()
        self.input_2_flour_orc_label.hide()
        bottom_layout.addWidget(self.input_2_flour_orc_label, 8, 3, )
        bottom_layout.addWidget(self.input_2_flour_orc, 8, 4, alignment=Qt.AlignLeft)

        # Input 3
        self.input_3_flour_bnm_label = QLabel("Banana nut muffins:")
        self.input_3_flour_bnm = QDoubleSpinBox()
        self.input_3_flour_bnm.setFont(font_input)
        self.input_3_flour_bnm_label.setFont(font_input_label)
        self.input_3_flour_bnm_label.setStyleSheet("color: #FFF;padding-bottom:5px;")
        self.input_3_flour_bnm.setStyleSheet("background-color: #F0F0F0;padding:5px;")
        self.input_3_flour_bnm.setRange(0.0, 1000.0)  # Set the range of values as needed
        self.input_3_flour_bnm.setSingleStep(0.1)  # Set the step size
        self.input_3_flour_bnm.setSuffix(" kg")
        self.input_3_flour_bnm.setFixedWidth(150)
        self.input_3_flour_bnm.setFixedHeight(40)
        self.input_3_flour_bnm.hide()
        self.input_3_flour_bnm_label.hide()
        bottom_layout.addWidget(self.input_3_flour_bnm_label, 9, 1, )
        bottom_layout.addWidget(self.input_3_flour_bnm, 9, 2, alignment=Qt.AlignLeft)

        # Input 4
        self.input_4_flour_blm_label = QLabel("Blueberry muffins:")
        self.input_4_flour_blm = QDoubleSpinBox()
        self.input_4_flour_blm.setFont(font_input)
        self.input_4_flour_blm_label.setFont(font_input_label)
        self.input_4_flour_blm_label.setStyleSheet("color: #FFF;padding-bottom:5px;")
        self.input_4_flour_blm.setStyleSheet("background-color: #F0F0F0;padding:5px;")
        self.input_4_flour_blm.setRange(0.0, 1000.0)  # Set the range of values as needed
        self.input_4_flour_blm.setSingleStep(0.1)  # Set the step size
        self.input_4_flour_blm.setSuffix(" kg")
        self.input_4_flour_blm.setFixedWidth(150)
        self.input_4_flour_blm.setFixedHeight(40)
        self.input_4_flour_blm.hide()
        self.input_4_flour_blm_label.hide()
        bottom_layout.addWidget(self.input_4_flour_blm_label, 9, 3, )
        bottom_layout.addWidget(self.input_4_flour_blm, 9, 4, alignment=Qt.AlignLeft) 


        # Input 2
        input_2_ingredients_label = QLabel("Sugar:")
        input_2_ingredients_label.setFont(font_input_label)
        input_2_ingredients_label.setStyleSheet("color: #FFF;padding-bottom:5px;")
        # Input 1
        self.input_1_sugar_ccc_label = QLabel("Chocolate chip cookies:")
        font_input = QFont()
        font_input.setPointSize(12)
        bottom_layout.addWidget(input_2_ingredients_label, 10, 1, )
        self.input_1_sugar_ccc_label.setFont(font_input_label)
        self.input_1_sugar_ccc_label.setStyleSheet("color: #FFF;padding-bottom:5px;")  # Set label text color
        self.input_1_sugar_ccc = QDoubleSpinBox()
        self.input_1_sugar_ccc.setFont(font_input)
        self.input_1_sugar_ccc.setStyleSheet("background-color: #F0F0F0;padding:5px;")
        self.input_1_sugar_ccc.setRange(0.0, 1000.0)  # Set the range of values as needed
        self.input_1_sugar_ccc.setSingleStep(0.1)  # Set the step size
        self.input_1_sugar_ccc.setSuffix(" kg")
        self.input_1_sugar_ccc.setFixedWidth(150)
        self.input_1_sugar_ccc.setFixedHeight(40)
        bottom_layout.addWidget(self.input_1_sugar_ccc_label, 11, 1, )
        bottom_layout.addWidget(self.input_1_sugar_ccc, 11, 2, alignment=Qt.AlignLeft)

        # Input 2
        self.input_2_sugar_orc_label = QLabel("Oatmeal raisin cookies:")
        self.input_2_sugar_orc = QDoubleSpinBox()
        self.input_2_sugar_orc.setFont(font_input)
        self.input_2_sugar_orc_label.setFont(font_input_label)
        self.input_2_sugar_orc_label.setStyleSheet("color: #FFF;padding-bottom:5px;")
        self.input_2_sugar_orc.setStyleSheet("background-color: #F0F0F0;padding:5px;")
        self.input_2_sugar_orc.setRange(0.0, 1000.0)  # Set the range of values as needed
        self.input_2_sugar_orc.setSingleStep(0.1)  # Set the step size
        self.input_2_sugar_orc.setSuffix(" kg")
        self.input_2_sugar_orc.setFixedWidth(150)
        self.input_2_sugar_orc.setFixedHeight(40)
        self.input_2_sugar_orc.hide()
        self.input_2_sugar_orc_label.hide()
        bottom_layout.addWidget(self.input_2_sugar_orc_label, 11, 3, )
        bottom_layout.addWidget(self.input_2_sugar_orc, 11, 4, alignment=Qt.AlignLeft)

        # Input 3
        self.input_3_sugar_bnm_label = QLabel("Banana nut muffins:")
        self.input_3_sugar_bnm = QDoubleSpinBox()
        self.input_3_sugar_bnm.setFont(font_input)
        self.input_3_sugar_bnm_label.setFont(font_input_label)
        self.input_3_sugar_bnm_label.setStyleSheet("color: #FFF;padding-bottom:5px;")
        self.input_3_sugar_bnm.setStyleSheet("background-color: #F0F0F0;padding:5px;")
        self.input_3_sugar_bnm.setRange(0.0, 1000.0)  # Set the range of values as needed
        self.input_3_sugar_bnm.setSingleStep(0.1)  # Set the step size
        self.input_3_sugar_bnm.setSuffix(" kg")
        self.input_3_sugar_bnm.setFixedWidth(150)
        self.input_3_sugar_bnm.setFixedHeight(40)
        self.input_3_sugar_bnm.hide()
        self.input_3_sugar_bnm_label.hide()
        bottom_layout.addWidget(self.input_3_sugar_bnm_label, 12, 1, )
        bottom_layout.addWidget(self.input_3_sugar_bnm, 12, 2, alignment=Qt.AlignLeft)

        # Input 4
        self.input_4_sugar_blm_label = QLabel("Blueberry muffins:")
        self.input_4_sugar_blm = QDoubleSpinBox()
        self.input_4_sugar_blm.setFont(font_input)
        self.input_4_sugar_blm_label.setFont(font_input_label)
        self.input_4_sugar_blm_label.setStyleSheet("color: #FFF;padding-bottom:5px;")
        self.input_4_sugar_blm.setStyleSheet("background-color: #F0F0F0;padding:5px;")
        self.input_4_sugar_blm.setRange(0.0, 1000.0)  # Set the range of values as needed
        self.input_4_sugar_blm.setSingleStep(0.1)  # Set the step size
        self.input_4_sugar_blm.setSuffix(" kg")
        self.input_4_sugar_blm.setFixedWidth(150)
        self.input_4_sugar_blm.setFixedHeight(40)
        self.input_4_sugar_blm.hide()
        self.input_4_sugar_blm_label.hide()
        bottom_layout.addWidget(self.input_4_sugar_blm_label, 12, 3, )
        bottom_layout.addWidget(self.input_4_sugar_blm, 12, 4, alignment=Qt.AlignLeft) 

        # Input 3
        input_3_ingredients_label = QLabel("Butter:")
        input_3_ingredients_label.setFont(font_input_label)
        input_3_ingredients_label.setStyleSheet("color: #FFF;padding-bottom:5px;")
        bottom_layout.addWidget(input_3_ingredients_label, 13, 1, )
        # Input 1
        self.input_1_butter_ccc_label = QLabel("Chocolate chip cookies:")
        font_input = QFont()
        font_input.setPointSize(12)

        self.input_1_butter_ccc_label.setFont(font_input_label)
        self.input_1_butter_ccc_label.setStyleSheet("color: #FFF;padding-bottom:5px;")  # Set label text color
        self.input_1_butter_ccc = QDoubleSpinBox()
        self.input_1_butter_ccc.setFont(font_input)
        self.input_1_butter_ccc.setStyleSheet("background-color: #F0F0F0;padding:5px;")
        self.input_1_butter_ccc.setRange(0.0, 1000.0)  # Set the range of values as needed
        self.input_1_butter_ccc.setSingleStep(0.1)  # Set the step size
        self.input_1_butter_ccc.setSuffix(" kg")
        self.input_1_butter_ccc.setFixedWidth(150)
        self.input_1_butter_ccc.setFixedHeight(40)
        bottom_layout.addWidget(self.input_1_butter_ccc_label, 14, 1, )
        bottom_layout.addWidget(self.input_1_butter_ccc, 14, 2, alignment=Qt.AlignLeft)

        # Input 2
        self.input_2_butter_orc_label = QLabel("Oatmeal raisin cookies:")
        self.input_2_butter_orc = QDoubleSpinBox()
        self.input_2_butter_orc.setFont(font_input)
        self.input_2_butter_orc_label.setFont(font_input_label)
        self.input_2_butter_orc_label.setStyleSheet("color: #FFF;padding-bottom:5px;")
        self.input_2_butter_orc.setStyleSheet("background-color: #F0F0F0;padding:5px;")
        self.input_2_butter_orc.setRange(0.0, 1000.0)  # Set the range of values as needed
        self.input_2_butter_orc.setSingleStep(0.1)  # Set the step size
        self.input_2_butter_orc.setSuffix(" kg")
        self.input_2_butter_orc.setFixedWidth(150)
        self.input_2_butter_orc.setFixedHeight(40)
        self.input_2_butter_orc.hide()
        self.input_2_butter_orc_label.hide()
        bottom_layout.addWidget(self.input_2_butter_orc_label, 14, 3, )
        bottom_layout.addWidget(self.input_2_butter_orc, 14, 4, alignment=Qt.AlignLeft)

        # Input 3
        self.input_3_butter_bnm_label = QLabel("Banana nut muffins:")
        self.input_3_butter_bnm = QDoubleSpinBox()
        self.input_3_butter_bnm.setFont(font_input)
        self.input_3_butter_bnm_label.setFont(font_input_label)
        self.input_3_butter_bnm_label.setStyleSheet("color: #FFF;padding-bottom:5px;")
        self.input_3_butter_bnm.setStyleSheet("background-color: #F0F0F0;padding:5px;")
        self.input_3_butter_bnm.setRange(0.0, 1000.0)  # Set the range of values as needed
        self.input_3_butter_bnm.setSingleStep(0.1)  # Set the step size
        self.input_3_butter_bnm.setSuffix(" kg")
        self.input_3_butter_bnm.setFixedWidth(150)
        self.input_3_butter_bnm.setFixedHeight(40)
        self.input_3_butter_bnm.hide()
        self.input_3_butter_bnm_label.hide()
        bottom_layout.addWidget(self.input_3_butter_bnm_label, 15, 1, )
        bottom_layout.addWidget(self.input_3_butter_bnm, 15, 2, alignment=Qt.AlignLeft)

        # Input 4
        self.input_4_butter_blm_label = QLabel("Blueberry muffins:")
        self.input_4_butter_blm = QDoubleSpinBox()
        self.input_4_butter_blm.setFont(font_input)
        self.input_4_butter_blm_label.setFont(font_input_label)
        self.input_4_butter_blm_label.setStyleSheet("color: #FFF;padding-bottom:5px;")
        self.input_4_butter_blm.setStyleSheet("background-color: #F0F0F0;padding:5px;")
        self.input_4_butter_blm.setRange(0.0, 1000.0)  # Set the range of values as needed
        self.input_4_butter_blm.setSingleStep(0.1)  # Set the step size
        self.input_4_butter_blm.setSuffix(" kg")
        self.input_4_butter_blm.setFixedWidth(150)
        self.input_4_butter_blm.setFixedHeight(40)
        self.input_4_butter_blm.hide()
        self.input_4_butter_blm_label.hide()
        bottom_layout.addWidget(self.input_4_butter_blm_label, 15, 3, )
        bottom_layout.addWidget(self.input_4_butter_blm, 15, 4, alignment=Qt.AlignLeft) 

        # Input 4
        input_4_ingredients_label = QLabel("Eggs:")
        input_4_ingredients_label.setFont(font_input_label)
        input_4_ingredients_label.setStyleSheet("color: #FFF;padding-bottom:5px;")
        bottom_layout.addWidget(input_4_ingredients_label, 16, 1, )
        # Input 1
        self.input_1_eggs_ccc_label = QLabel("Chocolate chip cookies:")
        font_input = QFont()
        font_input.setPointSize(12)

        self.input_1_eggs_ccc_label.setFont(font_input_label)
        self.input_1_eggs_ccc_label.setStyleSheet("color: #FFF;padding-bottom:5px;")  # Set label text color
        self.input_1_eggs_ccc = QDoubleSpinBox()
        self.input_1_eggs_ccc.setFont(font_input)
        self.input_1_eggs_ccc.setStyleSheet("background-color: #F0F0F0;padding:5px;")
        self.input_1_eggs_ccc.setRange(0.0, 1000.0)  # Set the range of values as needed
        self.input_1_eggs_ccc.setSingleStep(0.1)  # Set the step size
        self.input_1_eggs_ccc.setSuffix(" kg")
        self.input_1_eggs_ccc.setFixedWidth(150)
        self.input_1_eggs_ccc.setFixedHeight(40)
        bottom_layout.addWidget(self.input_1_eggs_ccc_label, 17, 1, )
        bottom_layout.addWidget(self.input_1_eggs_ccc, 17, 2, alignment=Qt.AlignLeft)

        # Input 2
        self.input_2_eggs_orc_label = QLabel("Oatmeal raisin cookies:")
        self.input_2_eggs_orc = QDoubleSpinBox()
        self.input_2_eggs_orc.setFont(font_input)
        self.input_2_eggs_orc_label.setFont(font_input_label)
        self.input_2_eggs_orc_label.setStyleSheet("color: #FFF;padding-bottom:5px;")
        self.input_2_eggs_orc.setStyleSheet("background-color: #F0F0F0;padding:5px;")
        self.input_2_eggs_orc.setRange(0.0, 1000.0)  # Set the range of values as needed
        self.input_2_eggs_orc.setSingleStep(0.1)  # Set the step size
        self.input_2_eggs_orc.setSuffix(" kg")
        self.input_2_eggs_orc.setFixedWidth(150)
        self.input_2_eggs_orc.setFixedHeight(40)
        self.input_2_eggs_orc.hide()
        self.input_2_eggs_orc_label.hide()
        bottom_layout.addWidget(self.input_2_eggs_orc_label, 17, 3, )
        bottom_layout.addWidget(self.input_2_eggs_orc, 17, 4, alignment=Qt.AlignLeft)

        # Input 3
        self.input_3_eggs_bnm_label = QLabel("Banana nut muffins:")
        self.input_3_eggs_bnm = QDoubleSpinBox()
        self.input_3_eggs_bnm.setFont(font_input)
        self.input_3_eggs_bnm_label.setFont(font_input_label)
        self.input_3_eggs_bnm_label.setStyleSheet("color: #FFF;padding-bottom:5px;")
        self.input_3_eggs_bnm.setStyleSheet("background-color: #F0F0F0;padding:5px;")
        self.input_3_eggs_bnm.setRange(0.0, 1000.0)  # Set the range of values as needed
        self.input_3_eggs_bnm.setSingleStep(0.1)  # Set the step size
        self.input_3_eggs_bnm.setSuffix(" kg")
        self.input_3_eggs_bnm.setFixedWidth(150)
        self.input_3_eggs_bnm.setFixedHeight(40)
        self.input_3_eggs_bnm.hide()
        self.input_3_eggs_bnm_label.hide()
        bottom_layout.addWidget(self.input_3_eggs_bnm_label, 18, 1, )
        bottom_layout.addWidget(self.input_3_eggs_bnm, 18, 2, alignment=Qt.AlignLeft)

        # Input 4
        self.input_4_eggs_blm_label = QLabel("Blueberry muffins:")
        self.input_4_eggs_blm = QDoubleSpinBox()
        self.input_4_eggs_blm.setFont(font_input)
        self.input_4_eggs_blm_label.setFont(font_input_label)
        self.input_4_eggs_blm_label.setStyleSheet("color: #FFF;padding-bottom:5px;")
        self.input_4_eggs_blm.setStyleSheet("background-color: #F0F0F0;padding:5px;")
        self.input_4_eggs_blm.setRange(0.0, 1000.0)  # Set the range of values as needed
        self.input_4_eggs_blm.setSingleStep(0.1)  # Set the step size
        self.input_4_eggs_blm.setSuffix(" kg")
        self.input_4_eggs_blm.setFixedWidth(150)
        self.input_4_eggs_blm.setFixedHeight(40)
        self.input_4_eggs_blm.hide()
        self.input_4_eggs_blm_label.hide()
        bottom_layout.addWidget(self.input_4_eggs_blm_label, 18, 3, )
        bottom_layout.addWidget(self.input_4_eggs_blm, 18, 4, alignment=Qt.AlignLeft) 
        




        # OvenTime list
        ovenTime_list_label = QLabel("Oven Time: ")
        font = QFont()
        font.setPointSize(20)
        ovenTime_list_label.setFont(font)
        ovenTime_list_label.setStyleSheet("color: #FFF;padding-bottom:5px;")  # Set label text color
        bottom_layout.addWidget(ovenTime_list_label, 19, 0, alignment=Qt.AlignLeft)
        # Input 1
        self.input_1_ovenTime_label = QLabel("Chocolate chip cookies:")
        font_input = QFont()
        font_input.setPointSize(13)

        self.input_1_ovenTime_label.setFont(font_input_label)
        self.input_1_ovenTime_label.setStyleSheet("color: #FFF;padding-bottom:5px;")  # Set label text color
        self.input_1_ovenTime = QDoubleSpinBox()
        self.input_1_ovenTime.setFont(font_input)
        self.input_1_ovenTime.setStyleSheet("background-color: #F0F0F0;padding:5px;")
        self.input_1_ovenTime.setRange(0.0, 1000.0)  # Set the range of values as needed
        self.input_1_ovenTime.setSingleStep(0.1)  # Set the step size
        self.input_1_ovenTime.setSuffix(" units")
        self.input_1_ovenTime.setFixedWidth(150)
        self.input_1_ovenTime.setFixedHeight(40)
        bottom_layout.addWidget(self.input_1_ovenTime_label, 20, 1, )
        bottom_layout.addWidget(self.input_1_ovenTime, 20, 2, alignment=Qt.AlignLeft)

        # Input 2
        self.input_2_ovenTime_label = QLabel("Oatmeal raisin cookies:")
        self.input_2_ovenTime = QDoubleSpinBox()
        self.input_2_ovenTime.setFont(font_input)
        self.input_2_ovenTime_label.setFont(font_input_label)
        self.input_2_ovenTime_label.setStyleSheet("color: #FFF;padding-bottom:5px;")
        self.input_2_ovenTime.setStyleSheet("background-color: #F0F0F0;padding:5px;")
        self.input_2_ovenTime.setRange(0.0, 1000.0)  # Set the range of values as needed
        self.input_2_ovenTime.setSingleStep(0.1)  # Set the step size
        self.input_2_ovenTime.setSuffix(" units")
        self.input_2_ovenTime.setFixedWidth(150)
        self.input_2_ovenTime.setFixedHeight(40)
        self.input_2_ovenTime.hide()
        self.input_2_ovenTime_label.hide()
        bottom_layout.addWidget(self.input_2_ovenTime_label, 20, 3, )
        bottom_layout.addWidget(self.input_2_ovenTime, 20, 4, alignment=Qt.AlignLeft)

        # Input 3
        self.input_3_ovenTime_label = QLabel("Banana nut muffins:")
        self.input_3_ovenTime = QDoubleSpinBox()
        self.input_3_ovenTime.setFont(font_input)
        self.input_3_ovenTime_label.setFont(font_input_label)
        self.input_3_ovenTime_label.setStyleSheet("color: #FFF;padding-bottom:5px;")
        self.input_3_ovenTime.setStyleSheet("background-color: #F0F0F0;padding:5px;")
        self.input_3_ovenTime.setRange(0.0, 1000.0)  # Set the range of values as needed
        self.input_3_ovenTime.setSingleStep(0.1)  # Set the step size
        self.input_3_ovenTime.setSuffix(" units")
        self.input_3_ovenTime.setFixedWidth(150)
        self.input_3_ovenTime.setFixedHeight(40)
        self.input_3_ovenTime.hide()
        self.input_3_ovenTime_label.hide()
        bottom_layout.addWidget(self.input_3_ovenTime_label, 21, 1, )
        bottom_layout.addWidget(self.input_3_ovenTime, 21, 2, alignment=Qt.AlignLeft)

        # Input 4
        self.input_4_ovenTime_label = QLabel("Blueberry muffins:")
        self.input_4_ovenTime = QDoubleSpinBox()
        self.input_4_ovenTime.setFont(font_input)
        self.input_4_ovenTime_label.setFont(font_input_label)
        self.input_4_ovenTime_label.setStyleSheet("color: #FFF;padding-bottom:5px;")
        self.input_4_ovenTime.setStyleSheet("background-color: #F0F0F0;padding:5px;")
        self.input_4_ovenTime.setRange(0.0, 1000.0)  # Set the range of values as needed
        self.input_4_ovenTime.setSingleStep(0.1)  # Set the step size
        self.input_4_ovenTime.setSuffix(" units")
        self.input_4_ovenTime.setFixedWidth(150)
        self.input_4_ovenTime.setFixedHeight(40)
        self.input_4_ovenTime.hide()
        self.input_4_ovenTime_label.hide()
        bottom_layout.addWidget(self.input_4_ovenTime_label, 21, 3, )
        bottom_layout.addWidget(self.input_4_ovenTime, 21, 4, alignment=Qt.AlignLeft)


        #Flour in Storage
        global_label = QLabel("Global Inputs: ")
        font = QFont()
        font.setPointSize(20)
        global_label.setFont(font)
        global_label.setStyleSheet("color: #FFF;padding-bottom:5px;")  # Set label text color
        bottom_layout.addWidget(global_label, 22, 0, alignment=Qt.AlignLeft)
        # Input 1
        input_1_flour_label = QLabel("Flour:")
        font_input = QFont()
        font_input.setPointSize(12)


    
        input_1_flour_label.setFont(font_input_label)
        input_1_flour_label.setStyleSheet("color: #FFF;padding-bottom:5px;")  # Set label text color
        self.input_1_flour = QDoubleSpinBox()
        self.input_1_flour.setFont(font_input)
        self.input_1_flour.setStyleSheet("background-color: #F0F0F0;padding:5px;")
        self.input_1_flour.setRange(0.0, 1000.0)  # Set the range of values as needed
        self.input_1_flour.setSingleStep(0.1)  # Set the step size
        self.input_1_flour.setSuffix(" kg")
        self.input_1_flour.setFixedWidth(150)
        self.input_1_flour.setFixedHeight(40)
        bottom_layout.addWidget(input_1_flour_label, 23, 1, )
        bottom_layout.addWidget(self.input_1_flour, 23, 2, alignment=Qt.AlignLeft)

        # Input 2
        input_2_sugar_label = QLabel("Sugar:")
        self.input_2_sugar = QDoubleSpinBox()
        self.input_2_sugar.setFont(font_input)
        input_2_sugar_label.setFont(font_input_label)
        input_2_sugar_label.setStyleSheet("color: #FFF;padding-bottom:5px;")
        self.input_2_sugar.setStyleSheet("background-color: #F0F0F0;padding:5px;")
        self.input_2_sugar.setRange(0.0, 1000.0)  # Set the range of values as needed
        self.input_2_sugar.setSingleStep(0.1)  # Set the step size
        self.input_2_sugar.setSuffix(" kg")
        self.input_2_sugar.setFixedWidth(150)
        self.input_2_sugar.setFixedHeight(40)
        bottom_layout.addWidget(input_2_sugar_label, 23, 3, )
        bottom_layout.addWidget(self.input_2_sugar, 23, 4, alignment=Qt.AlignLeft)

        # Input 3
        input_3_eggs_label = QLabel("Eggs:")
        self.input_3_eggs = QDoubleSpinBox()
        self.input_3_eggs.setFont(font_input)
        input_3_eggs_label.setFont(font_input_label)
        input_3_eggs_label.setStyleSheet("color: #FFF;padding-bottom:5px;")
        self.input_3_eggs.setStyleSheet("background-color: #F0F0F0;padding:5px;")
        self.input_3_eggs.setRange(0.0, 1000.0)  # Set the range of values as needed
        self.input_3_eggs.setSingleStep(0.1)  # Set the step size
        self.input_3_eggs.setSuffix(" units")
        self.input_3_eggs.setFixedWidth(150)
        self.input_3_eggs.setFixedHeight(40)
        bottom_layout.addWidget(input_3_eggs_label, 24, 1, )
        bottom_layout.addWidget(self.input_3_eggs, 24, 2, alignment=Qt.AlignLeft)

        # Input 4
        input_4_butter_label = QLabel("Butter:")
        self.input_4_butter = QDoubleSpinBox()
        self.input_4_butter.setFont(font_input)
        input_4_butter_label.setFont(font_input_label)
        input_4_butter_label.setStyleSheet("color: #FFF;padding-bottom:5px;")
        self.input_4_butter.setStyleSheet("background-color: #F0F0F0;padding:5px;")
        self.input_4_butter.setRange(0.0, 1000.0)  # Set the range of values as needed
        self.input_4_butter.setSingleStep(0.1)  # Set the step size
        self.input_4_butter.setSuffix(" kg")
        self.input_4_butter.setFixedWidth(150)
        self.input_4_butter.setFixedHeight(40)
        bottom_layout.addWidget(input_4_butter_label, 24, 3, )
        bottom_layout.addWidget(self.input_4_butter, 24, 4, alignment=Qt.AlignLeft)

        # Input 5
        input_5_gluten_label = QLabel("Glutten:")
        self.input_5_gluten = QDoubleSpinBox()
        self.input_5_gluten.setFont(font_input)
        input_5_gluten_label.setFont(font_input_label)
        input_5_gluten_label.setStyleSheet("color: #FFF;padding-bottom:5px;")
        self.input_5_gluten.setStyleSheet("background-color: #F0F0F0;padding:5px;")
        self.input_5_gluten.setRange(0.0, 1000.0)  # Set the range of values as needed
        self.input_5_gluten.setSingleStep(0.1)  # Set the step size
        self.input_5_gluten.setSuffix(" kg")
        self.input_5_gluten.setFixedWidth(150)
        self.input_5_gluten.setFixedHeight(40)
        bottom_layout.addWidget(input_5_gluten_label, 25, 1, )
        bottom_layout.addWidget(self.input_5_gluten, 25, 2, alignment=Qt.AlignLeft)

        # Input 6
        input_6_oven_capacity_label = QLabel("Oven capacity:")
        self.input_6_oven_capacity = QDoubleSpinBox()
        self.input_6_oven_capacity.setFont(font_input)
        input_6_oven_capacity_label.setFont(font_input_label)
        input_6_oven_capacity_label.setStyleSheet("color: #FFF;padding-bottom:5px;")
        self.input_6_oven_capacity.setStyleSheet("background-color: #F0F0F0;padding:5px;")
        self.input_6_oven_capacity.setRange(0.0, 1000.0)  # Set the range of values as needed
        self.input_6_oven_capacity.setSingleStep(0.1)  # Set the step size
        self.input_6_oven_capacity.setSuffix(" units")
        self.input_6_oven_capacity.setFixedWidth(150)
        self.input_6_oven_capacity.setFixedHeight(40)
        bottom_layout.addWidget(input_6_oven_capacity_label, 25, 3, )
        bottom_layout.addWidget(self.input_6_oven_capacity, 25, 4, alignment=Qt.AlignLeft)







        # Submit button
        self.problem1_submit_btn = QPushButton("Submit")
        self.problem1_submit_btn.setStyleSheet("background-color: #F0F0F0;")
        self.problem1_submit_btn.setFixedWidth(120)
        self.problem1_submit_btn.setFont(font_input_label)
        self.problem1_submit_btn.setFixedHeight(50)
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
        bottom_layout.addWidget(self.problem1_submit_btn, 26, 5)
        # Add the bottom widget to the problem_1_page layout
        scroll_layout.addWidget(checkbox_widget)
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
        pixmap_2 = QPixmap("Assets/problem_build_bakery.png")

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
        self.bottom_widget_2 = QWidget()

        # Create a layout for the bottom widget
        self.bottom_layout_2 = QGridLayout(self.bottom_widget_2)

        # Input 1
        self.input_1_label_2 = QLabel("Number of neighborhoods:")
        font_input_2 = QFont()
        font_input_2.setPointSize(12)
        font_2 = QFont()
        font_2.setPointSize(18)
        self.input_1_label_2.setFont(font_2)
        self.input_1_label_2.setStyleSheet("color: #FFF;padding-bottom:5px;")  # Set label text color
        self.input_1_2 = QSpinBox()
        self.input_1_2.setFont(font_input_2)
        self.input_1_2.setStyleSheet("background-color: #F0F0F0;padding:5px;")
        self.input_1_2.setRange(2, 5)
        self.input_1_2.setSuffix(" units")
        self.input_1_2.setFixedWidth(150)
        self.input_1_2.setFixedHeight(40)
        self.bottom_layout_2.addWidget(self.input_1_label_2, 0, 1, alignment=Qt.AlignRight)
        self.bottom_layout_2.addWidget(self.input_1_2, 0, 2,1,2, alignment=Qt.AlignLeft)

        # Input 2
        self.input_2_label_2 = QLabel("Number of locations:")
        self.input_2_2 = QSpinBox()
        self.input_2_2.setFont(font_input_2)
        self.input_2_label_2.setFont(font_2)
        self.input_2_label_2.setStyleSheet("color: #FFF;padding-bottom:5px;")
        self.input_2_2.setStyleSheet("background-color: #F0F0F0;padding:5px;")
        self.input_2_2.setRange(2, 5)
        self.input_2_2.setSuffix(" units")
        self.input_2_2.setFixedWidth(150)
        self.input_2_2.setFixedHeight(40)
        self.bottom_layout_2.addWidget(self.input_2_label_2, 0, 3, alignment=Qt.AlignRight)
        self.bottom_layout_2.addWidget(self.input_2_2, 0, 4,1,2, alignment=Qt.AlignLeft)
        # enter button
        self.problem2_enter_btn = QPushButton("Enter")
        self.problem2_enter_btn.setStyleSheet("background-color: #F0F0F0;")
        self.problem2_enter_btn.setFixedWidth(100)
        self.problem2_enter_btn.setFont(font_input_label)
        self.problem2_enter_btn.setFixedHeight(40)
        self.problem2_enter_btn.setStyleSheet("""
            QPushButton {
                color: #FFF;
                background-color: blue; /* Set background color */
                padding: 10px; /* Set padding */
                border-radius: 10px;
            }

            QPushButton:hover {
                background-color: #fff; /* Change background color on hover */
                color: blue;
            }

            QPushButton:pressed {
                border: 2px solid rgba(0, 0, 0, 0.5); /* Add shadow effect when pressed */
            }
        """)
        self.problem2_enter_btn.setCursor(Qt.PointingHandCursor)
        self.bottom_layout_2.addWidget(self.problem2_enter_btn, 1, 5, alignment=Qt.AlignRight)
        # Submit button
        self.problem2_submit_btn = QPushButton("Submit")
        self.problem2_submit_btn.setStyleSheet("background-color: #F0F0F0;")
        self.problem2_submit_btn.setFixedWidth(100)
        self.problem2_submit_btn.setFont(font_input_label)
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
        self.problem2_submit_btn.hide()
        self.bottom_layout_2.addWidget(self.problem2_submit_btn, 100, 5, alignment=Qt.AlignRight)
        # Add the bottom widget to the problem_2_page layout
        scroll_layout_2.addWidget(self.bottom_widget_2)
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
        # self.label_gurobi_res2.setText("This is Gurobi result 2")
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
        font.setPointSize(22)  # Set font size to 10 points
        label.setFont(font)
        label.setStyleSheet("color: #FFF;")
        label.setAlignment(Qt.AlignLeft)
        self.verticalLayout_8.addWidget(label)

        # Label table 1
        label_table1 = QLabel(self.page_3)
        label_table1.setObjectName("label_table1")
        label_table1.setText("Table Of Bakery Problem:")
        font = QFont()
        font.setPointSize(17)  # Set font size to 10 points
        label_table1.setFont(font)
        label_table1.setStyleSheet("color: #FFF;")
        label_table1.setAlignment(Qt.AlignCenter)
        self.verticalLayout_8.addWidget(label_table1)

        # Table
        self.table = QTableWidget(self.page_3)
        self.table.setColumnCount(12) 
        # Set column widths
        self.table.setColumnWidth(0, 8)  # "ID",
        self.table.setColumnWidth(1, 50)  # "Problem Name",
        self.table.setColumnWidth(2, 85)  # "Profit", 
        self.table.setColumnWidth(3, 85)  # "Weighting", 
        self.table.setColumnWidth(4, 85)  # "Flour list",     
        self.table.setColumnWidth(5, 85)  # "Butter",
        self.table.setColumnWidth(6, 85)  # "Sugar",
        self.table.setColumnWidth(7, 85)  # "Eggs",
        self.table.setColumnWidth(8, 85)  # "Oven Time",
        self.table.setColumnWidth(9, 105)  # "General list",
        self.table.setColumnWidth(10, 70)  # "Created In",
        self.table.setColumnWidth(11, 250)  # "Gurobi Result",
        # Set font size for table
        font = QFont()
        font.setPointSize(8)  # Set font size to 10 points
        self.table.setFont(font)

        # Set background color for cells
        self.table.setStyleSheet(
                                "QTableWidget::item { background-color: #ffffff; }"  # Set background color for cells
                                "QTableWidget::item:selected { background-color: #a6a6a6; }")  # Set background color for selected cells

        # Set row heights
        for row in range(self.table.rowCount()):
            self.table.setRowHeight(row, 100)  # Set height for each row
        # Set column headers
        self.table.setHorizontalHeaderLabels(["ID","Name", "Profit", "Weighting", "Flour list", "Butter", "Sugar", "Eggs", "Oven Time", "General list", "Created In", "Gurobi Result"])


        self.verticalLayout_8.addWidget(self.table)



        #-----------------------------------table 2 ----------------------------------

        # Label table 1
        label_table2 = QLabel(self.page_3)
        label_table2.setObjectName("label_table2")
        label_table2.setText("Table Of Build Bakery Problem:")
        font = QFont()
        font.setPointSize(17)  # Set font size to 10 points
        label_table2.setFont(font)
        label_table2.setStyleSheet("color: #FFF;")
        label_table2.setAlignment(Qt.AlignCenter)
        self.verticalLayout_8.addWidget(label_table2)

        # Table
        self.table2 = QTableWidget(self.page_3)
        self.table2.setColumnCount(12) 
        # Set column widths
        self.table2.setColumnWidth(0, 8)  # "ID",
        self.table2.setColumnWidth(1, 50)  # "Problem Name",
        self.table2.setColumnWidth(2, 90)  # "Profit", 
        self.table2.setColumnWidth(3, 85)  # "Weighting", 
        self.table2.setColumnWidth(4, 85)  # "Flour list",     
        self.table2.setColumnWidth(5, 85)  # "Butter",
        self.table2.setColumnWidth(6, 85)  # "Sugar",
        self.table2.setColumnWidth(7, 85)  # "Eggs",
        self.table2.setColumnWidth(8, 85)  # "Oven Time",
        self.table2.setColumnWidth(9, 105)  # "General list",
        self.table2.setColumnWidth(10, 70)  # "Created In",
        self.table2.setColumnWidth(11, 230)  # "Gurobi Result",
        # Set font size for table
        font = QFont()
        font.setPointSize(8)  # Set font size to 10 points
        self.table2.setFont(font)

        # Set background color for cells
        self.table2.setStyleSheet(
                                "QTableWidget::item { background-color: #ffffff; }"  # Set background color for cells
                                "QTableWidget::item:selected { background-color: #a6a6a6; }")  # Set background color for selected cells

       
        # Set column headers
        self.table2.setHorizontalHeaderLabels(["ID","Name","Neighborhoods", "Bakeries", "Capacities", "Costs", "Distances", "Distances min", "Distances max", "Distances bakeries", "Created In", "Gurobi Result"])


        self.verticalLayout_8.addWidget(self.table2)



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
