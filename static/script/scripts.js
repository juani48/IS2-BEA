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

// ✅ Al cargar la página, arma todo el header dinámico
document.addEventListener("DOMContentLoaded", () => {
  cargarHeaderUsuario();         // Muestra nombre o botón login
  configurarDropdownGestionar(); // Desplegable Gestionar si existe
  configurarDropdownCategorias(); // Desplegable Categorías
  mostrarBotonEmpleado();       // Agrega "Panel Empleado" si corresponde
});

// ✅ Carga la cuenta de usuario o login
function cargarHeaderUsuario() {
  const accountArea = document.getElementById("accountArea");
  if (!accountArea) return;

  fetch("/session/status")
    .then(res => res.json())
    .then(data => {
      if (data.authenticated) {
        localStorage.setItem("user", JSON.stringify(data));
        accountArea.innerHTML = `
          <div class="relative">
            <button onclick="toggleDropdown()"
              class="shrink-0 flex items-center gap-2 bg-gradient-to-r from-red-600 to-red-400 border border-white/30 shadow-md hover:shadow-lg text-white py-1.5 px-4 rounded-full transition-all duration-300 group">
              <i class="fas fa-user text-lg"></i>
              <span class="text-sm font-semibold tracking-wide">${data.name}</span>
            </button>
            <div id="userDropdown" class="hidden absolute right-0 mt-2 w-40 bg-white text-gray-700 rounded-lg shadow-lg z-50">
              <button onclick="window.location.href='/edit_profile.html'" class="block w-full text-left px-4 py-2 hover:bg-gray-100">Editar perfil</button>
              <button onclick="window.location.href='/historial'" class="block w-full text-left px-4 py-2 hover:bg-gray-100">Ver historial</button>
              <button onclick="logout()" class="block w-full text-left px-4 py-2 hover:bg-gray-100">Cerrar sesión</button>
            </div>
          </div>
        `;

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
    .catch(err => console.error("Error al cargar sesión:", err));
}

// ✅ Alternar menú del usuario
function toggleDropdown() {
  const dropdown = document.getElementById("userDropdown");
  if (dropdown) dropdown.classList.toggle("hidden");
}

// ✅ Cerrar sesión y limpiar almacenamiento
function logout() {
  localStorage.removeItem("user");
  sessionStorage.removeItem("user");
  fetch('/logout', { method: 'POST' }).then(() => {
    window.location.href = '/login.html';
  });
}

// ✅ Redirigir a home correcto según usuario
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

// ✅ Inyectar dropdown "Gestionar" solo para Admin
function mostrarDropdownGestionar() {
  const navList = document.querySelector("nav ul");
  if (!navList) return;

  const li = document.createElement("li");
  li.className = "relative";
  li.id = "dropdown-container";
  li.innerHTML = `
    <span id="dropdown-toggle" class="cursor-pointer text-white hover:underline inline-block">
      Gestionar <i class="fas fa-caret-down ml-1"></i>
    </span>
    <div id="dropdown-menu" class="hidden absolute left-0 mt-2 bg-white rounded-md shadow-lg w-64 z-50">
      <a href="register_machinery.html" class="block px-4 py-2 font-semibold !text-[#7f1d1d] hover:bg-red-100 hover:!text-red-900">➕ Dar de alta una maquinaria</a>
      <a href="register_categorie.html" class="block px-4 py-2 font-semibold !text-[#7f1d1d] hover:bg-red-100 hover:!text-red-900">➕ Dar de alta una categoría</a>
      <a href="register_employee.html" class="block px-4 py-2 font-semibold !text-[#7f1d1d] hover:bg-red-100 hover:!text-red-900">➕ Dar de alta un empleado</a>
      <a href="list_employee.html" class="block px-4 py-2 font-semibold !text-[#7f1d1d] hover:bg-red-100 hover:!text-red-900">📋 Ver lista de empleados</a>
    </div>
  `;
  navList.insertBefore(li, navList.children[3]);
}

// ✅ Comportamiento del desplegable "Gestionar"
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

// ✅ Agregar botón Panel Empleado solo si corresponde
function mostrarBotonEmpleado() {
  fetch("/session/status")
    .then((res) => res.json())
    .then((data) => {
      if (data.authenticated && (data.type === "Empleado" || data.type === "Admin")) {
        const nav = document.querySelector(".main-nav ul");
        if (nav) {
          const li = document.createElement("li");
          li.classList.add("relative");
          li.innerHTML = `
            <span id="empleadoDropdownToggle" class="cursor-pointer hover:underline text-yellow-300 font-semibold">
              👷 Panel Empleado <i class="fas fa-caret-down ml-1"></i>
            </span>
            <div id="empleadoDropdownMenu" class="hidden absolute bg-white shadow-lg rounded-md mt-2 z-50 min-w-[200px]">
              <a href="/pending_requests.html" class="block px-4 py-2 font-semibold !text-[#7f1d1d] hover:bg-red-100 hover:!text-red-900">📋 Listar Solicitudes</a>
              <a href="/list_reservation.html" class="block px-4 py-2 font-semibold !text-[#7f1d1d] hover:bg-red-100 hover:!text-red-900">📄 Listar Reservas</a>
            </div>
          `;
          nav.appendChild(li);

          const toggle = li.querySelector("#empleadoDropdownToggle");
          const menu = li.querySelector("#empleadoDropdownMenu");

          toggle.addEventListener("click", (e) => {
            e.stopPropagation();
            menu.classList.toggle("hidden");
          });

          document.addEventListener("click", (e) => {
            if (!li.contains(e.target)) menu.classList.add("hidden");
          });
        }
      }
    })
    .catch(err => console.error("Error al verificar tipo de usuario:", err));
}

// ✅ Configura desplegable de Categorías + fetch a backend
function configurarDropdownCategorias() {
  const toggle = document.getElementById("dropdown-categorias-toggle");
  const menu = document.getElementById("dropdown-categorias-menu");
  const container = document.getElementById("dropdown-categorias-container");

  if (toggle && menu && container) {
    toggle.addEventListener("click", (e) => {
      e.stopPropagation();
      menu.classList.toggle("hidden");
    });

    document.addEventListener("click", (e) => {
      if (!menu.contains(e.target) && !toggle.contains(e.target)) {
        menu.classList.add("hidden");
      }
    });

    // cargar categorías habilitadas
    fetch("/categories/enabled")
      .then(res => res.json())
      .then(categories => {
        menu.innerHTML = "";
        categories.forEach(cat => {
          const link = document.createElement("a");
          link.href = `/machinery.html?category=${encodeURIComponent(cat)}`;
          link.textContent = cat;
          link.className = "block px-4 py-2 font-semibold hover:bg-red-100 hover:text-red-900";
          link.style.color = "#7f1d1d";
          menu.appendChild(link);
        });
      })
      .catch(err => {
        console.error("Error al cargar categorías:", err);
      });
  }
}

function buscarMaquinaria() {
  const input = document.getElementById("searchInput").value.trim();
  if (input !== "") {
    const encoded = encodeURIComponent(input);
    window.location.href = `/machinery.html?search=${encoded}`;
  }
}
