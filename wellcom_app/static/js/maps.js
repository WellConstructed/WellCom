// Get all wells
var $wellData = {};

var map;
function initMap() {
    map = new google.maps.Map(document.getElementById('all_well_map'), {
      center: {lat: 36.9930780, lng: -79.9046890},
      zoom: 8,
      scrollwheel: false,
      styles: [
           {
             featureType: 'all',
             stylers: [
               { saturation: -70 }
             ]
           }
         ]
    });
}


$.ajax({
  type: 'GET',
  dataType: "json",
  url: '/api/well/',
  success: function(data, textStatus) {
    // Handle success
    $wellData = data.results;
    console.log($wellData);

      var infowindow = new google.maps.InfoWindow();

      // var image = new Image(100, 200);
      //   image.src = '../images/wellcom.png';
      //   console.log(image);

      var marker, i;

      for (i = 0; i < $wellData.length; i++) {

          marker = new google.maps.Marker({
              // position: new google.maps.LatLng($wellData[i].latitude, $wellData[i].longitude),
              position: new google.maps.LatLng(Number($wellData[i].latitude), Number($wellData[i].longitude)),
              map: map,
              icon: 'https://wellcom-staging.herokuapp.com/static/images/BlueSymbol.png',
          });
          google.maps.event.addListener(marker, 'click', (function(marker, i) {
              return function() {
              infowindow.setContent('<strong>' + $wellData[i].name + '</strong>'
                  + '<p> latitude:  ' + $wellData[i].latitude + '</p>' +
                    '<p> longitude:  ' + $wellData[i].longitude + '</p>');
              infowindow.open(map, marker);
    }
  })(marker, i));

      }

  },
  error: function(xhr, textStatus, errorThrown) {
    // Handle error
    console.log('Error getting the Well Data');
  }

});
