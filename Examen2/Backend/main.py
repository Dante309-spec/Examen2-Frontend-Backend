from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# CREACIÓN DE LA API
app = FastAPI(
    title="API GameZone",
    description="Catálogo de videojuegos",
    version="1.0"
)

# CONFIGURACIÓN CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://127.0.0.1:5500",
        "http://localhost:5500"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# BASE DE DATOS
videojuegos = [

    {
        # DESCRIPCION DE LOS JUEGOS, ID, NOMBRE, GENERO, PLATAFORMA, PRECIO E IMAGEN
        "id": 1,
        "nombre": "Mario Kart World",
        "genero": "Fiesta / Carreras",
        "plataforma": "Nintendo Switch 2",
        "precio": "$1,699 MXN",
        "imagen": "imagenes/mario-kart-world.jpg.jpg",

        "tiendas": [

            {
                "nombre": "Amazon México",
                "precio": "$1,649 MXN",
                "calificacion": "★★★★★",
                "url": "https://www.amazon.com.mx/"
            },

            {
                "nombre": "Liverpool",
                "precio": "$1,699 MXN",
                "calificacion": "★★★★☆",
                "url": "https://www.liverpool.com.mx/"
            },

            {
                "nombre": "GamePlanet",
                "precio": "$1,699 MXN",
                "calificacion": "★★★★★",
                "url": "https://www.gameplanet.com/"
            },

            {
                "nombre": "Nintendo eShop",
                "precio": "$1,699 MXN",
                "calificacion": "★★★★★",
                "url": "https://www.nintendo.com/es-mx/store/"
            }

        ]

    },

    {
        "id": 2,
        "nombre": "Super Mario Bros. Wonder",
        "genero": "Acción / Plataformas",
        "plataforma": "Nintendo Switch",
        "precio": "$1,199 MXN",
        "imagen": "imagenes/super-mario-bros-wonder.jpg.webp",

        "tiendas": [

            {
                "nombre": "Amazon México",
                "precio": "$1,149 MXN",
                "calificacion": "★★★★★",
                "url": "https://www.amazon.com.mx/"
            },

            {
                "nombre": "Walmart",
                "precio": "$1,189 MXN",
                "calificacion": "★★★★☆",
                "url": "https://www.walmart.com.mx/"
            },

            {
                "nombre": "GamePlanet",
                "precio": "$1,199 MXN",
                "calificacion": "★★★★★",
                "url": "https://www.gameplanet.com/"
            },

            {
                "nombre": "Nintendo eShop",
                "precio": "$1,199 MXN",
                "calificacion": "★★★★★",
                "url": "https://www.nintendo.com/es-mx/store/"
            }

        ]

    },

    {
        "id": 3,
        "nombre": "Super Mario Party Jamboree",
        "genero": "Fiesta / Acción",
        "plataforma": "Nintendo Switch / Nintendo Switch 2",
        "precio": "$1,399 MXN",
        "imagen": "imagenes/super-mario-party-jamboree.jpg.jpg",

        "tiendas": [

            {
                "nombre": "Amazon México",
                "precio": "$1,349 MXN",
                "calificacion": "★★★★★",
                "url": "https://www.amazon.com.mx/"
            },

            {
                "nombre": "Liverpool",
                "precio": "$1,399 MXN",
                "calificacion": "★★★★☆",
                "url": "https://www.liverpool.com.mx/"
            },

            {
                "nombre": "GamePlanet",
                "precio": "$1,389 MXN",
                "calificacion": "★★★★★",
                "url": "https://www.gameplanet.com/"
            },

            {
                "nombre": "Nintendo eShop",
                "precio": "$1,399 MXN",
                "calificacion": "★★★★★",
                "url": "https://www.nintendo.com/es-mx/store/"
            }

        ]

    },

    {
        "id": 4,
        "nombre": "Super Mario Galaxy + Super Mario Galaxy 2",
        "genero": "Aventura / Acción",
        "plataforma": "Nintendo Switch 2",
        "precio": "$1,599 MXN",
        "imagen": "imagenes/super-mario-galaxy-super-mario-galaxy-2.jpg.webp",

        "tiendas": [

            {
                "nombre": "Amazon México",
                "precio": "$1,549 MXN",
                "calificacion": "★★★★★",
                "url": "https://www.amazon.com.mx/"
            },

            {
                "nombre": "Liverpool",
                "precio": "$1,599 MXN",
                "calificacion": "★★★★★",
                "url": "https://www.liverpool.com.mx/"
            },

            {
                "nombre": "Mercado Libre",
                "precio": "$1,529 MXN",
                "calificacion": "★★★★☆",
                "url": "https://www.mercadolibre.com.mx/"
            },

            {
                "nombre": "Nintendo eShop",
                "precio": "$1,599 MXN",
                "calificacion": "★★★★★",
                "url": "https://www.nintendo.com/es-mx/store/"
            }

        ]

    }

]

# RUTA PRINCIPAL
@app.get("/")
def inicio():

    return {
        "mensaje": "Bienvenido a la API de GameZone"
    }

# OBTENER TODOS LOS VIDEOJUEGOS
@app.get("/videojuegos")
def obtener_videojuegos():

    return videojuegos

# OBTENER VIDEOJUEGO POR ID
@app.get("/videojuegos/{id}")
def obtener_videojuego(id: int):

    for juego in videojuegos:

        if juego["id"] == id:
            return juego

    return {
        "mensaje": "Videojuego no encontrado"
    }