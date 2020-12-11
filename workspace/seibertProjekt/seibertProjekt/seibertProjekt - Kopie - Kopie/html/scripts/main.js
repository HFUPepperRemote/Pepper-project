


function text1OnClick(){
  $.raiseALMemoryEvent("SBR/Test/Tablet/TextEvent", "Hallo");
}

function text2OnClick(){
  $.raiseALMemoryEvent("SBR/Test/Tablet/TextEvent", "Hallo Text2");
}

function textOnClick(meinText){
  console.log("Text: " + meinText);
  $.raiseALMemoryEvent("SBR/Test/Tablet/TextEvent", meinText);
}

function videoOnClick(){
  $.raiseALMemoryEvent("SBR/Test/Tablet/video");
}

function videoOnClick2(){
  $.raiseALMemoryEvent("SBR/Test/Tablet/video2");
}

function videoOnClick3(){
  $.raiseALMemoryEvent("SBR/Test/Tablet/video3");
}

function videoOnClick4(){
  $.raiseALMemoryEvent("SBR/Test/Tablet/video4");
}


function meinTextVersuch () {
  window.location.href = 'informiereDich.html';
  
}

function bildOnClick1(){
  $.raiseALMemoryEvent("SBR/Test/Tablet/bild");
}

function bildOnClickSWP(){
  $.raiseALMemoryEvent("SBR/Test/Tablet/bild1");
}

function bildOnClickSZI(){
  $.raiseALMemoryEvent("SBR/Test/Tablet/bild2");
}

function bildOnClickSE(){
  $.raiseALMemoryEvent("SBR/Test/Tablet/bild3");
}

function bildOnClickNIS(){
  $.raiseALMemoryEvent("SBR/Test/Tablet/bild4");
}

function bildOnClickRAS(){
  $.raiseALMemoryEvent("SBR/Test/Tablet/bild5");
}

function bildOnClickMENTOREN(){
  $.raiseALMemoryEvent("SBR/Test/Tablet/bild6");
}

function bildOnClickSPROBIEREN(){
  $.raiseALMemoryEvent("SBR/Test/Tablet/bild7");
}






/*
function bafoegallgemein(){
  $.raiseALMemoryEvent("SBR/Test/Tablet/bafoegallgemein", 1);
}

function bafoegansprechpartner(){
  $.raiseALMemoryEvent("SBR/Test/Tablet/bafoegansprechpartner", 1);
*/

