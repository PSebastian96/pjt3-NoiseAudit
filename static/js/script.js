//mobile navbar
$(document).ready(function(){
    $('.sidenav').sidenav();
  });

//active current page
  $(document).ready(function(){
    $('ul li a').click(function(){
      $('li a').removeClass("active");
      $(this).addClass("active");
  });
  });