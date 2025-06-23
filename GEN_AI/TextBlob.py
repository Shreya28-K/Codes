from textblob import TextBlob

text="I lve machin larnig and prgraming ."
blob=TextBlob(text)
corrected=blob.correct()
print("aoriginal Text = ",text)
print("\n Corrected Text = ",corrected)