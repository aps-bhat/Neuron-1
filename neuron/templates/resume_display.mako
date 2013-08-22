<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" xmlns:tal="http://xml.zope.org/namespaces/tal">
<head>
<title>
Resume
</title>
<link rel="stylesheet" href="${request.static_url('neuron:static/css/resume.css')}" type="text/css" media="screen" charset="utf-8" />
<link rel="stylesheet" href="${request.static_url('neuron:static/css/login.css')}" type="text/css" media="screen" charset="utf-8" />
</head>
<body>
<div class="one">
<div style="text-align:center; font-style:italic; font-family:'Comic Sans MS', cursive; font-size:35pt"> Resume</div>
<div style="text-align:center; font-weight:800; text-transform:uppercase; font-family:TimesNewRoman,'Times New Roman',Times,Baskerville,Georgia,Serif; font-size:30pt">${username}</div>
<div style="text-align:center; font-family:TimesNewRoman,'Times New Roman',Times,Baskerville,Georgia,Serif; font-size:15pt">${address}</div>
<div style="text-align:center; font-family:TimesNewRoman,'Times New Roman',Times,Baskerville,Georgia,Serif; font-size:15pt">phone number, email-id</div>
<a  align="right" href="/resume_edit">Edit my resume</a>
<br/>
<div class="sideheading">Employment</div>
<hr>
<div class="maintext-center">
<table name="employment" border="0" width="100%">
${display_employment()}
</table>
</div>
<br/>
<br/>
</div>

<%def name="display_employment()">
    %for i in range(0,int(no_of_emp)):
       <tr>
       <td> ${name_company[i]}, &nbsp&nbsp${place_company[i]}</td>
       <td> ${pos_company[i]}</td>
       <td> ${from_company[i]} - ${to_company[i]} </td>
       </tr>
    %endfor
</%def>             
</body>
</html>
