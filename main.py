from tkinter import *
from word_utils import WordUtils
from ui_utils import UiUtils

class SpeedTest:
    def __init__(self, window):
        # -------- Ekran Ayarları --------
        self.window = window
        self.window.title("Image Editor")
        window_width = 1280
        window_height = 720
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        x = (screen_width / 2) - (window_width / 2)
        y = (screen_height / 2) - (window_height / 2) -50
        self.window.geometry("%dx%d+%d+%d" % (window_width, window_height, x, y))
        self.window.resizable(False, False)

        # -------- Frame --------
        self.m_page = Frame(self.window, bg="#1f2024")
        self.m_page.pack(fill=BOTH, expand=True)
        self.mainpage()


    def mainpage(self):
        self.canvas = Canvas(self.m_page, highlightthickness=0, bd=0, bg="white")
        self.canvas.place(x=280, y=20, width=750, height=170)
        self.canvas.place_forget()

        self.result_canvas = Canvas(self.m_page, highlightthickness=0, bd=0, bg="white")
        self.result_canvas.place(x=280, y=20, width=750, height=400)
        self.result_canvas.place_forget()

        self.home_canvas = Canvas(self.m_page, highlightthickness=0, bd=0, bg="white")
        self.home_canvas.place(x=280, y=20, width=750, height=200)

        self.high_score_canvas = Canvas(self.m_page, highlightthickness=0, bd=0, bg="white")
        self.high_score_canvas.place(x=280, y=220, width=750, height=400)

        self.word_utils = WordUtils(self.m_page, self.canvas, self.result_canvas, self.home_canvas, self.high_score_canvas)



window = Tk()
app = SpeedTest(window)
window.mainloop()