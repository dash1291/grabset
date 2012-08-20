$( document ).ready( function() {
	var urlValidated = false;
	
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
		if( urlValidated ) {
			var url = $( '#url-field' ).val();
			$.get( '/download/' + url, function( data ) {

			} );
		}
		else {
			// Notify about bad url
		}
	} );
} );
