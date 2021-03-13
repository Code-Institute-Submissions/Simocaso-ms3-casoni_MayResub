$("#signup_form").submit(function(e) {
    var $form = $(this);
    var $error = $form("#error1")
    var data = $form.serialize();

    $.ajax({
        url: "/signup",
        type: "POST",
        data: data,
        dataType: "json",
        success: function(resp) {
            window.location.href = "/dashboard/";
    },
        error: function(resp) {
            $error.text(resp.responseJSON.$form.find("#error1")).removeClass("error--hidden");
    }
  });

  e.preventDefault();
});

$("#login_form").submit(function(e) {
    var $form = $(this);
    var $error = $form("#error2")
    var data = $form.serialize();
   
    $.ajax({
        url: "/login",
        type: "POST",
        data: data,
        dataType: "json",
        success: function(resp) {
            window.location.href = "/dashboard/";
    },
        error: function(resp) {
            $error.text(resp.responseJSON.$form.find("#error2")).removeClass("error--hidden");
    }
  });

  e.preventDefault();
});
