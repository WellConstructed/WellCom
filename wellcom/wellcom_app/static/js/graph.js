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
// while (data.)

nv.addGraph(function() {
  var chart = nv.models.lineWithFocusChart();

  chart.xAxis
      .tickFormat(d3.format(',f'));

  chart.yAxis
      .tickFormat(d3.format(',.2f'));

  chart.y2Axis
      .tickFormat(d3.format(',.2f'));

  d3.select('#well_graph')
      .datum(device_data_table_data)
      .transition().duration(500)
      .call(chart);

  nv.utils.windowResize(chart.update);

  return chart;
});

// TODO: Fix error: nv.d3.js:5 Uncaught TypeError: Cannot read property 'map' of undefined
// http://stackoverflow.com/questions/17157554/nvd3-pie-chart-says-uncaught-typeerror-cannot-call-method-map-of-undefined
