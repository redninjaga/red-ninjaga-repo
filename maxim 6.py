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
solar_system_1 = [30, 4.87, 12.10, 12.72, 6.77, 139.82, 116.46, 50.72, 49.24]
solar_system_distance = [0, 20, 36, 50, 76, 260, 475, 600, 750, 0]
solar_system_colors = ["#ffcc00", "#8585ad", "#ff6600", "#6699ff", "#804000", "#ff9966  ", "#ff9933", "#ff8000", "#1a53ff"]
Sun_color = "#ffcc00"
Mercury_color = "#8585ad"
Venus_color = "#ff6600"
Earth_color = "#6699ff"
Mars_color = "#804000"
Jupiter_color = "#ff9966"
Saturn_color = "#ff9933"
Uranus_color = "#ff8000"
Neptune_color = "#1a53ff"

t = turtle.Pen()
turtle.Screen().bgcolor("black")
t.speed(6)
Sun_orb = 0
Mercury_orb = -20
Venus_orb = -36
Earth_orb = -56
Mars_orb = -76
Jupiter_orb = -260
Saturn_orb = -475
Uranus_orb = -600
Neptune_orb = -750


t.pencolor("yellow")

draw_orbit(Sun_orb)
t.dot(Mercury, Mercury_color)
draw_orbit(Mercury_orb)
t.dot(Venus, Venus_color)
draw_orbit(Venus_orb)
t.dot(Earth, Earth_color)
draw_orbit(Earth_orb)
t.dot(Mars, Mars_color)
draw_orbit(Mars_orb)
t.dot(Jupiter, Jupiter_color)
draw_orbit(Jupiter_orb)
t.dot(Saturn)
draw_orbit(Saturn_orb)
t.dot(Uranus, Uranus_color)
draw_orbit(Uranus_orb)
t.dot(Neptune, Neptune_color)
draw_orbit(Neptune_orb)
# for x in range(9):
#     t.up()
#     t.goto(solar_system_distance[x], 0)
#     t.dot(solar_system_1[x], solar_system_colors[x])
#     t.down()
# turtle.mainloop()