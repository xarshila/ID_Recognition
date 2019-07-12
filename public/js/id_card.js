
function fill_card_data(data){
    $("#first_name_ge")[0].value = data.name_ge
    $("#first_name_en")[0].value = data.name_en 
    $("#last_name_ge")[0].value = data.last_name_ge
    $("#last_name_en")[0].value = data.last_name_en
    $("#nationality")[0].value =  data.nation
    $("#person_id")[0].value =  data.person_id
    $("#sex")[0].value =  data.sex
    $("#birth_date")[0].value =  data.birth_date
    $("#expiry_date")[0].value =  data.exp_date
    $("#card_id")[0].value =  data.card_id
    $("#card_photo_img")[0].src = "data:image/png;base64," + data.photo
    $("#detected_rect")[0].src = "data:image/png;base64," + data.detected_rect
    $("#field_first_name_en")[0].src = "data:image/png;base64," + data.field.name_en
    $("#field_first_name_ge")[0].src = "data:image/png;base64," + data.field.name_ge
    $("#field_last_name_en")[0].src = "data:image/png;base64," + data.field.last_name_en
    $("#field_last_name_ge")[0].src = "data:image/png;base64," + data.field.last_name_ge
    $("#field_card_id")[0].src = "data:image/png;base64," + data.field.card_id
    $("#field_person_id")[0].src = "data:image/png;base64," + data.field.person_id
    $("#field_nation")[0].src = "data:image/png;base64," + data.field.nation
    $("#field_sex")[0].src = "data:image/png;base64," + data.field.sex
    $("#field_birth_date")[0].src = "data:image/png;base64," + data.field.birth_date
    $("#field_exp_date")[0].src = "data:image/png;base64," + data.field.exp_date

}
function read_id_card(){
    image_data = $("#card-photo")[0].files[0]
    data = {
        fields: ["name_en"],
        image: image_data
    }
    form_data = new FormData()
    form_data.append("debug", true)
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