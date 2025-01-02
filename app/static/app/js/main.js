let songs = [];
let currentSongIndex = 0;
let isPlaying = false; // Trạng thái phát nhạc

// Lấy các phần tử từ DOM
const audio = document.getElementById('audio');
const playPauseButton = document.getElementById('play-pause');
const nextButton = document.getElementById('next');
const prevButton = document.getElementById('prev');
const songTitle = document.getElementById('song-title');
const artistName = document.getElementById('artist-name');
const currentTimeElement = document.getElementById('current-time');
const totalTimeElement = document.getElementById('total-time');
const progress = document.getElementById('progress');

// Fetch songs from API
fetch('/api/musics/')
  .then(response => {
    if (!response.ok) {
      throw new Error('Network response was not ok');
    }
    return response.json();
  })
  .then(data => {
    if (data && data.length > 0) {
      songs = data; // Gán dữ liệu bài hát
      loadSong(currentSongIndex); // Tải bài hát đầu tiên
    } else {
      console.error('No songs found in the response');
    }
  })
  .catch(error => console.error('Error fetching songs:', error));

// Hàm tải bài hát
function loadSong(index) {
    if (!songs || songs.length === 0) {
        console.error('No songs available to load');
        return;
    }
    const song = songs[index];
    if (!song) {
        console.error('Invalid song index');
        return;
    }
    audio.src = song.music_link;
    songTitle.textContent = song.name || "Unknown Title";
    artistName.textContent = song.artist.map(a => a.name).join(", ") || "Unknown Artist";
}

// Hàm phát nhạc
function playSong() {
    audio.play();
    isPlaying = true;
    playPauseButton.innerHTML = '<i class="fas fa-pause"></i>';
}

// Hàm tạm dừng nhạc
function pauseSong() {
    audio.pause();
    isPlaying = false;
    playPauseButton.innerHTML = '<i class="fas fa-play"></i>';
}

// Hàm chuyển bài kế tiếp
function nextSong() {
    currentSongIndex = (currentSongIndex + 1) % songs.length;
    loadSong(currentSongIndex);
    playSong();
}

// Hàm quay lại bài trước
function prevSong() {
    currentSongIndex = (currentSongIndex - 1 + songs.length) % songs.length;
    loadSong(currentSongIndex);
    playSong();
}

// Event listener cho nút Play/Pause
playPauseButton.addEventListener('click', () => {
    if (isPlaying) {
        pauseSong();
    } else {
        playSong();
    }
});

// Event listeners cho nút Next và Prev
nextButton.addEventListener('click', nextSong);
prevButton.addEventListener('click', prevSong);

// Xử lý khi bài hát kết thúc
audio.addEventListener('ended', nextSong);

// Cập nhật thời gian hiện tại và tổng thời gian
audio.addEventListener('timeupdate', () => {
    if (audio.duration) {
        currentTimeElement.textContent = formatTime(audio.currentTime);
        totalTimeElement.textContent = formatTime(audio.duration);
        const progressPercent = (audio.currentTime / audio.duration) * 100;
        progress.value = progressPercent;
    }
});

// Tua bài hát khi kéo thanh tiến trình
progress.addEventListener('input', () => {
    if (audio.duration) {
        const newTime = (progress.value / 100) * audio.duration;
        audio.currentTime = newTime;
    }
});

// Hàm định dạng thời gian
function formatTime(seconds) {
    const mins = Math.floor(seconds / 60);
    const secs = Math.floor(seconds % 60);
    return `${mins}:${secs < 10 ? '0' + secs : secs}`;
}
