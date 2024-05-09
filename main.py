palavra = "python"
letras_usuarios = []
chances = 5
ganhou = False

while True:
  for letras in palavra:
    if letras.lower() in letras_usuarios:
      print (letras, end=" ")
    else:
      print ("_", end=" ")

  print(f"Você tem {chances} chances")

  tentativa = input("chute uma letra: ")
  letras_usuarios.append(tentativa.lower())

  if tentativa.lower() not in palavra.lower():
    chances -= 1

  ganhou == True

  for letras in palavra:
    if letras.lower() not in letras_usuarios:
      ganhou == True

  if tentativa == 0 or ganhou:
    break 