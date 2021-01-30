import turtle

Sun = 30
Mercury = 4.87
Venus = 12.10
Earth = 12.72
Mars = 6.77
Jupiter = 139.82
Saturn = 116.46
Uranus = 50.72
Neptune = 49.24

Sun_color = "#ffcc00"
Mercury_color = "#8585ad"
Venus_color = "#ff6600"
Earth_color = "#6699ff"
Mars_color = "#804000"
Jupiter_color = "#ff9966s"
Saturn_color = "#ff9933"
Uranus_color = "#ff8000"
Neptune_color = "#1a53ff"

t = turtle.Pen()
turtle.Screen().bgcolor("black")

Sun_orb = 0
Mercury_orb = 20
Venus_orb = 36
Earth_orb = 56
Mars_orb = 76
Jupiter_orb = 260
Saturn_orb = 475
Uranus_orb = 600
Neptune_orb = 750


t.pencolor("yellow")
t.goto(0,Sun_orb*(-1))
t.down()
t.circle(Sun_orb)
t.up()
t.goto(0,Mercury_orb*(-1))
t.down()
t.circle(Mercury_orb)
t.up()
t.goto(0,Venus_orb*(-1))
t.down()
t.circle(Venus_orb)
t.up()
t.goto(0,Earth_orb*(-1))
t.down()
t.circle(Earth_orb)
t.up()
t.goto(0, Mars_orb*(-1))
t.down()
t.circle(Mars_orb)
t.up()
t.goto(0,  Jupiter_orb*(-1))
t.down()
t.circle(Jupiter_orb)
t.up()
t.goto(0, Saturn_orb*(-1))
t.down()
t.circle(Saturn_orb)
t.up()
t.goto(0, Uranus_orb*(-1))
t.down()
t.circle(Uranus_orb)
t.up()
t.goto(0, Neptune_orb*(-1))
t.down()
t.circle(Neptune_orb)
t.pencolor("#ffcc00")
t.dot()