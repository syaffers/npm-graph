var info = document.getElementById("info");
info.style.height = window.innerHeight + ".px";

document.getElementById('the-graph').addEventListener('load', function(){
  // Will get called after embed element was loaded
  svgPanZoom(document.getElementById('the-graph'), {
    viewportSelector: '.svg-pan-zoom_viewport',
    minZoom: 0.15,
    fit: true,
    center: true
  });
});

window.addEventListener('resize', function() {
  info.style.height = window.innerHeight + ".px";
});
