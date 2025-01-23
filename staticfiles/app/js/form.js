document.querySelectorAll('.dropdown-item').forEach(function(item) {
    item.addEventListener('mouseenter', function() {
        let submenu = item.querySelector('.submenu');
        if (submenu) {
            submenu.style.display = 'block';
            submenu.style.opacity = '1';
            submenu.style.transform = 'translateY(0)';
        }
    });

    item.addEventListener('mouseleave', function() {
        let submenu = item.querySelector('.submenu');
        if (submenu) {
            submenu.style.display = 'none';
            submenu.style.opacity = '0';
            submenu.style.transform = 'translateY(20px)';
        }
    });
});

