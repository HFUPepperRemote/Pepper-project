
// タッチイベントによるハンドラ
$(function() {
  $('#fast_button').on({
      'touchstart': function () {
          $.raiseALMemoryEvent("SBR/Test/Tablet/FastTouch", 1);
      },
  });
});

// HTML onClickeによるハンドラ
function slowRep(){
  $.raiseALMemoryEvent("SBR/Test/Tablet/SlowTouch", 1);
}

function bafoegallgemein(){
  $.raiseALMemoryEvent("SBR/Test/Tablet/bafoegallgemein", 1);
}

function bafoegansprechpartner(){
  $.raiseALMemoryEvent("SBR/Test/Tablet/bafoegansprechpartner", 1);
}

