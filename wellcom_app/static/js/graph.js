var $hourlyUsage;
var $hourly_usage_table_data;
var $hourly_usage_json;
$urlComponents = document.URL.split('/');
$wellId = $urlComponents[$urlComponents.length - 1];


//   },
//   error: function(xhr, textStatus, errorThrown) {
//     // Handle error
//   }
// });


$.ajax({
  type: 'GET',
  dataType: "json",
  url: '/api/hourly_usage/?well=' + $wellId,
  success: function(data, textStatus) {
    // Handle success
    $hourlyUsage = data;

    $hourly_usage_table_data = $hourlyUsage.results;
    console.log($hourly_usage_table_data);
    $hourly_usage_json = processHourlyUsage($hourly_usage_table_data);

    nv.addGraph(function() {
        var chart = nv.models.multiBarChart()
          .reduceXTicks(true)   //If 'false', every single x-axis tick label will be rendered.
          .rotateLabels(10)      //Angle to rotate x-axis labels.
          .showControls(true)   //Allow user to switch between 'Grouped' and 'Stacked' mode.
          .groupSpacing(0.1)    //Distance between each group of bars.
        ;

        chart.xAxis
          .tickFormat(function(d) {
            return d3.time.format('%x')(new Date(d));
        })
          .axisLabel("Time");

        chart.yAxis
            .tickFormat(d3.format(',.1f'))
            .axisLabel("Usage Count")

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
    var katanga = [];
    var kogadoone = [];
    var yipaala = [];
    var atolisum = [];
    var akukuni = [];
    var zuboko = [];

    for(var reading in $hourly_usage_table_data) {
        reading = $hourly_usage_table_data[reading];
        var xN = Number(new Date(reading.timestamp));
        var yN = Number(reading.usage_count);
        zorko.push({
            x: xN,
            y: yN
        });
    }
    return [
        {
                    key: "Zorko",
                    values: zorko,
                    color: "#0000ff"
                },
        {
                    key: "Katanga",
                    values: katanga,
                    color: "#0000ff"
                },
        {
                    key: "Kogadoone",
                    values: kogadoone,
                    color: "#0000ff"
                },
        {
                    key: "Yipaala",
                    values: yipaala,
                    color: "#0000ff"
                },
        {
                    key: "Atolisum",
                    values: atolisum,
                    color: "#0000ff"
                },
        {
                    key: "Akukuni",
                    values: akukuni,
                    color: "#0000ff"
                },
        {
                    key: "Zuboko",
                    values: zuboko,
                    color: "#0000ff"
                }
    ];
}
