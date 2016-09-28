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

    var  map = new google.maps.Map(document.getElementById('all_well_map'), {
        center: {lat: 36.9930780, lng: -79.9046890},
        zoom: 8,
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

      // TODO: add in logic for different images here!

      var imagebase = 'https://wellcom-staging.herokuapp.com/static/images/'
      var images = {
            good: {
              icon: imagebase + 'BlueSymbol.png',
            },
            down_com: {
              icon: imagebase + 'ic_signal_cellular_connected_no_internet_4_bar_black_24dp_2x.png',
            },
            non_use: {
              icon: imagebase + 'ic_build_black_24dp_2x.png',
            },
          };

      var marker, i;


      for (i = 0; i < $wellData.length; i++) {
        // TODO: TAKE THIS OUT later and replace with actual logic
        if ($wellData[i].name == "Zuboko-Bongo") {
          var image = images.down_com.icon;
        } else if ($wellData[i].name == "Katanga") {
          var image = images.non_use.icon;
        } else {
          var image = images.good.icon;
        }

          marker = new google.maps.Marker({
              // position: new google.maps.LatLng($wellData[i].latitude, $wellData[i].longitude),
              position: new google.maps.LatLng(Number($wellData[i].latitude), Number($wellData[i].longitude)),
              map: map,
              icon: {
                url: image,

                scaledSize: new google.maps.Size(45, 53),
              }
          });

          bounds.extend(marker.position);

          google.maps.event.addListener(marker, 'click', (function(marker, i) {
              return function() {
              infowindow.setContent('<h4>' + $wellData[i].name + '</h4>'
                  + '<h5> Flowing since:  ' + $wellData[i].date_installed + '</h5>' +
                    '<h5> Last updated:  ' + $wellData[i].last_update.split('T')[0] + '</h5>' +
                    '<h5> Battery:  ' + $wellData[i].batt_percent_charged + '%' + '</h5>');
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
