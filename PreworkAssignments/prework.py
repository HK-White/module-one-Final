people_info = {
    'Lil Karen': {
        'Favorite Holiday': 'Christmas',
        'Favorite Food': 'Blue Baby Bottle Pops and Hubbabuba',
        'Favorite Hobby': 'Cracking skulls in the playground fight pit',
    },
    'Karen': {
        'Favorite Holiday': 'WTH, What in gods basin of hell lovers you talking bout boy!',
        'Favorite Food': 'Any, and all Fast Food. However, her loyalties lie with KFC',
        'Favorite Hobby': 'Yelling at service employees, profesisonal scene starter'
    },
    'Barbara': {
        'Favorite Holiday': '''Flag Day, and the Day of Mourning for Barbaras 
         and Karens that have had their privelege checked''',
        'Favorite Food': 'Low Sodium Chicken Noodle Soup, 4 cans 3 times a day',
        'Favorite Hobby': 'Hating Everything, and spreading it for generations to come'
    }
}

def people_info_readable_print(info): 
    for person, details in info.items(): 
        print()
        print(f"{person}:") 
        for key, value in details.items(): 
            print(f" {key}: {value}") 
            print() # Add a blank line for readability # Call the function to print the dictionary in a readable manner 
            
people_info_readable_print(people_info)

