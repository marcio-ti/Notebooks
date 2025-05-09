import random
import json

class Flashcard:
	def __init__(self, question, answer):
		self.question = question
		self.answer = answer

	def __repr__(self):
		return f"Flashcard(Question: {self.question}, Answer: {self.answer})"

class FlashcardApp:
	def __init__(self, filename="flashcards.json"):
		self.flashcards = []
		self.filename = filename
		self.load_flashcards()

	def load_flashcards(self):
		try:
			with open(self.filename, "r") as file:
				data = json.load(file)
				self.flashcards = [Flashcard(**item) for item in data]
		except FileNotFoundError:
			self.flashcards = []

	def save_flashcards(self):
		with open(self.filename, "w") as file:
			json.dump([fc.__dict__ for fc in self.flashcards], file, indent=4)

	def add_flashcard(self):
		question = input("Digite a pergunta: ")
		answer = input("Digite a resposta: ")
		self.flashcards.append(Flashcard(question, answer))
		self.save_flashcards()
		print("Flashcard adicionado com sucesso!")

	def view_flashcards(self):
		if not self.flashcards:
			print("Nenhum flashcard disponível.")
			return

		for index, flashcard in enumerate(self.flashcards, start=1):
			print(f"{index}. Pergunta: {flashcard.question} | Resposta: {flashcard.answer}")

	def review_flashcards(self):
		if not self.flashcards:
			print("Nenhum flashcard disponível para revisão.")
			return

		random.shuffle(self.flashcards)
		for flashcard in self.flashcards:
			print(f"Pergunta: {flashcard.question}")
			input("Pressione Enter para ver a resposta...")
			print(f"Resposta: {flashcard.answer}\n")

	def menu(self):
		while True:
			print("\nMenu de Flashcards:")
			print("1. Adicionar flashcard")
			print("2. Ver flashcards")
			print("3. Revisar flashcards")
			print("4. Sair")

			choice = input("Escolha uma opção: ")

			if choice == "1":
				self.add_flashcard()
			elif choice == "2":
				self.view_flashcards()
			elif choice == "3":
				self.review_flashcards()
			elif choice == "4":
				print("Saindo do programa. Até logo!")
				break
			else:
				print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
	app = FlashcardApp()
	app.menu()
