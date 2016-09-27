var $hourlyUsage;
var $hourly_usage_table_data;
var $hourly_usage_json;
$urlComponents = document.URL.split('/');
$wellId = $urlComponents[$urlComponents.length - 1];
$wellId = parseInt($wellId);


//   },
//   error: function(xhr, textStatus, errorThrown) {
//     // Handle error
//   }
// });
// var mindate = new Date().setHours(0, 0, 0, 0);
// mindate = new Date(mindate);
// var maxdate = new Date().setHours(23, 0, 0, 0);
// maxdate = new Date(maxdate);

$.ajax({
  type: 'GET',
  dataType: "json",
  // url: '/api/hourly_usage/?well=' + $wellId,
  url: '/api/hourly_usage/',
  success: function(data, textStatus) {
    // Handle success
    $hourlyUsage = data;

    $hourly_usage_table_data = $hourlyUsage.results;
    $hourly_usage_json = processHourlyUsage($hourly_usage_table_data);
    $hourly_usage_json.forEach(function(stream) {
      if (stream.well_id == $wellId) {
        stream.disabled = false;
      }
    });

    nv.addGraph(function() {
        var chart = nv.models.multiBarChart()
          .reduceXTicks(true)   //If 'false', every single x-axis tick label will be rendered.
          .rotateLabels(-10)      //Angle to rotate x-axis labels.
          .showControls(true)   //Allow user to switch between 'Grouped' and 'Stacked' mode.
          .groupSpacing(0.1)    //Distance between each group of bars.
        ;

        chart.xAxis
          .tickFormat(function(d) {
            return d3.time.format('%d %b-%H:00')(new Date(d));
        })
          .axisLabel("Time(h)");

        chart.yAxis
            .tickFormat(d3.format(',.1f'))
            .axisLabel("Usage Count");


        d3.select('#chart svg')
            .datum($hourly_usage_json)
            .call(chart);

        nv.utils.windowResize(chart.update);

        return chart;
    });
  }
})


//Generate some nice data.

function processHourlyUsage($hourly_usage_table_data) {
    var zorko = [];
    var kogadoone = [];
    var katanga = [];
    var yipaala = [];
    var atolisum = [];
    var akukuni = [];
    var zuboko = [];

    for (var reading in $hourly_usage_table_data) {
    for (i=0; i<=reading.length; i++) {
        reading = $hourly_usage_table_data[reading];
        var xN = Number(new Date(reading.timestamp));
        var yN = Number(reading.usage_count);
        if (reading.well == 1) {
          zorko.push({
              x: xN,
              y: yN
          });
        } else if (reading.well == 2) {
          katanga.push({
              x: xN,
              y: yN
          });
        }
        else if (reading.well == 3) {
          kogadoone.push({
              x: xN,
              y: yN
          });
        }
        else if (reading.well == 4) {
          yipaala.push({
              x: xN,
              y: yN
          });
        }
        else if (reading.well == 5) {
          atolisum.push({
              x: xN,
              y: yN
          });
        }
        else if (reading.well == 6) {
          akukuni.push({
              x: xN,
              y: yN
          });
        }
        else if (reading.well == 7) {
          zuboko.push({
              x: xN,
              y: yN
          });
        } } }

        zorko = zorko.sort(function(x, y){
        return x.x - y.x;
    });
        kogadoone = kogadoone.sort(function(x, y){
        return x.x - y.x;
    });

        katanga = katanga.sort(function(x, y){
        return x.x - y.x;
    });

        yipaala = yipaala.sort(function(x, y){
        return x.x - y.x;
    });
        atolisum = atolisum.sort(function(x, y){
        return x.x - y.x;
    });
        akukuni = akukuni.sort(function(x, y){
        return x.x - y.x;
    });

        zuboko = zuboko.sort(function(x, y){
        return x.x - y.x;
    });

    return [
        {
                    key: "Zorko",
                    disabled: true,
                    values: zorko,
                    color: "#A0DFFF",
                    well_id: 1
                },
        {
                    key: "Katanga",
                    disabled: true,
                    values: katanga,
                    color: "#301BD1",
                    well_id: 2
                },
        {
                    key: "Kogadoone",
                    disabled: true,
                    values: kogadoone,
                    color: "#369FF4",
                    well_id: 3
                },
        {
                    key: "Yipaala",
                    disabled: true,
                    values: yipaala,
                    color: "#E7A4A3",
                    well_id: 4
                },
        {
                    key: "Atolisum",
                    disabled: true,
                    values: atolisum,
                    color: "#9F0005",
                    well_id: 5
                },
        {
                    key: "Akukuni",
                    disabled: true,
                    values: akukuni,
                    color: "#CB0000",
                    well_id: 6
                },
        {
                    key: "Zuboko",
                    disabled: true,
                    values: zuboko,
                    color: "#00102C",
                    well_id: 7
        }
    ];
}
