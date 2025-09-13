function inicializarMapa(locaciones, locacionesDataUrl) {
  $.getJSON(locacionesDataUrl, function(data) {
    const map = L.map('mapa').setView([-1.1690711, -78.5168839], 11);
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
      attribution: '&copy; OpenStreetMap contributors'
    }).addTo(map);

    $.each(locaciones, function(_, locacion) {
      const [canton, parroquia, barrio, conteo] = locacion;
      let lat = null, lon = null;
      if (data[canton] && data[canton][parroquia] && data[canton][parroquia][barrio]) {
        [lat, lon] = data[canton][parroquia][barrio];
      }
      if (lat && lon) {
        L.marker([lat, lon]).addTo(map)
          .bindPopup(`${barrio}: ${conteo}`);
      }
    });
    setTimeout(function() { map.invalidateSize(); }, 100);
  });
}