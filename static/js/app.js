// Message : notification timer

var message_timeout = document.getElementById("message-timer");
setTimeout(function ()
{

    message_timeout.style.display = "none";

}, 2000);


/* API */

document.addEventListener("DOMContentLoaded", function () {
    const apiList = document.getElementById("api-list");

    // Remplacez l'URL ci-dessous par l'URL de votre API
    const apiUrl = "https://exemple.com/api/data";

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
