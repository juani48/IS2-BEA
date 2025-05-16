function singin(){
    var dni = document.getElementById("singin-input-dni")
    var password = document.getElementById("singin-inpunt-password")
    var email = document.getElementById("singin-inpunt-email")
    var name = document.getElementById("singin-inpunt-name")
    var lastname = document.getElementById("singin-inpunt-lastname")
    var employee_number = 0

    fetch(
        "/singin",
        {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(
                {
                    dni: dni,
                    password: password,
                    email: email,
                    name: name,
                    lastname: lastname,
                    employee_number: employee_number
                }
            )
        }
    ).then(response => response.json())
}