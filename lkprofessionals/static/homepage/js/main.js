// JavaScript for Mobile Menu Toggle
document.addEventListener('DOMContentLoaded', () => {
    const menuToggle = document.getElementById('menu-toggle');
    const menu = document.getElementById('menu');

    if (menuToggle) {
        menuToggle.addEventListener('click', () => {
            menu.classList.toggle('hidden');
        });
    }
});
