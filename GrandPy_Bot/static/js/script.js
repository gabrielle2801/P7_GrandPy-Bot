let map;

function initMap()
    {
    map = new google.maps.Map(document.getElementById("map"),{
        center : { lat: 40.731, lng: -73.997 },
        zoom : 8,
        mapTypeId: google.maps.MapTypeId.ROADMAP
    });
    }
