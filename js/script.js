$(document).ready(function(){
	var oY = $(".column").offset().top;
	$(".column").css("top","-50%");
	$(".column").addClass("run");

    $(".navbar-brand").click(function(){
    	if($(".column").hasClass("run")){
			$(".column").animate({'top':oY},"slow");
			$(".column").removeClass("run");
		}
		else{
			$(".column").animate({'top':'-50%'},"slow");
			$(".column").addClass("run");
		}
    });

    var tVal;
    $(".nav-choice").click(function(){
    	tVal = $(this).attr('id');
    	console.log(tVal);
    	if($("."+ tVal).hasClass("run")){
    		console.log("Yes");
			$("."+ tVal).animate({'top':oY},"slow");
			$("."+ tVal).removeClass("run");
		}
		else{
			$("."+ tVal).animate({'top':'-50%'},"slow");
			$("."+ tVal).addClass("run");
		}
    });

	$(".name").click(function () {
			//stuff to do on mouse enter
			if($(".content").hasClass("off")){
				$(".content").css("bottom","5%");
				$(".name").css("top","20%");
				$(".content").removeClass("off");
			}
			//stuff to do on mouse leave
			else{
				$(".content").css("bottom","-100%");
				$(".name").css("top","75%");
				$(".content").addClass("off");
			}
	});
    var origin = 15;
    var size;
	for(var i = 1; i< 6; i++){
		if($(".column").hasClass(i)){
			size = origin*i;
			$("."+i).css("left",size+"%");
		}
	}
	
	$("div.tri0").toggleClass("toggle");
	$("div.name").click(function(){
        $("div.tri0").toggleClass("toggle");
    });
	
	var link;
	$(".link").click(function () {
		link = $(this).attr('id');
		$("#target").attr("src", ("data/"+link));
	});
});