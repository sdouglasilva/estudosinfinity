debugger;

const botao = document.querySelector("button");
function exibirMediaPonderada() {
  const n1 = Number(document.getElementById("n1").value);
  const n2 = Number(document.getElementById("n2").value);
  const n3 = Number(document.getElementById("n3").value);
  const p1 = Number(document.getElementById("p1").value);
  const p2 = Number(document.getElementById("p2").value);
  const p3 = Number(document.getElementById("p3").value);
  console.log(n1);
  let somaPesos = p1 + p2 + p3;
  console.log(n1);
  console.log(somaPesos);
  let notaPeso = n1 * p1 + n2 * p2 + n3 * p3;
  console.log(notaPeso);
  let mediaPonderada = notaPeso / somaPesos;
  console.log(mediaPonderada);
  const espaco2 = document.getElementsByClassName("espaco2");
  espaco2[0].append(mediaPonderada);
}
botao.addEventListener("click", exibirMediaPonderada);
