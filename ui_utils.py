import json
from tkinter import *
from PIL import Image, ImageTk
import sys
import os



def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base_path, relative_path)

class UiUtils:
    def __init__(self, m_page, canvas, result_canvas, home_canvas, high_score_canvas, start_test, game_break, time_select):
        self.m_page = m_page
        self.canvas = canvas
        self.result_canvas = result_canvas
        self.home_canvas = home_canvas
        self.high_score_canvas = high_score_canvas
        self.start_test = start_test
        self.game_break = game_break
        self.time_select = time_select
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
        self.images_load()
        self.welcome_page()




    def get_user_data_path(self, filename):
        home = os.path.expanduser("~")
        data_dir = os.path.join(home, ".myapp")
        os.makedirs(data_dir, exist_ok=True)
        return os.path.join(data_dir, filename)

    def score_placeholder(self):
        self.toplam_kelime = 0
        self.dogru_kelime = 0
        self.yanlis_kelime = 0
        self.kelime_hata_orani = 0
        self.toplam_k_sampiyona = 0
        self.hata_orani_shamp = 0
        self.dogru_tus_vurusu = 0
        self.yanlis_tus_vurusu = 0
        self.test_süresi = "1:00"

    def buttons(self):
        self.start_button = Button(self.m_page, highlightthickness=0, bd=0, bg="white", command=self.start_test, image=self.start_img)
        self.start_button.place(x=310,y=660, width=200, height=60)
        self.finish_button = Button(self.m_page, highlightthickness=0, bd=0, bg="white", command=self.game_break, image=self.stop_img)
        self.finish_button.place(x=550,y=660, width=200, height=60)
        self.time_config_button = Button(self.m_page, highlightthickness=0, bd=0, bg="white", command=self.time_select, image=self.time_img)
        self.time_config_button.place(x=790,y=660, width=200, height=60)

    def images_load(self):
        start = Image.open(resource_path("images/start_button.png")).resize((200,60))
        self.start_img = ImageTk.PhotoImage(start)
        stop = Image.open(resource_path("images/stop_button.png")).resize((200,60))
        self.stop_img = ImageTk.PhotoImage(stop)
        time = Image.open(resource_path("images/time_button.png")).resize((200,60))
        self.time_img = ImageTk.PhotoImage(time)

    def welcome_page(self):
        wlcm_label = Image.open(resource_path("images/label_welcome.png")).resize((750,200))
        self.welcome_img = ImageTk.PhotoImage(wlcm_label)

        self.welcome_label = Label(self.home_canvas, image=self.welcome_img, bg="white")
        self.welcome_label.pack()

        self.high_score()


    def high_score(self):
        with open(self.high_score_path, "r", encoding="utf-8") as file:
            data = json.load(file)

        # Sol Taraf - Katiplik
        self.bosluk_hesabi_h = Label(self.high_score_canvas, text="BOŞLUK HESABI (Katiplik)", bg="#3498db", fg="white",
                                     font=("Arial", 18, "bold"), anchor="n")
        self.bosluk_hesabi_h.place(x=0, y=0, width=330, height=35)

        self.dbk_result_h = Label(self.high_score_canvas,
                                  text=f"Dakika Başı Kelime       ({data['toplam_k_sampiyona']:>4})",
                                  bg="#ffffff", fg="#2c3e50", font=("Arial", 17), anchor="ne")
        self.dbk_result_h.place(x=0, y=45, width=300, height=30)

        self.t_y_k_result_h = Label(self.high_score_canvas, text=f"Toplam Yazılan Kelime  ({data['toplam_kelime']:>4})",
                                    bg="#ffffff", fg="#2c3e50", font=("Arial", 17), anchor="ne")
        self.t_y_k_result_h.place(x=0, y=90, width=300, height=30)

        self.d_y_k_result_h = Label(self.high_score_canvas, text=f"Doğru Yazılan Kelime    ({data['dogru_kelime']:>4})",
                                    bg="#ffffff", fg="#2c3e50", font=("Arial", 17), anchor="ne")
        self.d_y_k_result_h.place(x=0, y=135, width=300, height=30)

        self.y_y_k_result_h = Label(self.high_score_canvas,
                                    text=f"Yanlış Yazılan Kelime    ({data['yanlis_kelime']:>4})",
                                    bg="#ffffff", fg="#2c3e50", font=("Arial", 17), anchor="ne")
        self.y_y_k_result_h.place(x=0, y=180, width=300, height=30)

        self.h_o_result_h = Label(self.high_score_canvas,
                                  text=f"Hata Oranı            (% {data['kelime_hata_orani']:6.2f})",
                                  bg="#ffffff", fg="#2c3e50", font=("Arial", 17), anchor="ne")
        self.h_o_result_h.place(x=0, y=225, width=300, height=30)

        # Orta Kısım
        self.t_t_v_l_result_h = Label(self.high_score_canvas,
                                      text=f"Tuşvuruşları           ({data['toplam_tus_vurusu']:>4})",
                                      bg="#ffffff", fg="#2c3e50", font=("Arial", 15), anchor="n")
        self.t_t_v_l_result_h.place(x=200, y=300, width=300, height=45)

        self.d_y_result_h = Label(self.high_score_canvas,
                                  text=f"     Doğru | Yanlış             ({data['dogru_tus_vurusu']:>3} | {data['yanlis_tus_vurusu']:<3})",
                                  bg="#ffffff", fg="#3498db", font=("Arial", 13, "bold"), anchor="n")
        self.d_y_result_h.place(x=200, y=335, width=300, height=45)

        self.d_b_d_v_result_h = Label(self.high_score_canvas,
                                      text=f"Dakika Başına Vuruş     ({data['dogru_tus_vurusu']:>4})",
                                      bg="#ffffff", fg="#2c3e50", font=("Arial", 13), anchor="n")
        self.d_b_d_v_result_h.place(x=200, y=365, width=300, height=45)

        # Sağ Taraf - Şampiyona
        self.vurus_hesabi_h = Label(self.high_score_canvas, text="VURUŞ HESABI (Şampiyona)", bg="#3498db", fg="white",
                                    font=("Arial", 18, "bold"), anchor="n")
        self.vurus_hesabi_h.place(x=400, y=0, width=350, height=35)

        self.t_t_v_result_h = Label(self.high_score_canvas, text=f"Toplam Tuş Vuruşu   ({data['dogru_tus_vurusu']:>4})",
                                    bg="#ffffff", fg="#2c3e50", font=("Arial", 18), anchor="ne")
        self.t_t_v_result_h.place(x=415, y=45, width=300, height=45)

        self.t_k_s_result_h = Label(self.high_score_canvas,
                                    text=f"Toplam Kelime Sayısı ({data['toplam_k_sampiyona']:>4})",
                                    bg="#ffffff", fg="#2c3e50", font=("Arial", 18), anchor="ne")
        self.t_k_s_result_h.place(x=415, y=90, width=300, height=45)

        self.h_s_result_h = Label(self.high_score_canvas,
                                  text=f"Hata Sayısı                ({data['yanlis_kelime']:>4})",
                                  bg="#ffffff", fg="#2c3e50", font=("Arial", 18), anchor="ne")
        self.h_s_result_h.place(x=415, y=135, width=300, height=45)

        self.h_o_shamp_result_h = Label(self.high_score_canvas,
                                        text=f"Hata Oranı         (% {data['hata_orani_shamp']:6.2f})",
                                        bg="#ffffff", fg="#2c3e50", font=("Arial", 18), anchor="ne")
        self.h_o_shamp_result_h.place(x=415, y=180, width=300, height=45)

        self.t_s_result_h = Label(self.high_score_canvas, text=f"Test Süresi               ({data['test_süresi']:>4})",
                                  bg="#ffffff", fg="#2c3e50", font=("Arial", 18), anchor="ne")
        self.t_s_result_h.place(x=415, y=225, width=300, height=45)

    def scoreboard(self):
        self.canvas.place_forget()
        self.dogru_tus_vurusu += + self.dogru_kelime
        self.toplam_tus_vurusu = self.dogru_tus_vurusu + self.yanlis_tus_vurusu

        self.result_canvas.place(x=280, y=20, width=750, height=400)
        try:
            self.kelime_hata_orani = round((self.yanlis_kelime / self.toplam_kelime) * 100)
            self.toplam_k_sampiyona = round(self.dogru_tus_vurusu / 5)
            self.hata_orani_shamp = round((self.yanlis_kelime / self.dogru_tus_vurusu) * 100)

        except ZeroDivisionError:
            if self.kelime_hata_orani == 0:
                self.kelime_hata_orani = 0
            elif self.toplam_k_sampiyona == 0:
                self.toplam_k_sampiyona = 0

        # Sol Taraf
        self.bosluk_hesabi = Label(self.result_canvas, text="BOŞLUK HESABI (Katiplik)", bg="#3498db", fg="white",
                                   font=("Arial", 18, "bold"), anchor="n")
        self.bosluk_hesabi.place(x=0, y=0, width=330, height=35)

        self.dbk_result = Label(self.result_canvas, text=f"Dakika Başı Kelime       ({self.toplam_k_sampiyona:>4})",
                                bg="#ffffff", fg="#2c3e50", font=("Arial", 17), anchor="ne")
        self.dbk_result.place(x=0, y=45, width=300, height=30)

        self.t_y_k_result = Label(self.result_canvas, text=f"Toplam Yazılan Kelime  ({self.toplam_kelime:>4})",
                                  bg="#ffffff", fg="#2c3e50", font=("Arial", 17), anchor="ne")
        self.t_y_k_result.place(x=0, y=90, width=300, height=30)

        self.d_y_k_result = Label(self.result_canvas, text=f"Doğru Yazılan Kelime    ({self.dogru_kelime:>4})",
                                  bg="#ffffff", fg="#2c3e50", font=("Arial", 17), anchor="ne")
        self.d_y_k_result.place(x=0, y=135, width=300, height=30)

        self.y_y_k_result = Label(self.result_canvas, text=f"Yanlış Yazılan Kelime    ({self.yanlis_kelime:>4})",
                                  bg="#ffffff", fg="#2c3e50", font=("Arial", 17), anchor="ne")
        self.y_y_k_result.place(x=0, y=180, width=300, height=30)

        self.h_o_result = Label(self.result_canvas,
                                text=f"Hata Oranı            (% {self.kelime_hata_orani:6.2f})", bg="#ffffff",
                                fg="#2c3e50", font=("Arial", 17), anchor="ne")
        self.h_o_result.place(x=0, y=225, width=300, height=30)

        # Orta Kısım
        self.t_t_v_l_result = Label(self.result_canvas, text=f"Tuşvuruşları           ({self.toplam_tus_vurusu:>4})",
                                    bg="#ffffff", fg="#2c3e50", font=("Arial", 15), anchor="n")
        self.t_t_v_l_result.place(x=200, y=300, width=300, height=45)

        self.d_y_result = Label(self.result_canvas,
                                text=f"     Doğru | Yanlış             ({self.dogru_tus_vurusu:>3} | {self.yanlis_tus_vurusu:<3})",
                                bg="#ffffff", fg="#3498db", font=("Arial", 13, "bold"), anchor="n")
        self.d_y_result.place(x=200, y=335, width=300, height=45)

        self.d_b_d_v_result = Label(self.result_canvas, text=f"Dakika Başına Vuruş     ({self.dogru_tus_vurusu:>4})",
                                    bg="#ffffff", fg="#2c3e50", font=("Arial", 13), anchor="n")
        self.d_b_d_v_result.place(x=200, y=365, width=300, height=45)

        # Sağ Taraf
        self.vurus_hesabi = Label(self.result_canvas, text="VURUŞ HESABI (Şampiyona)", bg="#3498db", fg="white",
                                  font=("Arial", 18, "bold"), anchor="n")
        self.vurus_hesabi.place(x=400, y=0, width=350, height=35)

        self.t_t_v_result = Label(self.result_canvas, text=f"Toplam Tuş Vuruşu   ({self.dogru_tus_vurusu:>4})",
                                  bg="#ffffff", fg="#2c3e50", font=("Arial", 18), anchor="ne")
        self.t_t_v_result.place(x=415, y=45, width=300, height=45)

        self.t_k_s_result = Label(self.result_canvas, text=f"Toplam Kelime Sayısı ({self.toplam_k_sampiyona:>4})",
                                  bg="#ffffff", fg="#2c3e50", font=("Arial", 18), anchor="ne")
        self.t_k_s_result.place(x=415, y=90, width=300, height=45)

        self.h_s_result = Label(self.result_canvas, text=f"Hata Sayısı                ({self.yanlis_kelime:>4})",
                                bg="#ffffff", fg="#2c3e50", font=("Arial", 18), anchor="ne")
        self.h_s_result.place(x=415, y=135, width=300, height=45)

        self.h_o_shamp_result = Label(self.result_canvas, text=f"Hata Oranı         (% {self.hata_orani_shamp:6.2f})",
                                      bg="#ffffff", fg="#2c3e50", font=("Arial", 18), anchor="ne")
        self.h_o_shamp_result.place(x=415, y=180, width=300, height=45)

        self.t_s_result = Label(self.result_canvas, text=f"Test Süresi               ({self.test_süresi:>4})",
                                bg="#ffffff",
                                fg="#2c3e50", font=("Arial", 18), anchor="ne")
        self.t_s_result.place(x=415, y=225, width=300, height=45)