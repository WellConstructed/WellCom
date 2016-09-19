// Get all wells
var $wellData = {};

var map;

function initMap() {
    map = new google.maps.Map(document.getElementById('well_map'), {
        center: {
          lat: 36.9930780,
          lng: -79.9046890
        },
        zoom: 8,
        scrollwheel: false,
        styles: [{
            featureType: 'all',
            stylers: [{
                saturation: -70
            }]
        }]
    });
}



$urlComponents = document.URL.split('/');
$wellId = $urlComponents[$urlComponents.length - 1];

$.ajax({
    type: 'GET',
    dataType: "json",
    url: '/api/well/' + $wellId + '/',
    success: function(data, textStatus) {
        // Handle success
        $wellData = data;
        console.log($wellData);

        var infowindow = new google.maps.InfoWindow();

        var image = {
            url: 'https://wellcom-staging.herokuapp.com/static/images/BlueSymbol.png',
            scaledSize: new google.maps.Size(45, 56),
        };

        var marker = new google.maps.Marker({
            // position: new google.maps.LatLng($wellData[i].latitude, $wellData[i].longitude),
            position: new google.maps.LatLng(Number($wellData.latitude), Number($wellData.longitude)),
            map: map,
            icon: image,
        });
      },
    error: function(xhr, textStatus, errorThrown) {
        // Handle error
        console.log('Error getting the Well Data');
    }

});
