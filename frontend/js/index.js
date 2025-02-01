let darkLight = document.getElementById('light-dark');
let nav = document.querySelector("nav");
let footer = document.querySelector("footer");
let aTags = document.querySelectorAll("a");
let color = "white";

darkLight.addEventListener("click", function () {
    if (color === "white") {
        document.body.style.backgroundColor = "#292a2d";
        document.body.style.color = "white";
        footer.style.backgroundColor = "black";
        footer.style.color = "white";
        nav.style.color = "white";

        aTags.forEach(a => {
            a.style.color = "white";
        });

        color = "black";
    } else {
        document.body.style.backgroundColor = "#fbfbfb";
        document.body.style.color = "black";
        footer.style.backgroundColor = "white";
        footer.style.color = "black";
        nav.style.color = "black";

        aTags.forEach(a => {
            a.style.color = "black";
        });

        color = "white";
    }
});



let menuBtn = document.getElementById("menu-btn");
let sidebar = document.getElementById("sidebar");

menuBtn.addEventListener("click", function () {
    sidebar.classList.toggle("active");
});
