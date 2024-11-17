import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel,QVBoxLayout,QSpacerItem,QSizePolicy
from PyQt5 import uic
from PyQt5.QtGui import QFont, QPainter, QColor, QPixmap
from PyQt5.QtCore import Qt
import link_start


class FirstWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.background_pixmap = QPixmap('mainwindow/bizhi.jpg')  # 缓存背景图像

    def paintEvent(self, event=None):
        painter = QPainter(self)
        # 绘制背景图片，适应窗口大小
        painter.drawPixmap(0, 0, self.width(), self.height(), self.background_pixmap.scaled(self.size(), aspectRatioMode=1))

    def initUI(self):
        uic.loadUi('mainwindow/First.ui', self)
        self.setFixedSize(1200, 800)  # 设置窗口大小

        def custom_paint_event(self, event):
            painter = QPainter(self)

            # 绘制半透明背景
            painter.setOpacity(0.8)
            painter.fillRect(self.rect(), QColor(255, 255, 255))

            # 恢复透明度为1，绘制文本
            painter.setOpacity(1.0)
            painter.drawText(self.rect(), self.alignment(), self.text())

        # 在初始化UI时替换paintEvent
        self.label.paintEvent = custom_paint_event.__get__(self.label)

        self.b1.clicked.connect(self.open_second_window)
        self.b2.clicked.connect(self.close)

        # 设置标签的字体大小
        font_label = QFont()
        font_label.setPointSize(25)  # 设置标签字体大小
        self.label.setFont(font_label)
        self.label.setAlignment(Qt.AlignCenter)  # 设置文本居中
        self.label.setFixedSize(800, 400)  # 设置按钮大小
        # self.label.move(400, 350)

        # 设置按钮的字体大小
        font_button = QFont()
        font_button.setPointSize(16)  # 设置按钮字体大小
        self.b1.setFont(font_button)
        self.b1.setFixedSize(250, 100)  # 设置按钮大小
        self.b2.setFont(font_button)
        self.b2.setFixedSize(250, 100)  # 设置按钮大小

    def open_second_window(self):
        self.second_window = SecondWindow()
        self.second_window.show()
        self.close()  # 关闭当前窗口

class TransparentLabel(QLabel):
    def __init__(self, text, parent=None):
        super().__init__(text, parent)
        self.setAttribute(Qt.WA_TranslucentBackground)  # 允许透明背景

    def paintEvent(self, event):
        painter = QPainter(self)

        # 绘制半透明背景
        painter.setOpacity(0.5)  # 设置透明度为50%
        painter.fillRect(self.rect(), Qt.white)  # 填充半透明背景（可选颜色）

        # 恢复透明度为1，绘制文本
        painter.setOpacity(1.0)
        painter.drawText(self.rect(), self.alignment(), self.text())  # 绘制文本


class SecondWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.background_pixmap = QPixmap('mainwindow/bizhi.jpg')  # 缓存背景图像

    def initUI(self):
        uic.loadUi('mainwindow/Second.ui', self)

        self.setFixedSize(1200, 800)  # 设置窗口大小

        self.label.setAlignment(Qt.AlignCenter)  # 设置文本居中
        self.label.setFixedSize(700, 200)  # 设置按钮大小
        # 设置标签的字体大小
        font_label = QFont()
        font_label.setPointSize(25)  # 设置标签字体大小
        self.label.setFont(font_label)
        font_label.setPointSize(15)  # 设置标签字体大小
        self.label_3.setFont(font_label)
        # self.label_3.setFixedSize(250, 100)  # 设置按钮大小
        # self.label_4.setFixedSize(250, 100)  # 设置按钮大小
        self.label_4.setFont(font_label)
        self.label_5.setFont(font_label)

        self.pushButton.setFixedSize(250, 100)  # 设置按钮大小
        self.pushButton_2.setFixedSize(250, 100)  # 设置按钮大小
        self.pushButton.setFont(font_label)
        self.pushButton_2.setFont(font_label)

         # 获取布局并设置为透明背景
        self.verticalLayout = self.findChild(QVBoxLayout, 'verticalLayout')  # 确保 'verticalLayout' 是您在 Designer 中布局的名称

        self.pushButton.clicked.connect(self.button_clicked)
        self.pushButton_2.clicked.connect(self.button_clicked_2)

    def paintEvent(self, event=None):
        painter = QPainter(self)
        # 绘制背景图片，适应窗口大小
        painter.drawPixmap(0, 0, self.width(), self.height(), self.background_pixmap.scaled(self.size(), aspectRatioMode=1))

        # 绘制半透明背景
        painter.setOpacity(0.8)  # 设置透明度为50%
        painter.fillRect(self.verticalLayout.geometry(), QColor(255, 255, 255))  # 填充半透明背景

    def button_clicked(self):
        # 获取 ComboBox 的文本
        combo_text = self.comboBox.currentText()
        # 获取 LineEdit 的文本
        row = self.l1.text()
        column = self.l2.text()
        row = int(row)
        column = int(column)

        match combo_text:
            case 'Kruskal':
                maze = link_start.GeneratingMethod.KruskalAlgorithm(row,column)
            case 'Prim':
                maze = link_start.GeneratingMethod.PrimAlgorithm(row,column)
            case 'DFS':
                maze = link_start.GeneratingMethod.Dfs(row,column)
            case 'ReversiveDivision':
                maze = link_start.GeneratingMethod.RecursiveDivision(row,column)
        link_start.show_maze(maze)

    def button_clicked_2(self):
        # 获取 ComboBox 的文本
        combo_text = self.comboBox.currentText()
        # 获取 LineEdit 的文本
        row = self.l1.text()
        column = self.l2.text()
        row = int(row)
        column = int(column)

        match combo_text:
            case 'Kruskal':
                maze = link_start.GeneratingMethod.KruskalAlgorithm(row,column)
            case 'Prim':
                maze = link_start.GeneratingMethod.PrimAlgorithm(row,column)
            case 'DFS':
                maze = link_start.GeneratingMethod.Dfs(row,column)
            case 'ReversiveDivision':
                maze = link_start.GeneratingMethod.RecursiveDivision(row,column)
        
        self.third_window = ThirdWindow(maze)
        self.third_window.show()
        
        
class ThirdWindow(QWidget):
    def __init__(self, message):
        super().__init__()
        self.initUI(message)
        self.background_pixmap = QPixmap('mainwindow/bizhi.jpg')  # 缓存背景图像

    def initUI(self, message):
        uic.loadUi('mainwindow/Third.ui', self)

        self.setFixedSize(1200, 800)  # 设置窗口大小

        self.label.setAlignment(Qt.AlignCenter)  # 设置文本居中
        self.label.setFixedSize(700, 200)  # 设置按钮大小
        # 设置标签的字体大小
        font_label = QFont()
        font_label.setPointSize(25)  # 设置标签字体大小
        self.label.setFont(font_label)
        font_label.setPointSize(15)  # 设置标签字体大小
        self.l2.setFont(font_label)
        # self.label_3.setFixedSize(250, 100)  # 设置按钮大小
        # self.label_4.setFixedSize(250, 100)  # 设置按钮大小
        self.l1.setFont(font_label)

        self.pushButton.setFixedSize(250, 100)  # 设置按钮大小
        self.pushButton.setFont(font_label)


    def paintEvent(self, event=None):
        painter = QPainter(self)
        # 绘制背景图片，适应窗口大小
        painter.drawPixmap(0, 0, self.width(), self.height(), self.background_pixmap.scaled(self.size(), aspectRatioMode=1))

        # 绘制半透明背景
        painter.setOpacity(0.8)  # 设置透明度为50%
        painter.fillRect(self.verticalLayout.geometry(), QColor(255, 255, 255))  # 填充半透明背景

    



if __name__ == '__main__':
    app = QApplication(sys.argv)
    first_window = FirstWindow()
    first_window.show()
    sys.exit(app.exec_())
