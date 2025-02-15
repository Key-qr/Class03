// Referencias a los elementos del DOM
const formulario = document.getElementById("agregar-empleado");
const tablaEmpleados = document.getElementById("tabla-empleados");

// Lista de empleados (se manejará en memoria)
let empleados = [];

// Función para agregar un empleado
formulario.addEventListener("submit", function (e) {
  e.preventDefault(); // Evita recargar la página

  // Obtener valores del formulario
  const nombre = document.getElementById("nombre").value;
  const departamento = document.getElementById("departamento").value;
  const cargo = document.getElementById("cargo").value;
  const salario = document.getElementById("salario").value;

  // Crear un nuevo empleado
  const nuevoEmpleado = { nombre, departamento, cargo, salario };
  empleados.push(nuevoEmpleado);

  // Limpiar el formulario
  formulario.reset();

  // Actualizar la tabla
  mostrarEmpleados();
});

// Función para mostrar empleados en la tabla
function mostrarEmpleados() {
  tablaEmpleados.innerHTML = ""; // Limpiar tabla
  empleados.forEach((empleado, index) => {
    const fila = document.createElement("tr");
    fila.innerHTML = `
      <td>${empleado.nombre}</td>
      <td>${empleado.departamento}</td>
      <td>${empleado.cargo}</td>
      <td>${empleado.salario}</td>
    `;
    tablaEmpleados.appendChild(fila);
  });
}
