document.addEventListener('DOMContentLoaded', function() {
    const offerTypeSelect = document.getElementById('offer-type');
    
    // Événements lors de la sélection d'une offre et au changement de la quantité d'enfants
    offerTypeSelect.addEventListener('change', updateFieldsBasedOnOffer);


    updateFieldsBasedOnOffer(); // Configuration initiale au chargement de la page
});