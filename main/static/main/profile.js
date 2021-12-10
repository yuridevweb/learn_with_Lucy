const profileForm = document.getElementById('profile-form');
const profileFormToggle = document.getElementById('profile-form-toggle');

profileFormToggle.addEventListener('click', () => {
  profileForm.classList.toggle('show');
})