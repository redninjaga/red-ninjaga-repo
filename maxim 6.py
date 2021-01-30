import turtle


def draw_orbit(orbit):
    t.goto(0, orbit * (-1))
    t.down()
    t.circle(orbit)
    t.up()
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
draw_orbit(Sun_orb)
draw_orbit(Mercury_orb)
draw_orbit(Venus_orb)
draw_orbit(Earth_orb)
draw_orbit(Mars_orb)
draw_orbit(Jupiter_orb)
draw_orbit(Saturn_orb)
draw_orbit(Uranus_orb)
draw_orbit(Neptune_orb)
t.pencolor("#ffcc00")
t.dot()