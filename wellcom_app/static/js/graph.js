var $deviceData = {};

$.ajax({
  type: 'GET',
  dataType: "json",
  url: '/api/device_data/',
  success: function(data, textStatus) {
    // Handle success
    $deviceData = data;
  },
  error: function(xhr, textStatus, errorThrown) {
    // Handle error
  }
});

var device_data_table_data = $deviceData.results;

function myData() {
    var series1 = [];
    for(var i =1; i < 100; i ++) {
        series1.push({
            x: i, y: 100 / i
        });
    }
    return [
        {
            key: "Kogadoone",
            values: series1,
            color: "#0000ff"
        }
        // {
        //     key: "Atolisum Primary School - Anateem",
        //     values: series2,
        //     color: "#0000ff"
        // }
        // {
        //     key: "Zorko Gambrogo",
        //     values: series3,
        //     color: "#0000ff"
        // }
        // {
        //     key: "Akukuni",
        //     values: series4,
        //     color: "#0000ff"
        // }
        // {
        //     key: "Katanga",
        //     values: series5,
        //     color: "#0000ff"
        // }
        // {
        //     key: "Yipaala",
        //     values: series6,
        //     color: "#0000ff"
        // }
        // {
        //     key: "Zuboko",
        //     values: series7,
        //     color: "#0000ff"
        // }
    ];
}
nv.addGraph(function() {
        var width = 600, height = 300;
        var chart = nv.models.lineWithFocusChart();
        chart.brushExtent([50,70]);
        chart.xAxis
          .tickFormat(d3.format(',f'))
          .axisLabel("Time");
        chart.x2Axis.tickFormat(d3.format(',f'));
        chart.yAxis
          .axisLabel("Temperature(C)");
        chart.yTickFormat(d3.format(',.2f'));
        chart.useInteractiveGuideline(true);
        d3.select('#chart svg')
           .datum(myData())
           .style({ 'width': width, 'height': height })
           .call(chart);
       nv.utils.windowResize(chart.update);
       return chart;
   });

// while (data.)
//
// nv.addGraph(function() {
//   var chart = nv.models.lineWithFocusChart();
//
//   chart.xAxis
//       .tickFormat(d3.format(',f'));
//
//   chart.yAxis
//       .tickFormat(d3.format(',.2f'));
//
//   chart.y2Axis
//       .tickFormat(d3.format(',.2f'));
//
//   d3.select('#well_graph')
//       .datum(device_data_table_data)
//       .transition().duration(500)
//       .call(chart);
//
//   nv.utils.windowResize(chart.update);
//
//   return chart;
// });

// TODO: Fix error: nv.d3.js:5 Uncaught TypeError: Cannot read property 'map' of undefined
// http://stackoverflow.com/questions/17157554/nvd3-pie-chart-says-uncaught-typeerror-cannot-call-method-map-of-undefined
