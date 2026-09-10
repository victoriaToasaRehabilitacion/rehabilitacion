from PIL import Image

im = Image.open("kit de marca.png")

# Ajuste fino de recorte para los 4 iconos de navegación sin texto cortado
# Columna width aprox 68px
# Queremos sólo el recuadro redondeado del icono (Y de 485 a 548)
nav_icons = [
    ("nav_inicio", 25, 485, 80, 545),
    ("nav_ejercicio", 95, 485, 150, 545),
    ("nav_salud", 165, 485, 220, 545),
    ("nav_progreso", 300, 485, 360, 545),
    ("nav_perfil", 370, 485, 430, 545),
    # Fila 2
    ("nav_rutinas", 25, 575, 80, 635),
    ("nav_recordatorios", 95, 575, 150, 635),
    ("nav_logros", 165, 575, 220, 635),
    ("nav_ajustes", 235, 575, 290, 635),
    ("nav_ayuda", 305, 575, 360, 635),
    ("nav_salir", 375, 575, 430, 635),
]

for name, x1, y1, x2, y2 in nav_icons:
    crop = im.crop((x1, y1, x2, y2))
    crop.save(f"assets/{name}.png", quality=95)
    print(f"Generado {name}.png {crop.size}")

# Recorte preciso del logo completo SIN el texto de arriba "LOGO PRINCIPAL"
# Empezando desde Y=35 para quitar el título de la plantilla
logo_clean = im.crop((30, 36, 425, 432))
logo_clean.save("assets/logo_brand_clean.png", quality=95)
print("Logo limpio generado")
