let machines = [];
let currentPage = 1;
const cardsPerPage = 9;
const params = new URLSearchParams(window.location.search);
const categoryFromURL = params.get("category") || "";

let userType = "Cliente"; // por defecto


document.addEventListener("DOMContentLoaded", () => {
  cargarCategoriasSelect();

  fetch("/session/status")
    .then(res => res.json())
    .then(data => {
      if (data.authenticated && data.type) {
        userType = data.type;
      }
      document.getElementById("filter-apply")?.addEventListener("click", fetchMachinesWithFilters);
      fetchMachinesWithFilters();
    })
    .catch(err => {
      console.error("Error al obtener tipo de usuario:", err);
      document.getElementById("filter-apply")?.addEventListener("click", fetchMachinesWithFilters);
      fetchMachinesWithFilters();
    });
});


function getFilters() {
  return {
    mark: document.getElementById("filter-mark")?.value || "",
    model: document.getElementById("filter-model")?.value || "",
    price: parseFloat(document.getElementById("filter-price")?.value) || 0,
    categorie: document.getElementById("filter-categorie")?.value || categoryFromURL,
  };
}

function fetchMachinesWithFilters() {
  const filters = getFilters();
  const params = new URLSearchParams(window.location.search);
  const search = params.get("search") || "";

  const endpoint = userType === "Admin"
    ? "/machine/get_all_filter_admin"
    : "/machine/get_all_filter";

  fetch(endpoint, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      categorie: { apply: filters.categorie !== "", categorie: filters.categorie },
      string: { apply: search !== "", string: search },
      price: { apply: filters.price > 0, price: filters.price },
      mark: { apply: filters.mark !== "", mark: filters.mark },
      model: { apply: filters.model !== "", model: filters.model }
    }),
  })
    .then((res) => res.json())
    .then((data) => {
      if (!Array.isArray(data)) throw new Error("Respuesta no válida");
      machines = data;
      currentPage = 1;

      const noMachinesText = document.getElementById("no-machines");
      if (machines.length === 0) {
        document.getElementById("machine-list").innerHTML = "";
        noMachinesText.classList.remove("hidden");
        document.getElementById("pagination").innerHTML = "";
      } else {
        noMachinesText.classList.add("hidden");
        renderPage(currentPage);
        renderPagination();
      }
    })
    .catch((err) => {
      console.error("Error al cargar máquinas:", err);
    });
}


function renderPage(page) {
  const container = document.getElementById("machine-list");
  container.innerHTML = "";

  const start = (page - 1) * cardsPerPage;
  const end = start + cardsPerPage;
  const items = machines.slice(start, end);

  items.forEach((machine) => {
    const basePath = `/static/image/machines/`;
    const jsonPath = `${basePath}${machine.patent}.json`;
    const fallbackImg = `${basePath}${machine.patent}.jpg`;
    const defaultImg = `${basePath}default.png`;

    fetch(jsonPath)
      .then((res) => {
        if (!res.ok) throw new Error("No JSON");
        return res.json();
      })
      .then((lista) => {
        const img = lista?.[0] ? `${basePath}${lista[0]}` : fallbackImg;
        renderMachine(machine, img);
      })
      .catch(() => {
        const testImage = new Image();
        testImage.src = fallbackImg;
        testImage.onload = () => renderMachine(machine, fallbackImg);
        testImage.onerror = () => renderMachine(machine, defaultImg);
      });
  });
}

function renderMachine(machine, imageSrc) {
  const container = document.getElementById("machine-list");
  const card = document.createElement("div");

  card.innerHTML = `
    <a href="/description_machinery.html?machine_id=${machine.patent}" 
       class="block w-full max-w-[320px] aspect-auto bg-white rounded-2xl shadow-lg overflow-hidden mx-auto my-4 hover:shadow-xl transition duration-300 group relative">
      <div class="w-full aspect-square overflow-hidden">
        <img src="${imageSrc}" onerror="this.src='/static/image/machines/default.png'"
             alt="Imagen de ${machine.model}"
             class="w-full h-full object-cover group-hover:scale-105 transition duration-300" />
      </div>
      <div class="p-4 text-center">
        <h2 class="text-lg font-bold text-gray-800">${machine.mark} ${machine.model}</h2>
        <p class="text-sm text-gray-600 mt-1">Ubicación: ${machine.ubication}</p>
        <p class="text-red-600 font-semibold mt-2">$${machine.price_day} / día</p>
        <button class="mt-4 inline-block bg-red-600 hover:bg-red-700 text-white font-bold py-2 px-4 rounded transition"
                onclick="irAReserva(event, '${machine.patent}')">
          Reservar
        </button>
        ${userType === "Admin" && machine.disable ? `<p class="mt-2 text-sm text-red-600 font-semibold">Maquinaria deshabilitada</p>` : ""}

      </div>
    </a>`;
  container.appendChild(card.firstElementChild);
}

function renderPagination() {
  const pagination = document.getElementById("pagination");
  const totalPages = Math.ceil(machines.length / cardsPerPage);
  pagination.innerHTML = "";

  const prev = document.createElement("button");
  prev.textContent = "‹ Anterior";
  prev.disabled = currentPage === 1;
  prev.className =
    "px-3 py-1 bg-white text-gray-700 border rounded hover:bg-gray-200 disabled:opacity-50";
  prev.onclick = () => {
    if (currentPage > 1) {
      currentPage--;
      renderPage(currentPage);
      renderPagination();
    }
  };
  pagination.appendChild(prev);

  for (let i = 1; i <= totalPages; i++) {
    const btn = document.createElement("button");
    btn.textContent = i;
    btn.className =
      "px-3 py-1 rounded border " +
      (i === currentPage
        ? "bg-red-600 text-white"
        : "bg-white text-gray-700 hover:bg-gray-200");
    btn.onclick = () => {
      currentPage = i;
      renderPage(currentPage);
      renderPagination();
    };
    pagination.appendChild(btn);
  }

  const next = document.createElement("button");
  next.textContent = "Siguiente ›";
  next.disabled = currentPage === totalPages;
  next.className =
    "px-3 py-1 bg-white text-gray-700 border rounded hover:bg-gray-200 disabled:opacity-50";
  next.onclick = () => {
    if (currentPage < totalPages) {
      currentPage++;
      renderPage(currentPage);
      renderPagination();
    }
  };
  pagination.appendChild(next);
}

function irAReserva(event, patent) {
  event.preventDefault();
  event.stopPropagation();
  window.location.href = `/reserve.html?machine_id=${patent}`;
}

function cargarCategoriasSelect() {
  fetch("/categories/enabled")
    .then((res) => {
      if (!res.ok) throw new Error("Error al obtener categorías");
      return res.json();
    })
    .then((data) => {
      const categories = Array.isArray(data.categories) ? data.categories : data; // ✅ corrección
      const select = document.getElementById("filter-categorie");
      if (!select) {
        console.error(" No se encontró #filter-categorie en el DOM");
        return;
      }
      select.innerHTML = `<option value="">-- Todas --</option>`;
      if (Array.isArray(categories)) {
        categories.forEach((name) => {
          const opt = document.createElement("option");
          opt.value = name;
          opt.textContent = name;
          if (name === categoryFromURL) {
            opt.selected = true;
          }
          select.appendChild(opt);
        });
      }
    })
    .catch((err) => {
      console.error("Error al cargar categorías:", err);
    });
}
