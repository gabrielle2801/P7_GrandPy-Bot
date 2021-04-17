let adresse = document.getElementById('bouton');
adresse.addEventListener('click', getValue);
const regex = /[A-Z0-9][\w]*/gm;
var request = new XMLHttpRequest();
let map;

function getValue() {
    // Sélectionner l'élément input et récupérer sa valeur
    var input = document.getElementById("adress").value;
    const found = input.match(regex);
    if (found) {
        // Afficher la valeur
        alert(found);
    }
    else {
        alert("Invalide...Pas de lettres Majuscules")
    }
}

