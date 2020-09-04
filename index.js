function calculate(){
var data = new FormData();
data.append('amount', document.getElementById("amount").value);
data.append('product', document.getElementById("product").value);
//    var json = JSON.stringify({
//      amount: document.getElementById("amount").value,
//      product: document.getElementById("product").value
//    });

    var xmlhttp = new XMLHttpRequest();
    var url = "http://127.0.0.1:8001/";

    xmlhttp.onreadystatechange = handleResponse;
    xmlhttp.open("POST", url, true);
    xmlhttp.send(data);
//    console.log(xmlhttp.responseText);
    console.log(xmlhttp)
}

function renderResults(results) {
     document.getElementById("b1").innerHTML = results.prod_protein
     document.getElementById("j1").innerHTML = results.prod_fat
     document.getElementById("u1").innerHTML = results.prod_carb
}

function handleResponse(){
    if (this.readyState == 4 && this.status == 200) {
        var responseText = this.responseText

        console.log(this)
//        console.log(responseText)
//        var parsedjson = JSON.parse(responseText)
//        console.log(parsedjson)
//        renderResults(parsedjson);
        }
    };
