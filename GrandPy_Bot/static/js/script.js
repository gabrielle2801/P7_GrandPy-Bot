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
    spinner()
    postFormData("/post_address", new FormData(form))
    .then(response => {
        console.log(response);
        spinner()

        if (response.error){
            document.getElementById('address_geocode').textContent = response.error;
        }else{

            setTimeout(()=> {extract(response);},2500);


        /*var newDiv = document.createElement("div");
        newDiv.textContent='Hi there and greetings!';
        var currentDiv = document.getElementById('extract_wiki');
        currentDiv.appendChild(newDiv);
        document.getElementById("userText").value="";*/

    }
    })
})

function spinner(){
     $('#btn-one').html('<span class="spinner-border spinner-border-sm mr-2" role="status" aria-hidden="true"></span>Loading...').attr('disabled', true);
}

function extract(response){
    console.log('essai loading...')
    let address =response['sentences']+response['formatted_address'];
    document.getElementById('address_geocode').textContent = response['formatted_address'];
    document.getElementById('address_geocode').textContent=address;
    document.getElementById('extract_wiki').textContent = response['extract'];
    initMap(response['lat'],response['lng']);
    document.getElementById('map').style.height = "400px";
    map = new google.maps.Map(document.getElementById('map'), {
    zoom: 15,
    center: new google.maps.LatLng(response['lat'], response['lng'])
    });
    var marker = new google.maps.Marker({position: {lat: response['lat'], lng: response['lng']},
    map: map});
    $('#btn-one').html('Envoyer ...').attr('disabled', false);
    document.getElementById("user-text-form").reset();

}
