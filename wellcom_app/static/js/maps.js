// Get all wells
var $wellData = {};

var map;
function initMap() {

$.ajax({
  type: 'GET',
  dataType: "json",
  url: '/api/well/',
  success: function(data, textStatus) {
    // Handle success
    $wellData = data.results;
    console.log($wellData);

    var  map = new google.maps.Map(document.getElementById('all_well_map'), {
        center: {lat: 36.9930780, lng: -79.9046890},
        zoom: 9,
        scrollwheel: false,
        mapTypeId: 'terrain',
        styles: [
             {
               featureType: 'all',
               stylers: [
                 { saturation: 100 }
               ]
             }
           ]
      });

      var bounds = new google.maps.LatLngBounds();
      var infowindow = new google.maps.InfoWindow();

      var image = {
            url: 'https://wellcom-staging.herokuapp.com/static/images/BlueSymbol.png',
            scaledSize: new google.maps.Size(45, 56),
          };


      var marker, i;

      for (i = 0; i < $wellData.length; i++) {

          marker = new google.maps.Marker({
              // position: new google.maps.LatLng($wellData[i].latitude, $wellData[i].longitude),
              position: new google.maps.LatLng(Number($wellData[i].latitude), Number($wellData[i].longitude)),
              map: map,
              icon: image,
          });

          bounds.extend(marker.position);

          google.maps.event.addListener(marker, 'click', (function(marker, i) {
              return function() {
              infowindow.setContent('<h4>' + $wellData[i].name + '</h4>'
                  + '<h5> latitude:  ' + $wellData[i].latitude + '</h5>' +
                    '<h5> longitude:  ' + $wellData[i].longitude + '</h5>');
              infowindow.open(map, marker);
    }
  })(marker, i));
    map.fitBounds(bounds);
      }

  },
  error: function(xhr, textStatus, errorThrown) {
    // Handle error
    console.log('Error getting the Well Data');
  }

});
}
