/* exported inicializarGraficos */
function inicializarGraficos (datos) {
  // Especies
  new Chart($('#graficoEspecie'), {
    type: 'doughnut',
    data: {
      labels: datos.estadisticasEspecie.map((s) => s.especie),
      datasets: [
        {
          data: datos.estadisticasEspecie.map((s) => s.total),
          backgroundColor: [
            '#36A2EB',
            '#FF6384',
            '#FF9F40',
            '#4BC0C0',
            '#9966FF',
            '#FFCD56',
            '#C9CBCF'
          ]
        }
      ]
    }
  })

  // Género
  new Chart($('#graficoGenero'), {
    type: 'doughnut',
    data: {
      labels: datos.genderStats.map((g) => g.sexo),
      datasets: [
        {
          data: datos.genderStats.map((g) => g.total),
          backgroundColor: ['#4BC0C0', '#FFCE56', '#36A2EB']
        }
      ]
    }
  })

  // Parroquias
  new Chart($('#graficoParroquia'), {
    type: 'doughnut',
    data: {
      labels: datos.parroquiaStats.map((g) => g.parroquia_tutor),
      datasets: [
        {
          data: datos.parroquiaStats.map((g) => g.total),
          backgroundColor: ['#4BC0C0', '#FFCE56', '#36A2EB']
        }
      ]
    }
  })

  // Barrios
  new Chart($('#graficoBarrios'), {
    type: 'doughnut',
    data: {
      labels: datos.barrioStats.map((g) => g.barrio_tutor),
      datasets: [
        {
          data: datos.barrioStats.map((g) => g.total),
          backgroundColor: ['#4BC0C0', '#FFCE56', '#36A2EB']
        }
      ]
    }
  })

  // Razas
  new Chart($('#graficoRaza'), {
    type: 'bar',
    data: {
      labels: datos.razaStats.map((n) => n.raza_mascota),
      datasets: [
        {
          label: 'Conteo',
          data: datos.razaStats.map((n) => n.total),
          backgroundColor: '#36A2EB'
        }
      ]
    },
    options: {
      responsive: true,
      plugins: { legend: { display: false } },
      scales: {
        x: { ticks: { autoSkip: false } },
        y: { beginAtZero: true }
      }
    }
  })
}