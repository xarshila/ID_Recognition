
function fill_card_data(data){
    $("#first_name")[0].value =  data.name_ge + " / " + data.name_en
    $("#last_name")[0].value =  data.last_name_ge + " / " + data.last_name_en
    $("#nationality")[0].value =  data.nation
    $("#person_id")[0].value =  data.person_id
    $("#sex")[0].value =  data.sex
    $("#birth_date")[0].value =  data.birth_date
    $("#expiry_date")[0].value =  data.exp_date
    $("#card_id")[0].value =  data.card_id
    $("#card_photo_img")[0].src = "data:image/png;base64," + data.photo
}
function read_id_card(){
    image_data = $("#card-photo")[0].files[0]
    data = {
        fields: ["name_en"],
        image: image_data
    }
    form_data = new FormData()
    form_data.append("fields", ["name_en", "name_ge", "birth_date", "exp_date"])
    form_data.append("image", image_data)
    $("#id_card_div").hide()
    $.ajax({
        type: 'POST',
        url: window.location.origin + "/read",
        data: form_data,
        processData: false, 
        contentType: false, 
        success: function(data) {
            fill_card_data(data)
            $("#id_card_div").show()
         }
    }); 
}
$(function(){
    $("#process-button").click(read_id_card)
});