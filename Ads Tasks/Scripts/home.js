let n = 1;

document.getElementById("iconu").addEventListener("click", function(){

    if (n == 1){
        document.getElementById("list").style.display = "block";
        n = 2;
    } else {
        document.getElementById("list").style.display = "none";
        n = 1;
    }
});