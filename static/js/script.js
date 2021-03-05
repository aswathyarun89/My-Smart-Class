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

$.ajaxSetup({
    headers: {
        "X-CSRFToken": '{{csrf_token}}'
    }
});

function load_addins() {
    $("#searchtableheader").hide();
    $.ajax({
        url: 'dis_data_addins',
        type: 'GET',

        success: function(response) {
            b = response.key

            for (i = 0; i < b.length; i++) {
                $("#display").append("<tr><td><a href=''  data-toggle='modal' data-target='#exampleModalLong' data-backdrop='static' data-keyboard='false'onclick='view(" + b[i].iden1 + ")'>" + b[i].iden1 + "</a></td><td>" + b[i].iden2 + "</td><td>" + b[i].iden3 + "</td><td>" + b[i].iden4 + "</td></tr>")

            }
        }
    });
}
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

submit = function() {
    $("#maintableheader").hide();
    $("#searchtableheader").show();
    $.ajax({

        url: 'exact_url',
        type: 'POST',
        data: {
            name: $('#search_box').val(),

        },
        success: function(response) {
            document.getElementById('display').innerHTML = ""

            b = response.key_id


            for (i = 0; i < b.length; i++) {
                $("#display").append("<tr><td>" + b[i].key1 + "</td><td>" + b[i].key2 + "</td><td>" + b[i].key3 + "</td><td>" + b[i].key4 + "</td><td><button class='btn btn-success' data-toggle='modal' data-target='#exampleModalLong' data-backdrop='static' data-keyboard='false'onclick='view(" + b[i].key1 + ")'>View/Edit</button></td></tr>")


            }

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
                // photo_id = response.key[0]['data9']
                // console.log(photo_id)
            first_name = response.key[0]['data2']

            last_name = response.key[0]['data3']
            fullname = first_name.concat(" ", last_name)
            if (response.key[0]['data9'] == "") {
                document.getElementById('photo').innerHTML = ('<img class="img-fluid rounded" style="width:80px" src="/static/images/default_profile_pic_male.jpg">')
            } else {
                document.getElementById('photo').innerHTML = ('<img class="img-fluid rounded" style="width:80px" src="/myapp2/media/' + response.key[0]['data9'] + '">')
            }

            // document.getElementById('photo').innerHTML = ('<img class="img-fluid rounded" style="width:80px" src="/myapp2/media/' + response.key[0]['data9'] + '">')
            document.getElementById('instructortype').innerHTML = response.key1[0]['data_cred_3']
            document.getElementById('exampleModalLongTitle').innerHTML = fullname
            document.getElementById('firstname').value = response.key[0]['data2']
            document.getElementById('lastname').value = response.key[0]['data3']
            document.getElementById('email').value = response.key[0]['data4']
            document.getElementById('mobileno').value = response.key[0]['data5']
            document.getElementById('postad').value = response.key[0]['data6']
            document.getElementById('Uname').value = response.key1[0]['data_cred_1']
            document.getElementById('pword').value = response.key1[0]['data_cred_2']
            document.getElementById('status').value = response.key[0]['data7']
            document.getElementById('u_join_date').value = response.key[0]['data8']
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
            user_join_date: $('#u_join_date').val(),
            // x_photo: $('#userphoto').val()
        },
        success: function(response) {
            alert(response.key_update);
            window.location.href = '/addins/'
            document.getElementById('display').innerHTML = ""
        }
    });
}

$.ajaxSetup({
    headers: {
        "X-CSRFToken": '{{csrf_token}}'
    }
});

function load_createcourse() {
    $("#coursesearchtableheader").hide();

    $.ajax({

        url: 'dis_data_createcourse',
        type: 'GET',

        success: function(response) {
            b = response.key
                // document.getElementById('courseowner').innerHTML = response.key[0]['iden4']


            for (i = 0; i < b.length; i++) {
                $("#displaycourse").append("<tr><td><a href=''  data-toggle='modal' data-target='#MyModal' data-backdrop='static' data-keyboard='false'onclick='courseview(" + b[i].iden1 + ")'>" + b[i].iden1 + "</td><td>" + b[i].iden2 + "</td><td>" + b[i].iden3 + "</td><td>" + b[i].iden4 + "</td></tr>")
            }
        }
    });
}

submitcoursename = function() {
    $("#coursemaintableheader").hide();
    $("#coursesearchtableheader").show();

    $.ajax({

        url: 'search_course',
        type: 'POST',
        data: {
            name: $('#course_search_box').val(),

        },
        success: function(response) {

            document.getElementById('displaycourse').innerHTML = ""
            b = response.key_course


            for (i = 0; i < b.length; i++) {
                $("#displaycourse").append("<tr><td>" + b[i].key1 + "</td><td>" + b[i].key2 + "</td><td>" + b[i].key3 + "</td><td>" + b[i].key4 + "</td><td><button class='btn btn-success' data-toggle='modal' data-target='#MyModal' data-backdrop='static' data-keyboard='false'onclick='courseview(" + b[i].key1 + ")'>View/Edit</button></td></tr>")
            }
        }
    });
}

function courseview(y) {

    $.ajax({
        url: 'view_course_data_aj',
        type: 'POST',
        data: {
            view_id: y,

        },
        success: function(response) {
            document.getElementById('csmtable_id').innerHTML = ""
            m = response.table_key
                // a = response.key[0]['data1'];
            var f = response.key_course[0]['data1'];
            var a = response.key_course[0]['data2'];
            var b = response.key_course[0]['data3'];
            var c = response.key_course[0]['data4'];
            var d = response.key_course[0]['data5'];
            var e = response.key_student_name
            console.log(f)
            document.getElementById('coursename').innerHTML = a
            document.getElementById('owner').innerHTML = "courseowner:" + b
            document.getElementById('duration').innerHTML = c
            document.getElementById('areaforinfo').innerHTML = d

            // $('#csmtable_id').append('<table class="table table-sm table-striped" style="width:80%" id="courestudenttable_id"><button class="btn btn-success" onclick="load_csmtable(' + response.key_course[0]['data1'] + ')">View Assigned Students</button><thead><tr><th>User Id</th><th>Student Name</th></tr></thead></table>')
            $('#csmtable_id').append("<table class='table table-sm table-striped' style='width:80%' id='courestudenttable_id'><thead><tr><th>User Id</th><th>Student Name</th></tr></thead></table>")
            for (i = 0; i < m.length; i++) {
                var f_name = m[i].td2.concat(" ", m[i].td3)


                $('#courestudenttable_id').append("<tbody><tr><td>" + m[i].td1 + "</td><td>" + f_name + "</td></tr></tbody>")
            }


            // document.getElementById('').innerHTML = response.key1[0]['data_cred_3']
            if (response.key_course[0]['data6'] == "") {
                document.getElementById('courselogo').innerHTML = ('<img class="img-fluid rounded" style="width:80px;" src="/static/images/default_profile_pic_male.jpg">')
            } else {
                document.getElementById('courselogo').innerHTML = ('<img class="img-fluid rounded" style="width:80px;height:80px;" src="/myapp2/media/' + response.key_course[0]['data6'] + '">')
            }
            document.getElementById('assignbtn').innerHTML = ('<button type="submit" class="btn btn-success mr-auto" style="border-radius:12px; margin-left:50px" onclick="AssignStudent(' + response.key_course[0]['data1'] + ')">Assign</button>')
        }
    });
}

// function load_csmtable(CRS_ID) {
//     console.log('My loadpage')
//     $.ajax({
//         url: 'display_csmtable',
//         type: 'POST',
//         data: {
//             cid: CRS_ID,
//         },
//         success: function(response) {
//             tb_var = response.table_key
//             console.log(tb_var)
//             console.log(tb_var)

//             for (i = 0; i < tb_var.length; i++) {
//                 $('#courestudenttable_id').append("<tr><td>" + tb_var[i].td1 + "</td><td>" + tb_var[i].td2 + "</td></tr>")
//             }


//         }

//     });
// }

function AssignStudent(courseid) {
    var studentname = $("#studentname").val();
    console.log(studentname);
    var reg_no = parseInt(studentname.substring(0, 4));

    console.log(reg_no);
    $.ajax({
        url: 'assign_student_csm',
        type: 'POST',
        data: {
            c_id: courseid,
            stu_id: reg_no,
        },
        success: function(response) {

            alert(response.alert);
            re_courseid = response.Ref_crsid
            courseview(re_courseid);


        }
    });
}