# Portal-Web-CADUTPL


config
├── __init__.py
├── __pycache__
├── asgi.py
├── settings.py
├── urls.py
└── wsgi.py
core
├── __init__.py
├── __pycache__
├── admin.py
├── apps.py
├── migrations
├── models.py
├── static
│   └── core
│       ├── css
│       │   └── custom.css
│       └── img
│           ├── logo_CAD.png
│           └── team
│               ├── team-1.jpg
│               ├── team-2.jpg
│               ├── team-3.jpg
│               └── team-4.jpg
├── templates
│   └── core
│       ├── ahorros.html
│       ├── base.html
│       ├── creditos.html
│       ├── index.html
│       ├── login_entrada.html
│       ├── nosotros.html
│       ├── noticias.html
│       └── servicios.html
├── tests.py
├── urls.py
└── views.py
static
├── css
│   ├── argon-design-system.css
│   ├── argon-design-system.css.map
│   ├── argon-design-system.min.css
│   ├── font-awesome.css
│   ├── nucleo-icons.css
│   └── nucleo-svg.css
├── fonts
│   ├── FontAwesome.otf
│   ├── fontawesome-webfont.eot
│   ├── fontawesome-webfont.svg
│   ├── fontawesome-webfont.ttf
│   ├── fontawesome-webfont.woff
│   ├── fontawesome-webfont.woff2
│   ├── nucleo-icons.eot
│   ├── nucleo-icons.svg
│   ├── nucleo-icons.ttf
│   ├── nucleo-icons.woff
│   └── nucleo-icons.woff2
└── js
    ├── argon-design-system.js
    ├── argon-design-system.js.map
    ├── argon-design-system.min.js
    ├── core
    │   ├── bootstrap.min.js
    │   ├── jquery.min.js
    │   └── popper.min.js
    └── plugins
        ├── bootstrap-datepicker.min.js
        ├── bootstrap-switch.js
        ├── chartjs.min.js
        ├── datetimepicker.js
        ├── jquery.sharrre.min.js
        ├── moment.min.js
        ├── nouislider.min.js
        └── perfect-scrollbar.jquery.min.js
users
├── __init__.py
├── __pycache__
├── admin.py
├── apps.py
├── migrations
├── models.py
├── static
│   └── users
│       ├── css
│       │   └── login_styles.css
│       ├── img
│       └── js
├── templates
│   └── users
│       ├── change_password.html
│       ├── login.html
│       ├── password_reset_confirm.html
│       └── password_verify_code.html
├── tests.py
├── urls.py
└── views.py
socio
├── __init__.py
├── __pycache__
├── admin.py
├── apps.py
├── migrations
├── models.py
├── templates
│   └── socio
│       └── hazte_socio.html
├── tests.py
├── urls.py
└── views.py
dashboard
├── admin.py
├── apps.py
├── migrations
├── models.py
├── templates
│   └── dashboard
│       ├── admin
│       │   └── dashboardAdmin.html
│       └── socio
│           └── dashboardSocio.html
├── tests.py
├── urls.py
└── views.py