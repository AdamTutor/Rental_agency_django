var total = 0;
var button_ids = ['ps4', 'vr', 'ps4_controller','a', 'xbox1', 'kinect','xbox_controller','b','dt1','dt2',"laptop1", "laptop2", "ps4_motion", "xbox1_console","keyboard"]


function addToCart(name){
    var item = name;
    $('#receipt').append("<p>" + item + "</p>")

}


function Total(total){
    $("#total_price").empty()
     $("#total_price").append(total)
}



$(document).ready(function(){
    $("button").click(function(){
        
if (button_ids.includes(this.id)){
    addToCart(this.id)
};
if (this.id == 'ps4' || 'xbox1' || 'dt1' || 'dt2' || 'laptop1' || 'laptop2'){
total += 3
}
else if (this.id="total_price") {
    total += 0
} 
else{
    total += 1
}



$('#submit').click(function(){
        Total(total)
    });

});

    });

    
    




