document.addEventListener('DOMContentLoaded', () => {
    const subImages = document.querySelectorAll('.sub-image');
    subImages.forEach(image => {
        image.addEventListener('click', () => {
            const mainImage = document.querySelector(image.getAttribute('data-target'));
            mainImage.src = image.src;
        });
    });
});