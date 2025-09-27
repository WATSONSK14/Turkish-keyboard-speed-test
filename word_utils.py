from tkinter import *
from tkinter import font, messagebox
import json
import random
from tkinter.ttk import Combobox
from ui_utils import UiUtils
import sys
import os

def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base_path, relative_path)




class WordUtils:
    def __init__(self, m_page, canvas, result_canvas, home_canvas, high_score_canvas):
        self.m_page = m_page
        self.canvas = canvas
        self.result_canvas = result_canvas
        self.home_canvas = home_canvas
        self.high_score_canvas = high_score_canvas
        self.ui_utils = UiUtils(self.m_page, self.canvas, self.result_canvas, self.home_canvas, self.high_score_canvas, self.start_test,
                                self.game_break, self.time_select)
        self.placeholder()
        self.ui_utils.buttons()
        self.high_score_path = self.get_user_data_path("high_score.json")

        if not os.path.exists(self.high_score_path):
            with open(self.high_score_path, "w", encoding="utf-8") as file:
                json.dump({
                    "toplam_kelime": 0,
                    "dogru_kelime": 0,
                    "yanlis_kelime": 0,
                    "kelime_hata_orani": 0,
                    "toplam_k_sampiyona": 0,
                    "toplam_tus_vurusu": 0,
                    "hata_orani_shamp": 0,
                    "dogru_tus_vurusu": 0,
                    "yanlis_tus_vurusu": 0,
                    "test_süresi": "1:00"
                }, file, ensure_ascii=False, indent=4)

    def placeholder(self):
        self.word_list = []
        self.label_dict = {}
        self.main_dict = {}
        self.word_dict = {}
        self.current_index = 0
        self.current_satir = 1
        self.start_sayi = 3
        self.timer_number = 60
        self.game = False
        self.ui_utils.score_placeholder()

    def get_user_data_path(self, filename):
        home = os.path.expanduser("~")
        data_dir = os.path.join(home, ".myapp")
        os.makedirs(data_dir, exist_ok=True)
        return os.path.join(data_dir, filename)



    def high_scorer(self):
        with open(self.high_score_path, "r", encoding="utf-8") as file:
            data = json.load(file)
        score = data["toplam_k_sampiyona"]
        if self.ui_utils.toplam_k_sampiyona > score:
            new_dict = {
                        "toplam_kelime": self.ui_utils.toplam_kelime,
                        "dogru_kelime": self.ui_utils.dogru_kelime,
                        "yanlis_kelime": self.ui_utils.yanlis_kelime,
                        "kelime_hata_orani": self.ui_utils.kelime_hata_orani,
                        "toplam_k_sampiyona": self.ui_utils.toplam_k_sampiyona,
                        "toplam_tus_vurusu": self.ui_utils.toplam_tus_vurusu,
                        "hata_orani_shamp": self.ui_utils.hata_orani_shamp,
                        "dogru_tus_vurusu": self.ui_utils.dogru_tus_vurusu,
                        "yanlis_tus_vurusu": self.ui_utils.yanlis_tus_vurusu,
                        "test_süresi": self.ui_utils.test_süresi
                        }
            with open(self.high_score_path, "w", encoding="utf-8") as file_1:
                json.dump(new_dict, file_1, ensure_ascii=False, indent=4)

    def test(self):
        if not self.game:
            self.game = True
            self.timer()
        self.geri_sayim.destroy()
        self.m_page.after(1000, self.button_lock)

        self.canvas.place(x=280, y=20, width=750, height=170)
        self.time_label.place(x=0, y=20, width=250, height=170)
        self.entry = Entry(self.m_page, font=("Arial", 20))
        self.entry.place(x=280, y=225, width=750)
        self.entry.focus()
        self.entry.bind("<KeyRelease-space>", self.read_entry)

    def start_test(self):
        self.ui_utils.home_canvas.place_forget()
        self.ui_utils.high_score_canvas.place_forget()
        self.game_break()
        for i in self.main_dict:
            for j in self.main_dict[i]:
                j.destroy()
        if hasattr(self, "entry"):
            self.entry.destroy()

        fnt = font.Font(family="Arial", size=160, weight="bold")
        self.ui_utils.start_button.config(state=DISABLED)
        self.ui_utils.time_config_button.config(state=DISABLED)

        if not hasattr(self, "geri_sayim") or not self.geri_sayim.winfo_exists():
            self.result_canvas.place_forget()
            self.geri_sayim = Label(self.m_page, text="", fg="white", bg="#1f2024", font=fnt)
            self.geri_sayim.place(x=350, y=200, width=650, height=300)

        if self.start_sayi > 0:
            self.geri_sayim.config(text=self.start_sayi)
            self.start_sayi -= 1
            self.m_page.after(1000, self.start_test)

        elif self.start_sayi == 0:
            self.read_json()
            self.create_label()
            self.word_dicts()
            self.geri_sayim.config(text="Başla!")
            self.start_sayi -= 1
            self.m_page.after(1000, self.test)
            self.start_sayi = 3


    def timer(self):
        if not hasattr(self, 'time_label') or  not self.time_label.winfo_exists():
            self.time_label = Label(self.m_page, text=f"{self.ui_utils.test_süresi}",bg="#1f2024", bd=0, highlightthickness=0, font=("Arial", 45),fg="white")
            self.time_label.place(x=0, y=20, width=250, height=170)
        if self.game:
            if self.timer_number != 0:
                self.timer_number -= 1
                minutes = self.timer_number // 60
                seconds = self.timer_number % 60
                self.time_label.config(text=f"{minutes:02}:{seconds:02}")

                self.m_page.after(1000, self.timer)
            else:
                self.game_break()


    def game_break(self):
        if self.game:
            self.entry.destroy()
            self.timer_number = 60
            self.ui_utils.scoreboard()
            self.time_label.place_forget()
            self.high_scorer()
            self.ui_utils.score_placeholder()
        self.game = False
        self.current_index = 0
        self.current_satir = 1



    def time_select(self):
        if not self.game:
            if not hasattr(self, 'combo') or not self.combo.winfo_exists():
                self.combo = Combobox(self.m_page, values=["1 Dakika", "2 Dakika", "3 Dakika"])
                self.combo.current(0)
                self.combo.bind("<<ComboboxSelected>>", self.selected_time)
                self.combo.place(x=0, y=20, width=100, height=20)


    def selected_time(self, event):
        if self.combo.get() == "1 Dakika":
            self.timer_number = 60
            self.ui_utils.test_süresi = "1:00"
            self.combo.destroy()
        elif self.combo.get() == "2 Dakika":
            self.timer_number = 120
            self.ui_utils.test_süresi = "2:00"
            self.combo.destroy()
        elif self.combo.get() == "3 Dakika":
            self.timer_number = 180
            self.ui_utils.test_süresi = "3:00"
            self.combo.destroy()

    def button_lock(self):
        self.ui_utils.start_button.config(state="normal")
        self.ui_utils.time_config_button.config(state="normal")


    def read_json(self):
        with open(resource_path("words.json"), "r", encoding="utf-8") as file:
            data = json.load(file)
            self.word_list = data["words"]

    def random_word(self):
        new_list = []
        sayi = 200
        if self.ui_utils.test_süresi == "2:00":
            sayi = 450
        elif self.ui_utils.test_süresi == "3:00":
            sayi = 650
        else:
            sayi = 200

        for i in range(sayi):
            random_word = random.choice(self.word_list)
            if random_word not in new_list:
                new_list.append(random_word)
                self.word_list.remove(random_word)
        return new_list

    def create_label(self):
        for label_list in self.main_dict.values():
            for lbl in label_list:
                lbl.destroy()

        self.main_dict.clear()
        self.label_dict.clear()

        self.words = self.random_word()
        x, y, i, s = (0, 0, 0, 1)
        for word in self.words:
            metin = StringVar()
            metin.set(word)
            fnt = font.Font(family='Arial', size=20, underline=1)
            genislik = fnt.measure(word) + 10
            bosluk = genislik + 30
            label = Label(self.canvas, textvariable=metin, font=fnt, anchor="w", bg="white")
            label.place(x=x, y=y, width=genislik, height=30)
            self.label_dict[f"label{i}"] = label
            i += 1
            x += bosluk
            if x > 600 or len(self.words) == i:
                y += 60
                x = 0
                self.main_dict[f"satır{s}"] = list(self.label_dict.values())
                self.label_dict.clear()
                s += 1


    def word_dicts(self):
        for i in range(1, len(self.main_dict) +1):
            deneme = self.main_dict[f"satır{i}"]
            self.word_dict[f"satır{i}"] = [word.cget("text") for word in deneme]



    def read_entry(self, event):
        try:
            self.deger = self.entry.get().strip().lower()

            self.current_word = self.word_dict[f"satır{self.current_satir}"][self.current_index]
            self.current_label = self.main_dict[f"satır{self.current_satir}"][self.current_index]
            self.current_len_satır = len(self.word_dict[f"satır{self.current_satir}"])

            if self.current_word == self.deger:
                self.current_label.config(fg="green")
                self.current_index += 1
                self.ui_utils.dogru_kelime += 1
                self.ui_utils.toplam_kelime += 1
                for i in self.current_word:
                    self.ui_utils.dogru_tus_vurusu += 1
                self.entry.delete(0, END)
            else:
                self.current_label.config(fg="red")
                self.current_index += 1
                self.ui_utils.yanlis_kelime += 1
                self.ui_utils.toplam_kelime += 1
                for i in self.current_word:
                    self.ui_utils.yanlis_tus_vurusu += 1
                self.entry.delete(0, END)

            if self.current_len_satır == self.current_index:
                self.current_len_satır = 0
                self.current_index = 0
                self.current_satir += 1

                for j in range(1, len(self.main_dict) + 1):
                    deneme = self.main_dict[f"satır{j}"]
                    for i in deneme:
                        x = i.winfo_x()
                        y = i.winfo_y()
                        i.place(x=x, y=y - 60)

        except KeyError:
            self.game_break()