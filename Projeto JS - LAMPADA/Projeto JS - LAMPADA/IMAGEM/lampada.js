const botao = document.getElementById('botao');
const lampada = document.getElementById('lampada');
const botaooff = document.getElementById('botaooff');
const quebrar = document.getElementById('botaoquebrar');
const botaoPiscar = document.getElementById('botaopiscar');


function acenderLampada () {
    if (botao.value === "ligar")
    lampada.src = './IMAGEM/Lampada.jpeg'
        else if (botao.value === "ligar")
        lampada.src = './IMAGEM/Apagada.jpeg'
    
};

function apagarLampada (){
    if (botaooff.value ==="apagar")
    lampada.src ='./IMAGEM/LampApagada.jpeg'
};

function quebrarLampada (){
    if (quebrar.value ==="quebrar")
    lampada.src ='./IMAGEM/LampQuebrada.jpeg'
    };

    function piscarLampada (){
        let contador = 0;
        let intervalo =0;
        while(contador < 10) {
            intervalo +=300;
            setTimeout("document.getElementById('lampada').src='./IMAGEM/Lampada.jpeg';",intervalo);
            intervalo +=300;
            setTimeout("document.getElementById('lampada').src='./IMAGEM/LampApagada.jpeg';",intervalo);
            intervalo +=300;
            contador++;


}
}