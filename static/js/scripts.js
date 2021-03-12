$("#signup_form").submit(function(e) {
// retrieve form from its id/name https://stackoverflow.com/questions/10398783/jquery-serialize-form-and-other-parameters

  var $form = $(this);
  var $error = $form.find("#error");
  var data = $form.serialize();
  
//  ajax call
  $.ajax({
    url: "/signup",
    type: "POST",
    data: data,
    dataType: "json",
    success: function() {
        window.location.href = "/dashboard/";
        // this function will redirect the user to the dashboard once signed up
    },
    error: function(resp) {
        $error.text(resp.responseJSON.error).removeClass("error--hidden");
    }
  });

  e.preventDefault();
});
