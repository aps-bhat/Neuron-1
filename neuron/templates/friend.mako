<!doctype html>
<html lang="en">
<head>
<title>
Neuron - ${f_name} ${l_name}
</title>
<script src="http://code.jquery.com/jquery-1.9.1.js"></script>
<script src="http://code.jquery.com/ui/1.10.3/jquery-ui.js"></script>
<script>
$(function(){
		var name=document.getElementById("pursue").name;
		var datatosend={
			"Pursuing": name
		};
$(document).ready(function(){
	$.getJSON('/checkpursuing.json',datatosend,function(data)
	{
	$.each(data,function(key,val)
	{
		if(val=="true")
		{
			document.getElementById("pursue").value="pursuing";
		}
	});	
	});
});
function add_pursuer()
{
	
	$.getJSON('/addpursuer.json',datatosend,function(data)
	{
		$.each(data,function(key,val)
		{
			if(val=="success")
			{
				document.getElementById("pursue").value="pursuing";
			}
		});
	});
}	
function remove_pursuer()
{
	
	$.getJSON('/removepursuer.json',datatosend,function(data)
	{
		$.each(data,function(key,val)
		{
			if(val=="success")
			{
				document.getElementById("pursue").value="pursue";
			}
		});
	});
}
$("#pursue").click(function(){
	var value=document.getElementById("pursue").value;
	if(value=="pursue")
	{
		add_pursuer();	
	}
	else
	{
		remove_pursuer();
	}
});
});
</script>
</head>
<body>
<center><pre>${f_name}   ${l_name}</pre></center>
<input type="button" id="pursue" name="${this_username}" value="pursue" />
<br/>
<br/>
<a href="/home">home</a>
</body>
</html>