$("#signup_form").submit(function(e) {
    var $form = $(this);
    var $error = $form.find("#error1")
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

$("#login_form").submit(function(e) {
    var $form = $(this);
    var $error = $form.find("#error2")
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
