var Voyager = L.tileLayer('https://{s}.basemaps.cartocdn.com/rastertiles/voyager/{z}/{x}/{y}{r}.png')

var baseMaps = {
  "Voyager": Voyager              
};

var rainviewer = L.control.rainviewer({
  position: 'bottomleft',
  nextButtonText: '>',
  playStopButtonText: 'Start/Stop',
  prevButtonText: '<',
  positionSliderLabelText: "Time:",
  opacitySliderLabelText: "Opacity:",
  animationInterval: 500,
  opacity: 0.5
});

mymap = L.map('mapid').setView([-27.471, 153.026], 7);

L.control.layers(baseMaps).addTo(mymap);

baseMaps['Voyager'].addTo(mymap);

rainviewer.addTo(mymap);