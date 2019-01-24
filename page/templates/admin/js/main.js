
(function ($) {
    "use strict";

    function validate (input) {
        if($("id_email").attr('type') == 'email' || $(input).attr('name') == 'email') {
            if($("id_email")).val().trim().match(/^([a-zA-Z0-9_\-\.]+)@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.)|(([a-zA-Z0-9\-]+\.)+))([a-zA-Z]{1,5}|[0-9]{1,3})(\]?)$/) == null) {
                return false;
            }
        }
        else {
            if($(("id_email")).val().trim() == ''){
                return false;
            }
        }
   
      var phoneno = /^\+?([0-9]{2})\)?[-. ]?([0-9]{4})[-. ]?([0-9]{4})$/;
      if($('id_MobileNumber').value.match(phoneno))
            {
          return true;
            }
          else
            {
            alert("message");
            return false;
            }
}
    

})(jQuery);