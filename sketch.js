// Copyright (c) 2019 ml5
//
// This software is released under the MIT License.
// https://opensource.org/licenses/MIT

/* ===
ml5 Example
PoseNet example using p5.js
=== */

let video;
let poseNet;
let poses = [];
let fps = 16;

let poseClass = "Not detected yet";
let previousPose = 'Other';

let happyTime = 0;
let happyMoments = 0;
let shockTime = 0;
let shockMoments = 0;
let annoyTime = 0;
let annoyMoments = 0;
let temporaryVar = 0;



function setup() {
  createCanvas(640, 480);
  video = createCapture(VIDEO);
  video.size(width, height);

  // Create a new poseNet method with a single detection
  poseNet = ml5.poseNet(video, modelReady);
  // This sets up an event that fills the global variable "poses"
  // with an array every time new poses are detected
  poseNet.on('pose', function(results) {
    poses = results;
  });
  // Hide the video element, and just show the canvas
  video.hide();
}

function modelReady() {
  select('#status').html('Model Loaded');
}

function mousePressed(){
  console.log(JSON.stringify(poses))
}

function draw() {
  image(video, 0, 0, width, height);
  strokeWeight(2);

   if (poses.length > 0) {
     let pose = poses[0].pose;
     mousePressed();

  // Extract keypoints from each frame
  for (let i = 0; i < pose.keypoints.length; i++){
    let x = pose.keypoints[i].position.x;
    let y = pose.keypoints[i].position.y;
    fill(0,255,255);
    ellipse(x, y, 16, 16);
  }
  
  
  // For this assignment poses related to 3 emotions were selected: Happiness, Shock and Annoyance. 
  // In order to differentiate between these poses if-else statements with multiple conditions were written.
  
  ///// Pose "Happiness" is with both arms lifted high as if celebrating
  ///// Pose "Shock" is similar but with wrists around the head
  ///// Pose "Annoyed" is when arms are on the hips
  ///// Any pose outside these conditions will be classified as "Other"
  if ((pose['leftElbow'].y > pose['leftWrist'].y) && (pose['rightElbow'].y > pose['rightWrist'].y) 
	&& ((pose['leftElbow'].x - pose['leftWrist'].x) < 20) && ((pose['rightElbow'].x - pose['rightWrist'].x) < 20) 
	&& (pose['leftElbow'].y < pose['leftShoulder'].y)){
		previousPose = poseClass;
		poseClass = 'Happy';
  } else if ((pose['leftElbow'].y > pose['leftWrist'].y) && (pose['rightElbow'].y > pose['rightWrist'].y) 
	  && (pose['leftElbow'].x > pose['leftWrist'].x) && (pose['rightElbow'].x < pose['rightWrist'].x) 
	  && (pose['leftWrist'].y < pose['leftShoulder'].y)){
		previousPose = poseClass;
		poseClass = 'Shocked';  
  } else if ((pose['leftElbow'].y < pose['leftWrist'].y) && (pose['rightElbow'].y < pose['rightWrist'].y) 
	  && (pose['leftElbow'].x > pose['leftWrist'].x) && (pose['rightElbow'].x < pose['rightWrist'].x) 
	  && (pose['leftWrist'].y > pose['leftShoulder'].y)){
		previousPose = poseClass;
		poseClass = 'Annoyed';  
  } else {
	    previousPose = poseClass;
	    poseClass = 'Other';
  }
  
  
  // In order to get the stats on each pose, counters must be written:
  // However, as we are dealing with frame numbers rather than time data,
  // we have to use the frame per second ratio and by counting fps we estimate
  // time in seconds.
  // *In order to track how much time is spent on the current emotion pose, the variable
  //  temporaryVar has been created. When the pose changed to another, it is reseted. 
  if (previousPose == poseClass) {
	  if (poseClass == 'Happy') {
		happyTime = happyTime + 1;
		temporaryVar = temporaryVar + 1;
	  } else if (poseClass == 'Shocked') {
		shockTime = shockTime + 1;
		temporaryVar = temporaryVar + 1;
	  } else if (poseClass == 'Annoyed') {
		annoyTime = annoyTime + 1;
		temporaryVar = temporaryVar + 1;
	  } else {

	  }
  } else {
	  // Whenever the emotion pose changes to another, the counter of happy/shock/annoyed moments will increment.
	  // In order to eliminate the noise that occur when any emotion pose is selected accidentally for
	  // a short period of time, the temporaryVar counter of previous pose has to be at least 2 times fps (or 2 seconds). 
	  if (previousPose == 'Happy' && temporaryVar > (fps*2)) {
		happyMoments = happyMoments + 1;
		temporaryVar = 0;
	  } else if (previousPose == 'Shocked' && temporaryVar > (fps*2)) {
		shockMoments = shockMoments + 1;
		temporaryVar = 0;
	  } else if (previousPose == 'Annoyed' && temporaryVar > (fps*2)) {
		annoyMoments = annoyMoments + 1;
		temporaryVar = 0;
	  }
  }
  
  
  
  // Now, in order to display class name on the screen, we use:
  // *The class name text changes its color depending on the class for convenience
  textSize(30);
  if (poseClass == 'Happy') {
	fill(0,255,0);
  } else if (poseClass == 'Shocked') {
	fill(255,255,0);
  } else if (poseClass == 'Annoyed') {
	fill(255,0,100);
  } else {
	fill(255, 255, 255);
  }
  text('Class:   ' + poseClass, 10, 400);
  
  fill(255, 255, 255);
  textSize(15);
  text('Happiness moments (time): ' + happyMoments + ' (' + nf(happyTime/fps, 2, 2) + 's)', 10, 425);
  text('Shock moments (time): ' + shockMoments + ' (' + nf(shockTime/fps, 2, 2) + 's)', 10, 450);
  text('Annoyance moments (time): ' + annoyMoments + ' (' + nf(annoyTime/fps, 2, 2) + 's)', 10, 472);
  
}
}