$(document).on('click', '#recipe_add_ingredient', function(){
	$('#add_ingredient').append('<tr><th><input type="text" name="item_name" id="item_name" placeholder="Item Name" /></th><th><input type="text" name="item_quantity"id="item_quantity" placeholder="Item Quantity" /></th></tr>');
});

$(document).on('click', '#recipe_submit', function(){
	data = $('#save_recipe').serialize();
	$.ajax({
		url: '/recipes/commit',
		data: data,
		type: 'post',
		success: function(resp){
			if(resp == "Success"){
				window.location = '/recipes/view'
			}
			else{
				alert('something fucked up :[');
			}
		}
	});
});


$(document).on('click', '.view_recipe', function(){
	id = $(this).attr('id');
	window.location = "/recipes/view/" + id;
});

$(document).on('click', '#calendar_submit', function(){
	data = $('#date_recipe').serialize();
	$.ajax({
		url: '/calendar/commit',
		data: data,
		type: 'post', 
		success: function(resp){
			alert(resp);
		}
	});
});

$(document).ready(function(){
	$('#calendar_date').datepicker();
});
