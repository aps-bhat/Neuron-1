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
<div style="text-align:center;  font-family:'Brush Script MT','Comic Sans MS', cursive; font-size:40pt"> Resume</div>
<div style="text-align:center; font-weight:800; text-transform:uppercase; font-family:TimesNewRoman,'Times New Roman',Times,Baskerville,Georgia,Serif; font-size:25pt">${full_name}</div>
<div style="text-align:center; font-family:TimesNewRoman,'Times New Roman',Times,Baskerville,Georgia,Serif; font-size:15pt">${address}</div>
<div style="text-align:center; font-family:TimesNewRoman,'Times New Roman',Times,Baskerville,Georgia,Serif; font-size:15pt">phone number, email-id</div>
<a  align="right" href="/resume_edit">Edit my resume</a>
<br/>
<!-- displaying employment details -->
%if no_of_emp!=0: 
  <span class="sideheading">Employment</span>
  <hr>
  <span class="maintext-center">
  <table name="employment" border="0" width="100%">
  ${display_employment()}
  </table>
  </span> <!--closing of maintext-center for employment-->
  <br/>
  <br/>
%endif
<!-- displaying education details -->
%if no_of_p!=0 or no_of_pc!=0: 
  <span class="sideheading">Education</span>
  <hr>
  %if no_of_pc!=0:
    <span class="sideheading_mini"> College </span>
    <br/>
    <span class="maintext-center">
    <table name="college" border="0" width="100%">
    ${display_college()}
    </table>
    </span>
    <br/>
    <br/>
  %endif
  %if no_of_p!=0:
    <span class="sideheading_mini"> School </span>
    <br/>
    <span class="maintext-center">
    <table name="school" border="0" width="100%">
    ${display_school()}
    </table>
    </span>
    <br/> 
    <br/>
  %endif
%endif
<!-- displaying project details -->
%if no_of_pro!=0:      
  <span class="sideheading">Project</span>
  <hr>
  <span class="maintext-center">
  <table name="project" border="0" width="100%">
  ${display_project()}
  </table>
  </span> <!--closing of maintext-center for employment-->
  <br/>
  <br/>
%endif
 <!-- displaying skill details -->
%if no_of_skill!=0: 
  <span class="sideheading">Skills</span>
  <hr>
  <span class="maintext-center">
  <table name="project" border="0" width="100%">
  ${display_skills()}
  </table>
  </span> <!--closing of maintext-center for employment-->
  <br/>
  <br/>
%endif
</div> <!--closing of main div for class=one -->
<%def name="display_employment()"> <!-- displaying employment -->
    %for i in range(0,int(no_of_emp)):
       <tr>
       <td width="40%"> ${name_company[i]}, &nbsp&nbsp${place_company[i]}</td>
       <td width="40%"> ${pos_company[i]}</td>
       <td width="20%"> ${from_company[i]} - ${to_company[i]} </td>
       </tr>
    %endfor
</%def>    
<%def name="display_college()"> <!-- dispalying college -->
    %for i in range(0,int(no_of_pc)):
       <tr>
       <td width="40%"> ${name_coll[i]}, &nbsp&nbsp${place_coll[i]}</td>
       <td width="40%"> ${degree[i]}, &nbsp&nbsp${course[i]}</td>
       <td width="20%"> ${d_o_j_coll[i]} - ${d_o_l_coll[i]} </td>
       </tr>
       %if m_s_coll[i]:
          <tr>
          <td></td>
          %if o_f_coll[i]:
             <td>Marks Secured: &nbsp&nbsp&nbsp${m_s_coll[i]}/${o_f_coll[i]} </tr>
          %else: 
             <td>Marks Secured: &nbsp&nbsp&nbsp${m_s_coll[i]} </td>
          %endif
          </tr>
       %endif
    %endfor
</%def>         
<%def name="display_school()"> <!-- displaying school -->
    %for i in range(0,int(no_of_p)):
       <tr>
       <td width="40%"> ${name[i]}, &nbsp&nbsp${place[i]}</td>
       <td width="40%"> Class-from to class-to be updated</td>
       <td width="20%"> ${d_o_j[i]} - ${d_o_l[i]} </td>
       </tr>
       %if m_s[i]: 
          <tr>
          <td></td>
          %if o_f[i]:
             <td>Marks Secured: &nbsp&nbsp&nbsp${m_s[i]}/${o_f[i]} </tr>
          %else: 
             <td>Marks Secured: &nbsp&nbsp&nbsp${m_s[i]} </td>
          %endif
          </tr>
       <tr><td></td></tr>
       %endif
    %endfor
</%def>  
<%def name="display_project()"> <!-- displaying project details -->
    %for i in range(0,int(no_of_pro)):
       <tr>
       <td width="15%">Project no: ${i+1} </td>
       <td width="60%">${project_title[i]}</td>
       <td width="25%">${project_from[i]} - ${project_to[i]}</td>
       </tr>
       <tr>
       <td >Project Description:</td>
       <td>${project_desc[i]}</td>
       </tr>
       <tr>
       <td>Project Members:</td>
       <td>${project_mem[i]}</td>
       </tr>
       %if project_pub[i]:
         <tr>
         <td>Project Publications:</td>
         <td>${project_pub[i]}</td>
         </tr>
       %endif
       %if project_link[i]:
         <tr>
         <td>Project Links:</td>
         <td>${project_link[i]}</td>
         </tr>
       %endif
    %endfor
</%def>  
<%def name="display_skills()"> <!-- dispalying skill details -->
    %for i in range(0,int(no_of_skill)):
       <tr>
       <td width="15%"> ${i+1} </td>
       <td width="20%"> ${name_skill[i]} </td>
       <td width="20%">${level_skill[i]}</td>
       <td width="45%"> endorsed by </td>
       </tr>     
    %endfor
</%def>
</body>
</html>
