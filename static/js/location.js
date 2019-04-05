
$(document).ready(function(){
});

function myMap() {
    var mapProp= {
        center:new google.maps.LatLng(25.406760, 55.452641),
        zoom:17,
    };
    var map=new google.maps.Map(document.getElementById("gt-location"),mapProp);
}