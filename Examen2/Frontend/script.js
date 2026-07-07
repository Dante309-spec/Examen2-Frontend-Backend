/*GameZone*/
console.log("GameZone iniciado");

/*Variables globales*/
// Contenedor donde se mostrarán las tarjetas
const contenedor = document.getElementById("contenedor-juegos");

// Arreglo que almacenará los videojuegos obtenidos de la API
let videojuegos = [];

/*Obtener videojuegos desde la API*/
fetch("http://127.0.0.1:8000/videojuegos")

    .then(respuesta => respuesta.json())

    .then(datos => {

        videojuegos = datos;

        mostrarVideojuegos(videojuegos);

    })

    .catch(error => {

        console.error(error);

        contenedor.innerHTML = `

        <div class="col-12">

            <div class="alert alert-danger text-center">

                No fue posible conectar con la API.

            </div>

        </div>

        `;

    });

/*Mostrar videojuegos*/

function mostrarVideojuegos(lista) {

    contenedor.innerHTML = "";

    lista.forEach(juego => {

        contenedor.innerHTML += `

        <div class="col-lg-3 col-md-6 col-sm-6 col-12 mb-4">

            <div class="card shadow h-100">

                <img
                    src="${juego.imagen}"
                    class="card-img-top"
                    alt="${juego.nombre}">

                <div class="card-body d-flex flex-column">

                    <h5>${juego.nombre}</h5>

                    <p><strong>Género:</strong> ${juego.genero}</p>

                    <p><strong>Plataforma:</strong> ${juego.plataforma}</p>

                    <h4 class="text-success">${juego.precio}</h4>

                    <button
                        class="btn btn-primary mt-auto"
                        onclick="mostrarTiendas(${juego.id})">

                        Ver tiendas

                    </button>

                </div>

            </div>

        </div>

        `;

    });

}

function mostrarTiendas(id){

    const juego = videojuegos.find(j=>j.id===id);

    document.getElementById("tituloJuego").innerHTML = juego.nombre;

    let tarjetas = "";

    juego.tiendas.forEach(tienda=>{

        tarjetas += `

        <div class="col-12 mb-3">

            <div class="card border-primary">

                <div class="card-body">

                    <h5>

                        ${tienda.nombre}

                    </h5>

                    <p>

                        <strong>Precio:</strong>

                        <span class="text-success">

                            ${tienda.precio}

                        </span>

                    </p>

                    <p>

                        <strong>Calificación:</strong>

                        ${tienda.calificacion}

                    </p>

                    <a
                        href="${tienda.url}"
                        target="_blank"
                        class="btn btn-success">

                        Comprar ahora

                    </a>

                </div>

            </div>

        </div>

        `;

    });

    document.getElementById("listaTiendas").innerHTML = tarjetas;

    const modal = new bootstrap.Modal(
        document.getElementById("modalTiendas")
    );

    modal.show();

}