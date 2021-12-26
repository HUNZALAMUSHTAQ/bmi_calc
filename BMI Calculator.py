from tkinter import Tk, Label, Button, Entry

def bmi():
    bmi_value=(int(e2.get())*703)/(int(e1.get())**2)
    if bmi_value<(18.5):
        msg='UNDER WEIGHT '
    elif bmi_value >= (18.5) < 25 :
        msg= 'NORMAL'
    elif bmi_value > (25):
        msg = 'Over Weight'
    l3 = Label(win, text='Your BMI value is :'+str(round(bmi_value,2))+'  '+msg)

    l3.grid(row='3',column='0')

win=Tk()
win.title('BMI Calculator')
l1=Label(win,text='Enter your Height in inches:')
l2=Label(win,text='Enter your Weight pounds lbs :')
b=Button(win,text='Convert',command=bmi)
e1=Entry(win)
e2=Entry(win)
e3=Entry(win)
xx=e3.get()

e1.grid(row='0',column='1')
e2.grid(row='1',column='1')
l1.grid(row='0',column='0')
l2.grid(row='1',column='0')
b.grid(row='2',column='0')
win.mainloop()
