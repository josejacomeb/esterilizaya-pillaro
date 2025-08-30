function actualizarSelectorCantonParroquia(ciudadId, parroquiaId, url) {
  const $ciudad = $(`#${ciudadId}`);
  const $parroquia = $(`#${parroquiaId}`);

  function cargarParroquias() {
    const canton = $ciudad.val();
    $parroquia.empty();

    if (canton) {
      $.getJSON(url, { canton }, function (data) {
        (data.parroquias || []).forEach((parroquia) => {
          $parroquia.append($("<option>").val(parroquia).text(parroquia));
        });
      });
    }
  }

  $ciudad
    .off("change.actualizarParroquia")
    .on("change.actualizarParroquia", cargarParroquias);

  // Load parroquias at startup
  cargarParroquias();
}
