# 💼 Portafolio - Cristian Aranda

[![Django](https://img.shields.io/badge/Django-5.2-092E20?style=for-the-badge&logo=django&logoColor=white)](https://www.djangoproject.com/)
[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white)](https://getbootstrap.com/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)](https://www.postgresql.org/)

Portafolio profesional desarrollado con Django que muestra mis proyectos, habilidades técnicas y experiencia como Full Stack Developer. Este proyecto fue creado como parte de mi transición profesional desde Trabajo Social hacia el desarrollo de software.

🌐 **[Ver Demo en Vivo](https://portafolio-cristian-aranda.onrender.com/)**

---

## 📋 Tabla de Contenidos

- [Características](#-características)
- [Tecnologías](#️-tecnologías)
- [Capturas de Pantalla](#-capturas-de-pantalla)
- [Uso](#-uso)
- [Funcionalidades Destacadas](#-funcionalidades-destacadas)
- [Deploy](#-deploy)
- [Contribuciones](#-contribuciones)
- [Contacto](#-contacto)
- [Licencia](#-licencia)

---

## ✨ Características

### 🎨 Diseño y UX
- ✅ Diseño moderno y responsivo (móvil, tablet, desktop)
- ✅ Tema oscuro profesional con gradientes personalizados
- ✅ Animaciones y transiciones suaves
- ✅ Tarjetas interactivas con efectos hover
- ✅ Modal de detalles de proyectos

### 🛠️ Funcionalidades
- ✅ **CRUD completo** de proyectos (Crear, Leer, Actualizar, Eliminar)
- ✅ **Sistema de autenticación** Django integrado
- ✅ **Gestión de habilidades** técnicas por categorías (Frontend, Backend, Database, Soft Skills)
- ✅ **Orden personalizado** de proyectos desde el admin
- ✅ **Consultas SQL personalizadas** para reportes
- ✅ **Botones condicionales** (Demo/GitHub según disponibilidad)
- ✅ **Panel de administración** personalizado

### 🔒 Seguridad
- ✅ Protección CSRF
- ✅ Rutas protegidas con `@login_required`
- ✅ Logout seguro con método POST
- ✅ Validación de formularios Django

---

## 🛠️ Tecnologías

### Backend
- **Django 5.2** - Framework web principal
- **Python 3.11+** - Lenguaje de programación
- **PostgreSQL** - Base de datos en producción
- **SQLite** - Base de datos en desarrollo
- **Pillow** - Procesamiento de imágenes

### Frontend
- **Bootstrap 5.3** - Framework CSS
- **Font Awesome 6** - Iconos
- **JavaScript Vanilla** - Interactividad
- **CSS3 Custom Properties** - Variables CSS para temas

### DevOps
- **Render** - Plataforma de deployment
- **WhiteNoise** - Servicio de archivos estáticos
- **Gunicorn** - Servidor WSGI
- **Git & GitHub** - Control de versiones

---

## 📖 Uso

### Panel de Administración

1. Ingresa al admin: `/admin/`
2. Autentícate con tu superusuario

**Gestionar Proyectos:**
- Crear nuevo proyecto con imagen, descripción, enlaces y tecnologías
- Editar proyectos existentes
- Cambiar el orden de visualización (campo `order`)
- Eliminar proyectos

**Gestionar Skills:**
- Agregar habilidades técnicas
- Elegir tipo: Frontend, Backend, Database, Soft Skill
- Opcionalmente agregar ícono FontAwesome o imagen

### Vista Pública

**Navegación:**
- **Inicio**: Presentación y habilidades técnicas
- **Proyectos**: Grid con todos los proyectos
- **Modal**: Click en un proyecto para ver detalles
- **Enlaces**: Botones Demo y GitHub (cuando disponibles)

**Funciones Admin (autenticado):**
- Botón flotante (+) para crear proyecto
- Botones editar/eliminar en cada tarjeta
- Ícono de logout en el footer

---

## 📁 Estructura del Proyecto

```
Portafolio/
├── portafolio/                 # Configuración del proyecto Django
│   ├── settings.py            # Configuraciones
│   ├── urls.py                # URLs principales
│   └── wsgi.py                # WSGI para deploy
├── recursos/                   # App principal
│   ├── models.py              # Modelos (Project, Skill)
│   ├── views.py               # Vistas y lógica
│   ├── urls.py                # URLs de la app
│   ├── forms.py               # Formularios Django
│   └── admin.py               # Configuración del admin
├── templates/                  # Templates HTML
│   ├── base.html              # Template base
│   ├── index.html             # Página principal
│   ├── navbar.html            # Barra de navegación
│   └── recursos/              # Templates de proyectos
│       ├── project_list.html
│       ├── project_form.html
│       └── project_confirm_delete.html
├── static/                     # Archivos estáticos
│   ├── css/
│   │   ├── main.css           # Estilos principales
│   │   ├── index.css          # Estilos de inicio
│   │   └── projects.css       # Estilos de proyectos
│   ├── js/
│   │   └── main.js            # JavaScript
│   └── images/                # Imágenes
├── media/                      # Archivos subidos
│   ├── projects/              # Imágenes de proyectos
│   └── skills/                # Imágenes de skills
├── requirements.txt            # Dependencias Python
├── .gitignore                 # Archivos ignorados por Git
└── README.md                  # Este archivo
```

---

## 🌟 Funcionalidades Destacadas

### 1. Sistema de Orden Personalizado
Los proyectos pueden ordenarse manualmente desde el admin:
- Campo `order` editable desde la lista
- Menor número = mayor prioridad
- Permite destacar proyectos importantes

### 2. Botones Condicionales
Los botones Demo y GitHub solo aparecen si hay URLs:
- Si ambos existen: se dividen 50/50
- Si solo uno existe: ocupa 100% del ancho
- Si ninguno existe: el footer no muestra botones

### 3. Consulta SQL Personalizada
Ruta `/proyectos/sql/` muestra:
- Consulta SQL ejecutada
- Tabla con resultados formateados
- Relación proyectos-skills mediante JOIN

### 4. Admin Mejorado
- Inline para gestionar imágenes de galería (preparado para carrusel futuro)
- Indicadores visuales (✓/✗) para Demo y GitHub
- Contador de imágenes por proyecto
- Campos agrupados por secciones

---

1. Conecta tu repositorio GitHub a Render
2. Crea un nuevo Web Service
3. Configura las variables de entorno
4. Render detectará automáticamente que es Django
5. Deploy automático en cada push a main

---

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Para cambios importantes:

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

---

## 📬 Contacto

**Cristian Aranda Borquez**

- 💼 LinkedIn: [linkedin.com/in/cristian-arandab](https://www.linkedin.com/in/cristian-arandab)
- 🐱 GitHub: [github.com/carandab](https://github.com/carandab)
- 🌐 Portafolio: [portafolio-cristian-aranda.onrender.com](https://portafolio-cristian-aranda.onrender.com/)

---

## 📄 Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para más detalles.

---

## 🎓 Sobre Mí

Soy Trabajador Social en transición hacia el desarrollo de software, con formación en Full Stack Python/Django a través del bootcamp de Talento Digital. Combino mi experiencia en el sector público y social con habilidades técnicas en desarrollo web, buscando crear soluciones tecnológicas con impacto social.

### 🎯 Objetivos Profesionales
- Desarrollo Full Stack con Python y Django
- Creación de aplicaciones web escalables
- Integración de tecnología con impacto social
- Aprendizaje continuo en nuevas tecnologías

---

## 🙏 Agradecimientos

- **Talento Digital** y **Skillnest** por el bootcamp Full Stack Python
- Comunidad de desarrolladores de Django, Python y programadores en general


---

<div align="center">

⭐ Si te gustó este proyecto, dale una estrella en GitHub ⭐


</div>