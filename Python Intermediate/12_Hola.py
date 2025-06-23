def translator(language):
  translations = {
  'spanish': {'hello': 'hola', 'goodbye': 'adiós', 'thank you': 'gracias'},
  'french': {'hello': 'bonjour', 'goodbye': 'au revoir', 'thank you': 'merci'},
  'italian': {'hello': 'ciao', 'goodbye': 'arrivederci', 'thank you': 'grazie'}
     }
  def translate_word(word):
    for i in translations[language].keys():
      if i==word:
        return tanslations[language][word]
      else:
        print("Word  not exist..")
  
  return translate_word

translate_to_spanish = translator('spanish') # translate+word()  is returned
print(translate_to_spanish('hello')) 

