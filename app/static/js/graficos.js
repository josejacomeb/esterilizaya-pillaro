function generateColors(count) {
	const baseColors = [
		"#36A2EB",
		"#FF6384",
		"#FF9F40",
		"#4BC0C0",
		"#9966FF",
		"#FFCD56",
		"#C9CBCF",
		"#FF8A80",
		"#82B1FF",
		"#B39DDB",
		"#CCFF90",
		"#FFE57F",
		"#84FFFF",
		"#F48FB1",
		"#80CBC4",
		"#DCE775",
	];

	// If we need more colors than we have, generate them
	while (baseColors.length < count) {
		const h = Math.random() * 360;
		const s = 25 + Math.random() * 70 + "%";
		const l = 45 + Math.random() * 25 + "%";
		baseColors.push(`hsl(${h}, ${s}, ${l})`);
	}
	return baseColors.slice(0, count);
}

/* exported inicializarGraficos */
function inicializarGraficos(datos) {
	// Especies
	new Chart($("#graficoEspecie"), {
		type: "doughnut",
		data: {
			labels: datos.estadisticasEspecie.map((s) => s.especie),
			datasets: [
				{
					data: datos.estadisticasEspecie.map((s) => s.total),
					backgroundColor: generateColors(datos.estadisticasEspecie.length),
				},
			],
		},
	});

	// Género
	new Chart($("#graficoGenero"), {
		type: "doughnut",
		data: {
			labels: datos.genderStats.map((g) => g.sexo),
			datasets: [
				{
					data: datos.genderStats.map((g) => g.total),
					backgroundColor: generateColors(datos.genderStats.length),
				},
			],
		},
	});

	// Parroquias
	new Chart($("#graficoParroquia"), {
		type: "doughnut",
		data: {
			labels: datos.parroquiaStats.map((g) => g.parroquia_tutor),
			datasets: [
				{
					data: datos.parroquiaStats.map((g) => g.total),
					backgroundColor: generateColors(datos.parroquiaStats.length),
				},
			],
		},
	});

	// Barrios
	new Chart($("#graficoBarrios"), {
		type: "doughnut",
		data: {
			labels: datos.barrioStats.map((g) => g.barrio_tutor),
			datasets: [
				{
					data: datos.barrioStats.map((g) => g.total),
					backgroundColor: generateColors(datos.barrioStats.length),
				},
			],
		},
	});

	// Razas
	new Chart($("#graficoRaza"), {
		type: "bar",
		data: {
			labels: datos.razaStats.map((n) => n.raza_mascota),
			datasets: [
				{
					label: "Conteo",
					data: datos.razaStats.map((n) => n.total),
					backgroundColor: generateColors(datos.razaStats.length),
				},
			],
		},
		options: {
			responsive: true,
			plugins: { legend: { display: false } },
			scales: {
				x: { ticks: { autoSkip: false } },
				y: { beginAtZero: true },
			},
		},
	});
}
