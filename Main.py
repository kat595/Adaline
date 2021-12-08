from tkinter import *
import Dataset
import Functions

#Adaline z ładniejszym kodem, porozdzielanymi plikami

def on_black(num):  # definicja funkcji zaimplementowanej pozniej
    on_black1(num)


def clear():  # definicja funkcji zaimplementowanej pozniej
    clear1()


def on_left():  # definicja funkcji zaimplementowanej pozniej
    on_left1()


def on_up():  # definicja funkcji zaimplementowanej pozniej
    on_up1()


def on_down():  # definicja funkcji zaimplementowanej pozniej
    on_down1()


def on_right():  # definicja funkcji zaimplementowanej pozniej
    on_right1()

# GUI

window = Tk()  # instancja okna
window.geometry("785x750")
window.title("Perceptron")

button1 = Button(window, text="clear", command=clear, font=("Comic Sans", 20), width=15,
                 state=ACTIVE)  # przycisk wyczysc w lewym gornym rogu
button1.pack()
button1.place(x=0, y=0)

button2 = Button(window, text="ucz sie", command=Functions.learn, font=("Comic Sans", 20), width=15,
                 state=ACTIVE)  # przycisk ucz sie u góry ekranu
button2.pack()
button2.place(x=270, y=0)

button3 = Button(window, text="rozstrzygnij", command=lambda: Functions.decide(5), font=("Comic Sans", 20), width=15,
                 state=ACTIVE)  # przycisk rozstrzygnij w prawym gornym rogu
button3.pack()
button3.place(x=540, y=0)

button4 = Button(window, text="w lewo", command=on_left, font=("Comic Sans", 20), width=10,
                 state=ACTIVE)  # przycisk do przesuniecia cyfry w lewo

button4.pack()
button4.place(x=0, y=700)

button5 = Button(window, text="w góre", command=on_up, font=("Comic Sans", 20), width=10,
                 state=ACTIVE)  # przycisk do przesuniecia cyfry w góre

button5.pack()
button5.place(x=200, y=700)

button6 = Button(window, text="w dół", command=on_down, font=("Comic Sans", 20), width=10,
                 state=ACTIVE)  # przycisk do przesuniecia cyfry w dół

button6.pack()
button6.place(x=400, y=700)

button7 = Button(window, text="w prawo", command=on_right, font=("Comic Sans", 20), width=15,
                 state=ACTIVE)  # przycisk do przesuniecia cyfry w prawo

button7.pack()
button7.place(x=600, y=700)

button8 = Button(window, text="zaszum", command=Functions.zaszum, font=("Comic Sand", 20), width=10,
                 state=ACTIVE)  # przycisk do odszumiania ręcznego

button8.pack()
button8.place(x=600, y=400)

frame = Frame(window, bg="green", bd=5)  # ramka w ktorej trzymamy board do perceptronu 5x7
frame.pack()
frame.place(x=215, y=60)

poleA1 = Button(frame, font='Times 20 bold', bg='gray', fg='gray', height=2, width=4, relief=SUNKEN,
                command=lambda: on_black('A1'))  # 1 wiersz pól
poleA1.grid(row=0, column=0)
poleA2 = Button(frame, font='Times 20 bold', bg='gray', fg='gray', height=2, width=4, relief=SUNKEN,
                command=lambda: on_black('A2'))
poleA2.grid(row=0, column=1)
poleA3 = Button(frame, font='Times 20 bold', bg='gray', fg='gray', height=2, width=4, relief=SUNKEN,
                command=lambda: on_black('A3'))
poleA3.grid(row=0, column=2)
poleA4 = Button(frame, font='Times 20 bold', bg='gray', fg='gray', height=2, width=4, relief=SUNKEN,
                command=lambda: on_black('A4'))
poleA4.grid(row=0, column=3)
poleA5 = Button(frame, font='Times 20 bold', bg='gray', fg='gray', height=2, width=4, relief=SUNKEN,
                command=lambda: on_black('A5'))
poleA5.grid(row=0, column=4)

poleB1 = Button(frame, font='Times 20 bold', bg='gray', fg='gray', height=2, width=4, relief=SUNKEN,
                command=lambda: on_black('B1'))  # 2 wiersz pól
poleB1.grid(row=1, column=0)
poleB2 = Button(frame, font='Times 20 bold', bg='gray', fg='gray', height=2, width=4, relief=SUNKEN,
                command=lambda: on_black('B2'))
poleB2.grid(row=1, column=1)
poleB3 = Button(frame, font='Times 20 bold', bg='gray', fg='gray', height=2, width=4, relief=SUNKEN,
                command=lambda: on_black('B3'))
poleB3.grid(row=1, column=2)
poleB4 = Button(frame, font='Times 20 bold', bg='gray', fg='gray', height=2, width=4, relief=SUNKEN,
                command=lambda: on_black('B4'))
poleB4.grid(row=1, column=3)
poleB5 = Button(frame, font='Times 20 bold', bg='gray', fg='gray', height=2, width=4, relief=SUNKEN,
                command=lambda: on_black('B5'))
poleB5.grid(row=1, column=4)

poleC1 = Button(frame, font='Times 20 bold', bg='gray', fg='gray', height=2, width=4, relief=SUNKEN,
                command=lambda: on_black('C1'))  # 3 wiersz pól
poleC1.grid(row=2, column=0)
poleC2 = Button(frame, font='Times 20 bold', bg='gray', fg='gray', height=2, width=4, relief=SUNKEN,
                command=lambda: on_black('C2'))
poleC2.grid(row=2, column=1)
poleC3 = Button(frame, font='Times 20 bold', bg='gray', fg='gray', height=2, width=4, relief=SUNKEN,
                command=lambda: on_black('C3'))
poleC3.grid(row=2, column=2)
poleC4 = Button(frame, font='Times 20 bold', bg='gray', fg='gray', height=2, width=4, relief=SUNKEN,
                command=lambda: on_black('C4'))
poleC4.grid(row=2, column=3)
poleC5 = Button(frame, font='Times 20 bold', bg='gray', fg='gray', height=2, width=4, relief=SUNKEN,
                command=lambda: on_black('C5'))
poleC5.grid(row=2, column=4)

poleD1 = Button(frame, font='Times 20 bold', bg='gray', fg='gray', height=2, width=4, relief=SUNKEN,
                command=lambda: on_black('D1'))  # 4 wiersz pól
poleD1.grid(row=3, column=0)
poleD2 = Button(frame, font='Times 20 bold', bg='gray', fg='gray', height=2, width=4, relief=SUNKEN,
                command=lambda: on_black('D2'))
poleD2.grid(row=3, column=1)
poleD3 = Button(frame, font='Times 20 bold', bg='gray', fg='gray', height=2, width=4, relief=SUNKEN,
                command=lambda: on_black('D3'))
poleD3.grid(row=3, column=2)
poleD4 = Button(frame, font='Times 20 bold', bg='gray', fg='gray', height=2, width=4, relief=SUNKEN,
                command=lambda: on_black('D4'))
poleD4.grid(row=3, column=3)
poleD5 = Button(frame, font='Times 20 bold', bg='gray', fg='gray', height=2, width=4, relief=SUNKEN,
                command=lambda: on_black('D5'))
poleD5.grid(row=3, column=4)

poleE1 = Button(frame, font='Times 20 bold', bg='gray', fg='gray', height=2, width=4, relief=SUNKEN,
                command=lambda: on_black('E1'))  # 5 wiersz pól
poleE1.grid(row=4, column=0)
poleE2 = Button(frame, font='Times 20 bold', bg='gray', fg='gray', height=2, width=4, relief=SUNKEN,
                command=lambda: on_black('E2'))
poleE2.grid(row=4, column=1)
poleE3 = Button(frame, font='Times 20 bold', bg='gray', fg='gray', height=2, width=4, relief=SUNKEN,
                command=lambda: on_black('E3'))
poleE3.grid(row=4, column=2)
poleE4 = Button(frame, font='Times 20 bold', bg='gray', fg='gray', height=2, width=4, relief=SUNKEN,
                command=lambda: on_black('E4'))
poleE4.grid(row=4, column=3)
poleE5 = Button(frame, font='Times 20 bold', bg='gray', fg='gray', height=2, width=4, relief=SUNKEN,
                command=lambda: on_black('E5'))
poleE5.grid(row=4, column=4)

poleF1 = Button(frame, font='Times 20 bold', bg='gray', fg='gray', height=2, width=4, relief=SUNKEN,
                command=lambda: on_black('F1'))  # 5 wiersz pól
poleF1.grid(row=5, column=0)
poleF2 = Button(frame, font='Times 20 bold', bg='gray', fg='gray', height=2, width=4, relief=SUNKEN,
                command=lambda: on_black('F2'))
poleF2.grid(row=5, column=1)
poleF3 = Button(frame, font='Times 20 bold', bg='gray', fg='gray', height=2, width=4, relief=SUNKEN,
                command=lambda: on_black('F3'))
poleF3.grid(row=5, column=2)
poleF4 = Button(frame, font='Times 20 bold', bg='gray', fg='gray', height=2, width=4, relief=SUNKEN,
                command=lambda: on_black('F4'))
poleF4.grid(row=5, column=3)
poleF5 = Button(frame, font='Times 20 bold', bg='gray', fg='gray', height=2, width=4, relief=SUNKEN,
                command=lambda: on_black('F5'))
poleF5.grid(row=5, column=4)

poleG1 = Button(frame, font='Times 20 bold', bg='gray', fg='gray', height=2, width=4, relief=SUNKEN,
                command=lambda: on_black('G1'))  # 5 wiersz pól
poleG1.grid(row=6, column=0)
poleG2 = Button(frame, font='Times 20 bold', bg='gray', fg='gray', height=2, width=4, relief=SUNKEN,
                command=lambda: on_black('G2'))
poleG2.grid(row=6, column=1)
poleG3 = Button(frame, font='Times 20 bold', bg='gray', fg='gray', height=2, width=4, relief=SUNKEN,
                command=lambda: on_black('G3'))
poleG3.grid(row=6, column=2)
poleG4 = Button(frame, font='Times 20 bold', bg='gray', fg='gray', height=2, width=4, relief=SUNKEN,
                command=lambda: on_black('G4'))
poleG4.grid(row=6, column=3)
poleG5 = Button(frame, font='Times 20 bold', bg='gray', fg='gray', height=2, width=4, relief=SUNKEN,
                command=lambda: on_black('G5'))
poleG5.grid(row=6, column=4)

window.config(background='#100b40')  # kolor tła okna

# GUI


def on_black1(num):  # zamalowanie wybranego kafelka na czarno
    if num == 'A1':
        poleA1.configure(fg="black", bg="black")
        Dataset.Matrix[0][0] = 1
    if num == 'A2':
        poleA2.configure(fg="black", bg="black")
        Dataset.Matrix[0][1] = 1
    if num == 'A3':
        poleA3.configure(fg="black", bg="black")
        Dataset.Matrix[0][2] = 1
    if num == 'A4':
        poleA4.configure(fg="black", bg="black")
        Dataset.Matrix[0][3] = 1
    if num == 'A5':
        poleA5.configure(fg="black", bg="black")
        Dataset.Matrix[0][4] = 1
    if num == 'B1':
        poleB1.configure(fg="black", bg="black")
        Dataset.Matrix[1][0] = 1
    if num == 'B2':
        poleB2.configure(fg="black", bg="black")
        Dataset.Matrix[1][1] = 1
    if num == 'B3':
        poleB3.configure(fg="black", bg="black")
        Dataset.Matrix[1][2] = 1
    if num == 'B4':
        poleB4.configure(fg="black", bg="black")
        Dataset.Matrix[1][3] = 1
    if num == 'B5':
        poleB5.configure(fg="black", bg="black")
        Dataset.Matrix[1][4] = 1
    if num == 'C1':
        poleC1.configure(fg="black", bg="black")
        Dataset.Matrix[2][0] = 1
    if num == 'C2':
        poleC2.configure(fg="black", bg="black")
        Dataset.Matrix[2][1] = 1
    if num == 'C3':
        poleC3.configure(fg="black", bg="black")
        Dataset.Matrix[2][2] = 1
    if num == 'C4':
        poleC4.configure(fg="black", bg="black")
        Dataset.Matrix[2][3] = 1
    if num == 'C5':
        poleC5.configure(fg="black", bg="black")
        Dataset.Matrix[2][4] = 1
    if num == 'D1':
        poleD1.configure(fg="black", bg="black")
        Dataset.Matrix[3][0] = 1
    if num == 'D2':
        poleD2.configure(fg="black", bg="black")
        Dataset.Matrix[3][1] = 1
    if num == 'D3':
        poleD3.configure(fg="black", bg="black")
        Dataset.Matrix[3][2] = 1
    if num == 'D4':
        poleD4.configure(fg="black", bg="black")
        Dataset.Matrix[3][3] = 1
    if num == 'D5':
        poleD5.configure(fg="black", bg="black")
        Dataset.Matrix[3][4] = 1
    if num == 'E1':
        poleE1.configure(fg="black", bg="black")
        Dataset.Matrix[4][0] = 1
    if num == 'E2':
        poleE2.configure(fg="black", bg="black")
        Dataset.Matrix[4][1] = 1
    if num == 'E3':
        poleE3.configure(fg="black", bg="black")
        Dataset.Matrix[4][2] = 1
    if num == 'E4':
        poleE4.configure(fg="black", bg="black")
        Dataset.Matrix[4][3] = 1
    if num == 'E5':
        poleE5.configure(fg="black", bg="black")
        Dataset.Matrix[4][4] = 1
    if num == 'F1':
        poleF1.configure(fg="black", bg="black")
        Dataset.Matrix[5][0] = 1
    if num == 'F2':
        poleF2.configure(fg="black", bg="black")
        Dataset.Matrix[5][1] = 1
    if num == 'F3':
        poleF3.configure(fg="black", bg="black")
        Dataset.Matrix[5][2] = 1
    if num == 'F4':
        poleF4.configure(fg="black", bg="black")
        Dataset.Matrix[5][3] = 1
    if num == 'F5':
        poleF5.configure(fg="black", bg="black")
        Dataset.Matrix[5][4] = 1
    if num == 'G1':
        poleG1.configure(fg="black", bg="black")
        Dataset.Matrix[6][0] = 1
    if num == 'G2':
        poleG2.configure(fg="black", bg="black")
        Dataset.Matrix[6][1] = 1
    if num == 'G3':
        poleG3.configure(fg="black", bg="black")
        Dataset.Matrix[6][2] = 1
    if num == 'G4':
        poleG4.configure(fg="black", bg="black")
        Dataset.Matrix[6][3] = 1
    if num == 'G5':
        poleG5.configure(fg="black", bg="black")
        Dataset.Matrix[6][4] = 1


def on_black2(numx, numy):  # funkcja do przesuwania cyfry na planszy, zamalowanie wybranego kafelka na czarno
    if numx == 0 and numy == 0:
        poleA1.configure(fg="black", bg="black")
        Dataset.Matrix[0][0] = 1
    if numx == 0 and numy == 1:
        poleA2.configure(fg="black", bg="black")
        Dataset.Matrix[0][1] = 1
    if numx == 0 and numy == 2:
        poleA3.configure(fg="black", bg="black")
        Dataset.Matrix[0][2] = 1
    if numx == 0 and numy == 3:
        poleA4.configure(fg="black", bg="black")
        Dataset.Matrix[0][3] = 1
    if numx == 0 and numy == 4:
        poleA5.configure(fg="black", bg="black")
        Dataset.Matrix[0][4] = 1
    if numx == 1 and numy == 0:
        poleB1.configure(fg="black", bg="black")
        Dataset.Matrix[1][0] = 1
    if numx == 1 and numy == 1:
        poleB2.configure(fg="black", bg="black")
        Dataset.Matrix[1][1] = 1
    if numx == 1 and numy == 2:
        poleB3.configure(fg="black", bg="black")
        Dataset.Matrix[1][2] = 1
    if numx == 1 and numy == 3:
        poleB4.configure(fg="black", bg="black")
        Dataset.Matrix[1][3] = 1
    if numx == 1 and numy == 4:
        poleB5.configure(fg="black", bg="black")
        Dataset.Matrix[1][4] = 1
    if numx == 2 and numy == 0:
        poleC1.configure(fg="black", bg="black")
        Dataset.Matrix[2][0] = 1
    if numx == 2 and numy == 1:
        poleC2.configure(fg="black", bg="black")
        Dataset.Matrix[2][1] = 1
    if numx == 2 and numy == 2:
        poleC3.configure(fg="black", bg="black")
        Dataset.Matrix[2][2] = 1
    if numx == 2 and numy == 3:
        poleC4.configure(fg="black", bg="black")
        Dataset.Matrix[2][3] = 1
    if numx == 2 and numy == 4:
        poleC5.configure(fg="black", bg="black")
        Dataset.Matrix[2][4] = 1
    if numx == 3 and numy == 0:
        poleD1.configure(fg="black", bg="black")
        Dataset.Matrix[3][0] = 1
    if numx == 3 and numy == 1:
        poleD2.configure(fg="black", bg="black")
        Dataset.Matrix[3][1] = 1
    if numx == 3 and numy == 2:
        poleD3.configure(fg="black", bg="black")
        Dataset.Matrix[3][2] = 1
    if numx == 3 and numy == 3:
        poleD4.configure(fg="black", bg="black")
        Dataset.Matrix[3][3] = 1
    if numx == 3 and numy == 4:
        poleD5.configure(fg="black", bg="black")
        Dataset.Matrix[3][4] = 1
    if numx == 4 and numy == 0:
        poleE1.configure(fg="black", bg="black")
        Dataset.Matrix[4][0] = 1
    if numx == 4 and numy == 1:
        poleE2.configure(fg="black", bg="black")
        Dataset.Matrix[4][1] = 1
    if numx == 4 and numy == 2:
        poleE3.configure(fg="black", bg="black")
        Dataset.Matrix[4][2] = 1
    if numx == 4 and numy == 3:
        poleE4.configure(fg="black", bg="black")
        Dataset.Matrix[4][3] = 1
    if numx == 4 and numy == 4:
        poleE5.configure(fg="black", bg="black")
        Dataset.Matrix[4][4] = 1
    if numx == 5 and numy == 0:
        poleF1.configure(fg="black", bg="black")
        Dataset.Matrix[5][0] = 1
    if numx == 5 and numy == 1:
        poleF2.configure(fg="black", bg="black")
        Dataset.Matrix[5][1] = 1
    if numx == 5 and numy == 2:
        poleF3.configure(fg="black", bg="black")
        Dataset.Matrix[5][2] = 1
    if numx == 5 and numy == 3:
        poleF4.configure(fg="black", bg="black")
        Dataset.Matrix[5][3] = 1
    if numx == 5 and numy == 4:
        poleF5.configure(fg="black", bg="black")
        Dataset.Matrix[5][4] = 1
    if numx == 6 and numy == 0:
        poleG1.configure(fg="black", bg="black")
        Dataset.Matrix[6][0] = 1
    if numx == 6 and numy == 1:
        poleG2.configure(fg="black", bg="black")
        Dataset.Matrix[6][1] = 1
    if numx == 6 and numy == 2:
        poleG3.configure(fg="black", bg="black")
        Dataset.Matrix[6][2] = 1
    if numx == 6 and numy == 3:
        poleG4.configure(fg="black", bg="black")
        Dataset.Matrix[6][3] = 1
    if numx == 6 and numy == 4:
        poleG5.configure(fg="black", bg="black")
        Dataset.Matrix[6][4] = 1


def clear1():  # reset planszy do poziomu startowego
    poleA1.configure(fg="gray", bg="gray")
    poleA2.configure(fg="gray", bg="gray")
    poleA3.configure(fg="gray", bg="gray")
    poleA4.configure(fg="gray", bg="gray")
    poleA5.configure(fg="gray", bg="gray")

    poleB1.configure(fg="gray", bg="gray")
    poleB2.configure(fg="gray", bg="gray")
    poleB3.configure(fg="gray", bg="gray")
    poleB4.configure(fg="gray", bg="gray")
    poleB5.configure(fg="gray", bg="gray")

    poleC1.configure(fg="gray", bg="gray")
    poleC2.configure(fg="gray", bg="gray")
    poleC3.configure(fg="gray", bg="gray")
    poleC4.configure(fg="gray", bg="gray")
    poleC5.configure(fg="gray", bg="gray")

    poleD1.configure(fg="gray", bg="gray")
    poleD2.configure(fg="gray", bg="gray")
    poleD3.configure(fg="gray", bg="gray")
    poleD4.configure(fg="gray", bg="gray")
    poleD5.configure(fg="gray", bg="gray")

    poleE1.configure(fg="gray", bg="gray")
    poleE2.configure(fg="gray", bg="gray")
    poleE3.configure(fg="gray", bg="gray")
    poleE4.configure(fg="gray", bg="gray")
    poleE5.configure(fg="gray", bg="gray")

    poleF1.configure(fg="gray", bg="gray")
    poleF2.configure(fg="gray", bg="gray")
    poleF3.configure(fg="gray", bg="gray")
    poleF4.configure(fg="gray", bg="gray")
    poleF5.configure(fg="gray", bg="gray")

    poleG1.configure(fg="gray", bg="gray")
    poleG2.configure(fg="gray", bg="gray")
    poleG3.configure(fg="gray", bg="gray")
    poleG4.configure(fg="gray", bg="gray")
    poleG5.configure(fg="gray", bg="gray")

    for i in range(7): # wyzerowanie matrycy
        for j in range(5):
            Dataset.Matrix[i][j] = 0


def on_left1():  # przesuniecie cyfry na matrycy w lewo
    Dataset.Matrix_new = [
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]
    ]
    for i in range(7):
        for j in range(5):
            if Dataset.Matrix[i][j] == 1:
                if j - 1 >= 0:
                    Dataset.Matrix_new[i][j - 1] = 1

    for i in range(7):
        for j in range(5):
            Dataset.Matrix[i][j] = 0

    clear1()
    for i in range(7):
        for j in range(5):
            if Dataset.Matrix_new[i][j] == 1:
                on_black2(i, j)


def on_up1():  # przesuniecie cyfry na matrycy w góre
    Dataset.Matrix_new = [
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]
    ]
    for i in range(7):
        for j in range(5):
            if Dataset.Matrix[i][j] == 1:
                if i - 1 >= 0:
                    Dataset.Matrix_new[i - 1][j] = 1

    for i in range(7):
        for j in range(5):
            Dataset.Matrix[i][j] = 0

    clear1()
    for i in range(7):
        for j in range(5):
            if Dataset.Matrix_new[i][j] == 1:
                on_black2(i, j)


def on_down1():  # przesuniecie cyfry na matrycy w dół
    Dataset.Matrix_new = [
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]
    ]
    for i in range(7): 
        for j in range(5):
            if Dataset.Matrix[i][j] == 1:
                if i + 1 <= 6:
                    Dataset.Matrix_new[i + 1][j] = 1

    for i in range(7): # wyzerowanie macierzy
        for j in range(5):
            Dataset.Matrix[i][j] = 0

    clear1()
    for i in range(7): # wywołanie funkcji zamalowującej matryce na przesuniety ksztalt
        for j in range(5):
            if Dataset.Matrix_new[i][j] == 1:
                on_black2(i, j)


def on_right1():  # przesuniecie cyfry na matrycy w prawo
    Dataset.Matrix_new = [
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]
    ]
    for i in range(7):
        for j in range(5):
            if Dataset.Matrix[i][j] == 1:
                if j + 1 <= 4:
                    Dataset.Matrix_new[i][j + 1] = 1

    for i in range(7): # wyzerowanie macierzy
        for j in range(5):
            Dataset.Matrix[i][j] = 0

    clear1()
    for i in range(7): # wywołanie funkcji zamalowującej matryce na przesuniety ksztalt
        for j in range(5):
            if Dataset.Matrix_new[i][j] == 1:
                on_black2(i, j)



window.mainloop()  # zatrzymanie okna na ekranie komputera
