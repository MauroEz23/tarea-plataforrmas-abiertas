
// Direccion de la API
const url = "http://127.0.0.1:5000/estudiantes/api/v1/estudiantes";

// Consultar la API
fetch(url)
    .then(response => response.json())
    .then(data => {

        // Obtener la tabla
        const tabla = document.getElementById("tabla-estudiantes");

        // Recorrer la lista de estudiantes
        data.estudiantes.forEach(estudiante => {

            // Crear una nueva fila
            let fila = document.createElement("tr");

            // Agregar el nombre del estudiante
            fila.innerHTML = `<td>${estudiante}</td>`;

            // Agregar la fila a la tabla
            tabla.appendChild(fila);

        });

    })
    .catch(error => {
        console.log("Error al consultar la API:", error);
    });
