import os
from PIL import Image

def crop_and_save(im, box, path):
    cropped = im.crop(box)
    cropped.save(path, quality=95)
    print(f"Guardado: {path} con tamaño {cropped.size}")

def main():
    im = Image.open("kit de marca.png")
    w, h = im.size # 1536 x 1024
    os.makedirs("assets", exist_ok=True)

    # 1. LOGO PRINCIPAL (Grande con personajes e insignia MOVIFY SENIOR)
    # Ubicado aprox en [25, 25] a [430, 440]
    crop_and_save(im, (30, 30, 430, 435), "assets/logo_main.png")

    # 1b. LOGO SÓLO TEXTO "MOVIFY SENIOR" CON MANCUERNA
    crop_and_save(im, (35, 300, 425, 430), "assets/logo_text.png")

    # 2. ÍCONOS DE APP
    # Icono principal con logo (con pareja): [460, 75, 635, 250]
    crop_and_save(im, (465, 75, 630, 240), "assets/app_icon_full.png")

    # Ícono simplificado cyan / verde: [650, 75, 780, 215]
    crop_and_save(im, (655, 80, 775, 210), "assets/app_icon_simple_cyan.png")

    # Ícono simplificado fondo blanco: [790, 75, 900, 215]
    crop_and_save(im, (795, 80, 895, 210), "assets/app_icon_simple_light.png")

    # Ícono simplificado oscuro: [905, 75, 1020, 215]
    crop_and_save(im, (905, 80, 1020, 210), "assets/app_icon_simple_dark.png")

    # 3. AVATARES CIRCULARES (Abuelita y Abuelito arriba a la derecha)
    # Abuelita sonriendo con moño: [1365, 35, 1485, 150]
    crop_and_save(im, (1365, 40, 1480, 150), "assets/avatar_abuelita.png")
    # Abuelito sonriendo con gafas: [1365, 150, 1485, 260]
    crop_and_save(im, (1365, 155, 1480, 260), "assets/avatar_abuelito.png")

    # 4. PERSONAJES COMPLETOS / ILUSTRACIONES
    # Abuelita con mancuerna morada de pie: [1060, 50, 1195, 305]
    crop_and_save(im, (1060, 55, 1190, 305), "assets/char_abuelita_stand.png")

    # Abuelito con mancuerna azul de pie: [1165, 40, 1320, 305]
    crop_and_save(im, (1170, 42, 1320, 305), "assets/char_abuelito_stand.png")

    # Abuelita sentada en loto / meditación: [1065, 305, 1185, 455]
    crop_and_save(im, (1070, 310, 1180, 455), "assets/char_abuelita_meditate.png")

    # Abuelito estirando brazos lateral: [1190, 295, 1300, 455]
    crop_and_save(im, (1195, 298, 1295, 455), "assets/char_abuelito_stretch.png")

    # Pareja caminando activa: [1310, 275, 1505, 455]
    crop_and_save(im, (1310, 275, 1500, 455), "assets/char_couple_walking.png")

    # 5. ICONOGRAFÍA (3 filas de 6 columnas)
    # El bloque de iconografía está aproximadamente en X de 30 a 445, Y de 475 a 745
    # Fila 1: Inicio, Ejercicio, Salud, Nutrición, Progreso, Perfil
    # Fila 2: Rutinas, Recordatorios, Logros, Ajustes, Ayuda, Salir
    # Fila 3: Play/Video, Música, Tiempo, Ubicación, Notificación, Favorito
    col_w = (445 - 30) / 6.0 # ~69.16
    
    icons = [
        # Fila 1 (Y ~490 to 565)
        ("icon_inicio", 0, 490, 565),
        ("icon_ejercicio", 1, 490, 565),
        ("icon_salud", 2, 490, 565),
        ("icon_nutricion", 3, 490, 565),
        ("icon_progreso", 4, 490, 565),
        ("icon_perfil", 5, 490, 565),
        
        # Fila 2 (Y ~580 to 655)
        ("icon_rutinas", 0, 580, 655),
        ("icon_recordatorios", 1, 580, 655),
        ("icon_logros", 2, 580, 655),
        ("icon_ajustes", 3, 580, 655),
        ("icon_ayuda", 4, 580, 655),
        ("icon_salir", 5, 580, 655),

        # Fila 3 (Y ~670 to 745)
        ("icon_play", 0, 670, 745),
        ("icon_musica", 1, 670, 745),
        ("icon_tiempo", 2, 670, 745),
        ("icon_ubicacion", 3, 670, 745),
        ("icon_notificacion", 4, 670, 745),
        ("icon_favorito", 5, 670, 745),
    ]

    for name, c_idx, y1, y2 in icons:
        x1 = int(30 + c_idx * col_w + 10)
        x2 = int(30 + (c_idx + 1) * col_w - 10)
        crop_and_save(im, (x1, y1, x2, y2), f"assets/{name}.png")

    # 6. ELEMENTOS GRÁFICOS: Corazón con pulso y hojas verdes
    crop_and_save(im, (935, 430, 1025, 510), "assets/badge_heart_pulse.png")
    crop_and_save(im, (795, 400, 930, 520), "assets/badge_leaves.png")
    
    # Mensaje de éxito 'Muy bien! Has completado tu rutina de hoy'
    crop_and_save(im, (460, 560, 765, 640), "assets/badge_success_routine.png")

    print("¡Todos los recortes se han completado con éxito!")

if __name__ == "__main__":
    main()
