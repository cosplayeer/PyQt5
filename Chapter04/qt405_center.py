# -*- coding: utf-8 -*-

'''
    【简介】
	PyQT5将窗口放在屏幕中间例子
    
'''

from PyQt5.QtWidgets import QDesktopWidget, QApplication ,QMainWindow
import sys  
    
class Winform( QMainWindow): 
    
    def __init__(self, parent=None):
        super( Winform, self).__init__(parent)
          
        self.setWindowTitle('主窗口放在屏幕中间例子')  
        self.resize(370,  250)  
        self.center()  
        self.status = self.statusBar()
        self.status.showMessage("这是状态栏提示",2000)
          
    def center(self):  
        screen = QDesktopWidget().screenGeometry()  
        size = self.geometry()        
        self.move(int((screen.width() - size.width()) / 2),  int((screen.height() - size.height()) / 2))  
  
if __name__ == "__main__": 
    app = QApplication(sys.argv)   
    win = Winform()  
    win.show()  
    sys.exit(app.exec_())  
