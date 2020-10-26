class Producto {
    nombre;
    precio;
    descripcion;

    setNombre(nombre) { this.nombre = nombre; }
    setPrecio(precio) { this.precio = precio; }
    setDescripcion(descripcion) { this.descripcion = descripcion; }

    getNombre() { return this.nombre; }
    getPrecio() { return this.precio; }
    getDescripcion() { return this.descripcion; }
}

var arregloP = new Array();
var indice = 0;

/*Funcion para guardar producto en el local storage*/
function grabarProducto() {
    var nombre = document.getElementById("txtNombre").value;
    var precio = document.getElementById("txtPrecio").value;
    var descripcion = document.getElementById("txtDescripcion").value;
    pro = new Producto();
    pro.setNombre(nombre);
    pro.setPrecio(precio);
    pro.setDescripcion(descripcion);
    arregloP[indice] = JSON.stringify(pro);
    indice++;
    localStorage.setItem("Registro Producto", arregloP);
    alert("Producto Guardo Exitosamente");
}