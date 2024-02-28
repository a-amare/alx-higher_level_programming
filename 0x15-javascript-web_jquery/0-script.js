// header variable for changing the color of the element header
const header = document.querySelector('header');

if (header) {
  header.style.color = '#FF0000';
}
else {
  console.error('header element not found.')
}
