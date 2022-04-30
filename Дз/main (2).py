import tkinter as tk
from tkinter import messagebox

font_header = ('Arial', 15)
font_entry = ('Arial', 12)
label_font = ('Arial', 11)
entry_font = ('Arial', 12, 'bold')
base_padding = {'padx': 10, 'pady': 8}
header_padding = {'padx': 10, 'pady': 12}

class Hotel(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)


        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)



        self.frames = {}
        for F in (LoginPage, MainPage, SevenRoom, TwobadRoom, FamilyRoom, AboutUs):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame


            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("LoginPage")

    def show_frame(self, page_name):

        frame = self.frames[page_name]
        frame.tkraise()


class LoginPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.frame = tk.Frame
        self.frame.configure(self, background='#536872')

        # метка для поля ввода имени
        username_label = tk.Label(self, text='Имя пользователя', font=label_font, **base_padding,
                                  bg='#F4D000')
        username_label.place(x=130,y=100,width=150,height=20)
        self.controller.configure(background='#334353')
        # поле ввода имени
        self.username_entry = tk.Entry(self, bg='#838996', fg='#FDF5E6', font=font_entry)
        self.username_entry.place(x=130,y=120,width=150,height=20)

        # метка для поля ввода пароля
        password_label = tk.Label(self, text='Пароль', font=label_font, **base_padding,
                                  bg='#F4D000')
        password_label.place(x=130,y=200,width=150,height=20)

        # поле ввода пароля
        self.password_entry = tk.Entry(self, show='*', bg='#838996', fg='#FDF5E6', font=font_entry)
        self.password_entry.place(x=130,y=220,width=150,height=20)

        # кнопка отправки формы
        self.send_btn = tk.Button(self, text='Войти', font='bold',  bg='#318FE7',
                                  activebackground='#20B2AA', width=10,
                                  command=lambda: self.check_password())
        self.send_btn.place(x=150,y=300,width=100,height=25)

    def check_password(self):
        if self.password_entry.get() == "0" and self.username_entry.get() == "0":
            self.controller.show_frame("MainPage")
        else:
            messagebox.showinfo("ERROR", "Неверный пароль или логин")


class MainPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.frame = tk.Frame
        self.frame.configure(self, background='#536872')

        self. main_lbl= tk.Label(self,text='Khorezm Palace', font=label_font, **base_padding,
                                  bg='#CEBCE6')
        self.main_lbl.place(y=5, height=25, width=400)

        self.about_btn = tk.Button(self, text='О нас:', font=label_font, **base_padding,
                                 bg='#CEBCE6',
                                   command=lambda: self.show_pageab())
        self.about_btn.place(y=80, height=25, width=400)

        self.main_btn1 = tk.Button(self, text='Семиместная комната',  bg='#F07427',
                                  activebackground='#20B2AA',width=10,
                                  command=lambda: self.show_page1())
        self.main_btn2 = tk.Button(self, text='Комната с раздельными кроватями',  bg='#F07427',
                                  activebackground='#20B2AA',width=10,
                                  command=lambda: self.show_page2())
        self.main_btn3 = tk.Button(self, text='Семейная комната', bg='#F07427',
                                  activebackground='#20B2AA',width=10,
                                  command=lambda: self.show_page3())


        self.main_btn1.place(y=150,width=200, height=25)
        self.main_btn2.place(x=199,y=150, width=200, height=25)
        self.main_btn3.place(x=110,y=190,width=200, height=25)

    def show_pageab(self):
        self.controller.show_frame("AboutUs")
    def show_page1(self):
        self.controller.show_frame("SevenRoom")
    def show_page2(self):
        self.controller.show_frame("TwobadRoom")
    def show_page3(self):
        self.controller.show_frame("FamilyRoom")

class AboutUs(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.frame = tk.Frame
        self.frame.configure(self, background='#536872')
        self.sub_title = tk.Label(self, text='Khorezm Palace\n '
                                             'сочетает в себе уют домашнего очага и комфорт\n  современной обстановки.\n  Все номера выходят окнами на тихий закрытый двор,\n оснащены стеклопакетами и кондиционерами,\n имеют отдельную туалетную комнату с душевой кабиной и феном.',
                                  bg='#FFE042', fg='#2A502A')
        self.sub_title.place(y=10, width=400,height=90)



        self.goback_btn = tk.Button(self, text='Назад', font='bold',  bg='#318FE7',
                                  activebackground='#20B2AA', width=10,
                                  command=lambda: self.go_back())
        self.goback_btn.place(x=50,y=400,width=100,height=25)

    def go_back(self):
        self.controller.show_frame("MainPage")

class SevenRoom(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.frame = tk.Frame
        self.frame.configure(self, background='#536872')

        self.sevenroom_lbl = tk.Label(self, text='Семиместная комната', font=label_font, **base_padding,
                                 bg='#CEBCE6')
        self.sevenroom_lbl.place(y=5, height=25, width=400)

        self.info = tk.Label(self, text="Стоимость за одну ночь 30$. В стоимость входит завтрак",
                             bg='#FFE042', fg='#2A502A')
        self.info.place(y=25, width=400,height=15)


        self.one_btn = tk.Button(self, text='Первая кровать', font='bold',  bg='#318FE7',
                                  activebackground='#20B2AA', width=10,
                                  command=lambda: self.basket_ent.insert(0, "Первая кровать "))
        self.one_btn.place(y=70,width=200,height=25)

        self.two_btn = tk.Button(self, text='Вторая кровать', font='bold',  bg='#318FE7',
                                  activebackground='#20B2AA', width=10,
                                  command=lambda: self.basket_ent.insert(0, "Вторая кровать "))
        self.two_btn.place(x=200,y=70,width=200,height=25)

        self.three_btn = tk.Button(self, text='Третья кровать', font='bold',  bg='#318FE7',
                                  activebackground='#20B2AA', width=10,
                                  command=lambda: self.basket_ent.insert(0, "Третья кровать "))
        self.three_btn.place(y=110,width=200,height=25)

        self.fore_btn = tk.Button(self, text='Четвертая кровать', font='bold',  bg='#318FE7',
                                  activebackground='#20B2AA', width=10,
                                  command=lambda: self.basket_ent.insert(0, "Четвертая кровать "))
        self.fore_btn.place(x=200,y=110,width=200,height=25)

        self.five_btn = tk.Button(self, text='Пятая кровать', font='bold',  bg='#318FE7',
                                  activebackground='#20B2AA', width=10,
                                  command=lambda: self.basket_ent.insert(0, "Пятая кровать "))
        self.five_btn.place(y=170,width=200,height=25)

        self.six_btn = tk.Button(self, text='Шестая кровать', font='bold',  bg='#318FE7',
                                  activebackground='#20B2AA', width=10,
                                  command=lambda: self.basket_ent.insert(0, "Шестая кровать "))
        self.six_btn.place(x=200,y=170,width=200,height=25)

        self.seven_btn = tk.Button(self, text='Седьмая кровать', font='bold',  bg='#318FE7',
                                  activebackground='#20B2AA', width=10,
                                  command=lambda: self.basket_ent.insert(0, "Седьмая кровать "))
        self.seven_btn.place(x=105,y=220,width=200,height=25)

        self.basket_ent = tk.Entry(self, font=label_font,
                                   bg='#3591CD')
        self.basket_ent.place(x=20, y=270, width=350, height=50)


        self.goback_btn = tk.Button(self, text='Назад', font='bold',  bg='#318FE7',
                                  activebackground='#20B2AA', width=10,
                                  command=lambda: self.go_back())
        self.goback_btn.place(x=50,y=400,width=100,height=25)

        self.delet_btn = tk.Button(self, text="Удалить", font='bold', bg='#3591CD',
                                   activebackground='#20B2AA', width=20,
                                   command=lambda: self.Delete())
        self.delet_btn.place(x=200, y=400, width=100, height=25)



    def Delete(self):
        self.basket_ent.delete(0, tk.END)

    def go_back(self):
        self.controller.show_frame("MainPage")

class TwobadRoom(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.frame = tk.Frame
        self.frame.configure(self, background='#536872')

        self.sevenroom_lbl = tk.Label(self, text='Комната с раздельными кроватями', font=label_font, **base_padding,
                                 bg='#CEBCE6')
        self.sevenroom_lbl.place(y=5, height=25, width=400)


        self.three_btn = tk.Button(self, text='2-комната', font='bold', bg='#318FE7',
                                   activebackground='#20B2AA', width=10,
                                   command=lambda: self.basket_ent.insert(0, "2-комната "))
        self.three_btn.place(y=100, width=200, height=25)

        self.fore_btn = tk.Button(self, text='3-комната', font='bold', bg='#318FE7',
                                  activebackground='#20B2AA', width=10,
                                  command=lambda: self.basket_ent.insert(0, "3-комната "))
        self.fore_btn.place(x=200, y=100, width=200, height=25)

        self.five_btn = tk.Button(self, text='4-комната', font='bold', bg='#318FE7',
                                  activebackground='#20B2AA', width=10,
                                  command=lambda: self.basket_ent.insert(0, "4-комната "))
        self.five_btn.place(y=150, width=200, height=25)

        self.six_btn = tk.Button(self, text='5-комната', font='bold', bg='#318FE7',
                                 activebackground='#20B2AA', width=10,
                                 command=lambda: self.basket_ent.insert(0, "5-комната "))
        self.six_btn.place(x=200, y=150, width=200, height=25)




        self.goback_btn = tk.Button(self, text='Назад', font='bold', bg='#318FE7',
                                    activebackground='#20B2AA', width=10,
                                    command=lambda: self.go_back())
        self.goback_btn.place(x=50, y=400, width=100, height=25)

        self.delet_btn = tk.Button(self, text="Удалить", font='bold', bg='#3591CD',
                                   activebackground='#20B2AA', width=20,
                                   command=lambda: self.Delete())
        self.delet_btn.place(x=200, y=400, width=100, height=25)

        self.basket_ent = tk.Entry(self, font=label_font,
                                   bg='#3591CD')
        self.basket_ent.place(x=20, y=270, width=350, height=50)

    def Delete(self):
        self.basket_ent.delete(0, tk.END)
    def go_back(self):
        self.controller.show_frame("MainPage")

class FamilyRoom(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.frame = tk.Frame
        self.frame.configure(self, background='#536872')

        self.sevenroom_lbl = tk.Label(self, text='Семейная комната', font=label_font, **base_padding,
                                 bg='#CEBCE6')
        self.sevenroom_lbl.place(y=5, height=25, width=400)

        self.three_btn = tk.Button(self, text='6-комната', font='bold', bg='#318FE7',
                                   activebackground='#20B2AA', width=10,
                                   command=lambda: self.basket_ent.insert(0, "6-комната "))
        self.three_btn.place(y=100, width=200, height=25)

        self.fore_btn = tk.Button(self, text='7-комната', font='bold', bg='#318FE7',
                                  activebackground='#20B2AA', width=10,
                                  command=lambda: self.basket_ent.insert(0, "7-комната "))
        self.fore_btn.place(x=200, y=100, width=200, height=25)

        self.five_btn = tk.Button(self, text='8-комната', font='bold', bg='#318FE7',
                                  activebackground='#20B2AA', width=10,
                                  command=lambda: self.basket_ent.insert(0, "8-комната "))
        self.five_btn.place(y=150, width=200, height=25)



        self.goback_btn = tk.Button(self, text='Назад', font='bold', bg='#318FE7',
                                    activebackground='#20B2AA', width=10,
                                    command=lambda: self.go_back())
        self.goback_btn.place(x=50, y=400, width=100, height=25)

        self.delet_btn = tk.Button(self, text="Удалить", font='bold', bg='#3591CD',
                                   activebackground='#20B2AA', width=20,
                                   command=lambda: self.Delete())
        self.delet_btn.place(x=200, y=400, width=100, height=25)

        self.basket_ent = tk.Entry(self, font=label_font,
                                   bg='#3591CD')
        self.basket_ent.place(x=20, y=270, width=350, height=50)

    def Delete(self):
        self.basket_ent.delete(0, tk.END)

    def go_back(self):
        self.controller.show_frame("MainPage")

if __name__ == "__main__":
    app = Hotel()

    app.title("Отель")
    app.geometry("400x500")
    app.resizable(False, False)

    app.grid_columnconfigure(0, minsize=100)
    app.mainloop()