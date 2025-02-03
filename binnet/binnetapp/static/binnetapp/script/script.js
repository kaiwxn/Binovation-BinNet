// Creating map options
const mapOptions = {
    center: [48.060863614253165, 11.670241807559309], // Set center of Map to "Wolf-Ferrari-Haus"
    zoom: 14,
    minZoom: 14,
};

// Creating a map object
const map = new L.map('map', mapOptions);

// Creating a Layer object
const layer = new L.TileLayer('http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png');

// Adding layer to the map
map.addLayer(layer);

// Add markers to the map
const data = JSON.parse(document.getElementById('bin-data').textContent);

// Define marker colors for ranking
const greenIcon = new L.Icon({
    iconUrl: 'https://raw.githubusercontent.com/pointhi/leaflet-color-markers/master/img/marker-icon-2x-green.png',
    shadowUrl: 'https://cdnjs.cloudflare.com/ajax/libs/leaflet/0.7.7/images/marker-shadow.png',
    iconSize: [25, 41],
    iconAnchor: [12, 41],
    popupAnchor: [1, -34],
    shadowSize: [41, 41]
});

const orangeIcon = new L.Icon({
    iconUrl: 'https://raw.githubusercontent.com/pointhi/leaflet-color-markers/master/img/marker-icon-2x-orange.png',
    shadowUrl: 'https://cdnjs.cloudflare.com/ajax/libs/leaflet/0.7.7/images/marker-shadow.png',
    iconSize: [25, 41],
    iconAnchor: [12, 41],
    popupAnchor: [1, -34],
    shadowSize: [41, 41]
});

const redIcon = new L.Icon({
    iconUrl: 'https://raw.githubusercontent.com/pointhi/leaflet-color-markers/master/img/marker-icon-2x-red.png',
    shadowUrl: 'https://cdnjs.cloudflare.com/ajax/libs/leaflet/0.7.7/images/marker-shadow.png',
    iconSize: [25, 41],
    iconAnchor: [12, 41],
    popupAnchor: [1, -34],
    shadowSize: [41, 41]
});

// Function to get icon based on color
const getIconByColor = (color) => {
    switch (color) {
        case 'O':
            return orangeIcon;
        case 'R':
            return redIcon;
        default:
            return greenIcon;
    }
};

// Add markers to the map
data.forEach(bin => {
    const [id, latitude, longitude, color, fillrate] = bin;
    const icon = getIconByColor(color);

    L.marker([latitude, longitude], { icon: icon }).addTo(map)
        .bindPopup(
            `Mülleimer ${id} | Koordinaten: ${latitude}, ${longitude} | Ranking: ${color} | Füllrate: ${fillrate}cm/h`
        );
});
