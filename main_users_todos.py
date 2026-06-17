import json
from pprint import pprint
from collections import Counter

def main():
    todos_file = "todos.json"
    users_file = "users.json"

    with open(users_file) as f:
        # chargement du json en une liste de dictionnaire
        users = json.load(f)


    with open(todos_file) as f:
        # chargement du json en une liste de dictionnaire
        todos = json.load(f)
        
    # Affichage du premier dictionnaire de la liste
    print(todos[0])

    # Affichage du title du premier dictionnaire de la liste ?
    print(todos[0]['title'])
    cpt = 0


    # pour chaque dictionnaire
    for todo in todos:
        # on affiche le title
        print(todo['title'],todo['completed'])
        if todo['completed']:
            cpt+=1 # cpt = cpt+1
    
    print(f"Il y a {cpt} todo(s)")
    
    completed_todos = len([t for t in todos if t['completed']])
    print(f"Il y a {completed_todos} todo(s)")

    # completed_todos = sum([t['completed'] for t in todos])
    # print(f"Il y a {completed_todos} todo(s)")
    completed_todos = Counter([t['completed'] for t in todos])
    print(completed_todos)
    
    print(50*'-')

    for user in users:
        user_id = user['id']
        user_todos = [t for t in todos if t['userId']==user_id]
        print(user['name'])
        for t in user_todos:
            print(f"\t{t['title']}, {t['completed']}")
        print()

if __name__=='__main__':
    main()
