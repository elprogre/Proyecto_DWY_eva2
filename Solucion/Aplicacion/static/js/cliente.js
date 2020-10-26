class Cliente {
    rut;
    nombre;
    apellido;
    email;
    fechaNacimiento;
    usuario;
    contraseña;

    setRut(rut) { this.rut = rut; }
    setNombre(nombre) { this.nombre = nombre; }
    setApellido(apellido) { this.apellido = apellido; }
    setEmail(email) { this.email = email; }
    setFechaNacimiento(fechaNacimiento) { this.fechaNacimiento = fechaNacimiento; }
    setUsuario(usuario) { this.usuario = usuario; }
    setContraseña(contraseña) { this.contraseña = contraseña; }

    getRut() { return this.rut; }
    getNombre() { return this.nombre; }
    getApellido() { return this.apellido; }
    getEmail() { return this.email; }
    getFechaNacimiento() { return this.fechaNacimiento; }
    getUsuario() { return this.usuario; }
    getContraseña() { return this.contraseña; }

    /*Metodo imprimir*/
    imprimir() {
        return "Rut:" + this.rut + " Nombre:" + this.nombre + " Apellido" + this.apellido + " Email:" + this.email +
            " Nacimiento:" + this.fechaNacimiento + " Usuario:" + this.usuario + " Contraseña:" + this.contraseña;
    }
}