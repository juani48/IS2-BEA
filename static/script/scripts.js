 tailwind.config = {
            theme: {
                extend: {
                    colors: {
                        'bob-red': '#D10000',
                        'bob-dark-red': '#A30000',
                        'bob-light-red': '#FF3333',
                    }
                },
                fontFamily: {
                    'sans': ['Montserrat', 'sans-serif'],
                }
            }
        }
// static/script/scripts.js

// 👤 Carga el header con nombre de usuario o botón de login
function cargarHeaderUsuario() {
  const accountArea = document.getElementById("accountArea");
  if (!accountArea) return;

  fetch("/session/status")
    .then((res) => res.json())
    .then((data) => {
      if (data.authenticated) {
        accountArea.innerHTML = `
          <div class="relative">
            <button onclick="toggleDropdown()"
              class="shrink-0 flex items-center gap-2 bg-gradient-to-r from-red-600 to-red-400 border border-white/30 shadow-md hover:shadow-lg text-white py-1.5 px-4 rounded-full transition-all duration-300 group">
              <i class="fas fa-user text-lg"></i>
              <span class="text-sm font-semibold tracking-wide">${data.name}</span>
            </button>
            <div id="userDropdown" class="hidden absolute right-0 mt-2 w-40 bg-white text-gray-700 rounded-lg shadow-lg z-50">
              <button onclick="window.location.href='/editar_perfil'" class="block w-full text-left px-4 py-2 hover:bg-gray-100">Editar perfil</button>
              <button onclick="window.location.href='/historial'" class="block w-full text-left px-4 py-2 hover:bg-gray-100">Ver historial</button>
              <button onclick="logout()" class="block w-full text-left px-4 py-2 hover:bg-gray-100">Cerrar sesión</button>
            </div>
          </div>
        `;

        // Si es admin, mostrar menú Gestionar
        if (data.type === "Admin") mostrarDropdownGestionar();
      } else {
        accountArea.innerHTML = `
          <a href="login.html"
            class="shrink-0 flex items-center gap-2 cursor-pointer bg-gradient-to-r from-red-600 to-red-400 border border-white/30 shadow-md hover:shadow-lg text-white py-1.5 px-4 rounded-full transition-all duration-300 group">
            <i class="fas fa-user text-lg group-hover:hidden"></i>
            <i class="fas fa-user-circle text-lg hidden group-hover:inline"></i>
            <span class="hidden sm:inline text-sm font-semibold tracking-wide">Iniciar sesión</span>
          </a>
        `;
      }
    })
    .catch((err) => console.error("Error al cargar sesión:", err));
}

// 👤 Alterna el menú del usuario
function toggleDropdown() {
  const dropdown = document.getElementById("userDropdown");
  if (dropdown) dropdown.classList.toggle("hidden");
}

// 🔚 Cierra sesión
function logout() {
        // Eliminar datos de usuario del almacenamiento
        localStorage.removeItem('user');
        sessionStorage.removeItem('user');
        
        // Opcional: hacer logout también en el servidor
        fetch('/logout', { method: 'POST' })
            .then(() => {
                window.location.href = '/login.html';
            });
    }

// 🏠 Redirige a home según tipo de usuario
function goHome() {
  fetch("/session/status")
    .then((res) => res.json())
    .then((data) => {
      if (data.authenticated) {
        switch (data.type) {
          case "Cliente":
            window.location.href = "/panelUsuario.html";
            break;
          case "Empleado":
            window.location.href = "/panelEmpleado.html";
            break;
          case "Admin":
            window.location.href = "/panelAdmin.html";
            break;
          default:
            window.location.href = "/main.html";
        }
      } else {
        window.location.href = "/main.html";
      }
    })
    .catch((err) => {
      console.error("Error al verificar sesión:", err);
      window.location.href = "/main.html";
    });
}

// 🧩 Inyecta el dropdown Gestionar si corresponde (solo Admin)
function mostrarDropdownGestionar() {
  const navList = document.querySelector("nav ul");
  if (!navList) return;

  const gestionar = document.createElement("li");
  gestionar.className = "relative";
  gestionar.id = "dropdown-container";
  gestionar.innerHTML = `
    <span id="dropdown-toggle" class="cursor-pointer text-white hover:underline inline-block">
      Gestionar <i class="fas fa-caret-down ml-1"></i>
    </span>
    <div id="dropdown-menu" class="hidden absolute left-0 mt-2 bg-white rounded-md shadow-lg w-64 z-50" style="color: #7f1d1d;">
      <a href="register_machinery.html" class="block px-4 py-2 font-semibold hover:bg-red-100 hover:text-red-900" style="color: #7f1d1d !important;">
        ➕ Dar de alta una maquinaria
      </a>
      <a href="register_categorie.html" class="block px-4 py-2 font-semibold hover:bg-red-100 hover:text-red-900" style="color: #7f1d1d !important;">
        ➕ Dar de alta una categoría
      </a>
    </div>
  `;
  navList.insertBefore(gestionar, navList.children[2]); // lo ponemos antes de Preguntas Frecuentes
}

// 📌 Configura comportamiento del dropdown Gestionar
function configurarDropdownGestionar() {
  document.addEventListener("click", (e) => {
    const toggle = document.getElementById("dropdown-toggle");
    const menu = document.getElementById("dropdown-menu");
    if (toggle && menu) {
      if (toggle.contains(e.target)) {
        menu.classList.toggle("hidden");
      } else if (!menu.contains(e.target)) {
        menu.classList.add("hidden");
      }
    }
  });
}
