from ursina import *
from tkinter import filedialog
app = Ursina()
window.color = color.black
file = input('Напишите названия текстуры планеты:')
planet_model = Entity(model = 'sphere', texture = f'{file}.jpg')
def update():
    if held_keys['w']:
        planet_model.z -= 4 * time.dt
    if held_keys['s']:
        planet_model.z += 4 * time.dt
    if held_keys['a']:
        planet_model.x += 4 * time.dt
    if held_keys['d']:
        planet_model.x -= 4 * time.dt
    if held_keys['z']:
        planet_model.rotation_y += 25 * time.dt
    if held_keys['x']:
        planet_model.rotation_y -= 25 * time.dt
    if held_keys['y']:
        planet_model.rotation_x += 25 * time.dt
    if held_keys['h']:
        planet_model.rotation_x -= 25 * time.dt
app.run()
