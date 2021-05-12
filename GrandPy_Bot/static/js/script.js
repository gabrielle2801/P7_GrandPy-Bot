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
        spinner();

        if (response.error){
            document.getElementById('address_geocode').textContent = response.error;
            reset();
        }else{

            setTimeout(()=> {extract(response);},2500);
    }
    })
})

function spinner(){
     $('#btn-one').html('<span class="spinner-border spinner-border-sm mr-2" role="status" aria-hidden="true"></span>Loading...').attr('disabled', true);
}

function extract(response){
    let div = document.createElement('div');
    div.innerHtml = '<p>'+ form + '</p>';
    console.log(div);
    message_request();
    document.body.appendChild(div);
    let address =response['sentences']+response['formatted_address'];
    $('#address_geocode').html('<p class="message-grandpy">'+ address +'</p>');
    $('#extract_wiki').html('<p class="text-white bg-dark p-2 rounded">'+ response['extract'] +'</p>');
    initMap(response['lat'],response['lng']);
    document.getElementById('map').style.height = "400px";
    map = new google.maps.Map(document.getElementById('map'), {
    zoom: 15,
    center: new google.maps.LatLng(response['lat'], response['lng'])
    });
    var marker = new google.maps.Marker({position: {lat: response['lat'], lng: response['lng']},
    map: map});
    reset()
};


function reset(){
    $('#btn-one').html('Envoyer').attr('disabled', false);
    document.getElementById("user-text-form").reset();
};


function message_request(){

}
