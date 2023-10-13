// Message : notification timer
document.addEventListener("DOMContentLoaded", function() {
            "use strict";
            let message_timeout = document.getElementById("message-timer");
            setTimeout(function() {
                message_timeout.style.display = "none";
            }, 2000);
        });

// Recherche
 $(document).ready(function(){
    $("#search").on("keyup", function(){
        let value = $(this).val().toLowerCase();
        $("#table td").filter(function(){
            $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1);
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

// calculer la promotion
function calculateSalePrice() {
    let price = parseFloat("{{ product.price }}");
    let discountPercentage = parseFloat(document.getElementById("id_discount_percentage").value);
    let newPrice = price - (price * (discountPercentage / 100));
    document.getElementById("id_new_price").textContent = newPrice.toFixed(2);
}

document.getElementById("id_discount_percentage").addEventListener("input", calculateSalePrice);

// Calculate the initial sale price if the discount percentage is pre-filled
calculateSalePrice();
