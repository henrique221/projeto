
function initMap() {
    var catho = {lat: -23.502308, lng: -46.828120};
    var loja2 = {lat: -23.501225, lng: -46.831575};
    var loja3 = {lat: -23.495374, lng: -46.821759};
    var map = new google.maps.Map(document.getElementById('map'), {
        zoom: 15,
        center: catho
});
    var marker = new google.maps.Marker({
        position: catho,
        map: map,
        title: 'Catho',
        label: 'Catho',
        animation: google.maps.Animation.DROP,
});
 

    var marker2 = new google.maps.Marker({
        position: loja2,
        map: map,
        title: 'loja 2',
        label: 'loja 2',
        animation: google.maps.Animation.DROP,
});
    var marker3 = new google.maps.Marker({
        position: loja3,
        map: map,
        title: 'loja 3',
        label: 'loja 3',
        animation: google.maps.Animation.DROP,
    });
    
}

function toggleBounce() {
    if (marker.getAnimation() !== null) {
      marker.setAnimation(null);
    } else {
      marker.setAnimation(google.maps.Animation.BOUNCE);
    }
  }