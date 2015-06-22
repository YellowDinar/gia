$(window).scroll(function() {
	
		"use strict";

		if ($().easyPieChart) {
			var count = 0 ;
			var colors = ['#3cbea7'];
			$('.percentage').each(function(){

					
				var imagePos = $(this).offset().top;
				var topOfWindow = $(window).scrollTop();
				if (imagePos < topOfWindow+600) {

					$(this).easyPieChart({
						barColor: colors[count],
						trackColor: '#202020',
						scaleColor: false,
						scaleLength: false,
						lineCap: 'butt',
						lineWidth: 8,
						size: 130,
						rotate: 0,
						animate: 2000,
						onStep: function(from, to, percent) {
								$(this.el).find('.percent').text(Math.round(percent));
							}
					});
				}

				count++;
				if (count >= colors.length) { count = 0};
			});
		}

	});