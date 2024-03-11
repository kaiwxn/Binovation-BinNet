

// Creating map options
var mapOptions = {
    center: [48.060863614253165, 11.670241807559309], // Set center of Map to "Wolf-Ferrari-Haus"
    zoom: 14,
    minZoom: 14,
}

// Creating a map object
var map = new L.map('map', mapOptions);

// Creating a Layer object
var layer = new L.TileLayer('http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png');

// Adding layer to the map
map.addLayer(layer);

// Add markers to the map
const data = JSON.parse(document.getElementById('bin-data').textContent);

for (var i = 0; i < data.length; i++) {
    id = data[i][0];
    latitude = data[i][1];
    longitude = data[i][2];

    L.marker([latitude, longitude]).addTo(map)
        .bindPopup("Mülleimer " + id + " " + "lat: " + latitude + " lon: " + longitude);
}
