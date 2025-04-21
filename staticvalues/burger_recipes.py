from ingredients import *

# List of burger recipes with ingredients

BURGER_RECIPES = [
    [
        "Cheeseburger", 
        [
            burger_buns_bottom,
            patty,
            cheese,
            burger_buns_top
        ]
    ],
    [
        "Bacon Cheeseburger",
        [
            burger_buns_bottom,
            patty,
            cheese,
            bacon,
            burger_buns_top
        ]
    ],
    [
        "Double Cheeseburger",
        [
            burger_buns_bottom,
            patty,
            cheese,
            patty,
            cheese,
            burger_buns_top
        ]
    ],
    [
        "Veggie Burger",
        [
            burger_buns_bottom,
            lettuce,
            tomato,
            onion,
            pickle,
            mayonnaise,
            burger_buns_top
        ]
    ],
    [
        "Beese Churger",
        [
            cheese,
            patty,
            cheese
        ]
    ]
]

owned_recipes = []

# Temporary duplicated the list for testing purposes
# Players must get the recipes via other means
owned_recipes = BURGER_RECIPES