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
//alert("value of i and k on entrance is "+i);
$('#addNewSchool').live('click', function() {
var j=i+1;
$('<p><h3 align="center"> SCHOOL - '+j+' </h3><br/\>Name of High School: <input type="text" name="name_school_'+i+'" id="name_school_'+i+'"> <br/\>Date of Joining: <input type="text" name="doj_school_'+i+'" id="doj_school_'+i+'"> <br/\> Date of leaving: <input type="text" name="dol_school_'+i+'" id="dol_school_'+i+'"><br/\>City: <input type="text" name="city_school_'+i+'" id="city_school_'+i+'"> <br/\>Marks Secured: <input type="text" name="ms_school_'+i+'" id="ms_school_'+i+'"> <br/\> Out of: <input type="text" name="outof_school_'+i+'" id="outof_school_'+i+'"> <br/\><input type="button"  value="Remove" id="sch_'+i+'"> <br/\></p>').appendTo(addDiv);
i++;
//alert("value of i is " + i);
document.resume_form.p_tag.value=i; 
	return false;
	});
var addDiv1 = $('#addcolleges')
var coll_p=$('#addcolleges p').size()/2
$('#addNewCollege').live('click', function() {
var j=coll_p+1;
$('<p><h3 align="center"> COLLEGE - '+j+' </h3><br/\>Name of College: <input type="text" name="name_college_'+coll_p+'" id="name_college_'+coll_p+'"> <br/\>Degree: <input type="text" name="degree_college_'+coll_p+'" id="degree_college_'+coll_p+'"><br/\>Course: <input type="text" name="course_college_'+coll_p+'" id="course_college_'+coll_p+'"><br/\>Date of Joining: <input type="text" name="doj_college_'+coll_p+'" id="doj_college_'+coll_p+'"> <br/\> Date of leaving: <input type="text" name="dol_college_'+coll_p+'" id="dol_college_'+coll_p+'"><br/\>City: <input type="text" name="city_college_'+coll_p+'" id="city_college_'+coll_p+'"> <br/\>Marks Secured: <input type="text" name="ms_college_'+coll_p+'" id="ms_college_'+coll_p+'"> <br/\> Out of: <input type="text" name="outof_college_'+coll_p+'" id="outof_college_'+coll_p+'"> <br/\><input type="button"  value="Remove" id="cch_'+coll_p+'"> <br/\></p>').appendTo(addDiv1);
coll_p++;
document.resume_form.no_of_pc.value=coll_p;return false;})
var addDiv2 = $('#addprojects')
var proj_p=$('#addprojects p').size()/2
$('#addNewProject').live('click', function() {
var j=proj_p+1;
$('<p><br/\><h3 align="center"> PROJECT - '+j+' </h3><br/\>Project title: <input type="text" name="project_title_'+proj_p+'" id="project_title_'+proj_p+'"><br/\>Description: <input type="text" name="project_desc_'+proj_p+'" id="project_desc_'+proj_p+'"> <br/\>From: <input type="text" name="project_from_'+proj_p+'" id="project_from_'+proj_p+'"><br/\>To: <input type="text" name="project_to_'+proj_p+'" id="project_to_'+proj_p+'"><br/\>Members: <input type="text" name="project_mem_'+proj_p+'" id="project_mem_'+proj_p+'"><br/\>Publications: <input type="text" name="project_pub_'+proj_p+'" id="project_pub_'+proj_p+'"><br/\>Link: <input type="text" name="project_link_'+proj_p+'" id="project_link_'+proj_p+'"><br/\><input type="button"  id="pch'+proj_p+'" value="Remove"> <br/\></p>').appendTo(addDiv2);
proj_p++;
document.resume_form.no_of_pro.value=proj_p;return false;})
var addDiv3 = $('#addemployments')
var emp_p=$('#addemployments p').size()/2
$('#addNewEmployment').live('click', function() {
var j=emp_p+1;
$('<p><br/\><h3 align="center"> EMPLOYMENT - '+j+'</h3><br/\>Name of Company: <input type="text" name="name_company_'+emp_p+'" id="name_company_'+emp_p+'"><br/\>Place: <input type="text" name="place_company_'+emp_p+'" id="place_company_'+emp_p+'"><br/\>From: <input type="text" name="from_company_'+emp_p+'" id="from_company_'+emp_p+'"><br/\>To: <input type="text" name="to_company_'+emp_p+'" id="to_company_'+emp_p+'"><br/\>Position: <input type="text" name="pos_company_'+emp_p+'" id="pos_company_'+emp_p+'"><br/\><input type="button"  id="ech_'+emp_p+'" value="Remove"><br/\></p>').appendTo(addDiv3);
emp_p++;
document.resume_form.no_of_emp.value=emp_p;return false;})
var addDiv4 = $('#addskills')
var skill_p=$('#addskills p').size()
$('#addNewSkill').live('click',function() {
var j=skill_p+1;
$('<p><br /\> Skill - '+j+': <input type="text" name="name_skill_'+skill_p+'" id="name_skill_'+skill_p+'"/\> &nbsp &nbsp &nbsp Skill - level: <select name="level_skill_'+skill_p+'"><option value="novice">novice</option><option value="intermediate">intermediate</option><option value="expert">expert</option></select><br/\></p>').appendTo(addDiv4);
skill_p++;
document.resume_form.no_of_skill.value=skill_p; return false;})

   // this function displays the ID of the clicked button
        $(':button').click(function() {
  var buttonElementId = $(this).attr('id');
  //alert(buttonElementId);
  document.getElementById("del").value=buttonElementId;
  var r=confirm("Are u sure you want to delete??")
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
var j = $('#addcolleges p').size()/2;
var k = $('#addprojects p').size()/2;
var l = $('#addemployments p').size()/2;
var m=$('#addskills p').size();
document.getElementById("display_name").readOnly=true;
//document.getElementById("address").readOnly=true;
document.resume_form.p_tag.value=i;
document.resume_form.no_of_pc.value=j;
document.resume_form.no_of_pro.value=k;
document.resume_form.no_of_emp.value=l;
document.resume_form.no_of_skill.value=m;
return true;
}
function DisplayTextBox(){
 document.getElementById("address").readOnly=false;
}

</script> 
 <link rel="stylesheet" href="${request.static_url('neuron:static/css/resume.css')}" type="text/css" media="screen" charset="utf-8" />
</head>
<body  onload="SetReadOnly()">
<div class="resume">
<form method="post" name="resume_form" id="resume_form" action="/resume_entered">
<br />
<br />
<h1 style="text-align:center;font-family: 'Script MT Bold','Trebuchet MS', Helvetica, sans-serif; font-size:35pt"> Resume</h1>
<br/>
Display name: <input type="text" name="display_name" id="display_name" value="${full_name}"> &nbsp &nbsp &nbsp
Address: <input type="text" name="address" id="address" value="${address}">
<br />
<br />
<!--<input type="text" name="edit_address" id="edit_address" style='display:none'>
<input type="button" onclick="DisplayTextBox()" value="edit">-->
<input type="submit" value="Save me!!!" >
<a href="#" id="addNewSchool">AddNewSchool</a>
<a href='#' id="addNewCollege">AddNewCollege</a>
<a href='#' id="addNewProject">AddNewProject</a>
<a href='#' id="addNewEmployment">AddNewEmployment</a>
<a href='#' id="addNewSkill">AddNewSkill</a>
<div id="addschools">
<h1 align="center"> SCHOOL FORM </h1>
${count_school()}
</div>
<div id="addcolleges">
<h1 align="center"> COLLEGE FORM </h1>
${count_college()}
</div>
<div id="addprojects">
<h1 align="center"> PROJECT FORM </h1>
${count_project()}
</div>
<div id="addemployments">
<h1 align="center"> EMPLOYMENT FORM</h1>
${count_employment()}
</div>
<div id="addskills">
<h1 align="center"> SKILLS FORM</h1>
${count_skills()}
</div>
<input type="text" name="p_tag" hidden="true" >
<input type="text" name="no_of_pc" hidden="true" >
<input type="text" name="no_of_pro" hidden="true">
<input type="text" name="no_of_emp" hidden="true">
<input type="text" name="no_of_skill" hidden="true">
</form>

<%def name="count_school()">
    % for i in range(0,int(no_of_p)):
        <p>
        <br/>
        
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

<%def name="count_employment()">
    % for i in range(0,int(no_of_emp)):
        <p>
        <br/>
        
        <h3 align="center"> EMPLOYMENT - ${i+1} </h3><br/>
        Name of Company: <input type="text" name="name_company_${i}" id="name_company_${i}" value="${name_company[i]}">
        <br/>
        Place: <input type="text" name="place_company_${i}" id="place_company_${i}" value="${place_company[i]}"> 
        <br/>
        From: <input type="text" name="from_company_${i}" id="from_company_${i}" value="${from_company[i]}">
        <br/>
        To: <input type="text" name="to_company_${i}" id="to_company_${i}" value="${to_company[i]}">  
        <br/>
        Position: <input type="text" name="pos_company_${i}" id="pos_company_${i}" value="${pos_company[i]}">
        <br/>
        <input type="button"  id="ech_${i}" value="Remove"> 
        <br/>
        </p>
    % endfor
</%def>
<%def name="count_project()">
    % for i in range(0,int(no_of_pro)):
        <p>
        <br/>
        
        <h3 align="center"> PROJECT - ${i+1} </h3><br/>
        Project title: <input type="text" name="project_title_${i}" id="project_title_${i}" value="${project_title[i]}">
        <br/>
        Description: <input type="text" name="project_desc_${i}" id="project_desc_${i}" value="${project_desc[i]}"> 
        <br/>
        From: <input type="text" name="project_from_${i}" id="project_from_${i}" value="${project_from[i]}">
        <br/>
        To: <input type="text" name="project_to_${i}" id="project_to_${i}" value="${project_to[i]}">  
        <br/>
        Members: <input type="text" name="project_mem_${i}" id="project_mem_${i}" value="${project_mem[i]}">
        <br/> 
        Publications: <input type="text" name="project_pub_${i}" id="project_pub_${i}" value="${project_pub[i]}">
        <br/>
        Link: <input type="text" name="project_link_${i}" id="project_link_${i}" value="${project_link[i]}">
        <br/>
        <input type="button"  id="pch_${i}" value="Remove"> 
        <br/>
        </p>
    % endfor
</%def>

<%def name="count_college()">
    % for i in range(0,int(no_of_pc)):
        <p>
        <br/>
        
        <h3 align="center"> COLLEGE - ${i+1} </h3><br/>
        Name of college: <input type="text" name="name_college_${i}" id="name_college_${i}" value="${name_coll[i]}">
        <br/>
        Degree: <input type="text" name="degree_college_${i}" id="degree_college_${i}" value="${degree[i]}">
        <br/>
        Course: <input type="text" name="course_college_${i}" id="course_college_${i}" value="${course[i]}">
        <br/>
        Date of Joining: <input type="text" name="doj_college_${i}" id="doj_college_${i}" value="${d_o_j_coll[i]}"> 
        <br/>
        Date of leaving: <input type="text" name="dol_college_${i}" id="dol_college_${i}" value="${d_o_l_coll[i]}">
        <br/>
        City: <input type="text" name="city_college_${i}" id="city_college_${i}" value="${place_coll[i]}">  
        <br/>
        Marks Secured: <input type="text" name="ms_college_${i}" id="ms_college_${i}" value="${m_s_coll[i]}">
        <br/> 
        Out of: <input type="text" name="outof_college_${i}" id="outof_college_${i}" value="${o_f_coll[i]}">
        <br/>
        <input type="button"  id="cch_${i}" value="Remove"> 
        <br/>
        </p>
    % endfor
</%def>
<%def name="count_skills()">
    % for i in range(0,int(no_of_skill)):
         <p>
         <br />
        Skill - ${i+1}: <input type="text" name="name_skill_${i}" id="name_skill_${i}" value="${name_skill[i]}"/> &nbsp &nbsp &nbsp 
        Skill - level: <select name="level_skill_${i}"><option value="novice">novice</option><option value="intermediate">intermediate</option><option value="expert">expert</option></select>
         <br/>
         </p>
    % endfor
</%def>
<!-- To be hidden-->
<form name="delete" id="delete" action="/delete_education">
<input type="text" name="del" id="del" hidden="true">
</form>
</div>
</body>
</html>



