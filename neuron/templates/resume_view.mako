<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" xmlns:tal="http://xml.zope.org/namespaces/tal">
<head>
<title>
Resume
</title>
<script  src="https://ajax.googleapis.com/ajax/libs/jquery/1.4.4/jquery.min.js"></script> 
<script type="text/javascript">
$(function() {
var addDiv = $('#addschools');
var i = $('#addschools p').size()/2;
alert("value of i and k on entrance is "+i);
$('#addNewSchool').live('click', function() {
var j=i+1;
$('<p><h3 align="center"> SCHOOL - '+j+' </h3><br/\>Name of High School: <input type="text" name="name_school_'+i+'" id="name_school_'+i+'"> <br/\>Date of Joining: <input type="text" name="doj_school_'+i+'" id="doj_school_'+i+'"> <br/\> Date of leaving: <input type="text" name="dol_school_'+i+'" id="dol_school_'+i+'"><br/\>City: <input type="text" name="city_school_'+i+'" id="city_school_'+i+'"> <br/\>Marks Secured: <input type="text" name="ms_school_'+i+'" id="ms_school_'+i+'"> <br/\> Out of: <input type="text" name="outof_school_'+i+'" id="outof_school_'+i+'"> <br/\><input type="button"  id="s_'+i+'"> <br/\></p>').appendTo(addDiv);
//alert("value of i is " + i);
document.school_form.p_tag.value=i; 
	return false;
	});

	$('#remNew').live('click', function() {
	alert("inside remove");
        if( i > 2 ) {
        alert("inside greater part")
	$(this).parents('p').remove();
	i--;
        alert("i is "+i);
	}
	return false;
	});
   // this function displays the ID of the clicked button
        $(':button').click(function() {
  var buttonElementId = $(this).attr('id');
  alert(buttonElementId);
  document.getElementById("del").value=buttonElementId;
  var r=confirm("Are u sure you want to delete this school??")
  if(r==true)
  {
 document.forms["delete"].submit()
  }
  else
  {}

});
	});
function SetReadOnly()
{
var i = $('#addschools p').size()/2;
document.getElementById("uname").readOnly=true;
document.getElementById("address").readOnly=true;
document.school_form.p_tag.value=i;
return true;
}
function DisplayTextBox(){
 document.getElementById("address").readOnly=false;
}


</script> 
 <link rel="stylesheet" href="${request.static_url('neuron:static/css/login.css')}" type="text/css" media="screen" charset="utf-8" />
</head>
<body  onload="SetReadOnly()">
<div class="one">
<form method="post" name="school_form" id="school_form" action="/resume_entered">
<br />
<br />

username: <input type="text" name="uname" id="uname" value="${username}"> &nbsp &nbsp &nbsp
Address: <input type="text" name="address" id="address" value="${address}">
<br />
<br />
<!--<input type="text" name="edit_address" id="edit_address" style='display:none'>-->
<input type="button" onclick="DisplayTextBox()" value="edit">
<input type="submit" value="Save me!!!" >
<a href="#" id="addNewSchool">AddNewSchool</a>
<div id="addschools">
${count_school()}
</div>
<input type="text" name="p_tag" >
</form>
<%def name="count_school()">
    % for i in range(0,int(no_of_p)):
        <p>
        <br/>
        <h1 align="center"> SCHOOL FORM </h1>
        <h3 align="center"> SCHOOL - ${i+1} </h3><br/>
        Name of High School: <input type="text" name="name_school_${i}" id="name_school_${i}" value="${name[i]}">
        <br/>
        Date of Joining: <input type="text" name="doj_school_${i}" id="doj_school_${i}" value="${d_o_j[i]}"> 
        <br/>
        Date of leaving: <input type="text" name="dol_school_${i}" id="dol_school_${i}" value="${d_o_l[i]}">
        <br/>
        City: <input type="text" name="city_school_${i}" id="city_school_${i}" value="${place[i]}">  
        <br/>
        Marks Secured: <input type="text" name="ms_school_${i}" id="ms_school_${i}" value="${m_s[i]}">
        <br/> 
        Out of: <input type="text" name="outof_school_${i}" id="outof_school_${i}" value="${o_f[i]}">
        <br/>
        <input type="button"  id="sch_${i}" value="Remove"> 
        <br/>
        </p>
    % endfor
</%def>
<!-- To be hidden-->
<form name="delete" id="delete" action="/delete_education">
<input type="text" name="del" id="del">
</form>
</div>
</body>
</html>



