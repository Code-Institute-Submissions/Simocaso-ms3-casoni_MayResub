$("form[name=signup_form").submit(function(e) {
    var $form = $(this);
    var $error = $form.find(".error");
    var data = $form.serialize();

    $.ajax({
        url: "/user/signup",
        type: "POST",
        data: data,
        dataType: "json",
        success: function(resp) {
        window.location.href = "/dashboard/";
        },
        error: function(resp) {
            $error.text(resp.responseJSON.error).removeClass("error--hidden");
        }
    });

    e.preventDefault();
});


$("form[name=login_form").submit(function(e) {

    var $form = $(this);
    var $error = $form.find(".error");
    var data = $form.serialize();

    $.ajax({
        url: "/user/login",
        type: "POST",
        data: data,
        dataType: "json",
        success: function(resp) {
            window.location.href = "/dashboard/";
        },
        error: function(resp) {
            $error.text(resp.responseJSON.error).removeClass("error--hidden");
        }
    });

    e.preventDefault();
});


$("form[name=tasks_form").submit(function(e) {
    var $form = $(this);
    var data = $form.serialize();

    $.ajax({
        url: "/user/addTask",
        type: "POST",
        data: data,
        dataType: "json",
        success: function(resp) {
            // console.log(resp);
            window.location.href = "/dashboard/";
        },
    });

    e.preventDefault();
});

// $("form[name=list_form").submit(function(e) {
//     var $form = $(this);
//     var data = $form.serialize();

//     $.ajax({
//         url: "/user/marked/<oid>",
//         type: "POST",
//         data: data,
//         dataType: "json",
//         success: function(resp) {
//             // console.log(resp);
//             window.location.href = "/dashboard/";
//         },
//     });

//     e.preventDefault();
// });
