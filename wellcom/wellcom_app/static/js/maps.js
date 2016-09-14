var map;
function initMap() {
    map = new google.maps.Map(document.getElementById('all_well_map'), {
      center: {lat: -34.397, lng: 150.644},
      zoom: 8
    });
  }
// new google.maps.event.addDomListener(window, "load", initMap);
