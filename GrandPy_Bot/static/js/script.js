let form = document.querySelector("#user-text-form");
let geocoder;
let map ;

function initMap(lat,lng){
    geocoder = new google.maps.Geocoder();
    var latlng = new google.maps.LatLng(lat, lng);

  }
function postFormData(url, data){
    return fetch(url,{
        method: "POST",
        body: data,

    })
    .then(response => response.json())
    .catch(error => console.log(error));

}

form.addEventListener("submit", function(event){
    event.preventDefault();
    postFormData("/post_address", new FormData(form))
    .then(response => {
        console.log(response);
        if (response.error){
            document.getElementById('address_geocode').textContent = response.error;
        }else{
        let address =response['sentences']+response['formatted_address'];
        document.getElementById('address_geocode').textContent = response['formatted_address'];
        document.getElementById('address_geocode').textContent=address;
        document.getElementById('extract_wiki').textContent = response['extract'];
        initMap(response['lat'],response['lng']);
        map = new google.maps.Map(document.getElementById('map'), {
      zoom: 15,
      center: new google.maps.LatLng(response['lat'], response['lng'])
    });
        var marker = new google.maps.Marker({position: {lat: response['lat'], lng: response['lng']},
    map: map});
        var newDiv = document.createElement("div")
        newDiv.textContent='Hi there and greetings!';
        var currentDiv = document.getElementById('extract_wiki');
        currentDiv.appendChild(newDiv);
    }
    })

})


