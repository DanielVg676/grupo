from turtle import *
import turtle as tur
tur.width(5)
yd=xd=-64
tur.tracer(delay=0) 
for i in range(2):
    tur.up()
    tur.goto(-197.5,yd)
    tur.down()
    tur.seth(0)
    tur.fd(394)
    yd+=128
    tur.up()
    tur.goto(xd,197.5)
    tur.down()
    tur.seth(270)
    tur.fd(394)
    xd+=128
tur.mainloop()