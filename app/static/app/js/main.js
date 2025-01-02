// Đoạn mã JavaScript đã sửa
const songs = [
    { title: "Những kẻ mộng mơ", artist: "Noo Phước Thịnh", src: "media/audio/nhung-ke-mong-mo.mp3" },
    { title: "Tái sinh", artist: "Tùng Dương", src: "media/audio/tai-sinh.mp3" },
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


const currentTimeElement = document.getElementById('current-time');
const totalTimeElement = document.getElementById('total-time');

// Hàm định dạng thời gian (giây -> phút:giây)
function formatTime(seconds) {
    const mins = Math.floor(seconds / 60);
    const secs = Math.floor(seconds % 60);
    return `${mins}:${secs < 10 ? '0' + secs : secs}`;
}

// Cập nhật thời gian hiện tại và tổng thời gian
audio.addEventListener('timeupdate', () => {
    currentTimeElement.textContent = formatTime(audio.currentTime);
    totalTimeElement.textContent = formatTime(audio.duration || 0);
});

const progress = document.getElementById('progress');

// Cập nhật tiến trình khi bài hát phát
audio.addEventListener('timeupdate', () => {
    const progressPercent = (audio.currentTime / audio.duration) * 100;
    progress.value = progressPercent || 0;
});

// Tua bài hát khi kéo thanh tiến trình
progress.addEventListener('input', () => {
    const newTime = (progress.value / 100) * audio.duration;
    audio.currentTime = newTime;
});


// Xem thêm nếu mô tả bài hát dài
document.querySelectorAll(".toggle-text").forEach((btn) => {
  btn.addEventListener("click", function () {
    const cardText = this.previousElementSibling;
    const isTruncated = cardText.classList.toggle("text-truncate");
    const fullText = cardText.getAttribute("data-full-text");
    if (!isTruncated) {
      cardText.textContent = fullText; // Hiển thị đầy đủ nội dung
      this.textContent = "Thu gọn";
    } else {
      cardText.textContent = fullText.substring(0, 100) + "..."; // Rút gọn nội dung
      this.textContent = "Xem thêm";
    }
  });
});


