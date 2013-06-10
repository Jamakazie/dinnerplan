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


//$(document).on('click', '.view_recipe', function(){
//	id = $(this).attr('id');
//	window.location = "/recipes/view/" + id;
//});

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

$(document).on('change', '#calendar_date', function(){
	date = encodeURIComponent($('#calendar_date').val());
	$.ajax({
		url: '/calendar/add/getrecipe',
		data: 'date=' +date,
		type: 'get',
		success: function(resp){
			$('#calendar_recipe').val(resp);
		}
	});

});

$(document).on('click', '#list_submit', function(){
	start_date = encodeURIComponent($('#start_date').val());
	end_date = encodeURIComponent($('#end_date').val());
	$.ajax({
		url: '/calendar/grocerylist/generate',
		data: 'start_date=' + start_date + '&end_date=' + end_date,
		type: 'get',
		success: function(resp){
			$('#grocery_list_body').html('');
			items = JSON.parse(resp);
			for (var key in items){
				for( var subkey in items[key]){
					ingredient = subkey;
					quantity = items[key][subkey];
					$('#grocery_list_body').append('<tr class="sortable"><th>'+ingredient+'</th><th>'+quantity+'</th></tr>');
				}
			}
		}
	});
});

$(document).on('click', '.sortable', function(){
	$(this).toggleClass('strikeout')
});

$(document).ready(function(){
	$('#calendar_date').datepicker();
	$('#start_date').datepicker();
	$('#end_date').datepicker();
});
