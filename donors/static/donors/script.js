// Hero typing effect
const heroText = document.querySelector(".hero h2");
const text = "Donate Blood, Save Lives ❤️";
let index = 0;

function typeEffect() {
  if (index < text.length) {
    heroText.innerHTML = text.slice(0, index + 1);
    index++;
    setTimeout(typeEffect, 100);
  }
}
typeEffect();
