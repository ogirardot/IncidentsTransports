$(document).ready(function() {
	
	// CSS3 rounded corners / shadows
	$("div#header li.active a").css({ '-moz-border-radius': '6px', '-webkit-border-radius': '6px', 'border-radius': '6px' });
	$("div.sidebar_box").css({ '-moz-border-radius': '8px', '-webkit-border-radius': '8px', 'border-radius': '8px' });
	$("div#price_table table").css({ '-moz-border-radius': '8px', '-webkit-border-radius': '8px', 'border-radius': '8px' });
	$("span.highlight_dark, span.highlight_light").css({ '-moz-border-radius': '2px', '-webkit-border-radius': '2px', 'border-radius': '2px' });
	$("div#about .team ul li a").css({ '-moz-border-radius': '8px', '-webkit-border-radius': '8px', 'border-radius': '8px' });
	$("form .text_field").css({ '-moz-border-radius': '8px', '-webkit-border-radius': '8px', 'border-radius': '8px' });
	$("a.button span").css({ 'text-shadow': '#000 0px -0px 2px' });
	$("div#page .section_title h3").css({ 'text-shadow': '#3e2828 0px 0px 2px' });

	// Default text field values
	$(".text_field").focus(function(srcc)
  {
      if ($(this).val() == $(this)[0].title)
      {
          $(this).addClass("default_text_active");
          $(this).val("");
      }
  });
  $(".text_field").blur(function()
  {
      if ($(this).val() == "")
      {
          $(this).removeClass("default_text_active");
          $(this).val($(this)[0].title);
      }
  });
  $(".text_field").blur();
	
	// Button Hover
	if($.browser.msie && $.browser.version == "7.0") {
		$(".button").css("padding-top", "0px");
	} else {
		jQuery('.button').hover(
			function() { jQuery(this).stop().animate({opacity:0.8},400); },
			function() { jQuery(this).stop().animate({opacity:1},400); }
		);
	}
	
	// Add form submit capability to buttons
	$("a.submit").click(function() {
		$(this).parent().submit();
	});
	
	// Ajax contact form
	$('#send').click(function() {
       var name = $('input#name').val();
       var email = $('input#email').val();
			 var subject = $('select#subject').val();
       var message = $('textarea#message').val();
       $.ajax({
           type: 'post',
           url: 'scripts/send_email.php',
           data: 'name=' + name + '&email=' + email + '&topic=' + subject + '&message=' + message,

           success: function(results) {
							if(results == "error") {
								$('p.validation').html("Please fill in all fields").addClass("error");
							} else {
								$("form#contact_form").fadeOut("fast");
               $('p.validation').html(results);
							}
           }
       }); // end ajax
   });

});