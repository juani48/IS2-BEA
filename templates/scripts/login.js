function login(){
    var dni = document.getElementById("login-input-dni")
    var password = document.getElementById("login-inpunt-password")

    fetch(
        "/login",
        {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(
                {
                    dni: dni,
                    password: password
                }
            )
        }
    ).then(response => response.json())
}