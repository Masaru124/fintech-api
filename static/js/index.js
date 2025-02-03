let menuBtn = document.getElementById("menu-btn");
let sidebar = document.getElementById("sidebar");

menuBtn.addEventListener("click", function () {
    sidebar.classList.toggle("active");
});
