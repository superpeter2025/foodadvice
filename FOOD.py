import streamlit as st

# A dictionary of food recommendations and their descriptions.
food_recommendations = {
    "Whole Foods - Vegetables": (
        "Vegetables like leafy greens, broccoli, cauliflower, and other colorful veggies "
        "are nutrient-dense and essential for overall health. They provide vitamins, "
        "minerals, fiber, and antioxidants, supporting digestion, reducing inflammation, "
        "and protecting against chronic diseases. Including a variety of vegetables in "
        "your diet ensures a wide range of health benefits."
    ),
    "Whole Foods - Fruits": (
        "Low-glycemic fruits like berries, apples, and citrus are excellent sources of "
        "fiber, vitamins, and antioxidants. These fruits help regulate blood sugar levels, "
        "support immune function, and provide natural sweetness without causing glucose spikes. "
        "Moderation is key to enjoying their health benefits."
    ),
    "Healthy Proteins": (
        "Lean meats like chicken, turkey, and fish (e.g., salmon, sardines) provide high-quality "
        "protein for muscle repair and overall health. Plant-based options like tofu, tempeh, "
        "and edamame are rich in protein and beneficial nutrients. Eggs are also an affordable "
        "and versatile source of complete protein."
    ),
    "Healthy Fats": (
        "Nuts, seeds, avocados, and olive oil are sources of healthy fats that support heart health, "
        "brain function, and inflammation reduction. These fats are energy-dense, so consume them "
        "in moderation to balance calorie intake and reap their health benefits."
    ),
    "Whole Grains and Legumes": (
        "Whole grains like quinoa, brown rice, and oats, along with legumes such as lentils, chickpeas, "
        "and black beans, provide complex carbohydrates, fiber, and essential nutrients. These foods "
        "support sustained energy, healthy digestion, and blood sugar regulation."
    ),
    "Hydration": (
        "Water is essential for life and maintaining bodily functions. Herbal teas and unsweetened drinks "
        "are great alternatives to sugary beverages. Staying hydrated supports metabolism, skin health, "
        "and overall well-being."
    ),
    "AVOID! - Sugary Foods": (
        "Avoid sugary drinks, candy, desserts, and baked goods made with refined sugar. These can cause "
        "blood sugar spikes, contribute to insulin resistance, and increase the risk of chronic diseases "
        "like diabetes and heart disease."
    ),
    "AVOID! - Refined Carbohydrates": (
        "Refined carbohydrates like white bread, pasta, and processed snacks lack fiber and nutrients. "
        "They can lead to rapid blood sugar spikes and crashes, contributing to poor energy levels and weight gain."
    ),
    "AVOID! - Highly Processed Foods": (
        "Packaged meals, fast food, and processed meats contain unhealthy additives, high sodium, and "
        "low nutritional value. Avoid these foods to reduce inflammation and support long-term health."
    ),
    "AVOID! - Unhealthy Fats and Alcohol": (
        "Trans fats found in fried foods and processed snacks are harmful to heart health. Limit alcohol "
        "consumption to prevent glucose spikes and reduce liver strain. Focus on nutrient-dense food choices instead."
    ),
}

# Sidebar: let the user pick one of the food recommendations
selected_recommendation = st.sidebar.radio("Select a food recommendation:", list(food_recommendations.keys()))

# Main area: show the selected recommendation’s title and description
st.title(selected_recommendation)
st.write(food_recommendations[selected_recommendation])
