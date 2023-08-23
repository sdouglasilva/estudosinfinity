from ursina import Ursina, window, color, Entity, EditorCamera, time, load_texture
from ursina.shaders.lit_with_shadows_shader import lit_with_shadows_shader
app = Ursina()

EditorCamera()

window.size = (800, 600)
window.title = "FirstGame"
window.fullscreen = False
window.development_mode = True
window.ui_enabled = True
window.borderless =False
window.show_ursina_splash = True
window.color = color.blue
window.bottom = (0,5)

primeiro_ent = Entity(
    model= 'cube',
    texture = load_texture('completa.jpg'),
    scale =(1,2,3),
    rotation =(89,90,56),
    animation =(2,5,6),
    position =(0,0,0),
    shader= lit_with_shadows_shader
)
    
    
def update():
    primeiro_ent.rotation_x += time.dt * 50
    pass
def input(key):
    if key == 'escape':
        app.exit()


app.run()