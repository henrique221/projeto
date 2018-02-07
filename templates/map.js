
function initMap() {
    var catho = {lat: -23.502308, lng: -46.828120};
    var loja2 = {lat: -23.501225, lng: -46.831575};
    var map = new google.maps.Map(document.getElementById('map'), {
        zoom: 15,
        center: catho
});
    var marker = new google.maps.Marker({
        position: catho, loja2,
        map: map
});
}
