function login() {
    // Obtener valores CORRECTOS con .value y corregir typo en "input"
    var dni = document.getElementById("usuario").value;
    var password = document.getElementById("password").value;

    fetch("/login", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(
            {
                dni: dni,
                password: password
            }
        )
    }).then(response => {
        if (!response.ok) {
            // Si hay error HTTP (ej: 401, 400), lanzar excepción
            return response.json().then(err => { throw err; });
        }
        return response.json();
    })
    .then(data => {
        // Guardar usuario en localStorage (opcional)
        //localStorage.setItem("user", JSON.stringify(data.user));
        // Redirigir
        window.location.href = "/panelUsuario.html";
    })
    .catch(error => {
        // Mostrar error al usuario
        alert("Error: " + error.error);
        console.error("Error:", error);
    });
}