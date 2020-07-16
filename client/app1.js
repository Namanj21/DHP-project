  function getBHKValue() {
    var uiBHK = document.getElementsByName("uiBHK");
    for(var i in uiBHK) {
        if(uiBHK[i].checked) {
            return parseInt(i)+1;
        }
    }

    return -1;
}

function OnClickedEstimatePrice() {

    console.log("Estimate price button clicked");
    var area = document.getElementById("uisqft");
    var bhk = getBHKValue();
    var locations = document.getElementById("uiLocations");
    var estPrice = document.getElementById("uiEstimatedPrice");

    var url = "http://127.0.0.1:5000/predict_home_price";

    $.post(url , {
        area: parseFloat(area.value),
        bhk: bhk,
        location : locations.value
    },function(data, status) {
        console.log(data.estimated_price);
        estPrice.innerHTML = "<h2>" + data.estimated_price.toString() + " RS </h2>";
        console.log(status);

    });

}

function onPageLoad() {

    console.log("document loaded");
    var url = "http://127.0.0.1:5000/get_location_names";
    $.get(url,function(data, status) {
        console.log("got response for get_location_names request");
        if(data) {
            var location = data.locations;
            var uiLocations = document.getElementById("uiLocations");
            $('#uiLocations').empty();
            for(var i in location) {

                var opt = new Option(location[i]);
                $('#uiLocations').append(opt);

            }
        }
    });

}

window.onload = onPageLoad;