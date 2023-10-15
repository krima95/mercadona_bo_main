// Message : notification timer
document.addEventListener("DOMContentLoaded", function() {
            "use strict";
            let message_timeout = document.getElementById("message-timer");
            setTimeout(function() {
                message_timeout.style.display = "none";
            }, 2000);
});

// Bouton afficher le filtre
 $(document).ready(function () {
        // Gérer le basculement de l'affichage du formulaire
        $("#filter-toggle").click(function () {
            $("#filter-form").toggle();
        });
});

// Calendrier
 $(document).ready(function() {
    $("#id_start_date").datepicker({
        showAnim: "fadeIn",
        dateFormat: "yy-mm-dd", // Utilisez le format "yyyy-MM-dd" ici
        // Autres options personnalisées...
    });

    $("#id_end_date").datepicker({
        showAnim: "fadeIn",
        dateFormat: "yy-mm-dd", // Utilisez le format "yyyy-MM-dd" ici
        // Autres options personnalisées...
    });
});

