const hamburger = document.getElementById('hamburger');
const navUL = document.getElementById('nav-ul');

hamburger.addEventListener('click', () => {
  navUL.classList.toggle('show');
})

const profileForm = document.getElementById('profile-form');
const profileFormToggle = document.getElementById('profile-form-toggle');

profileFormToggle.addEventListener('click', () => {
  profileForm.classList.toggle('show');
})
