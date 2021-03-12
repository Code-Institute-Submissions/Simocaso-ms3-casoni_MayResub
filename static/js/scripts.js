$("#signup_form").submit(function(e) {
// retrieve form from its id/name https://stackoverflow.com/questions/10398783/jquery-serialize-form-and-other-parameters

  var $form = $(this);
  var $error = $form.find("#error");
  var data = $form.serialize();
  
//  ajax call
// this function will redirect the user to the dashboard once signed up
  $.ajax({
    url: "/signup",
    type: "POST",
    data: data,
    dataType: "json",
    success: function(resp) {
        window.location.href = "/dashboard/";
        // console.log(resp)
    },
    error: function(resp) {
        $error.text(resp.responseJSON.error).removeClass("error--hidden");
        // console.log(resp)
    }
  });

  e.preventDefault();
});
