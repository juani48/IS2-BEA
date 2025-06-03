/* 
 document.addEventListener("DOMContentLoaded", () => {
    const toggle = document.getElementById("dropdown-toggle");
    const menu = document.getElementById("dropdown-menu");
    const container = document.getElementById("dropdown-container");

    if (toggle && menu && container) {
      toggle.addEventListener("click", (e) => {
      e.stopPropagation(); // evita que el documento lo cierre enseguida
      menu.classList.toggle("hidden");
    });

    document.addEventListener("click", (e) => {
      if (!menu.contains(e.target) && !toggle.contains(e.target)) {
        menu.classList.add("hidden");
      }
});

    configurarDropdownCategorias();

    }
  });

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

    /*
    fetch("/categories/enabled")
  .then(res => res.json())
  .then(categories => {
    const menu = document.getElementById("dropdown-categorias-menu");
    menu.innerHTML = "";
    categories.forEach(cat => {
      const link = document.createElement("a");
      link.href = `/machinery.html?category=${encodeURIComponent(cat)}`; // ← IMPORTANTE
      link.textContent = cat;
      link.className = "block w-full px-4 py-2 font-semibold hover:bg-red-100 hover:text-red-900";
      link.style.color = "#7f1d1d";
      menu.appendChild(link);
    });
  });

  }
  
}
  function buscarMaquinaria() {
    const input = document.getElementById("searchInput")?.value.trim();
    if (input !== "") {
      const encoded = encodeURIComponent(input);
      window.location.href = `/machinery.html?search=${encoded}`;
    }
  }

 */