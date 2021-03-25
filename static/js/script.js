// Toggling of the buttons in theindex page starts

jQuery(document).ready(function() {
    jQuery('#knowmorebutton').on('click', function(event) {
        jQuery('#knowmoresection').toggle()
        $(document).scrollTop(200)
    });
    jQuery('#readmorebutton').on('click', function(event) {
        jQuery('#readmoresection').toggle()
        $(document).scrollTop(800)
    });
});

// Toggling of the buttons in theindex page ends

// Ajax function starts

// Add/Update Instructor in Admin Module Starts


$.ajaxSetup({
    headers: {
        "X-CSRFToken": '{{csrf_token}}'
    }
});


// Add/Update Instructor html page with displaying the page with instructor data in Admin Module

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
// Add/Update Instructor html page with on key up function in add instructor form in Admin Module

$.ajaxSetup({
    headers: {
        "X-CSRFToken": '{{csrf_token}}'
    }
});

// Add Instructor in Admin Module

function addinstructor() {
    var formData = new FormData();
    formData.append('fir_name', $('#FirstName').val())
    formData.append('l_name', $('#LastName').val())
    formData.append('e_mail', $('#Email').val())
    formData.append('mob_no', $('#MobileNo').val())
    formData.append('post_ad', $('#address').val())
    formData.append('u_name', $('#username').val())
    formData.append('pass_word', $('#pword').val())
    formData.append('user_join_date', $('#joining_date').val())
    formData.append('gender', $('.gendertype:checked').val())
    formData.append('ins_photo', $('#inpFile')[0].files[0])
    formData.append('action', 'addinstructor')
    formData.append('csrfmiddlewaretoken', '{{csrf_token}}')


    $.ajax({
        type: 'POST',
        url: 'insformsubmit',
        data: formData,
        cache: false,
        contentType: false,
        processData: false,
        enctype: 'multipart-form/data',
        success: function(response) {
            window.location.href = '/addins/'
        }
    });
};


// Username already exists in Add Instructor in Admin Module


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

// Add/Update Instructor Search functionality in Admin Module

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


// Add/Update Instructor View/Edit function- View singledata of the instructor in Admin Module

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
// Add/Update Instructor View/Edit function- Update singledata of the instructor in Admin Module

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

// Add/Update Instructor in Admin Module Ends


// Add/Update Student page in Admin Module starts

// Add/Update Student html page with displaying the page with Student data in Admin Module

function load_addstu() {
    $("#searchstudenttableheader").hide();
    $.ajax({
        url: 'display_studentdata',
        type: 'GET',
        success: function(response) {
            x = response.s_data
            for (i = 0; i < x.length; i++) {
                $('#studentdisplay').append("<tr><td><a href=''  data-toggle='modal' data-target='#exampleModalLong' data-backdrop='static' data-keyboard='false'onclick='viewstudent(" + x[i].s_data1 + ")'>" + x[i].s_data1 + "</a></td><td>" + x[i].s_data2 + "</td><td>" + x[i].s_data3 + "</td><td>" + x[i].s_data4 + "</td></tr>")
            }
        }
    });
}
$.ajaxSetup({
    headers: {
        "X-CSRFToken": '{{csrf_token}}'
    }
});

// Add Student in Admin module

function addstudent() {

    var formData = new FormData();
    formData.append('f_name', $('#FirstName').val())
    formData.append('l_name', $('#LastName').val())
    formData.append('e_mail', $('#Email').val())
    formData.append('mob_no', $('#MobileNo').val())
    formData.append('post_ad', $('#Address').val())
    formData.append('u_name', $('#username').val())
    formData.append('pass_word', $('#Password').val())
    formData.append('user_join_date', $('#Joiningdate').val())
    formData.append('gender', $('.gendertype:checked').val())
    formData.append('stu_photo', $('#stuphoto')[0].files[0])
    formData.append('action', 'addstudent')
    formData.append('csrfmiddlewaretoken', '{{csrf_token}}')


    $.ajax({
        type: 'POST',
        url: 'stuformsubmit',
        data: formData,
        cache: false,
        contentType: false,
        processData: false,
        enctype: 'multipart-form/data',
        success: function(response) {
            alert("data successfully added")
            location.reload()

            // window.location.href = '/addstu/'
        }
    });

}

// Add/Update Student Search functionality in Admin Module


function submitstudent() {
    $("#mainstudenttableheader").hide();
    $("#searchstudenttableheader").show();
    $.ajax({
        url: 'searchstudent',
        type: 'POST',
        data: {
            search_name: $('#searchstudent').val(),
        },
        success: function(response) {
            document.getElementById('studentdisplay').innerHTML = ""

            x = response.stukey
            for (i = 0; i < x.length; i++) {
                $("#studentdisplay").append("<tr><td>" + x[i].data1 + "</td><td>" + x[i].data2 + "</td><td>" + x[i].data3 + "</td><td>" + x[i].data4 + "</td><td><button type='submit'class='btn btn-success' data-toggle='modal' data-target='#exampleModalLong' data-backdrop='static' data-keyboard='false'onclick='viewstudent(" + x[i].data1 + ")'>Edit</button></td></tr>")
                    // <td><button class='btn btn-success' data-toggle='modal' data-target='#exampleModalLong' data-backdrop='static' data-keyboard='false'onclick='view(" + b[i].key1 + ")'>View/Edit</button></td>
            }
        }
    });
}

// Add/Update Student View/Edit function- View singledata of the student in Admin Module

function viewstudent(stu_view_id) {
    console.log('mypage')
    $.ajax({
        url: 'viewstudentdata_aj',
        type: 'POST',
        data: {
            s_view_id: stu_view_id
        },
        success: function(response) {
            a = response.key_info[0]['data1']
            first_name = response.key_info[0]['data2']
            last_name = response.key_info[0]['data3']
            fullname = first_name.concat(" ", last_name)
            console.log(response.key_info[0]['data_cred_1'])
            if (response.key_info[0]['data9'] == "") {
                document.getElementById('studentphoto').innerHTML = ('<img class="img-fluid rounded" style="width:80px" src="/static/images/default_profile_pic_male.jpg">')
            } else {
                document.getElementById('studentphoto').innerHTML = ('<img class="img-fluid rounded" style="width:80px" src="/myapp2/media/' + response.key_info[0]['data9'] + '">')
            }
            document.getElementById('studenttype').innerHTML = response.key_cred[0]['data_cred_3']
            document.getElementById('FullName').innerHTML = fullname
            document.getElementById('firstname').value = response.key_info[0]['data2']
            document.getElementById('lastname').value = response.key_info[0]['data3']
            document.getElementById('email').value = response.key_info[0]['data4']
            document.getElementById('mobileno').value = response.key_info[0]['data5']
            document.getElementById('postad').value = response.key_info[0]['data6']
            document.getElementById('Uname').value = response.key_cred[0]['data_cred_1']
            document.getElementById('pword').value = response.key_cred[0]['data_cred_2']
            document.getElementById('status').value = response.key_info[0]['data7']
            document.getElementById('u_join_date').value = response.key_info[0]['data8']
        }
    });
}

// Add/Update Student View/Edit function- Update singledata of the instructor in Admin Module

function updatestudent(stu_update_id) {
    $.ajax({
        url: 'updatestudent_aj',
        type: 'POST',
        data: {
            student_update_id: stu_update_id,
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
            alert(response.key_stu_update);
            window.location.href = '/addstu/'
            document.getElementById('studentdisplay').innerHTML = ""
        }
    });
}

// Add/Update Student page in Admin Module starts

// Add/Update Course in Admin Module starts

$.ajaxSetup({
    headers: {
        "X-CSRFToken": '{{csrf_token}}'
    }
});
// Add/Update Course html page-loading the course data in Admin Module

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

// Create course in Admin Module

function createcourse() {

    var formData = new FormData();
    formData.append('crs_name', $('#coursename').val())
    formData.append('crs_owner', $('#courseowner').val())
    formData.append('crs_duration', $('#courseduration').val())
    formData.append('crs_startdate', $('#CourseStartDate').val())
    formData.append('crs_enddate', $('#CourseEndDate').val())
    formData.append('crs_details', $('#coursedetails').val())
    formData.append('crs_logopic', $('#CourseLogoPic')[0].files[0])
    formData.append('action', 'createcourse')
    formData.append('csrfmiddlewaretoken', '{{csrf_token}}')
    console.log(formData)

    $.ajax({
        type: 'POST',
        url: '/createcourse/addcrsform',
        data: formData,
        cache: false,
        contentType: false,
        processData: false,
        enctype: 'multipart-form/data',
        success: function(response) {
            window.location.href = '/createcourse/'
        }
    });



}

// Add/Update Course html page-search functionality in Admin Module
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

// Add/Update course html page -view details of single course in Admin Module

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
            document.getElementById('coursename').innerHTML = a
            document.getElementById('owner').innerHTML = "courseowner:" + b
            document.getElementById('duration').innerHTML = c
            document.getElementById('areaforinfo').innerHTML = d

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

// Add/Update Course html page- assigning students to the course in Admin Module

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