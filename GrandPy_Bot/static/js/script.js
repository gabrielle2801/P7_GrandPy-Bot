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
    .catch(error => console.log(error))
}

form.addEventListener("submit", function(event){
    event.preventDefault();

    spinner()
    postFormData("/post_address", new FormData(form))
    .then(response => {
        console.log(response);
        spinner();
        if (response.error){
            let newDiv=document.createElement('div');
            newDiv.textContent=response.error;
            newDiv.setAttribute('class','message-error');
            document.querySelector('.question-adress').append(newDiv);
            reset();
        } else{
            setTimeout(()=> {extract(response);},1000);
        }
    })
})

function spinner(){
     $('#btn-one').html('<span class="spinner-border spinner-border-sm mr-2" role="status" aria-hidden="true"></span>Loading...').attr('disabled', true);
}

function extract(response){

    message_request();
    let address =response['sentences']+response['formatted_address'];
    response_address(address);
    createMap(response['lat'],response['lng']);
    let wiki =response['sentences_wiki']+response['extract'];
    response_wiki(wiki);
    console.log(response['sentences_wiki']);
    reset()
};


function reset(){
    $('#btn-one').html('Envoyer').attr('disabled', false);
    document.getElementById("user-text-form").reset();
};


function message_request(){
    console.log(document.getElementById("userText").value);
    let newDiv=document.createElement('div');
    newDiv.textContent=document.getElementById("userText").value;
    newDiv.setAttribute('class','quest-adress');
    document.querySelector('.question-adress').append(newDiv);
}

function response_address(address){
    let newDiv=document.createElement('div');
    newDiv.textContent=address;
    newDiv.setAttribute('class','message-grandpy');
    document.querySelector('.question-adress').append(newDiv);
}

function response_wiki(wiki){
    let newDiv=document.createElement('div');
    newDiv.textContent=wiki;
    newDiv.setAttribute('class','message-grandpy');
    document.querySelector('.question-adress').append(newDiv);
}

function createMap(lat,lng){
    try{
        let newDiv=document.createElement('div');
        newDiv.setAttribute('class','map');
        document.querySelector('.question-adress').append(newDiv);
        initMap(lat,lng);
        map = new google.maps.Map(newDiv, {
        zoom: 15,
        center: new google.maps.LatLng(lat, lng)
        });
        var marker = new google.maps.Marker({position: {lat: lat, lng: lng},
        map: map});
    } catch (error){
        let newDiv = document.createElement('div');
        newDiv.textContent='carte manquante';
        document.querySelector('.question-adress').append(newDiv)
    }

}


