$("form[name=signup_form]").submit(function(e) {

    var $form = $(this);
    var $error = $form.find(".error");
    var data = $form.serialize();

// ajax call
    $.ajax({
    url: "/signup",
    type: "POST",
    data: data,
    dataType: "json",
    success: function(resp) {
    // if succesful, user will be redirect
        window.location.href="/dashboard/"
    },
    error: function(resp) {
    // error message shown above sign up button, error refer to error in models.py 
      $error.text(resp.responseJSON.error).removeClass("error--hidden")
    }
  });


    e.preventDefault();
})