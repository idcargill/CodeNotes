// holds all our rectangles
var boxes = [];

//Box object to hold data for all drawn rects
function Box() {
  this.x = 0;
  this.y = 0;
  this.w = 1; // default width and height?
  this.h = 1;
  this.fill = "#444444";
}

//Initialize a new Box, add it, and invalidate the canvas
function addRect(x, y, w, h, fill) {
  var rect = new Box();
  rect.x = x;
  rect.y = y;
  rect.w = w;
  rect.h = h;
  rect.fill = fill;
  boxes.push(rect);
  // invalidate();
}

var canvas;
var ctx;
var WIDTH;
var HEIGHT;
var INTERVAL = 20; // how often, in milliseconds, we check to see if a redraw is needed

var isDrag = false;
var mx, my; // mouse coordinates

// when set to true, the canvas will redraw everything
// invalidate() just sets this to false right now
// we want to call invalidate() whenever we make a change
var canvasValid = false;

// The node (if any) being selected.
// If in the future we want to select multiple objects, this will get turned into an array
var mySel;

// The selection color and width. Right now we have a red selection with a small width
var mySelColor = "#CC0000";
var mySelWidth = 2;

// we use a fake canvas to draw individual shapes for selection testing
var ghostcanvas;
var gctx; // fake canvas context

// since we can drag from anywhere in a node
// instead of just its x/y corner, we need to save
// the offset of the mouse when we start dragging.
var offsetx, offsety;

// Padding and border style widths for mouse offsets
var stylePaddingLeft, stylePaddingTop, styleBorderLeft, styleBorderTop;

// initialize our canvas, add a ghost canvas, set draw loop
// then add everything we want to intially exist on the canvas
function init() {
  canvas = document.getElementById("canvas");
  HEIGHT = canvas.height;
  WIDTH = canvas.width;
  ctx = canvas.getContext("2d");
  ghostcanvas = document.createElement("canvas");
  ghostcanvas.height = HEIGHT;
  ghostcanvas.width = WIDTH;
  gctx = ghostcanvas.getContext("2d");

  //fixes a problem where double clicking causes text to get selected on the canvas
  canvas.onselectstart = function () {
    return false;
  };

  // fixes mouse co-ordinate problems when there's a border or padding
  // see getMouse for more detail
  if (document.defaultView && document.defaultView.getComputedStyle) {
    stylePaddingLeft = parseInt(document.defaultView.getComputedStyle(canvas, null)["paddingLeft"], 10) || 0;
    stylePaddingTop = parseInt(document.defaultView.getComputedStyle(canvas, null)["paddingTop"], 10) || 0;
    styleBorderLeft = parseInt(document.defaultView.getComputedStyle(canvas, null)["borderLeftWidth"], 10) || 0;
    styleBorderTop = parseInt(document.defaultView.getComputedStyle(canvas, null)["borderTopWidth"], 10) || 0;
  }

  // make draw() fire every INTERVAL milliseconds.
  setInterval(draw, INTERVAL);

  // add our events. Up and down are for dragging,
  // double click is for making new boxes
  canvas.onmousedown = myDown;
  canvas.onmouseup = myUp;
  canvas.ondblclick = myDblClick;

  // add custom initialization here:

  // add an orange rectangle
  addRect(200, 200, 40, 40, "#FFC02B");

  // add a smaller blue rectangle
  addRect(25, 90, 25, 25, "#2BB8FF");
}
