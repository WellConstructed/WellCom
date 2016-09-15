// Get all wells
var $wellData = {};

var map;
function initMap() {
    map = new google.maps.Map(document.getElementById('all_well_map'), {
      center: {lat: 36.9930780, lng: -79.9046890},
      zoom: 8
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



      var marker, i;
      for (i = 0; i < $wellData.length; i++) {
          console.log('lat');
          console.log(Number($wellData[i].latitude));
          console.log('long');
          console.log(Number($wellData[i].longitude));
          marker = new google.maps.Marker({
              // position: new google.maps.LatLng($wellData[i].latitude, $wellData[i].longitude),
              position: new google.maps.LatLng(Number($wellData[i].latitude), Number($wellData[i].longitude)),
              map: map
          });

          infowindow = new google.maps.InfoWindow({
               content: '<div id="content">' + '<strong>' + $wellData.name + '</strong>'
            });


      }

      google.maps.event.addListener(marker, 'click', function() {
          content: infowindow;
          infowindow.open(map, marker);
        });
      //
      // marker.addListener('click', function() {
      //   infowindow.open(map, marker);
      // });


  },
  error: function(xhr, textStatus, errorThrown) {
    // Handle error
    console.log('Error getting the Well Data');
  }
});


// var infowindow = new google.maps.InfoWindow();


// new google.maps.event.addDomListener(window, "load", initMap);
console.log('length');
console.log($wellData.length);
// Add locations onto map

//
// marker = new google.maps.Marker({
//     // position: new google.maps.LatLng($wellData[i].latitude, $wellData[i].longitude),
//     position: new google.maps.LatLng(-34.397, 150.644),
//     map: map
// })
