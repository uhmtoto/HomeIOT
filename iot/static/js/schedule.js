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
        var _time = $("#s_time").val();
        var io = $("#btn-on").attr("disabled") ? 'i' : 'o';
        var _temp = $("#s_temp").val();
        if (io == 'o') {
            _temp = '0';
        }
        //validate temp
        if (_temp < 5 || _temp > 40) {
            alert('err');
        }
        //validate time
        else if (_time / 100 < 0 || _time / 100 > 24 || _time % 100 >= 60) {
            alert('err');
        }
        else {
            $.post('#', {
                    time: _time,
                    temp: _temp
                }, function(data) {
                    if (data == 'ok') {
                        alert('scheduled successfully');
                    }
                    else {
                        alert(data);
                    }
                }
            );
        }
    });
});