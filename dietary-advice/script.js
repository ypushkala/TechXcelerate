const apiKey = '01216fa67f75018c87dfce8bfbec128f';  // Replace with your actual Nutritionix API key
const apiUrl = 'https://api.nutritionix.com/v1_1/search/'; // Endpoint for searching recipes

// Function to fetch recipes based on the user's search query
async function fetchRecipes() {
    const query = document.getElementById('recipe-search').value.trim();
    if (!query) {
        alert("Please enter a search term");
        return;
    }

    try {
        const response = await fetch(`${apiUrl}${encodeURIComponent(query)}?results=0:5&fields=item_name,brand_name,nf_calories,nf_sugars,food_type&appId=39edf576&appKey=${apiKey}`);
        const data = await response.json();
        
        if (data.hits && data.hits.length > 0) {
            displayRecipes(data.hits);
        } else {
            document.getElementById('recipe-results').innerHTML = 'No recipes found.';
        }
    } catch (error) {
        console.error('Error fetching data:', error);
        document.getElementById('recipe-results').innerHTML = 'An error occurred. Please try again.';
    }
}

// Function to display the fetched recipes
function displayRecipes(recipes) {
    const resultsContainer = document.getElementById('recipe-results');
    resultsContainer.innerHTML = ''; // Clear previous results

    recipes.forEach(recipe => {
        const recipeCard = document.createElement('div');
        recipeCard.classList.add('recipe-card');

        const image = document.createElement('img');
        image.src = 'https://via.placeholder.com/250'; // You can replace this with actual image URL if available

        const title = document.createElement('h3');
        title.textContent = recipe.fields.item_name;

        const brand = document.createElement('p');
        brand.textContent = `Brand: ${recipe.fields.brand_name || 'N/A'}`;

        const calories = document.createElement('p');
        calories.textContent = `Calories: ${recipe.fields.nf_calories || 'N/A'} kcal`;

        const sugars = document.createElement('p');
        sugars.textContent = `Sugars: ${recipe.fields.nf_sugars || 'N/A'} g`;

        recipeCard.appendChild(image);
        recipeCard.appendChild(title);
        recipeCard.appendChild(brand);
        recipeCard.appendChild(calories);
        recipeCard.appendChild(sugars);

        resultsContainer.appendChild(recipeCard);
    });
}
