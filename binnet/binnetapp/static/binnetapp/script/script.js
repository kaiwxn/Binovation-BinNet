
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

// Define marker colors for ranking
var greenIcon = new L.Icon({
    iconUrl: 'https://raw.githubusercontent.com/pointhi/leaflet-color-markers/master/img/marker-icon-2x-green.png',
    shadowUrl: 'https://cdnjs.cloudflare.com/ajax/libs/leaflet/0.7.7/images/marker-shadow.png',
    iconSize: [25, 41],
    iconAnchor: [12, 41],
    popupAnchor: [1, -34],
    shadowSize: [41, 41]
});

var orangeIcon = new L.Icon({
    iconUrl: 'https://raw.githubusercontent.com/pointhi/leaflet-color-markers/master/img/marker-icon-2x-orange.png',
    shadowUrl: 'https://cdnjs.cloudflare.com/ajax/libs/leaflet/0.7.7/images/marker-shadow.png',
    iconSize: [25, 41],
    iconAnchor: [12, 41],
    popupAnchor: [1, -34],
    shadowSize: [41, 41]
});

var redIcon = new L.Icon({
    iconUrl: 'https://raw.githubusercontent.com/pointhi/leaflet-color-markers/master/img/marker-icon-2x-red.png',
    shadowUrl: 'https://cdnjs.cloudflare.com/ajax/libs/leaflet/0.7.7/images/marker-shadow.png',
    iconSize: [25, 41],
    iconAnchor: [12, 41],
    popupAnchor: [1, -34],
    shadowSize: [41, 41]
});

for (var i = 0; i < data.length; i++) {
    id = data[i][0];
    latitude = data[i][1];
    longitude = data[i][2];
    color = data[i][3];

    switch (color) {
        case 'O':
            icon = orangeIcon;
            break;
        case 'R':
            icon = redIcon;
            break;
        default:
            icon = greenIcon;
            break;
    }

    L.marker([latitude, longitude], { icon: icon }).addTo(map)
        .bindPopup("Mülleimer " + id + " " + "lat: " + latitude + " lon: " + longitude + " color: " + color);
}