// Adding JavaScript code to create a search bar that filters recipes by name
function search_recipe() {
  let input = document.getElementById("searchbar").value;
  input = input.toLowerCase();
  let recipes = document.getElementsByClassName("recipe_searched");

  let recipe_box = document.getElementsByClassName("search_results");
  recipe_box[0].style.display = "block";

  for (i = 0; i < recipes.length; i++) {
    if (!recipes[i].innerHTML.toLowerCase().includes(input)) {
      // Hide recipe name if it does not match the search
      recipes[i].style.display = "none";
    } else {
      recipes[i].style.display = "block"; // Show recipe if matches search
    }
  }
  if (input == "") {
    recipe_box[0].style.display = "none"; // If the search input is empty, hide the search results box
  }
}
