//First number is size in mB
const MAX_FILE_SIZE = 200 * 1024 * 1024;

window.onload = function () {
  const uploadForm = document.getElementById("send-file-form");
  uploadForm.addEventListener("submit", (event) => {
    var input = document.getElementById("uploadedFile");
    if (!input.files[0]) {
      alert("Please select a file");
      event.preventDefault();
    } else if (input.files[0].size > MAX_FILE_SIZE) {
      alert("File is to big");
      event.preventDefault();
    } else {
      alert("Have fun");
    }
  });
};
