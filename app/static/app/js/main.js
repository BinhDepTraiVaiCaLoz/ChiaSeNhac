// Đoạn mã JavaScript đã sửa
const songs = [
    { title: "Tái sinh", artist: "Tùng Dương", src: "static/app/audio/tai-sinh.mp3" },
    { title: "Những kẻ mộng mơ", artist: "Noo Phước Thịnh", src: "static/app/audio/nhung-ke-mong-mo.mp3" },
];

let currentSongIndex = 0;

// Lấy các phần tử từ DOM
const audio = document.getElementById('audio');
const playPauseButton = document.getElementById('play-pause');
const nextButton = document.getElementById('next');
const prevButton = document.getElementById('prev');
const songTitle = document.getElementById('song-title');
const artistName = document.getElementById('artist-name');

// Biến trạng thái phát nhạc
let isPlaying = false;

// Hàm tải bài hát
function loadSong(index) {
    const song = songs[index];
    audio.src = song.src;
    songTitle.textContent = song.title;
    artistName.textContent = song.artist;
}

// Hàm phát nhạc
function playSong() {
    audio.play();
    isPlaying = true;
    playPauseButton.innerHTML = '<i class="fas fa-pause"></i>'; // Cập nhật biểu tượng thành Pause
}

// Hàm tạm dừng nhạc
function pauseSong() {
    audio.pause();
    isPlaying = false;
    playPauseButton.innerHTML = '<i class="fas fa-play"></i>'; // Cập nhật biểu tượng thành Play
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

// Tải bài hát đầu tiên khi trang được mở
loadSong(currentSongIndex);
