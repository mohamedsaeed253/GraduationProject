var segTest = document.getElementById('seg');
var preTest = document.getElementById('pre');
var fltTest = document.getElementById('flt');

function show1(){
    segTest.style.display = 'flex';
    preTest.style.display = 'none';
    fltTest.style.display = 'none';
}

function show2(){
    segTest.style.display = 'none';
    preTest.style.display = 'flex';
    fltTest.style.display = 'none';
}

function show3(){
    segTest.style.display = 'none';
    preTest.style.display = 'none';
    fltTest.style.display = 'flex';
}

$('ul li a').click(function(){
    $('ul li a').removeClass('active');
    $(this).addClass('active');
 }) ;

$(window).scroll(function(){
    if($(window).scrollTop()>500){
        $('#gotop').fadeIn();
    }    
    else{
        $('#gotop').fadeOut();
    }
});
$('#gotop').click(function(){
    $('html,body').animate({scrollTop:0},1500)
});