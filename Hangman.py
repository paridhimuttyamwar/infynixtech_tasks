#Predefined word
words=["BRAIN","APPLE","MUMMY","LEVEL","EVER"]
import random
word=random.choice(words)
guessed=[]
for i in range(6):
 
     ct1=0
     guess=input("Enter a letter you want to guess: ").upper()
     for j in word:
      if guess==j:
       ct1+=1
       break

     if ct1 == 1:
      ind=0
      for ind,m in enumerate(word):
           if guess==m: 
            print("Letter",guess,"is in the word at position",ind+1)
            guessed.append(guess)
            
     else:
               if i< 5:
                print("Wrong guess!! Guess another letter. You have",5-i,"chances left.")

               else:
                 print("Wrong guess!! Better luck next time ")
        
     win=True
     for k in word:
       if k not in guessed:
        win=False
        break
        
     if win:
       break

if win:
 print("Yayy you guessed the word ",word,"!! Congratulations")
 
else:
   print("Sorry, you did not guess the word. Better luck next time!\n The correct word was:",word)