async function upload() {
const fileInput = document.getElementById("pdfFile");
const status = document.getElementById("status");
const table = document.getElementById("resultsTable");
const tbody = document.getElementById("resultsBody");


status.textContent = "";
tbody.innerHTML = "";
table.style.display = "none";


if (!fileInput.files.length) {
status.textContent = "Seleccione un archivo PDF.";
status.className = "status error";
return;
}


const formData = new FormData();
formData.append("file", fileInput.files[0]);


status.textContent = "Analizando PDF...";


try {
const res = await fetch("/check-duplicates", {
method: "POST",
body: formData
});


const data = await res.json();


if (data.status === "ok") {
status.textContent = data.message;
status.className = "status no-duplicates";
return;
}


status.textContent = `Se encontraron ${data.total} nombres duplicados`;
status.className = "status";


for (const nombre in data.data) {
data.data[nombre].forEach(item => {
const row = document.createElement("tr");
row.innerHTML = `
<td>${nombre}</td>
<td>${item.pagina}</td>
<td>${item.linea}</td>
`;
tbody.appendChild(row);
});
}


table.style.display = "table";


} catch (err) {
status.textContent = "Error conectando con el servidor.";
status.className = "status error";
}
}