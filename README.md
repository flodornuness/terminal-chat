# A terminal chat for beginners in python language ![image]({(https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue))

“terminal-chat” is a simple chat application built in Python that can be executed directly in the terminal. Its purpose is to help beginners create their first simple project and become familiar with the Python programming language.

# Prerequisites
You must have Python 3.14.3 installed, which already includes the built-in `os` library (the library used in this project).

Once these requirements are met, you should be able to run the command normally in your IDE.
# Code usage
```
import os
```
This line imports the built-in os module, which allows the program to interact with the operating system. In this project, it is used to clear the terminal screen.
```
mensagens = []
```
This creates an empty list called mensagens.
The list is used to store all chat messages during program execution.

Each message will be saved as a dictionary containing:

The user’s name

The message text
```
nome = input("Nome: ")
```
This line prompts the user to enter their name.
The value entered is stored in the variable nome, which will be associated with every message sent.
```
while True:
```
This creates an infinite loop.
The program will continue running until a break statement is executed.
```
os.system("cls" if os.name == "nt" else "clear")
```
This line clears the terminal screen.

"cls" is used on Windows systems.

"clear" is used on Unix-based systems (Linux and macOS).

os.name checks the operating system.

"nt" refers to Windows.

This ensures cross-platform compatibility.
```
if len(mensagens) > 0:
```
This condition checks whether there are any messages stored in the list.

If the list is not empty, the program displays all previous messages.
```
for m in mensagens:
```
This loop goes through each message stored in the mensagens list.

Each message (m) is a dictionary containing:
```
m["nome"]

m["texto"]
````
````
print(f"{m['nome']} - {m['texto']}")
````
This prints each message in a formatted string, showing:

UserName - MessageText
```
print("________________")
```
This prints a separator line to visually organize the chat history in the terminal.
```
texto = input("Mensagem (ou 'fim' para sair): ")
```
This prompts the user to enter a new message.

The user can also type "fim" to exit the program.
```
if texto.lower() == "fim":
```
This checks whether the user typed "fim" (case-insensitive).
The .lower() method ensures that variations like "FIM" or "Fim" will also work.
```
break
```
If the user types "fim", the loop is terminated and the program ends.
```
mensagens.append({ "nome": nome, "texto": texto })
```
If the user did not type "fim", the program adds the new message to the mensagens list.
Each message is stored as a dictionary with:

"nome" → the user's name
"texto" → the message content

This allows the chat history to be preserved during execution.


