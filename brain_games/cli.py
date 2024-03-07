import prompt
def welcome_user():
	name = prompt.string('May I have Your name? ')
	print(f'Hello, {name}!')
def main():
	welcome_user()
	
