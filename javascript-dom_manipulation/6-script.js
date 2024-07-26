document.addEventListener("DOMContentLoaded", () => {
  const url = "https://swapi-api.hbtn.io/api/people/5/?format=json";
  fetch(url)
    .then(response => response.json())
    .then(data => {
      const characterElement = document.getElementById("character");
      characterElement.textContent = data.name;
    })
    .catch(error => console.error("Error fetching data:", error));
});
