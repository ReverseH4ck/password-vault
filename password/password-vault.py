from classes import PasswordVault, Password
import getpass
import os
import json


vault = PasswordVault()
vault.load_json()

print("""
      1. Ajouter un mot de passe.
      2. Modifier un mot de passe.
      3. Supprimer un mot de passe.
""")


while True:
  try:
    choice = input("Votre choix : ")
    choice = int(choice)
    if choice in [1, 2, 3]:
      break
    else:
      print("Invalid choice, enter 1, 2 or 3.")
  except KeyboardInterrupt:
    print("\nInterrupted")
    exit()
  except ValueError:
    print("Invalid choice, enter 1, 2 or 3.")


if choice == 1:
  service = input("Service : ")
  username = input("Username : ")
  email = input("Email : ")
  password = getpass.getpass("Password : ")
  vault.add_password(service, username, email, password)


vault.save_json()