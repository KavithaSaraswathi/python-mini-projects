import random
import game_art
import game_database

print(game_art.logo)

account1=random.choice(game_database.instagram_data)
account2=random.choice(game_database.instagram_data)

def display(account):

    name=account["name"]
    des=account["description"]
    country=account["country"]

    return (f"{name}, a {des} from {country}")

print("Compare 1:",display(account1))
print(game_art.vs)
print("Compare 1:",display(account2))
