

//Funktion zum Ausgeben von Texten. Der Übergabeparameter 'meinText' ist vom Typ String. Der Text wird beim Aufrufen der Methode definiert, also in der HTML Datei. "SBR/Test/Tablet/TextEvent" ist die Bezeichnung des Aktors der im Choreograph Projekt aufgerufen wird
function textOnClick(meinText){
  console.log("Text: " + meinText);
  $.raiseALMemoryEvent("SBR/Test/Tablet/TextEvent", meinText);
}


//Funktion videoOnClick 1-n zum Ausgeben von Videos.Die Videos sind im Ordner 'Videos' hinterlegt. Der relative Pfad zum Video befindet sich im Choreograph Projekt. "SBR/Test/Tablet/video" ist die Bezeichnung des Aktors der im Choreograph Projekt aufgerufen wird. Für jedes Video musste ein seperater Aktor definiert werden.
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


//Funktion bildOnClick 1-n zum Ausgeben von Bildern.Die Bilder sind im Ordner 'Bilder' hinterlegt. Der relative Pfad zum Bild befindet sich im Choreograph Projekt. "SBR/Test/Tablet/bild" ist die Bezeichnung des Aktors der im Choreograph Projekt aufgerufen wird. Für jedes Bild musste ein seperater Aktor definiert werden.
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

