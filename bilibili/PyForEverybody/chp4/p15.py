x = 5
print('Hello')

def print_lyrics():
  print("I'm a lumberjack, and I'm okay")
  print('I sleep all night and I work all day')

print('Yo')
print_lyrics()
x = x + 2
print(x)

# params
def greet(lang):
  if lang == 'es':
    print('Hola')
    return 'Hola'
  elif lang == 'fr':
    print('Bonjour')
    return 'Bonjour'
  else:
    print('Hello')
    return 'Hello'

print(greet('en'), 'what is this?')
print(greet('es'), 'english')
print(greet('fr'), 'france')