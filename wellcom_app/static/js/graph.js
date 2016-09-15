var $deviceData;
var $device_data_table_data;
var $device_data_json;

$.ajax({
  type: 'GET',
  dataType: "json",
  url: '/api/device_data/',
  success: function(data, textStatus) {
    // Handle success
    $deviceData = data;

    $device_data_table_data = $deviceData.results;

    $device_data_json = processDeviceData($device_data_table_data);


    nv.addGraph(function() {
            var width = 600, height = 400;
            var chart = nv.models.lineWithFocusChart();
            chart.brushExtent([50,70]);

            // chart.xAxis
            //   .tickFormat(d3.format(',f'))
            //   .axisLabel("Time");

            chart.xAxis
              .tickFormat(function(d) {
                return d3.time.format('%x')(new Date(d));
            })
              .axisLabel("Time");

          chart.x2Axis
            .tickFormat(function(d) {
              return d3.time.format('%x')(new Date(d));
          });

            // chart.x2Axis.tickFormat(d3.format(',f'));


            chart.yAxis
              .axisLabel("Temperature(C)");
            chart.yTickFormat(d3.format(',.2f'));
            chart.useInteractiveGuideline(true);

            d3.select('#chart svg')
            //    .datum(myData())
               .datum($device_data_json)
               .style({ 'width': width, 'height': height })
               .call(chart);

           nv.utils.windowResize(chart.update);
           return chart;
       });


  },
  error: function(xhr, textStatus, errorThrown) {
    // Handle error
  }
});

function processDeviceData(device_data_table_data) {
    var series1 = [];
    for(var reading in device_data_table_data) {
        reading = device_data_table_data[reading];
        var xN = Number(new Date(reading.timestamp));
        var yN = Number(reading.temperature_c);
        // console.log(xN);
        // console.log(typeof xN);
        series1.push({
            // TODO: This is ugly!  We should get the data from Arduino as a timestamp, and this conversion would be unecessary
            x: xN,
            y: yN
        });
    }
    return [
        {
                    key: "Kogadoone",
                    values: series1,
                    color: "#0000ff"
                }
    ];
}


//
// function myData() {
//     var series1 = [];
//     for(var i =1; i < 100; i ++) {
//         series1.push({
//             x: i, y: 100 / i
//         });
//     }
//     return [
//         {
//             key: "Kogadoone",
//             values: series1,
//             color: "#0000ff"
//         }
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
//     ];
// }


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
