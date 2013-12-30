<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Neuron - ${f_name} ${l_name}</title>
</head>
<body>
<div id="pursuing">
	<h1>Pursuing</h1>
</div>
<div id="pursuers">
	<h1>Pursuers</h1>
</div>
<div id="mutual">
	<h1>Mutual</h1>
</div>	
<script src="http://code.jquery.com/jquery-1.9.1.js"></script>
<script src="http://code.jquery.com/ui/1.10.3/jquery-ui.js"></script>
<script>
$(document).ready(function(){ //this is supposed to be the default tab. When the other tabs are clicked, similar methods have to be performed
	pursuing=$('#pursuing');
	pursuers=$('#pursuers');
	mutual=$('#mutual');
	$.getJSON('/viewpursuing.json',function(data){
		$.each(data,function(key,val)
		{
		$('<div class="person"><h3>'+key+'</h3><img src="'+val+'" alt="friend" height="50" width="50"/\><br/\></div').appendTo(pursuing);
		});
	});	
	$.getJSON('/viewpursuers.json',function(data){
		$.each(data,function(key,val)
		{
		$('<div class="person"><h3>'+key+'</h3><img src="'+val+'" alt="friend" height="50" width="50"/\><br/\></div').appendTo(pursuers);
		});
	});
	$.getJSON('/viewmutual.json',function(data){
		$.each(data,function(key,val)
		{
		$('<div class="person"><h3>'+key+'</h3><img src="'+val+'" alt="friend" height="50" width="50"/\><br/\></div').appendTo(mutual);
		});
	});
});
</script>
</body>
</html>

