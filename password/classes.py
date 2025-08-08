class Password:
  def __init__(self, service, username, email, password_chiffre):
    self.service = service
    self.username = username
    self.email = email
    self.password_chiffre = password_chiffre
  
  def to_dict(self):
    return {
      "service": self.service,
      "username": self.username,
      "email": self.email,
      "password": self.password_chiffre
    }

  @staticmethod
  def from_dict(data):
    return Password(
      service=data["service"],
      username=data["username"],
      email=data["email"],
      password_chiffre=data["password_chiffre"]
    )


class PasswordVault:
  def __init__(self):
    self.passwords = []

  def add_password(self, service, username, email, password_chiffre):
    password = Password(service, username, email, password_chiffre)
    self.passwords.append(password)
    print(f"[+] Mot de passe ajouter pour {service}.")

  def remove_password(self):
    pass

  def search_password(self, service):
    for password in self.passwords:
      if password.service.lower() == service.lower():
        return password
      print(f"[-] Aucun mot de passe trouver pour {service}.")

  def save_json(self):
    pass

  def load_json(self):
    pass