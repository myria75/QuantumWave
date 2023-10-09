const btnSubmit = document.querySelector(".positive-button");
const inputTxtArea = document.querySelector(".input-textarea");

btnSubmit.addEventListener("click", e => { 
    try {
        doPost(inputTxtArea.value);
    } catch (error) {
        alert(error);
    }
});

function doPost(xml_str) {
    $.ajax(
        {
            data : xml_str,
            url : 'http://127.0.0.1:8000/xml_check/',
            type : "post",
            success : querySuccess,
            error: queryError,
            crossDomain: true,
            headers: { "Accept": "text/xml"}
        }
    );
}

function querySuccess(response) {
    alert(response)
    if (response["correct"]) {
        alert('Vamos bien');
    } else {
        alert('Vamos mal');    
    }
}

function queryError(response) {
    console.log(response)
    alert(response);
    alert('Vamos mal');
}

function cleanXML(xml_str) {
    let xml_nl = xml_str.replace("\n", "");
    let xml_bl = xml_nl.replace(" ", "");
    let xml_tb = xml_bl.replace("\t", "");
    return xml_tb;
}