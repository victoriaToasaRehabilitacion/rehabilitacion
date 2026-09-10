# Movify Senior 🌟
> Plataforma web de rehabilitación, movilidad y bienestar para personas adultas mayores y profesionales de salud.

---

## 🚀 Despliegue en Netlify (2 Métodos Rápidos)

### Opción 1: Arrastrar y Soltar (Sin código ni terminal)
1. Inicia sesión en [app.netlify.com](https://app.netlify.com).
2. Ve a la sección **"Sites"** (Sitios).
3. Arrastra y suelta la carpeta entera **`Movify_Senior_web`** en el recuadro que dice **"Drag & drop your site output folder here"**.
4. ¡Listo! En menos de 10 segundos Netlify te otorgará una URL pública (ejemplo: `https://movify-senior-ec.netlify.app`).

### Opción 2: Conectar con GitHub / GitLab / Bitbucket
1. Sube este repositorio a GitHub.
2. En Netlify, pulsa **"Add new site"** > **"Import an existing project"**.
3. Selecciona tu repositorio.
4. Parámetros de configuración:
   - **Build command**: *(dejar en blanco o vacío)*
   - **Publish directory**: `.` *(o la raíz)*
5. Pulsa **"Deploy site"**. El archivo `netlify.toml` incluido aplicará automáticamente las reglas de seguridad, redirecciones y caché de alto rendimiento.

---

## 📱 Características Principales

- **Diseñado para Adultos Mayores**:
  - Contraste visual accesible y paleta cromática corporativa.
  - Tipografía clara (Google Fonts Outfit y Plus Jakarta Sans).
  - Botones táctiles de gran tamaño (>48px) para fácil pulsación.
- **Asistencia Activa durante Ejercicios**:
  - Guía por voz sintética natural en español (Web Speech API).
  - Sonidos tonales de confirmación en cada repetición.
  - Botón de seguridad ante fatiga o dolor agudo.
- **Portal de Paciente**:
  - Rutinas paso a paso: Calentamiento, Equilibrio, Movilidad y Fuerza.
  - Contador de racha y medallas motivacionales.
  - Agenda de citas médicas y recordatorios de medicación.
  - Botón de emergencia SOS con notificación inmediata a familiar.
- **Portal de Fisioterapeuta / Médico**:
  - Vista de monitoreo de adherencia, alertas de dolor y prescripción adaptada.
- **PWA Ready**:
  - Archivo `manifest.json` configurado para poder instalarse como App en el teléfono o tablet sin necesidad de pasar por tiendas de aplicaciones.
