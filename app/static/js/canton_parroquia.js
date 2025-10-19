// eslint-disable-next-line no-unused-vars
function actualizarSelectorCantonParroquia(ciudadId, parroquiaId, url) {
	const $ciudad = $(`#${ciudadId}`);
	const $parroquia = $(`#${parroquiaId}`);

	function cargarParroquias() {
		const canton = $ciudad.val();
		const defaultParroquiaValue = $parroquia.val();
		$parroquia.empty();

		if (canton) {
			$.getJSON(url, { canton }, function (data) {
				let matchCantonValue = false;
				(data.parroquias || []).forEach((parroquia) => {
					$parroquia.append($("<option>").val(parroquia[0]).text(parroquia[1]));
					if (parroquia[0] === defaultParroquiaValue) {
						matchCantonValue = true;
					}
				});
				if (matchCantonValue) {
					$parroquia.val(defaultParroquiaValue);
				}
			});
		}
	}

	$ciudad
		.off("change.actualizarParroquia")
		.on("change.actualizarParroquia", cargarParroquias);

	// Load parroquias at startup
	cargarParroquias();
}
