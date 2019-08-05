var uri = window.location.pathname, res='';
uri = uri.substring(1, uri.length - 1).split('/')
var device = uri[0], room = uri[1];

function light_update() {
    $.get("/0/L1", function(data, status) {
        if (status != 'success') {
            exit();
        }
        if (room == 'living1') {
            if (data.indexOf("10") == -1) {
                $("#now_data").text("");
                $("#btn-off").attr("disabled", true);
                $("#btn-on").attr("disabled", false);
            }
            else {
                $("#now_data").text("");
                $("#btn-off").attr("disabled", false);
                $("#btn-on").attr("disabled", true);
            }
        }
        if (room == 'living2') {
            if (data.indexOf("20") == -1) {
                $("#now_data").text("");
                $("#btn-off").attr("disabled", true);
                $("#btn-on").attr("disabled", false);
            }
            else {
                $("#now_data").text("");
                $("#btn-off").attr("disabled", false);
                $("#btn-on").attr("disabled", true);
            }
        }
        if (room == 'hallway') {

        }
    });
}

function gas_update() {
    $.get("/1/R1", function(data, status) {
        if (status != "success") {
            exit();
        }
        if (data.indexOf("10") == -1) {
            $("#now_data").text("closed");
            $("#btn-off").attr("disabled", true);
        }
        else {
            $("#now_data").text("");
            $("#btn-off").attr("disabled", false);
        }
    });
}

function heating_update() {
    room_code = room=='living'?'L1':room=='bed'?'R1':room=='seohun'?'R3':'R2';
    var flag = 0;
    $.get("/2/" + room_code, function(data, status) {
        if (status != "success") {
            exit();
        }
        if (data.indexOf("p0") == -1) {
            $("#btn-off").attr("disabled", true);
            $("#btn-on").attr("disabled", false);
            $("#temp").attr("disabled", true);
            $("#button-set").attr("disabled", true);
        }
        else {
            $("#btn-on").attr("disabled", true);
            $("#btn-off").attr("disabled", false);
            $("#temp").attr("disabled", false);
            $("#button-set").attr("disabled", false);
            flag = 1;
        }

        var tmp = new Array;
        for (var i=0; i<4; ++i) {
            tmp[i] = data.substring(data.indexOf("num") + 3, data.indexOf("num") + 4) - '0';
            data = data.substring(data.indexOf("num") + 5);
        }
        var nowtemp = tmp[0] * 10 + tmp[1];
        var settemp = tmp[2] * 10 + tmp[3];
        
        $("#now_data").text('now ' + nowtemp + '°C');
        if (flag == 1) {
            $("#now_data").text($("#now_data").text() + ', set ' + settemp + '°C');
        }
    });
}

function ventil_update() {
    $.get("/5/L1", function(data, status) {
        if (status != "success") {
            exit();
        }
        if (data.indexOf("p0") == -1) {
            $("#now_data").text('');
            $("#btn-off").attr("disabled", true);
            $("#btn-on").attr("disabled", false);
            $(".wind-p").attr("disabled", true);
        }
        else {
            $("#now_data").text('');
            $("#btn-on").attr("disabled", true);
            $("#btn-off").attr("disabled", false);
            $(".wind-p").attr("disabled", false);
        }
    })
}

function update() {
    if (device == 'light') light_update();
    if (device == 'heating') heating_update();
    if (device == 'gas') gas_update();
    if (device == 'ventilation') ventil_update();
}