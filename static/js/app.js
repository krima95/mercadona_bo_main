// Message : notification timer
document.addEventListener("DOMContentLoaded", function() {
            "use strict";
            let message_timeout = document.getElementById("message-timer");
            setTimeout(function() {
                message_timeout.style.display = "none";
            }, 2000);
});

// Recherche
$(document).ready(function () {
    $("#search").on("input", function () {
        let searchTerm = $(this).val().toLowerCase();

        // Réinitialisez l'affichage de toutes les lignes
        $("#table tbody tr").show();

        // Parcourez chaque ligne du tableau et masquez celles qui ne correspondent pas au terme de recherche
        $("#table tbody tr").each(function () {
            let productTitle = $(this).find("td:eq(0)").text().toLowerCase();
            let description = $(this).find("td:eq(1)").text().toLowerCase();
            let price = $(this).find("td:eq(2)").text().toLowerCase();

            if (!productTitle.includes(searchTerm) && !description.includes(searchTerm) && !price.includes(searchTerm)) {
                $(this).hide();
            }
        });
    });
});






// Calendrier
 $(document).ready(function() {
        $("#id_start_date").datepicker({
            showAnim: "fadeIn", // Animation d'affichage
            dateFormat: "dd/mm/yy", // Format de date
            // Autres options personnalisées...
        });
         $("#id_end_date").datepicker({
            showAnim: "fadeIn", // Animation d'affichage
            dateFormat: "dd/mm/yy", // Format de date
            // Autres options personnalisées...
        });
    });

