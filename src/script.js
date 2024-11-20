$(document).ready(function(){

  var liEngagement = $(".linkedin__engagement");
  var randomNumbers = [];

  liEngagement.each(function(index){
    number = Math.floor((Math.random() * 525) + 1);

    while( $.inArray(number,randomNumbers) != -1 ){
      number = Math.floor((Math.random() * 525) + 1);
    }

    randomNumbers.push(number);
    liEngagement.eq(index).html(number);

  });
});