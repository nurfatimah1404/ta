//  Bikin Object DOM
var ctx1 = document.getElementById('chartTemperature').getContext('2d');
var ctx2 = document.getElementById('chartHumidity').getContext('2d');
var ctx3 = document.getElementById('chartPressure').getContext('2d');
var ctx4 = document.getElementById('chartTemperature_rahmad').getContext('2d');
var ctx5 = document.getElementById('chartHumidity_rahmad').getContext('2d');
var ctx6 = document.getElementById('chartPressure_rahmad').getContext('2d');
var ctx7 = document.getElementById('chartHeight_rahmad').getContext('2d');
var ctx8 = document.getElementById('chartCO_rahmad').getContext('2d');
var ctx9 = document.getElementById('chartSO2_rahmad').getContext('2d');
var ctx10 = document.getElementById('chartPM10_rahmad').getContext('2d');
// var ctx11 = document.getElementById('chartTemperature_fau').getContext('2d');        
// var ctx12 = document.getElementById('chartHumidity_fau').getContext('2d');        
// var ctx13 = document.getElementById('chartCO2_fau').getContext('2d');        
// var ctx14 = document.getElementById('chartCO_fau').getContext('2d');        
// var ctx15 = document.getElementById('chartPM25_fau').getContext('2d');
var dataPoints = [];
// Bikin Objek Chart dan Konfigurasinya
var chart1 = new Chart(ctx1, {
    type: 'line',
    data: {
        labels: [],
        datasets: [{
            label: 'Temperature',
            backgroundColor: '#ff7961',
            borderColor: '#ba000d',
            data: [],
            lineTension: 0,
            // autoSkip: true,
            // autoSkipPadding: 0,
            // spanGaps: true
            // skipNullValues: true
        }]
    },
    options: {
        bezierCurve: true,
        scales: {
            xAxes: [{
                type: 'time',
                time: {
                    unit: 'hour',
                    displayFormats: {
                        hour: 'YYYY-MM-DD HH:mm',
                    }
                },
            }]
        }
    },
    externals: {
        moment: 'moment'
    }
});
var chart2 = new Chart(ctx2, {
    type: 'line',
    data: {
        labels: [],
        datasets: [{
            label: 'Humidity',
            backgroundColor: '#63a4ff',
            borderColor: '#004ba0',
            data: [],
            lineTension: 0,
            autoSkip: true,
            autoSkipPadding: 0,
            spanGaps: true
        }]
    },
    options: {
        bezierCurve: true,
        scales: {
            xAxes: [{
                type: 'time',
                time: {
                    unit: 'hour',
                    displayFormats: {
                        hour: 'YYYY-MM-DD HH:mm',
                    }
                },
            }]
        }
    },
    externals: {
        moment: 'moment'
    }
});
var chart3 = new Chart(ctx3, {
    type: 'line',
    data: {
        labels: [],
        datasets: [{
            label: 'Pressure',
            backgroundColor: '#6abf69',
            borderColor: '#00600f',
            data: [],
            lineTension: 0,
            autoSkip: true,
            autoSkipPadding: 0,
            spanGaps: true
        }]
    },
    options: {
        bezierCurve: true,
        scales: {
            xAxes: [{
                type: 'time',
                time: {
                    unit: 'hour',
                    displayFormats: {
                        hour: 'YYYY-MM-DD HH:mm',
                    }
                },
            }]
        }
    },
    externals: {
        moment: 'moment'
    }
});
var chart4 = new Chart(ctx4, {
    type: 'line',
    data: {
        labels: [],
        datasets: [{
            label: 'Pressure',
            backgroundColor: '#6abf69',
            borderColor: '#00600f',
            data: [],
            lineTension: 0,
            autoSkip: true,
            autoSkipPadding: 0,
            spanGaps: true
        }]
    },
    options: {
        bezierCurve: true,
        scales: {
            xAxes: [{
                type: 'time',
                time: {
                    unit: 'hour',
                    displayFormats: {
                        hour: 'YYYY-MM-DD HH:mm',
                    }
                },
            }]
        }
    },
    externals: {
        moment: 'moment'
    }
});
var chart5 = new Chart(ctx5, {
    type: 'line',
    data: {
        labels: [],
        datasets: [{
            label: 'Pressure',
            backgroundColor: '#6abf69',
            borderColor: '#00600f',
            data: [],
            lineTension: 0,
            autoSkip: true,
            autoSkipPadding: 0,
            spanGaps: true
        }]
    },
    options: {
        bezierCurve: true,
        scales: {
            xAxes: [{
                type: 'time',
                time: {
                    unit: 'hour',
                    displayFormats: {
                        hour: 'YYYY-MM-DD HH:mm',
                    }
                },
            }]
        }
    },
    externals: {
        moment: 'moment'
    }
});
var chart6 = new Chart(ctx6, {
    type: 'line',
    data: {
        labels: [],
        datasets: [{
            label: 'Pressure',
            backgroundColor: '#6abf69',
            borderColor: '#00600f',
            data: [],
            lineTension: 0,
            autoSkip: true,
            autoSkipPadding: 0,
            spanGaps: true
        }]
    },
    options: {
        bezierCurve: true,
        scales: {
            xAxes: [{
                type: 'time',
                time: {
                    unit: 'hour',
                    displayFormats: {
                        hour: 'YYYY-MM-DD HH:mm',
                    }
                },
            }]
        }
    },
    externals: {
        moment: 'moment'
    }
});
var chart7 = new Chart(ctx7, {
    type: 'line',
    data: {
        labels: [],
        datasets: [{
            label: 'Pressure',
            backgroundColor: '#6abf69',
            borderColor: '#00600f',
            data: [],
            lineTension: 0,
            autoSkip: true,
            autoSkipPadding: 0,
            spanGaps: true
        }]
    },
    options: {
        bezierCurve: true,
        scales: {
            xAxes: [{
                type: 'time',
                time: {
                    unit: 'hour',
                    displayFormats: {
                        hour: 'YYYY-MM-DD HH:mm',
                    }
                },
            }]
        }
    },
    externals: {
        moment: 'moment'
    }
});
var chart8 = new Chart(ctx8, {
    type: 'line',
    data: {
        labels: [],
        datasets: [{
            label: 'CO2',
            backgroundColor: '#6abf69',
            borderColor: '#00600f',
            data: [],
            lineTension: 0,
            autoSkip: true,
            autoSkipPadding: 0,
            spanGaps: true
        }]
    },
    options: {
        bezierCurve: true,
        scales: {
            xAxes: [{
                type: 'time',
                time: {
                    unit: 'hour',
                    displayFormats: {
                        hour: 'YYYY-MM-DD HH:mm',
                    }
                },
            }]
        }
    },
    externals: {
        moment: 'moment'
    }
});
var chart9 = new Chart(ctx9, {
    type: 'line',
    data: {
        labels: [],
        datasets: [{
            label: 'Temperature',
            backgroundColor: '#ff7961',
            borderColor: '#ba000d',
            data: [],
            lineTension: 0,
            autoSkip: true,
            autoSkipPadding: 0,
            spanGaps: true
            // skipNullValues: true
        }]
    },
    options: {
        bezierCurve: true,
        scales: {
            xAxes: [{
                type: 'time',
                time: {
                    unit: 'hour',
                    displayFormats: {
                        hour: 'YYYY-MM-DD HH:mm',
                    }
                },
            }]
        }
    },
    externals: {
        moment: 'moment'
    }
});
// Get Datanya pakae AJAX

//data dari IRMAN
// $.getJSON("getAverage?sensor=temperature&id=cd14", function (data) {
//     data.forEach(element => {
//         chart1.data.labels.push(element.time);
//         if (element.mean != 0){
//             chart1.data.datasets[0].data.push(Number.parseFloat(element.mean))
//         }
//         else{
//         continue;
//         }
//     });
//     chart1.update();
// });
$.getJSON("getAverage?sensor=temperature&id=cd14", function (data) {

    data.forEach(element => {
        if (element.mean != null) {
            chart1.data.labels.push(element.time);
            chart1.data.datasets[0].data.push(Number.parseFloat(element.mean))
        }
    });
    chart1.update();
});
$.getJSON("getAverage?sensor=humidity&id=cd14", function (data) {
    console.log(data)
    data.forEach(element => {
        if (element.mean != null) {
            chart2.data.datasets[0].data.push(Number.parseFloat(element.mean))
            chart2.data.labels.push(element.time);
        }
    });
    chart2.update();
});
$.getJSON("getAverage?sensor=pressure&id=cd14", function (data) {
    data.forEach(element => {
        if (element.mean != null) {
            chart3.data.labels.push(element.time);
            chart3.data.datasets[0].data.push(Number.parseFloat(element.mean))
        }
    });
    chart3.update();
});


//data dari rahmad

$.getJSON("getAverageRahmad?sensor=temperature&id=025f", function (data) {
    data.forEach(element => {
        if (element.mean != null) {
            chart4.data.labels.push(element.time);
            chart4.data.datasets[0].data.push(Number.parseFloat(element.mean))
        }
    });
    chart4.update();
});
$.getJSON("getAverageRahmad?sensor=humidity&id=025f", function (data) {
    data.forEach(element => {
        if (element.mean != null) {
            chart5.data.labels.push(element.time);
            chart5.data.datasets[0].data.push(Number.parseFloat(element.mean))
        }
    });
    chart5.update();
});
$.getJSON("getAverageRahmad?sensor=pressure&id=025f", function (data) {
    data.forEach(element => {
        if (element.mean != null) {
            chart6.data.labels.push(element.time);
            chart6.data.datasets[0].data.push(Number.parseFloat(element.mean))
        }
    });
    chart6.update();
});
$.getJSON("getAverageRahmad?sensor=height&id=025f", function (data) {
    data.forEach(element => {
        if (element.mean != null) {
            chart7.data.labels.push(element.time);
            chart7.data.datasets[0].data.push(Number.parseFloat(element.mean))
        }
    });
    chart7.update();
});
$.getJSON("getAverageRahmad?sensor=co&id=015e", function (data) {
    data.forEach(element => {
        if (element.mean != null) {
            chart8.data.labels.push(element.time);
            chart8.data.datasets[0].data.push(Number.parseFloat(element.mean))
        }
    });
    chart8.update();
});
$.getJSON("getAverageRahmad?sensor=so2&id=015e", function (data) {
    data.forEach(element => {
        if (element.mean != null) {
            chart9.data.labels.push(element.time);
            chart9.data.datasets[0].data.push(Number.parseFloat(element.mean))
        }
    });
    chart9.update();

});
$.getJSON("getAverageRahmad?sensor=pm10&id=015e", function (data) {
    data.forEach(element => {
        if (element.mean != null) {
            chart10.data.labels.push(element.time);
            chart10.data.datasets[0].data.push(Number.parseFloat(element.mean))
        }
    });
    chart10.update();
});


// // DATA DARI FAU


// $.getJSON("getAverageRahmad?sensor=pm.10&id=3F0D", function (data) {
//     data.forEach(element => {
//         chart15.data.labels.push(element.time);
//         if(element.mean != null){
//             chart15.data.datasets[0].data.push(Number.parseFloat(element.mean))
//         } else {
//             chart15.data.datasets[0].data.push(0)
//         }
//     });
//     chart15.update();
// });
// $.getJSON("http://192.168.1.14:8000/getData?id=015e", function (data) {
//     data.forEach(element => {
//         chart.data.labels.push(element.time);
//         chart.data.datasets[0].data.push(element.value)
//     });
//     chart.update();
// });




$(document).ready(function () {
    $('#idSensor').change(function () {
        var a = $(this).children("option:selected").val();
        console.log(a);
        if (a == "cd14") {
            $('#irman').show(200);
            $('#rahmad').hide();
            $('#rahmad2').hide();
            $('#fauzan').hide();
        }
        else if (a == "015e") {
            $('#rahmad').show(200);
            $('#irman').hide(200);
            $('#rahmad2').hide();
            $('#fauzan').hide();
        }
        else if (a == "3F0D") {
            $('#fauzan').show(200);
            $('#irman').hide(200);
            $('#rahmad').hide();
            $('#rahmad2').hide();
        }
    });
});



mapboxgl.accessToken = 'pk.eyJ1IjoiZmF0aW1haDE0IiwiYSI6ImNrZWZuNmE0ODB2ajUydGxnbWljYXp6OW4ifQ.53UTfZmsMUXJjDmF9OVYBg';
// mapboxgl.accessToken = 'pk.eyJ1IjoiZGFpbnQiLCJhIjoiY2tlZ29pbXI1MTV1YzM0bGcxaXdkbmR0ZyJ9.DKWwkyXev1SJTzCv-YpCuQ';
var map = new mapboxgl.Map({
    container: 'map',
    style: 'mapbox://styles/mapbox/streets-v11',
    center: [119.481961, -5.137894],
    zoom: 16
});

map.on('load', function () {
    map.resize();
    map.loadImage(
        'https://docs.mapbox.com/mapbox-gl-js/assets/custom_marker.png',
        // Add an image to use as a custom marker
        function (error, image) {
            if (error) throw error;
            map.addImage('custom-marker', image);


            map.addSource('places',
                {
                    'type': 'geojson',
                    'data':
                    {
                        'type': 'FeatureCollection',
                        'features': [
                            {
                                'type': 'Feature',
                                'properties':
                                {
                                    'description':
                                        '<h3>INI WAKTU</h3> <p>lat &#8451;</p> <p>long</p> <p>co</p> <p>so</p> <p>pm10</p>'
                                },
                                'geometry':
                                {
                                    'type': 'Point',
                                    'coordinates': [119.481961, -5.137894]
                                }
                            }]
                    }
                });

            // Add a layer showing the places.
            map.addLayer({
                'id': 'places',
                'type': 'symbol',
                'source': 'places',
                'layout':
                {
                    'icon-image': 'custom-marker',
                    'icon-allow-overlap': true
                }
            });
        }
    );

    // Create a popup, but don't add it to the map yet.
    var popup = new mapboxgl.Popup({
        closeButton: false,
        closeOnClick: false
    });

    map.on('mouseenter', 'places', function (e) {
        // Change the cursor style as a UI indicator.
        map.getCanvas().style.cursor = 'pointer';

        var coordinates = e.features[0].geometry.coordinates.slice();
        var description = e.features[0].properties.description;

        // Ensure that if the map is zoomed out such that multiple
        // copies of the feature are visible, the popup appears
        // over the copy being pointed to.
        while (Math.abs(e.lngLat.lng - coordinates[0]) > 180) {
            coordinates[0] += e.lngLat.lng > coordinates[0] ? 360 : -360;
        }

        // Populate the popup and set its coordinates
        // based on the feature found.
        popup
            .setLngLat(coordinates)
            .setHTML(description)
            .addTo(map);
    });

    map.on('mouseleave', 'places', function () {
        map.getCanvas().style.cursor = '';
        popup.remove();
    });

});

$.getJSON("getFau?sensor=pm10&id=3F0D", function (data) {
    data.forEach(element => {
        console.log(element);
    });
});