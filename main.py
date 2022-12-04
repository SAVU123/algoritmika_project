class TestWin(QWidget):
    def __init__(self):
    super().__init__()
    self.set_appear()
    self.initUI()
    self.connects()
    self.show()


    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)

        txt_title = 'Здоровье'
        win_x, win_y = 200, 100
        win_width, win_height = 1000, 600

