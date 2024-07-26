document.addEventListener("DOMContentLoaded", () => {
  const url = "https://swapi-api.hbtn.io/api/films/?format=json";
  
  fetch(url)
    .then(response => response.json())
    .then(data => {
      const movies = data.results;
      const listMoviesElement = document.getElementById("list_movies");
      
      movies.forEach(movie => {
        const listItem = document.createElement("li");
        listItem.textContent = movie.title;
        listMoviesElement.appendChild(listItem);
      });
    })
    .catch(error => console.error("Error fetching data:", error));
});
