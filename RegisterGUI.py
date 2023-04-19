from tkinter import *
from tkinter.font import *
import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry
import tkinter.messagebox
import requests
import json


class RegisterGUI:
    def __init__(self):
        self.__dept_entry = None
        self.__dept_show = None
        self.__selected_user_type = None

        self.__register = Tk()
        self.__header_font = Font(family="Kanit", weight="bold", size=20)
        self.__normal_font = Font(family="Kanit", weight="normal", size=16)
        self.__txtbox_font = Font(family="Kanit", weight="normal", size=12)
        self.__register.title("Register")
        self.__register.geometry("400x700")
        self.__register.resizable(width=False, height=False)

        Label(text="Register", font=self.__header_font).pack()

        Label(text="Username :", font=self.__normal_font).place(x=25, y=50)
        self.__username_entry = Entry(self.__register, font=self.__txtbox_font)
        self.__username_entry.place(x=140, y=55)

        Label(text="Password :", font=self.__normal_font).place(x=25, y=80)
        self.__pwd_entry = Entry(self.__register, font=self.__txtbox_font)
        self.__pwd_entry.place(x=140, y=85)

        Label(text="Email :", font=self.__normal_font).place(x=25, y=110)
        self.__email_entry = Entry(self.__register, font=self.__txtbox_font)
        self.__email_entry.place(x=140, y=115)

        Label(text="Name :", font=self.__normal_font).place(x=25, y=140)
        self.__name_entry = Entry(self.__register, font=self.__txtbox_font)
        self.__name_entry.place(x=140, y=145)

        Label(text="Surname :", font=self.__normal_font).place(x=25, y=170)
        self.__surname_entry = Entry(self.__register, font=self.__txtbox_font)
        self.__surname_entry.place(x=140, y=175)

        Label(text="Gender :", font=self.__normal_font).place(x=25, y=200)
        n = tk.StringVar()
        self.__genderChoose = ttk.Combobox(self.__register, width=10, textvariable=n)
        self.__genderChoose['values'] = ('Male', 'Female', 'Other')
        self.__genderChoose.place(x=140, y=210)
        self.__genderChoose.current()

        Label(text="BirthDate :", font=self.__normal_font).place(x=25, y=230)
        self.__cal = DateEntry(self.__register, width=10,
                               background="blue", foreground="skyblue", bd=4)
        self.__cal.place(x=140, y=240)

        Label(text="Education :", font=self.__normal_font).place(x=25, y=260)
        self.__educate_entry = Entry(self.__register, font=self.__txtbox_font)
        self.__educate_entry.place(x=140, y=265)

        Label(text="Province :", font=self.__normal_font).place(x=25, y=290)
        self.__prov_entry = Entry(self.__register, font=self.__txtbox_font)
        self.__prov_entry.place(x=140, y=295)

        Label(text="Country :", font=self.__normal_font).place(x=25, y=320)
        self.__country_entry = Entry(self.__register, font=self.__txtbox_font)
        self.__country_entry.place(x=140, y=325)

        Label(text="UserType :", font=self.__normal_font).place(x=25, y=350)
        i = tk.StringVar()
        self.__userTypeChoose = ttk.Combobox(self.__register, width=10, textvariable=i)
        self.__userTypeChoose['values'] = ('Teacher', 'Student')
        self.__userTypeChoose.place(x=140, y=360)
        self.__userTypeChoose.current()

        Button(text="register", font=self.__normal_font, command=self.register).place(x=140, y=420)
        self.__register.mainloop()

    def show_dept(self):
        self.__dept_show = Tk()
        self.__dept_show.title("Department")
        self.__dept_show.geometry("300x300")
        Label(self.__dept_show, text="Enter your Department", font=self.__header_font).pack()
        Label(self.__dept_show, text="Department :", font=self.__normal_font).place(x=25, y=115)
        self.__dept_entry = Entry(self.__dept_show, font=self.__txtbox_font)
        self.__dept_entry.place(x=140, y=115)
        Button(self.__dept_show, text="Done", font=self.__normal_font, command=self.register).place(x=140, y=250)
        self.__dept_show.mainloop()

    def register(self):
        if self.__userTypeChoose.get() == 'Teacher':
            self.show_dept()

        if self.__username_entry.get() == "" or self.__pwd_entry.get() == "" or (
                self.__userTypeChoose.get() not in ['Teacher', 'Student']):
            tkinter.messagebox.showerror(message="Please enter a Username, Password and UserType", title="Error")
        else:
            data = {
                "username": self.__username_entry.get(),
                "password": self.__pwd_entry.get(),
                "email": self.__email_entry.get(),
                "fname": self.__name_entry.get(),
                "lname": self.__surname_entry.get(),
                "gender": self.__genderChoose.get(),
                "birth_date": self.__cal.get(),
                "education": self.__educate_entry.get(),
                "province": self.__pwd_entry.get(),
                "country": self.__country_entry.get(),
                "user_type": self.__userTypeChoose.get()
            }

            # Add teacher_dept if usertype is Teacher
            if self.__userTypeChoose.get() == 'Teacher':
                data['teacher_dept'] = self.__dept_entry.get()

            r = requests.post("http://127.0.0.1:8000/register", json=data)
            res = json.loads(r.text)
            print(data)
            print(res)
            tkinter.messagebox.showinfo(message="Success", title="Successfully")
            self.__register.destroy()


RegisterGUI()