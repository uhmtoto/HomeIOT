$(document).ready(function() {
    $("#btn-on").click(function() {
        $("#s_temp").attr("disabled", false);
        $("#btn-on").attr("disabled", true);
        $("#btn-off").attr("disabled", false);
    });
    $("#btn-off").click(function() {
        $("#s_temp").attr("disabled", true);
        $("#btn-on").attr("disabled", false);
        $("#btn-off").attr("disabled", true);
    });

    $("#set").click(function() {
        var time = $("#s_time").val();
        var io = $("#btn-on").attr("disabled") ? 'i' : 'o';
        var temp = $("#s_temp").val();
        if (io == 'o') {
            temp = '5';
        }
        $.get('./'+time+'/'+io+'/'+temp, function(data, status) {
            if (data == 'ok') {
                alert('scheduled successfully');
            }
            else {
                alert(data);
            }
        });
    });
});