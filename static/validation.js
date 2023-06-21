  function redirectToPage(page) {
    window.location.href = page;
  }

  function register() {
    var email = document.forms.Reg.email.value;
    var password = document.forms.Reg.password.value;
    var confirmPassword = document.forms.Reg.confirmPassword.value;
  
    if (email === '') {
      window.alert('Please enter your email properly.');
      document.forms.Reg.email.focus();
      return false;
    }
  
    if (password === '') {
      alert('Please enter your password');
      document.forms.Reg.password.focus();
      return false;
    }
  
    if (password.length < 8) {
      alert('Password should be at least 8 characters long');
      document.forms.Reg.password.focus();
      return false;
    }
  
    if (confirmPassword === '') {
      alert('Please confirm your password');
      document.forms.Reg.confirmPassword.focus();
      return false;
    }
  
    if (password !== confirmPassword) {
      alert('Password and Confirm Password must be the same');
      document.forms.Reg.confirmPassword.focus();
      return false;
    }
  
    alert('An OTP is sent to your mobile number. Please verify.');
    return true;
  }
  
  function login() {
    var email = document.forms.log.email.value;
    var password = document.forms.log.password.value;
  
    if (email === '') {
      window.alert('Please enter correct email');
      document.forms.log.email.focus();
      return false;
    }
    if (!validateEmail(email)) {
      window.alert("Invalid email format");
      document.forms.log.email.focus();
      return false;
    }
  
    if (password === '') {
      alert('Please enter correct password');
      document.forms.log.password.focus();
      return false;
    }
  
    return true;
  }
  function validateEmail(email) {
    var emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailPattern.test(email);
  }
  var draggable = document.querySelector('.drag-drop-parent');
  var droppable = document.getElementById('droppable');
  
  draggable.addEventListener('dragstart', function(event) {
    console.log('Drag start');
    event.dataTransfer.setData('text/plain', event.target.id);
  });
  
  droppable.addEventListener('dragover', function(event) {
    event.preventDefault();
    console.log('Drag over');
  });
  
  droppable.addEventListener('drop', function(event) {
    event.preventDefault();
    console.log('Drop');
    var draggableId = event.dataTransfer.getData('text/plain');
    var draggableElement = document.getElementById(draggableId);
    droppable.appendChild(draggableElement);
  });
  
 
  function previewImage(event){
    const reader = new FileReader();
  
    // Define a callback function to be executed when the FileReader has finished reading the file
    reader.onload = function (event) {
      // Get the URL of the uploaded image
    const imageUrl = event.target.result;
      
      // Create an img element and set its src attribute to the uploaded image URL
    const uploadedImage = document.createElement('img');
    uploadedImage.src = imageUrl;
  
    // Append the uploaded image element to a container on the page
    const imageContainer = document.querySelector('#imagePreview');
    imageContainer.innerHTML = ''; // Clear previous uploaded images
    imageContainer.appendChild(uploadedImage);
    }
  }
  function submitForm() {
    removeTable();
}