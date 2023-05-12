'use strict';

var chaigaramContainer = document.querySelector('.chaigaram');
var allCards = document.querySelectorAll('.chaigaram--card');
var nope = document.getElementById('nope');
var love = document.getElementById('love');

function initCards(card, index) {
  var newCards = document.querySelectorAll('.chaigaram--card:not(.removed)');

  newCards.forEach(function (card, index) {
    card.style.zIndex = allCards.length - index;
    card.style.transform = 'scale(' + (20 - index) / 20 + ') translateY(-' + 30 * index + 'px)';
    card.style.opacity = (10 - index) / 10;
  });
  
  chaigaramContainer.classList.add('loaded');
}

function newtab(url){
  window.open(url,"_blank")
}


initCards();

allCards.forEach(function (el) {
  var hammertime = new Hammer(el);

  hammertime.on('pan', function (event) {
    el.classList.add('moving');
    // This function here runs when we move a card
    
  });

  hammertime.on('pan', function (event) {
    if (event.deltaX === 0) return;
    if (event.center.x === 0 && event.center.y === 0) return;

    chaigaramContainer.classList.toggle('chaigaram_love', event.deltaX > 0);
    
    chaigaramContainer.classList.toggle('chaigaram_nope', event.deltaX < 0);

    var xMulti = event.deltaX * 0.03;
    var yMulti = event.deltaY / 80;
    var rotate = xMulti * yMulti;

    event.target.style.transform = 'translate(' + event.deltaX + 'px, ' + event.deltaY + 'px) rotate(' + rotate + 'deg)';
  });

  hammertime.on('panend', function (event) {
    // console.log('Yes')
    el.classList.remove('moving');
    chaigaramContainer.classList.remove('chaigaram_love');
    chaigaramContainer.classList.remove('chaigaram_nope');

    var moveOutWidth = document.body.clientWidth;
    var keep = Math.abs(event.deltaX) < 80 || Math.abs(event.velocityX) < 0.5;

    event.target.classList.toggle('removed', !keep);

    if (keep) {
      // console.log('keep')
      event.target.style.transform = '';
    } else {
      // console.log('else')
      // this will run if we remove the card by swiping left or right
      var endX = Math.max(Math.abs(event.velocityX) * moveOutWidth, moveOutWidth);
      var toX = event.deltaX > 0 ? endX : -endX;
      var endY = Math.abs(event.velocityY) * moveOutWidth;
      var toY = event.deltaY > 0 ? endY : -endY;
      var xMulti = event.deltaX * 0.03;
      var yMulti = event.deltaY / 80;
      var rotate = xMulti * yMulti;

      event.target.style.transform = 'translate(' + toX + 'px, ' + (toY + event.deltaY) + 'px) rotate(' + rotate + 'deg)';
      
      
      var notMobile = !(navigator.userAgent.match(/Android/i)
      || navigator.userAgent.match(/webOS/i)
      || navigator.userAgent.match(/iPhone/i)
      || navigator.userAgent.match(/iPad/i)
      || navigator.userAgent.match(/iPod/i)
      || navigator.userAgent.match(/BlackBerry/i)
      || navigator.userAgent.match(/Windows Phone/i)) 
      if(notMobile){
        //If the website is not being viewed on a mobile then this will run
      if(event.deltaX > 0){
        // console.log('love')
        //swiping left does nothing

      } else {
        //swiping right open the link if it exists
        
        url = event.target.childNodes[3].textContent
        console.log(event.target.childNodes[3].textContent)
        if (url != 'None'){
          newtab(url)
        }
        
      }}



      initCards();
    }
  });
});
