const heroSlides = document.querySelectorAll(".hero-slide");
const nextBtn = document.querySelector(".hero-next-btn");
const prevBtn = document.querySelector(".hero-prev-btn");

let currentSlide = 0;

function showHeroSlide(index) {
  heroSlides.forEach((slide, i) => {
    slide.classList.remove("hero-active");
    slide.style.opacity = 0;
    if (i === index) {
      slide.classList.add("hero-active");
      slide.style.opacity = 1;
      slide.style.transition = "opacity 1s ease-in-out";
    }
  });
}

function nextHeroSlide() {
  currentSlide = (currentSlide + 1) % heroSlides.length;
  showHeroSlide(currentSlide);
}

function prevHeroSlide() {
  currentSlide = (currentSlide - 1 + heroSlides.length) % heroSlides.length;
  showHeroSlide(currentSlide);
}

nextBtn.addEventListener("click", nextHeroSlide);
prevBtn.addEventListener("click", prevHeroSlide);

// Auto-change every 4 seconds
setInterval(nextHeroSlide, 4000);
