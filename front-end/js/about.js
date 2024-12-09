'use strict';

function updateTime() {
  const now = new Date();
  const hours = now.getHours().toString().padStart(2, '0');
  const minutes = now.getMinutes().toString().padStart(2, '0');
  const seconds = now.getSeconds().toString().padStart(2, '0');
  document.getElementById('time').textContent = `${hours}:${minutes}:${seconds}`;
}

function displayDate()  {
  const now = new Date();
  const day = now.getDate().toString().padStart(2, '0');
  const month = (now.getMonth() + 1).toString().padStart(2, '0');
  const year = now.getFullYear();
  document.getElementById('date').textContent = `${day}/${month}/${year}`;
}

async function details() {
  const monument = document.querySelector('#monument');
  const table = document.createElement('table');

  const row = table.insertRow(0);
  const cell1 = row.insertCell(0);
  cell1.innerHTML = 'ID';
  const cell2 = row.insertCell(1);
  cell2.innerHTML = 'Name';
  const cell3 = row.insertCell(2);
  cell3.innerHTML = 'Location';

  try {
    const response = await fetch('http://127.0.0.1:5000/get_monument_table')
    const losers = await response.json();
    for (const loser of losers) {
      const row = table.insertRow();
      const cell1 = row.insertCell(0);
      cell1.innerHTML = loser['ID'];
      const cell2 = row.insertCell(1);
      cell2.innerHTML = loser['Name'];
      const cell3 = row.insertCell(2);
      const txt = await fetch(`http://127.0.0.1:5000/locate/code=${loser['Place Of Sacrifice']}`);
      const json_txt = await txt.json();
      cell3.innerHTML = `${json_txt['Name']}, ${json_txt['Municipality']}, ${json_txt['Country']}`;
    }
    monument.appendChild(table);
  } catch (error) {
    console.log(error.message);
  }
}

updateTime();
setInterval(updateTime, 1000);
displayDate();

details();