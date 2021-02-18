jQuery(document).ready(function() {
    jQuery('#hid').on('click', function(event) {
        jQuery('#test').toggle()
        $(document).scrollTop(200)
    });
    jQuery('#hid1').on('click', function(event) {
        jQuery('#test1').toggle()
        $(document).scrollTop(800)
    });
    jQuery('#hid2').on('click', function(event) {
        jQuery('#test2').toggle()
        $(document).scrollTop(800)
    });
});

// one key up function

$.ajaxSetup({
    headers: {
        "X-CSRFToken": '{{csrf_token}}'
    }
});
checkname = function() {
    $.ajax({

        url: 'inputcheck',
        type: 'POST',
        data: {
            name: $('#username').val(),

        },
        success: function(response) {
            console.log(response.error)
            document.getElementById('error').innerHTML = response.error



        }

    });
}


$.ajaxSetup({
    headers: {
        "X-CSRFToken": '{{csrf_token}}'
    }
});

function view(y) {

    $.ajax({
        url: 'view_data_aj',
        type: 'POST',
        data: {
            view_id: y,

        },
        success: function(response) {
            a = response.key[0]['data1']

            document.getElementById('firstname').value = response.key[0]['data2']
            document.getElementById('lastname').value = response.key[0]['data3']
            document.getElementById('email').value = response.key[0]['data4']
            document.getElementById('mobileno').value = response.key[0]['data5']
            document.getElementById('postad').value = response.key[0]['data6']
            document.getElementById('Uname').value = response.key1[0]['data_cred_1']
            document.getElementById('pword').value = response.key1[0]['data_cred_2']
            document.getElementById('status').value = response.key[0]['data7']
            document.getElementById('joiningdate').value = response.key[0]['data8']
        }

    });

}

// Update Function

function update(x) {
    $.ajax({
        url: 'update_aj',
        type: 'POST',
        data: {
            update_id: x,
            f_name: $('#firstname').val(),
            l_name: $('#lastname').val(),
            e_mail: $('#email').val(),
            mob_no: $('#mobileno').val(),
            post_ad: $('#postad').val(),
            p_word: $('#pword').val(),
            u_status: $('#status').val(),
            u_join_date: $('#joiningdate').val()
        },
        success: function(response) {

            alert(response.key_update);
            // $("#display").append("#show");
            window.location.href = '/addins/'

        }
    });
}

// function hidden() {
//     $('#hideaction').hide();
// }


// function showaction() {
//     $('#hideaction').show();

// }

// function showaction() {
//     document.getElementById('hideaction').style.display = "block";
// }