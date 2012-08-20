$( document ).ready( function() {
	var urlValidated = false;
  $( '#reporter' ).hide();	
	$( '#url-field' ).on( 'blur', function() {
		var p = 'flickr.com/photos/[^/]+/sets/[^/]+';
		var patt = new RegExp( p );
		var value = $( this ).val();
		urlValidated = false;
		if( patt.test( value ) ) {
			urlValidated = true;
			var url = 'http://www.' + $( this ).val().match( patt ) + '/';
			$( this ).val( url );
		}
	} );
	
	$( '#btn-download' ).on( 'click', function() {
		$( '#reporter' ).html('');
		var validationError = '<span class="error">You need to re-check the URL provided.</span>';
		var waiting = '<span id="waiting">Preparing the set for you to download...</span>';
		if( urlValidated ) {
			var url = $( '#url-field' ).val();
			$( '#reporter' ).html( waiting );
			$( '#reporter' ).slideDown('fast');

			function animateWaiting() {
				$( '#waiting' ).animate( { opacity: 0 }, 500 );
				$( '#waiting' ).animate( { opacity: 1 }, 500 );
				setTimeout( animateWaiting );
			}
			animateWaiting();

			$.get( '/download/' + url, function( data ) {
				var success = '<span>Here\'s the link</span><br/>' +
					'<a href="' + data + '">' + data + '</a>';
				$( '#reporter' ).html( success );
			} );
		}
		else {
			$( '#reporter' ).html( validationError );
			$( '#reporter' ).slideDown('fast');
		}
	} );
} );
