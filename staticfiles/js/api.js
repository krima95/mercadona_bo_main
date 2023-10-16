/* API */

document.addEventListener("DOMContentLoaded", function () {
    const apiList = document.getElementById("api-list");

    // Remplacez l'URL ci-dessous par l'URL de votre API
    const apiUrl = "https://127.0.0.1:8000/products";

    fetch(apiUrl)
        .then((response) => response.json())
        .then((data) => {
            data.forEach((item) => {
                const listItem = document.createElement("li");
                listItem.textContent = item.product_title;
                apiList.appendChild(listItem);
            });
        })
        .catch((error) => {
            console.error("Une erreur s'est produite : " + error);
        });
});
