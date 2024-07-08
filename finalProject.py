import requests

class RecipeRecommender:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = 'https://api.spoonacular.com/recipes/complexSearch'
    
    def recommend_recipes(self, diet, ingredients):
        params = {
            'apiKey': self.api_key,
            'diet': diet,
            'includeIngredients': ','.join(ingredients),
            'number': 5  # Number of recipes to retrieve
        }
        
        try:
            response = requests.get(self.base_url, params=params)
            response.raise_for_status()
            data = response.json()
            
            if 'results' in data:
                return data['results']
            else:
                print("No recipes found.")
                return []
        
        except requests.exceptions.RequestException as e:
            print(f"Error fetching data: {e}")
            return []
        
# Example usage:
if __name__ == "__main__":
    # Replace 'YOUR_API_KEY' with your actual Spoonacular API key
    api_key = 'a188e979ffd445c3ac10cc2ced66c36b'
    recommender = RecipeRecommender(api_key)
    
    # Example user preferences
    diet = input("Enter your dietary preference (Choose any of the following: 'No Diet , 'Lacto Vegetarian , 'Paleo' , 'Primal' , 'Pescetarian' , 'Vegan' , 'Vegetarian' , 'Ketogenic' , 'Whole 30'): ").lower()  # Can be 'vegetarian', 'vegan', 'gluten free', etc.
    
    # Ask user for ingredients (comma-separated list)
    ingredients_input = input("Enter available ingredients (comma-separated): ")
    ingredients = [ingredient.strip() for ingredient in ingredients_input.split(',')]
    
    # Get recommended recipes based on preferences
    recommended_recipes = recommender.recommend_recipes(diet, ingredients)
    
    # Display recommended recipes
    if recommended_recipes:
        print(f"Recommended Recipes based on '{diet}' diet and available ingredients:")
        for recipe in recommended_recipes:
            print(f"- {recipe['title']} (ID: {recipe['id']})")
    else:
         print("No recipes found based on the given preferences.")
