// rent_form.js
function actualizarInfoVehiculo() {
    var select = document.getElementById("id_tipo_vehiculo"); // Ajusta el ID según tu formulario
    var imagenPreview = document.getElementById("imagen-preview");
    var precioSpan = document.getElementById("precio");
  
    // Obtén la opción seleccionada
    var selectedOption = select.options[select.selectedIndex];
  
    // Actualiza la imagen y el precio en el formulario
    imagenPreview.src = selectedOption.getAttribute("data-imagen");
    precioSpan.textContent = selectedOption.getAttribute("data-precio");
  }
  
  // Llama a la función una vez para mostrar la información inicial si hay un tipo de vehículo seleccionado
  actualizarInfoVehiculo();
  