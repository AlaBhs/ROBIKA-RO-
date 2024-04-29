from PyQt5.QtCore import Qt, QEasingCurve, QPropertyAnimation
from PyQt5.QtWidgets import QMainWindow 

class UIFunctions(QMainWindow):
    def toggleMenu(self, maxWidth, enable):
        if enable:
            # GET WIDTH
            width = self.ui.frame_left_menu.width()
            maxExtend = maxWidth
            standard = 70

            # SET MAX WIDTH
            if width == 70:
                widthExtended = maxExtend
                self.ui.btn_page_1.setText("Problems")
                self.ui.btn_page_2.setText("Solutions")
                self.ui.btn_page_3.setText("History")
            else:
                widthExtended = standard
                self.ui.btn_page_1.setText("")
                self.ui.btn_page_2.setText("")
                self.ui.btn_page_3.setText("")
            
            
            # ANIMATION
            self.animation = QPropertyAnimation(self.ui.frame_left_menu, b"minimumWidth")
            self.animation.setDuration(400)
            self.animation.setStartValue(width)
            self.animation.setEndValue(widthExtended)
            self.animation.setEasingCurve(QEasingCurve.InOutQuart)
            self.animation.start()

            # ANIMATION text button
            self.animation_btn = QPropertyAnimation(self.ui.btn_page_1, b"minimumWidth")
            self.animation_btn.setDuration(400)
            self.animation_btn.setStartValue(width)
            self.animation_btn.setEndValue(widthExtended)
            self.animation_btn.setEasingCurve(QEasingCurve.InOutQuart)
            self.animation_btn.start()
