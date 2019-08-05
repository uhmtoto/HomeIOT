$(document).ready(function() {
    $(".set").click(function() {
        $.get($(this).attr("data"), function(data, status){
            if (data == 'ok' && status == 'success') {
                update();
            }
            else {
                alert('there are some errors..');
            }
        });
    });
    $(".temp-set").click(function() {
        var usr_temp = $("#temp").val()
        if (usr_temp < 5 || usr_temp > 40) {
            alert('over limit\n5 ~ 40 (°C)');
            exit();
        }
        $.get($("#temp").val(), function(data, status){
            if (data == 'ok' && status == 'success') {
                update();
            }
            else {
                alert('there are some errors..');
            }
        });
    });
});