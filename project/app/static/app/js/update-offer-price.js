document.addEventListener('DOMContentLoaded', function() {
    const offerTypeSelect = document.getElementById('offer-type');
    const totalPriceDisplay = document.getElementById('total_price_display');
    const totalPriceDiv = document.getElementById('total_price');

    function updatePrices() {
        const selectedOption = offerTypeSelect.options[offerTypeSelect.selectedIndex];
        const standardPrice = parseFloat(document.getElementById('eventData').getAttribute('data-standard-price'));

        totalPriceDisplay.textContent = totalPrice.toFixed(2) + ' €';

        // Vérifier si le tarif est différent de 0 ou de None
        if (totalPrice !== 0 && !isNaN(totalPrice)) {
            // Afficher la div si le tarif est différent de 0 ou de None
            totalPriceDiv.style.display = 'block';
        } else {
            // Masquer la div si le tarif est égal à 0 ou à None
            totalPriceDiv.style.display = 'none';
        }
    }

    function calculateDiscountedPrice(price, discount) {
        return price * (1 - (discount / 100));
    }

    offerTypeSelect.addEventListener('change', updatePrices);
    updatePrices(); // Initial setup on page load
});
