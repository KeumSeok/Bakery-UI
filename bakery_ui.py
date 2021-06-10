import tkinter
from tkinter import *


class BakeryView:
    def __init__(self, window):
        self.__init_window(window)

    def __init_window(self, window):
        window.title("빵집")
        window.geometry('400x200')
        label = Label(window, text='주문내역')
        label.pack()
        self.orderText = Text(window)
        self.orderText.pack()

    def add_order(self, orders):
        self.orderText.insert(0.0, orders + "\n")


class CustomerView:
    def __init__(self, name, window, bakery_view):
        self.name = name
        self.__init_window(window)
        self.bakeryView = bakery_view

    def __init_window(self, window):
        window.title("고객: " + self.name)
        window.geometry('350x200')
        Label(window, text='샌드위치 (5000원)').grid(column=0, row=0)
        Label(window, text='케이크 (20000원)').grid(column=0, row=1)
        Button(window, text='주문하기', command=self.send_order).grid(column=0, row=2)
        self.sand = Entry(window, width=10)
        self.cake = Entry(window, width=10)
        self.sand.grid(column=1, row=0)
        self.cake.grid(column=1, row=1)


    def send_order(self):
        num1 = self.sand.get()
        num2 = self.cake.get()

        try:
            if int(num1)>0 and int(num2)>0:
                order_text = self.name+": 샌드위치 (5000원) "+num1+"개, 케이크 (20000원) "+num2+"개"
            elif int(num1)>0 and int(num2)==0:
                order_text = self.name+": 샌드위치 (5000원) "+num1+"개"
            elif int(num1)==0 and int(num2)>0:
                order_text = self.name+": 케이크 (20000원) "+num2+"개"

            self.bakeryView.add_order(order_text)
            
        except ValueError:
            print("")
        except UnboundLocalError:
            print("")


if __name__ == '__main__':
    app = Tk()
    bakery = BakeryView(app)
    CustomerView('고객A', Toplevel(app), bakery)
    CustomerView('고객B', Toplevel(app), bakery)
    app.mainloop()
