// Get all wells
var $wellData = {};

// var map;

function initMap() {

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

         var map = new google.maps.Map(document.getElementById('well_map'), {
            center: {lat: Number($wellData.latitude), lng: Number($wellData.longitude)},
            zoom: 10,
            disableDefaultUI: true,
            scrollwheel: false,
            mapTypeId: 'terrain',
            styles: [{
                featureType: 'all',
                stylers: [{
                    saturation: 100
                }]
            }]
        });

        var infowindow = new google.maps.InfoWindow();

        var image = {
            url: 'https://wellcom-staging.herokuapp.com/static/images/BlueSymbol.png',
            scaledSize: new google.maps.Size(30, 43),
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
}
