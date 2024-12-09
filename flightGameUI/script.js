// Initialize the script
const script = L.map('script').setView([60.2934, 24.9633], 10); // Coordinates for Helsinki, Finland

// Add a tile layer (script appearance)
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
  attribution: '© OpenStreetMap contributors'
}).addTo(script);

// Optional: Add a marker for Helsinki Airport
L.marker([60.2934, 24.9633])
  .addTo(script)
  .bindPopup('Helsinki Vantaa Airport')
  .openPopup();
