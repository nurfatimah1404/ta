//  Bikin Object DOM
// Irman
var ctx1 = document.getElementById('chartTemperature').getContext('2d');
var ctx2 = document.getElementById('chartHumidity').getContext('2d');
var ctx3 = document.getElementById('chartPressure').getContext('2d');
var ctx10 = document.getElementById('chartPM10').getContext('2d');
// Rahmad lok 1
var ctx11 = document.getElementById('chartPM10_rahmad').getContext('2d');
var ctx12 = document.getElementById('chartCO_rahmad').getContext('2d');
var ctx13 = document.getElementById('chartSO2_rahmad').getContext('2d');
//LOK 2 //

var ctx14 = document.getElementById('chartPM10_rahmad2').getContext('2d');
var ctx15 = document.getElementById('chartCO_rahmad2').getContext('2d');
var ctx16 = document.getElementById('chartSO2_rahmad2').getContext('2d');

//LOK 3//
var ctx17 = document.getElementById('chartPM10_rahmad3').getContext('2d');
// var ctx18 = document.getElementById('chartCO_rahmad3').getContext('2d');
// var ctx19 = document.getElementById('chartSO2_rahmad3').getContext('2d');

// //LOK 4//
// var ctx20 = document.getElementById('chartPM10_rahmad4').getContext('2d');
// var ctx21 = document.getElementById('chartCO_rahmad4').getContext('2d');
// var ctx22 = document.getElementById('chartSO2_rahmad4').getContext('2d');

// // // LOK 5//
// var ctx21 = document.getElementById('chartPM10_rahmad5').getContext('2d');
// var ctx22 = document.getElementById('chartCO_rahmad5').getContext('2d');
// var ctx23 = document.getElementById('chartSO2_rahmad5').getContext('2d');

// // LOK 6//
// var ctx32 = document.getElementById('chartPM10_rahmad5').getContext('2d');
// var ctx33 = document.getElementById('chartCO_rahmad5').getContext('2d');
// var ctx34 = document.getElementById('chartSO2_rahmad5').getContext('2d');


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
                }
            }],
            yAxes: [{
                ticks: {
                    suggestedMin: 25,
                    suggestedMax: 40,
                },
                scaleLabel: {
                    display: true,
                    labelString: 'Temperature (°C)'
                }
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
            }],
            yAxes: [{
                ticks: {
                    suggestedMin: 30,
                    suggestedMax: 60,
                },
                scaleLabel: {
                    display: true,
                    labelString: 'Hummidity (%)'
                }
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
            }],
            yAxes: [{
                ticks: {
                    suggestedMin: 1005,
                    suggestedMax: 1010,
                },
                scaleLabel: {
                    display: true,
                    labelString: 'Pressure (hPa)'
                }
            }]
        }
    },
    externals: {
        moment: 'moment'
    }
});
var chart10 = new Chart(ctx10, {
    type: 'line',
    data: {
        labels: [],
        datasets: [{
            label: 'PM10',
            backgroundColor: '#ffee58',
            borderColor: '#c9bc1f',
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
                }
            }],
            yAxes: [{
                ticks: {
                    suggestedMin: 25,
                    suggestedMax: 40,
                },
                scaleLabel: {
                    display: true,
                    labelString: 'PM10 (ppm)'
                }
            }]
        }
    },
    externals: {
        moment: 'moment'
    }
});

// rahmad LOK 1 /////////////////////////////////////////


var chart11 = new Chart(ctx11, {
    type: 'line',
    data: {
        labels: [],
        datasets: [{
            label: 'PM.10',
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
            }],
            yAxes: [{
                ticks: {
                    suggestedMin: 25,
                    suggestedMax: 40,
                },
                scaleLabel: {
                    display: true,
                    labelString: 'PM.10 (ppm)'
                }
            }]
        }
    },
    externals: {
        moment: 'moment'
    }
});
var chart12 = new Chart(ctx12, {
    type: 'line',
    data: {
        labels: [],
        datasets: [{
            label: 'CO',
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
            }],
            yAxes: [{
                ticks: {
                    suggestedMin: 25,
                    suggestedMax: 40,
                },
                scaleLabel: {
                    display: true,
                    labelString: 'CO (ppm)'
                }
            }]
        }
    },
    externals: {
        moment: 'moment'
    }
});
var chart13 = new Chart(ctx13, {
    type: 'line',
    data: {
        labels: [],
        datasets: [{
            label: 'SO2',
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
            }],
            yAxes: [{
                ticks: {
                    suggestedMin: 25,
                    suggestedMax: 40,
                },
                scaleLabel: {
                    display: true,
                    labelString: 'SO2 (ppm)'
                }
            }]
        }
    },
    externals: {
        moment: 'moment'
    }
});


// ------------------------LOK 2 --------------//

var chart14 = new Chart(ctx14, {
    type: 'line',
    data: {
        labels: [],
        datasets: [{
            label: 'PM.10',
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
            }],
            yAxes: [{
                ticks: {
                    suggestedMin: 25,
                    suggestedMax: 40,
                },
                scaleLabel: {
                    display: true,
                    labelString: 'PM.10 (ppm)'
                }
            }]
        }
    },
    externals: {
        moment: 'moment'
    }
});
var chart15 = new Chart(ctx15, {
    type: 'line',
    data: {
        labels: [],
        datasets: [{
            label: 'CO',
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
            }],
            yAxes: [{
                ticks: {
                    suggestedMin: 25,
                    suggestedMax: 40,
                },
                scaleLabel: {
                    display: true,
                    labelString: 'CO (ppm)'
                }
            }]
        }
    },
    externals: {
        moment: 'moment'
    }
});
var chart16 = new Chart(ctx16, {
    type: 'line',
    data: {
        labels: [],
        datasets: [{
            label: 'SO2',
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
            }],
            yAxes: [{
                ticks: {
                    suggestedMin: 25,
                    suggestedMax: 40,
                },
                scaleLabel: {
                    display: true,
                    labelString: 'SO2 (ppm)'
                }
            }]
        }
    },
    externals: {
        moment: 'moment'
    }
});

// LOK 3 ///
var chart17 = new Chart(ctx17, {
    type: 'line',
    data: {
        labels: [],
        datasets: [{
            label: 'SO2',
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
            }],
            yAxes: [{
                ticks: {
                    suggestedMin: 25,
                    suggestedMax: 40,
                },
                scaleLabel: {
                    display: true,
                    labelString: 'SO2 (ppm)'
                }
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
$.getJSON("getAverage?sensor=pm10&id=cd14", function (data) {
    data.forEach(element => {
        if (element.mean != null) {
            chart10.data.labels.push(element.time);
            chart10.data.datasets[0].data.push(Number.parseFloat(element.mean))
        }
    });
    chart10.update();
});


// rahmad LOK 1/////////////////////////////////////////

$.getJSON("getRahmad?sensor=pm10&id=015e&latitude=-5.1381 | longitude=119.482", function (data) {
    console.log(data);
    data.forEach(element => {
        if (element.value != null) {
            chart11.data.labels.push(element.time);
            chart11.data.datasets[0].data.push(Number.parseFloat(element.value))
        }
    });
    chart11.update();
});
$.getJSON("getRahmad?sensor=co&id=015e&latitude=-5.1381 | longitude=119.482", function (data) {
    data.forEach(element => {
        if (element.value != null) {
            chart12.data.labels.push(element.time);
            chart12.data.datasets[0].data.push(Number.parseFloat(element.value))
        }
    });
    chart12.update();

});
$.getJSON("getRahmad?sensor=so2&id=015e&latitude=-5.1381|longitude=119.482", function (data) {
    data.forEach(element => {
        if (element.value != null) {
            chart13.data.labels.push(element.time);
            chart13.data.datasets[0].data.push(Number.parseFloat(element.value))
        }
    });
    chart13.update();
});

// lok 2///////////////////////

$.getJSON("getRahmad?sensor=pm10&id=015e&latitude=-5.1374|longitude=119.5153", function (data) {
    data.forEach(element => {
        if (element.value != null) {
            chart14.data.labels.push(element.time);
            chart14.data.datasets[0].data.push(Number.parseFloat(element.value))
        }
    });
    chart14.update();
});
$.getJSON("getRahmad?sensor=co&id=015e&latitude=-5.1374|longitude=119.5153", function (data) {
    data.forEach(element => {
        if (element.value != null) {
            chart15.data.labels.push(element.time);
            chart15.data.datasets[0].data.push(Number.parseFloat(element.value))
        }
    });
    chart15.update();

});
$.getJSON("getRahmad?sensor=so2&id=015e&latitude=-5.1374|longitude=119.5153", function (data) {
    data.forEach(element => {
        if (element.value != null) {
            chart16.data.labels.push(element.time);
            chart16.data.datasets[0].data.push(Number.parseFloat(element.value))
        }
    });
    chart16.update();
});


// lok 3////////////
$.getJSON("getRahmad?sensor=pm10&id=015e&latitude=-5.1381", function (data) {
    data.forEach(element => {
        if (element.value != null) {
            chart17.data.labels.push(element.time);
            chart17.data.datasets[0].data.push(Number.parseFloat(element.value))
        }
    });
    chart17.update();
});
// $.getJSON("getRahmad?sensor=co&id=015e&latitude=-5.1381", function (data) {
//     data.forEach(element => {
//         if (element.value != null) {
//             chart18.data.labels.push(element.time);
//             chart18.data.datasets[0].data.push(Number.parseFloat(element.value))
//         }
//     });
//     chart18.update();

// });
// $.getJSON("getRahmad?sensor=so2&id=015e&latitude=-5.1381", function (data) {
//     data.forEach(element => {
//         if (element.value != null) {
//             chart19.data.labels.push(element.time);
//             chart19.data.datasets[0].data.push(Number.parseFloat(element.value))
//         }
//     });
//     chart19.update();
// });






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
     function satu(){
         $('#satu').show(200);
         $('#dua').hide(200);
         $('#tiga').hide(200);
     }
     function dua(){
        $('#dua').show(200);
        $('#satu').hide(200);
        $('#tiga').hide(200);
    }
    function tiga(){
        $('#satu').hide(200);
        $('#dua').hide(200);
        $('#tiga').show(200);
    }
});

// map
mapboxgl.accessToken = 'pk.eyJ1IjoiZmF0aW1haDE0IiwiYSI6ImNrZWZuNmE0ODB2ajUydGxnbWljYXp6OW4ifQ.53UTfZmsMUXJjDmF9OVYBg';
// mapboxgl.accessToken = 'pk.eyJ1IjoiZGFpbnQiLCJhIjoiY2tlZ29pbXI1MTV1YzM0bGcxaXdkbmR0ZyJ9.DKWwkyXev1SJTzCv-YpCuQ';
var map = new mapboxgl.Map({
    container: 'map',
    style: 'mapbox://styles/mapbox/streets-v11',
    center: [119.481961, -5.137894],
    zoom: 14


});


$.getJSON("getFau?sensor=pm10&id=3F0D", function (data) {
    // console.log(data);
    data.forEach(element => {
        if (element.latitude != null || element.longitude != null) {
            var marker = new mapboxgl.Marker()
                .setLngLat([element.longitude, element.latitude])
                .setPopup(new mapboxgl.Popup().setHTML(`
                <p style="margin-bottom:0px;font-size:15px">PM10 : ${element.pm10} ppm</p><br>
                <p style="margin-bottom:0px;font-size:15px">CO2 : ${element.co2} ppm</p><br>
                <p style="margin-bottom:0px;font-size:15px">CO : ${element.co} ppm</p><br>
                <p style="margin-bottom:0px; padding-top:0px; font-size:15px">Temperature : ${element.temperature} &#8451;</p><br>
                <p style="margin-bottom:0px; padding-top:0px; font-size:15px">Humidity : ${element.humidity} &#37;</p><br>
                `))
                .addTo(map);
        }
        // console.log(element);
    });
});



const getStatusData = () => {
    $.ajax({
        url: 'getCounter',
        success: (respond) => {
            $("#dataReceived").text(respond.received);
            $("#dataBlocked").text(respond.blocked);
            $("#waktuUpdate").text(respond.time);
        }
    })
}
getStatusData()
setInterval(() => {
    getStatusData();
}, 5000)
