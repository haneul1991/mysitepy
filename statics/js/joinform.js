$(function(){
	$('#email').change(function(){
		console.log('changed!!!');
		$('#btn-emailcheck').show();
		$('#img-emailcheck').hide();
	});

	$('#btn-emailcheck').click(function(){

		email = $('#email').val();
		if(email == ''){
			return;
		}

		$.ajax({
			url: '/user/checkemail?email=' + email,
			type: 'get',
			data: '',
			dataType: 'json',
			success: function(response){
				if(response.result == false){
					alert('이미 존재하는 email입니다.');
					$('#email').val('').focus;
					return;
				}
				$('#btn-emailcheck').hide();
				$('#img-emailcheck').show();
				}
		});
	});
});