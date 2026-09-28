const students = {
  IAI0001: "Ada Lovelace",
  IAI0002: "Alan Turing",
  IAI0003: "Grace Hopper",
};

const form = document.querySelector("#student-form");
const input = document.querySelector("#enrollment");
const result = document.querySelector("#result");
const resultType = document.querySelector("#result-type");
const studentName = document.querySelector("#student-name");
const studentEnrollment = document.querySelector("#student-enrollment");
const downloadLink = document.querySelector("#download-link");

form.addEventListener("submit", (event) => {
  event.preventDefault();
  const enrollment = input.value.trim().toUpperCase();
  const name = students[enrollment];

  result.classList.remove("hidden", "success", "error");
  if (name) {
    result.classList.add("success");
    resultType.textContent = "ESTUDIANTE ENCONTRADO";
    studentName.textContent = name;
    studentEnrollment.textContent = `Matrícula: ${enrollment}`;
    downloadLink.href = `/downloads/kardex-${enrollment}.pdf`;
    downloadLink.classList.remove("hidden");
  } else {
    result.classList.add("error");
    resultType.textContent = "EXCEPCIÓN DE NEGOCIO";
    studentName.textContent = "Matrícula inexistente";
    studentEnrollment.textContent = `No se encontró ${enrollment || "una matrícula"}.`;
    downloadLink.classList.add("hidden");
    downloadLink.removeAttribute("href");
  }
});

