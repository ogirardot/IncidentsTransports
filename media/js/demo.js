$(document).ready(function() {
	
	var c = readCookie('freshserve_style');
	if (c) switchStylesheet(c);
	
	$("#theme_colors ul li").click(function() {
			switchStylesheet($(this).attr("class"));
	});
	
	$(".show_switcher").hover(function() {
		$(this).hide();
		$(".color_picker").fadeIn(200);
	});
	$(".color_picker").mouseleave(function() {
		$(this).fadeOut(200);
		$(".show_switcher").delay(200).fadeIn(200);
	});
});
function switchStylesheet(styleName) {
			if(styleName == "") {
				
			} else {
				$("link[media='screen']").attr("href", 'stylesheets/'+styleName+'.css');
			}
			createCookie('freshserve_style', styleName, 365);
		}
function createCookie(name,value,days)
{
	if (days)
	{
		var date = new Date();
		date.setTime(date.getTime()+(days*24*60*60*1000));
		var expires = "; expires="+date.toGMTString();
	}
	else var expires = "";
	document.cookie = name+"="+value+expires+"; path=/";
}
function readCookie(name)
{
	var nameEQ = name + "=";
	var ca = document.cookie.split(';');
	for(var i=0;i < ca.length;i++)
	{
		var c = ca[i];
		while (c.charAt(0)==' ') c = c.substring(1,c.length);
		if (c.indexOf(nameEQ) == 0) return c.substring(nameEQ.length,c.length);
	}
	return null;
}
function eraseCookie(name)
{
	createCookie(name,"",-1);
}
