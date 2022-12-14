//button
// $('.container-btn').on('click', '.btn-modal', function(e){
// 	e.preventDefault();
// 	if ( $(this).hasClass('play') ) {
// 		$(this).removeClass('play');
// 		$(this).addClass('pause');
// 	} else {
// 		$(this).removeClass('pause');
// 		$(this).addClass('play');
// 	}
// });

//audio
const audio = document.getElementsByTagName("audio")[0]
const playButton = document.getElementById("play")
const stopButton = document.getElementById("stop")
const audioEnd = document.querySelector('audio')

playButton.addEventListener('click', () => {
  if (audio.paused) {
	audio.play()
	let elements = document.getElementsByClassName("btn-modal");
    elements[0].classList.add("pause");
	elements[0].classList.remove("play");
  } else {
	audio.pause()
	let elements = document.getElementsByClassName("btn-modal");
    elements[0].classList.add("play");
	elements[0].classList.remove("pause");
  }
})

audioEnd.addEventListener('ended', (event) => {
	let elements = document.getElementsByClassName("btn-modal");
    elements[0].classList.add("play");
	elements[0].classList.remove("pause");
	playButton.addEventListener('click', () => {
		audio.play()
		let elements = document.getElementsByClassName("btn-modal");
		elements[0].classList.add("pause");
		elements[0].classList.remove("play");
	  })
})



stopButton.addEventListener('click', () => {
  audio.pause()
  audio.currentTime = 0
  let elements = document.getElementsByClassName("btn-modal");
  elements[0].classList.add("play");
  elements[0].classList.remove("pause");
})

audio.addEventListener("timeupdate", (e) => {
  const current = Math.floor(audio.currentTime)
  const duration = Math.round(audio.duration)
  if(!isNaN(duration)){
	document.getElementById('current').innerHTML = playTime(current)
	document.getElementById('duration').innerHTML = playTime(duration)
	const percent = Math.round((audio.currentTime/audio.duration)*1000)/10
	document.getElementById('seekbar').style.backgroundSize = percent + '%'
  }
})

document.getElementById('seekbar').addEventListener("click", (e) => {
  const duration = Math.round(audio.duration)
  if(!isNaN(duration)){
	const mouse = e.pageX
	const element = document.getElementById('seekbar')
	const rect = element.getBoundingClientRect()
	const position = rect.left + window.pageXOffset
	const offset = mouse - position
	const width = rect.right - rect.left
	audio.currentTime = Math.round(duration * (offset / width))
  }
})

function playTime (t) {
  let hms = ''
  const h = t / 3600 | 0
  const m = t % 3600 / 60 | 0
  const s = t % 60
  const z2 = (v) => {
	const s = '00' + v
	return s.substr(s.length - 2, 2)
  }
  if(h != 0){
	hms = h + ':' + z2(m) + ':' + z2(s)
  }else if(m != 0){
	hms = z2(m) + ':' + z2(s)
  }else{
	hms = '00:' + z2(s)
  }
  return hms
}