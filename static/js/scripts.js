document.addEventListener("DOMContentLoaded", function () {
    console.log("Horizon Dashboard Loaded!");

    // Animation pour l'apparition des liens
    const links = document.querySelectorAll(".link-item");
    links.forEach((link, index) => {
        setTimeout(() => {
            link.classList.add("visible");
        }, index * 100);
    });

    // Animation pour le formulaire d'ajout
    const form = document.querySelector("form");
    if (form) {
        form.addEventListener("submit", function () {
            alert("Lien ajouté avec succès !");
        });
    }
});
