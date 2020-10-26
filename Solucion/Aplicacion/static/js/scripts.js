var arregloC = new Array();
var indice = 0;

/*METODO OBSOLETOOOO*/
/*Funcion para guardar formulario en el local storage*/
function grabar() {
    var rut = document.getElementById("txtRut").value;
    var nombre = document.getElementById("txtNombre").value;
    var apellido = document.getElementById("txtApellido").value;
    var email = document.getElementById("txtEmail").value;
    var fechaNacimiento = document.getElementById("txtFecha").value;
    var usuario = document.getElementById("txtUsuario").value;
    var contraseña = document.getElementById("txtPass").value;
    cli = new Cliente();
    cli.setRut(rut);
    cli.setNombre(nombre);
    cli.setApellido(apellido);
    cli.setEmail(email);
    cli.setFechaNacimiento(fechaNacimiento);
    cli.setUsuario(usuario);
    cli.setContraseña(contraseña);
    arregloC[indice] = JSON.stringify(cli);
    indice++;
    localStorage.setItem("Registro Clientes", arregloC);
    alert("Cuenta Creada Exitosamente");
}

/*Funcion para validar el digito verificador*/
function validarRut() {
    var rut = document.getElementById("txtRut").value;
    if (rut.length != 10) {
        alert("Rut no tiene el largo necesario");
        return false;
    }
    var num = 3;
    var sum = 0;
    for (let index = 0; index < 8; index++) {
        var carac = rut.slice(index, index + 1);
        sum = sum + (carac * num);
        num = num - 1;
        if (num == 1) {
            num = 7;
        }
    }
    var resto = sum % 11;
    var dv = 11 - resto;
    if (dv > 9) {
        if (dv == 10) {
            dv = 'K';
        } else {
            dv = 0;
        }
    }
    var dv_usuario = rut.slice(-1).toUpperCase();
    if (dv != dv_usuario) {
        alert("Rut incorrecto")
        return false;
    } else {
        return true;
    }
}

/*Funcion para validad fecha*/
function validadFecha() {
    var fechaForm = document.getElementById("txtFecha").value;
    var fechaSistema = new Date();
    var ano = fechaForm.slice(0, 4);
    var mes = fechaForm.slice(5, 7);
    var dia = fechaForm.slice(8, 10);
    var fechaMia = new Date(ano, mes - 1, dia);
    if (fechaMia > fechaSistema) {
        alert("Fecha de nacimiento Incorrecto");
        return false;
    }
    return true;
}

/*Valida todos los input*/
function validarTodo() {
    var resp;
    resp = validarRut();
    if (resp == false) {
        return false;
    }
    resp = validadFecha();
    if (resp == false) {
        return false;
    }
    resp = validarNombre();
    if (resp == false) {
        return false;
    }
    resp = validarApellido();
    if (resp == false) {
        return false;
    }
    resp = validarUsuario();
    if (resp == false) {
        return false;
    }

    return true;
}

function validarNombre() {
    var nombre = document.getElementById("txtNombre").value;
    var nlargo = nombre.trim().length;
    if (nlargo >= 3 && nlargo <= 80) {
        return true;
    } else {
        return false;
    }

}

function validarApellido() {
    var apellido = document.getElementById("txtApellido").value;
    var alargo = apellido.trim().length;
    if (alargo >= 3 && alargo <= 80) {
        return true;
    } else {
        return false;
    }
}

function validarUsuario() {
    var usuario = document.getElementById("txtUsuario").value;
    var ulargo = usuario.trim().length;
    if (alargo >= 3 && alargo <= 80) {
        return true;
    } else {
        return false;
    }
}