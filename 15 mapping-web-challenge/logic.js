var layer = "https://api.mapbox.com/styles/v1/mapbox/satellite-streets-v9/tiles/256/{z}/{x}/{y}" + 
            "?access_token=pk.eyJ1IjoibWFyY2dvbGRzdGVpbiIsImEiOiJjamR3Z2syejAwNW1rMndvMWJodjBuNTZkIn0." +
            "lu5mvkpt_gLeTFkV4htK6g";
            // pk.eyJ1IjoibWFyY2dvbGRzdGVpbiIsImEiOiJjamR3Z2syejAwNW1rMndvMWJodjBuNTZkIn0.lu5mvkpt_gLeTFkV4htK6g

// base layer
var sataliteMap = L.tileLayer(layer)
      
var link = 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/1.0_week.geojson';

function markerSize(magnitude) {
    return magnitude * 3;
}


d3.json(link, function(error, data) {
    
//point color
    var color = d3.scaleLinear()
        .domain(d3.extent(data.features, function(earthquake){
            return +earthquake.properties.mag;
        }))
        .range(['white', 'red']);
    
    var legendData = [];

    // add geoJSON data
    var equakeLayer = L.geoJSON(data, {
        pointToLayer: function (feature, latlng) {

            
            size = markerSize(feature.properties.mag);
            markerColor = color(feature.properties.mag);


            legendData.push([+feature.properties.mag, markerColor]);
            
            marker = L.circleMarker(latlng, {
                radius: size,
                fillColor: markerColor,
                color: "#000",
                weight: 2,
                fillOpacity: 0.5,
              
            })
            return marker;
        },
        // add popup at each point
        onEachFeature: function popUpText(feature, layer) {
            layer.bindPopup(`Location: <strong>${feature.properties.place}</strong><br>` +
                            `Earthquake Magnitude: <strong>${feature.properties.mag}</strong>`);
        }
    });
    
    // sort legend
    legendData.sort(function(a, b){return a[0]-b[0]})

    // call to tectonic plates json file
    d3.json(link, function(error) {
        if (error) {
            console.warn(error);    
            };
        
        // create leaflet map
        var myMap = L.map("map", {
            center: [40, -105.71],
            zoom: 4,
            layers: [
                sataliteMap, equakeLayer
            ]
        });

        var legend = L.control({
            position: "bottomright"
        });

        legend.onAdd = function() {
            var div = L.DomUtil.create("div", "info legend");

            var labels = [];
            
            // legend min max
            var legendInfo = "<h1>Earthquake Magnitude</h1>" +
        "<div class='labels'>" +
            "<div class='min'>" + legendData[0][0] + "</div>" +
            "<div class='max'>" + legendData[legendData.length - 1][0] + "</div>" +
        "</div>";

            div.innerHTML = legendInfo;

            legendData.forEach(function(marker) {
                labels.push("<li style='background-color: " + marker[1] + "'></li>");
            });

            div.innerHTML += "<ul>" + labels.join("") + "</ul>";

            return div;
        };

        // Add legend to map
        legend.addTo(myMap);
    });
});