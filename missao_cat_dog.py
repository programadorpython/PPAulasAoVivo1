'''
ask the user for a sentence about a pet and then reply
	• get user input in variable: about_pet
	• using a series of if statements respond with appropriate conversation
		○ check if "dog" is in the string about_pet (sample reply "Ah, a dog")
		○ check if "cat" is in the string about_pet
		○ check if 1 or more animal is in string about_pet
	• no need for else's
	• finish with thanking for the story

# [ ] complete pet conversation

about_pet = input("Digite uma frase sobre animais.")
'''

about_pet = input("Insira o pet: ")

if 'dog' in about_pet and 'cat' in about_pet:
    print("Tem Cachorro ou Gato")
elif 'dog' in about_pet:
    print("Tem Cachorro")
elif 'cat' in about_pet:
    print("Tem Gato")


print()
print("Obrigado pela participação!")


