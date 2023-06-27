import tkinter as tk
from tkinter import *
from tkinter import messagebox
import random
import pygame  # importar pygame para adicionar som de fundo
import playsound  # importar playsound para tocar os sons de efeito
import time

proporcao = ["640x360", "1280x720"]

window = tk.Tk()
window.title("Escritamatica")
window.geometry(proporcao[0])
window.resizable(0, 0)

background = PhotoImage(file="testesla.png")
background_label = Label(window, image=background)
background_label.place(relx=0.5, rely=0.5, anchor=CENTER)


def play_background_music():
    pygame.mixer.init()
    pygame.mixer.music.load("background.mp3")
    pygame.mixer.music.play(-1)


pygame.init()
play_background_music()

# -----MENU-----
jogar = tk.Button(window, text="JOGAR", width=9, height=1, bg="purple", fg="white", font=("Arial", 20, "bold"),
                  command=lambda: menu())
jogar.pack()
jogar.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
menu_sound = pygame.mixer.Sound("menu.mp3")
start_button = tk.Button(window, text="Iniciar Jogo", width=9, height=1, bg="green", fg="white",
                         font=("Arial", 16, "bold"), command=lambda: [play_sound_button(), start_game()])

mjogo = PhotoImage(file="escritamatica.png")
mjogo_label = Label(window, image=mjogo, bg="black")
start_button = tk.Button(window, text="Iniciar Jogo", width=10, height=1, bg="green", fg="white",
                         font=("Arial", 16, "bold"), command=lambda: [play_sound_button(), start_game()])
options_button = tk.Button(window, text="Opções", width=10, height=1, bg="blue", fg="white", font=("Arial", 16, "bold"),
                           command=lambda: [play_sound_button(), show_options()])
exit_button = tk.Button(window, text="Sair do Jogo", width=10, height=1, bg="red", fg="white",
                        font=("Arial", 16, "bold"), command=lambda: [play_sound_button(), window.destroy()])

# -----CONFIGURAÇÕES-----
tam = tk.StringVar()
tam.set(proporcao[0])

tamanho1 = tk.Button(window, text="640 x 360", width=9, height=1, bg="blue", fg="white", font=("Arial", 16, "bold"),
                     command=lambda: [window.geometry(proporcao[0]), tam.set(proporcao[0])])
tamanho2 = tk.Button(window, text="1280 x 720", width=9, height=1, bg="blue", fg="white", font=("Arial", 16, "bold"),
                     command=lambda: [window.geometry(proporcao[1]), tam.set(proporcao[1])])
back_button = tk.Button(window, text="Voltar", width=9, height=1, bg="red", fg="white", font=("Arial", 16, "bold"),
                        command=lambda: [menu()])

# -----BOTOES VOLTAR-----
voltar1 = tk.Button(window, text="Voltar", width=6, height=1, bg="red", fg="white", font=("Arial", 12, "bold"),
                    command=lambda: [play_sound_button(), menu()])
voltar2 = tk.Button(window, text="Voltar", width=6, height=1, bg="red", fg="white", font=("Arial", 12, "bold"),
                    command=lambda: [start_game()])
voltar3 = tk.Button(window, text="Voltar", width=6, height=1, bg="red", fg="white", font=("Arial", 12, "bold"),
                    command=lambda: [play_sound_button(), palavras_option()])
voltar4 = tk.Button(window, text="Voltar", width=6, height=1, bg="red", fg="white", font=("Arial", 12, "bold"),
                    command=lambda: [play_sound_button(), numeros_option()])

# ----JOGO-----
tipo = tk.Label(window, text="Escolha um modo:", bg="black", fg="#ffce00", font=("Courier", 20, "bold"))
palavras_button = tk.Button(window, text="Palavras", width=9, height=1, bg="blue", fg="white",
                            font=("Arial", 16, "bold"), command=lambda: [palavras_option()])
numeros_button = tk.Button(window, text="Números", width=9, height=1, bg="blue", fg="white", font=("Arial", 16, "bold"),
                           command=lambda: [numeros_option()])

# -----FASES PALAVRAS-----
fasesp = tk.Label(window, text="Escolha uma fase:", bg="black", fg="#ffce00", font=("Courier", 20, "bold"))
fasep1_button = tk.Button(window, text="Fase 1", width=9, height=1, bg="green", fg="white", font=("Arial", 16, "bold"),
                          command=lambda: [play_sound_button(), fasep1()])
fasep2_button = tk.Button(window, text="Fase 2", width=9, height=1, bg="green", fg="white", font=("Arial", 16, "bold"),
                          command=lambda: [play_sound_button(), fasep2()])
fasep3_button = tk.Button(window, text="Fase 3", width=9, height=1, bg="green", fg="white", font=("Arial", 16, "bold"),
                          command=lambda: [play_sound_button(), fasep3()])
boxp = tk.Label(window, width=0, height=0, bg="black")

# -----FASEP 1 = FORCA-----
f1palavras = ["python", "tkinter", "forca", "jogo", "palavra", "faculdade"]
f1palavra = random.choice(f1palavras)

pOculta = tk.StringVar()
pOculta.set("-" * len(f1palavra))
palavraEsc = tk.Label(window, textvariable=pOculta, font=("Arial", 20))

tentativas = tk.IntVar()
tentativas.set(6)
label_tentativas = tk.Label(window, textvariable=tentativas, font=("Arial", 16))

letras_usadas = tk.StringVar()
letras_usadas.set("")
label_letras_usadas = tk.Label(window, textvariable=letras_usadas, font=("Arial", 16))

entry_letra = tk.Entry(window)

enviar = tk.Button(window, text="Enviar", command=lambda: checar_letra())

recomecar_forca = tk.Button(window, text="Recomeçar", command=lambda: reiniciar_forca())
recomecar_forca.config(state=tk.DISABLED)

# -----FASEP 2 = ANAGRAMA-----
f2palavras = ["casa", "mesa", "cadeira", "livro", "janela", "frio", "flor", "bola", "roda", "cachorro"]
f2palavra = random.choice(f2palavras)
letras = list(f2palavra)
random.shuffle(letras)
anagrama = "".join(letras)

rotulo_anagrama = tk.Label(window, text=anagrama, font=("Arial", 24))
entrada = tk.Entry(window)
botao_novo = tk.Button(window, text="Novo Anagrama", command=lambda: novo_anagrama())
botao = tk.Button(window, text="Verificar", command=lambda: verificar())
botao_novo.config(state=tk.DISABLED)

# -----FASEP 3 = Adivinhe a palavra-----
words = ["conta", "vento", "festa", "gente", "sinal", "livro","samba", "sonho", "filme", "risco"]
palav = random.choice(words)
tries = 0
win = False
correct = []
acertos = ["_"] * 5
nao_tem = []
possui_up = []

label = tk.Label(window, text="Tente adivinhar a palavra de 5 letras", font=("Arial", 16))
entry = tk.Entry(window, font=("Arial", 16))
button_verificar = tk.Button(window, text="Verificar", font=("Arial", 16), command=lambda: check())
button_restart = tk.Button(window, text="Recomeçar", font=("Arial", 16), command=lambda: restart_p3())
button_restart.config(state=tk.DISABLED)

# -----FASES NUMEROS-----
fasesn = tk.Label(window, text="Escolha uma fase:", bg="black", fg="#ffce00", font=("Courier", 20, "bold"))
fasen1_button = tk.Button(window, text="Fase 1", width=9, height=1, bg="green", fg="white", font=("Arial", 16, "bold"),
                          command=lambda: [play_sound_button(), fasen1()])
fasen2_button = tk.Button(window, text="Fase 2", width=9, height=1, bg="green", fg="white", font=("Arial", 16, "bold"),
                          command=lambda: [play_sound_button(), fasen2()])
fasen3_button = tk.Button(window, text="Fase 3", width=9, height=1, bg="green", fg="white", font=("Arial", 16, "bold"),
                          command=lambda: [play_sound_button(), fasen3()])
boxn = tk.Label(window, width=0, height=0, bg="black")

# -----FASEN 1 = ADIVINHE O NUMERO-----
max_number = 100
secret = random.randint(1, max_number)
attempts = 10

instructions = tk.Label(window, text=f"Eu pensei em um número entre 1 e {max_number}. \n Tente adivinhar qual é!",
                        font=("Arial", 20))
guess = tk.Entry(window, font=("Arial", 20))
result = tk.Label(window, text="", font=("Arial", 20))
check_button = tk.Button(window, text="Verificar", font=("Arial", 20), command=lambda: check_guess())
restart_button = tk.Button(window, text="Recomeçar", font=("Arial", 20), command=lambda: restart())
rotulo_resultado = tk.Label(window, text="", font=("Arial", 18))
restart_button["state"] = tk.DISABLED

# -----FASEN 2 = Aritmética-----
question = tk.StringVar()
question.set("")
num1 = 0
num2 = 0
operator = ""

label_question = tk.Label(window, textvariable=question, font=("Arial", 20))
entry_answer = tk.Entry(window)
button_send = tk.Button(window, text="Enviar", command=lambda: check_answer())
resultado = tk.StringVar()
resultado.set("")
label_result = tk.Label(window, textvariable=resultado, font=("Arial", 16))
score = tk.IntVar()
score.set(0)
label_score = tk.Label(window, textvariable=score, font=("Arial", 16))
obs_button1 = tk.Button(window, text="Obs", fg="white", bg="red", command=lambda: obs1())
obs = tk.Label(window, text="Obs.: Na divisão \n"
                            "Se o resultado for um valor inteiro, adicione \n"
                            "apenas 1 casa decimal. Ex: 10/2='5.0' \n"
                            "Mas se o resultado for um numero quebrado com mais de 2 \n"
                            "casas decimais, arredonde para apenas 2. Ex: 5/7='0.71'", fg="red", bg="black",
               font=("Arial", 10))
obs_button2 = tk.Button(window, text="Obs", fg="white", bg="red", command=lambda: obs2())

# -----FASEN 3 = Campo Minado-----
fasen3cm = tk.Frame(window)
size = 10
mines = 10
buttons = []

restart_cm = tk.Button(fasen3cm, text="Recomeçar", font=("Arial", 10), state=tk.DISABLED)

for i in range(size):
    row = []
    for j in range(size):
        button = tk.Button(fasen3cm, text="  ", font=("Arial", 10))
        button.grid(row=i, column=j)
        row.append(button)
    buttons.append(row)

restart_cm.grid(row=size, columnspan=size)

board = []
for i in range(size):
    row = []
    for j in range(size):
        row.append(0)
    board.append(row)


def menu():
    jogar.pack()
    jogar.pack_forget()
    tamanho1.place_forget()
    tamanho2.place_forget()
    back_button.place_forget()
    voltar1.place_forget()
    tipo.place_forget()
    palavras_button.place_forget()
    numeros_button.place_forget()
    mjogo_label.place(relx=0.5, rely=0.3, anchor=tk.CENTER)
    start_button.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    options_button.place(relx=0.5, rely=0.65, anchor=tk.CENTER)
    exit_button.place(relx=0.5, rely=0.8, anchor=tk.CENTER)


def play_sound_button():
    pygame.mixer.init()
    pygame.mixer.music.load("click.mp3")
    pygame.mixer.music.play()
    time.sleep(0.3)
    pygame.mixer.music.load("background.mp3")
    pygame.mixer.music.play(-1)


def start_game():
    start_button.place_forget()
    options_button.place_forget()
    exit_button.place_forget()
    voltar2.place_forget()
    fasesp.place_forget()
    fasep1_button.place_forget()
    fasep2_button.place_forget()
    fasep3_button.place_forget()
    fasesn.place_forget()
    fasen1_button.place_forget()
    fasen2_button.place_forget()
    fasen3_button.place_forget()
    voltar1.place(relx=0.05, rely=0.05)
    mjogo_label.place(relx=0.5, rely=0.35, anchor=tk.CENTER)
    tipo.place(relx=0.5, rely=0.55, anchor=tk.CENTER)
    palavras_button.place(relx=0.35, rely=0.7, anchor=tk.CENTER)
    numeros_button.place(relx=0.65, rely=0.7, anchor=tk.CENTER)


def palavras_option():
    tipo.place_forget()
    palavras_button.place_forget()
    numeros_button.place_forget()
    voltar3.place_forget()
    boxp.place_forget()
    palavraEsc.place_forget()
    label_tentativas.place_forget()
    label_letras_usadas.place_forget()
    entry_letra.place_forget()
    enviar.place_forget()
    voltar1.place_forget()
    rotulo_anagrama.place_forget()
    entrada.place_forget()
    botao.place_forget()
    rotulo_resultado.place_forget()
    botao_novo.place_forget()
    label.place_forget()
    entry.place_forget()
    button_verificar.place_forget()
    recomecar_forca.place_forget()
    button_restart.place_forget()
    mjogo_label.place(relx=0.5, rely=0.35, anchor=tk.CENTER)
    voltar2.place(relx=0.05, rely=0.05)
    fasesp.place(relx=0.5, rely=0.55, anchor=tk.CENTER)
    fasep1_button.place(relx=0.3, rely=0.7, anchor=tk.CENTER)
    fasep2_button.place(relx=0.5, rely=0.7, anchor=tk.CENTER)
    fasep3_button.place(relx=0.7, rely=0.7, anchor=tk.CENTER)


def fasep1():
    mjogo_label.place_forget()
    fasesp.place_forget()
    fasep1_button.place_forget()
    fasep2_button.place_forget()
    fasep3_button.place_forget()
    voltar2.place_forget()
    if tam.get() == "640x360":
        boxp.config(width=32, height=16, bg="black")
    else:
        boxp.config(width=32, height=28, bg="black")
    voltar3.place(relx=0.05, rely=0.05)
    boxp.place(relx=0.5, rely=0.55, anchor=tk.CENTER)
    palavraEsc.place(relx=0.5, rely=0.3, anchor=tk.CENTER)
    label_tentativas.place(relx=0.5, rely=0.4, anchor=tk.CENTER)
    label_letras_usadas.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    entry_letra.place(relx=0.5, rely=0.6, anchor=tk.CENTER)
    enviar.place(relx=0.5, rely=0.7, anchor=tk.CENTER)
    recomecar_forca.place(relx=0.5, rely=0.8, anchor=tk.CENTER)


def checar_letra():
    letra = entry_letra.get()

    entry_letra.delete(0, tk.END)

    if letra in letras_usadas.get():
        flusada = tk.Label(window, text="Você já usou essa letra", font=("Arial", 16))
        flusada.pack()
        window.after(2000, lambda: erase_label(flusada))
        return

    letras_usadas.set(letras_usadas.get() + letra + " ")

    if letra in f1palavra:
        facertou = tk.Label(window, text="Você acertou uma letra", font=("Arial", 16))
        facertou.pack()
        window.after(2000, lambda: erase_label(facertou))

        new_hidden_word = ""
        for i in range(len(f1palavra)):
            if f1palavra[i] == letra:
                new_hidden_word += letra
            else:
                new_hidden_word += pOculta.get()[i]
        pOculta.set(new_hidden_word)

        if pOculta.get() == f1palavra:
            fganhou = tk.Label(window, text="Você ganhou!", font=("Arial", 16))
            fganhou.pack()
            window.after(2000, lambda: erase_label(fganhou))
            entry_letra.config(state=tk.DISABLED)
            enviar.config(state=tk.DISABLED)
            recomecar_forca.config(state=tk.NORMAL)

    else:
        ferrou = tk.Label(window, text="Você errou uma letra", font=("Arial", 16))
        ferrou.pack()
        window.after(2000, lambda: erase_label(ferrou))

        tentativas.set(tentativas.get() - 1)

        if tentativas.get() == 0:
            fperdeu = tk.Label(window, text="Você perdeu!", font=("Arial", 16))
            fperdeu.pack()
            window.after(2000, lambda: erase_label(fperdeu))
            entry_letra.config(state=tk.DISABLED)
            enviar.config(state=tk.DISABLED)
            recomecar_forca.config(state=tk.NORMAL)


def reiniciar_forca():
    global f1palavra
    f1palavra = random.choice(f1palavras)
    pOculta.set("-" * len(f1palavra))
    tentativas.set(6)
    letras_usadas.set("")
    entry_letra.config(state=tk.NORMAL)
    enviar.config(state=tk.NORMAL)
    recomecar_forca.config(state=tk.DISABLED)


def fasep2():
    mjogo_label.place_forget()
    fasesp.place_forget()
    fasep1_button.place_forget()
    fasep2_button.place_forget()
    fasep3_button.place_forget()
    voltar2.place_forget()
    if tam.get() == "640x360":
        boxp.config(width=41, height=17, bg="black")
    else:
        boxp.config(width=41, height=30, bg="black")
    voltar3.place(relx=0.05, rely=0.05)
    boxp.place(relx=0.5, rely=0.55, anchor=tk.CENTER)
    rotulo_anagrama.place(relx=0.5, rely=0.3, anchor=tk.CENTER)
    entrada.place(relx=0.5, rely=0.45, anchor=tk.CENTER)
    botao.place(relx=0.5, rely=0.58, anchor=tk.CENTER)
    rotulo_resultado.place(relx=0.5, rely=0.7, anchor=tk.CENTER)
    botao_novo.place(relx=0.5, rely=0.82, anchor=tk.CENTER)


def novo_anagrama():
    global f2palavra
    entrada.config(state=tk.NORMAL)
    botao.config(state=tk.NORMAL)
    botao_novo.config(state=tk.DISABLED)
    f2palavra = random.choice(f2palavras)
    letras = list(f2palavra)
    random.shuffle(letras)
    anagrama = "".join(letras)
    rotulo_anagrama.config(text=anagrama)
    entrada.delete(0, tk.END)
    rotulo_resultado.config(text="")


def verificar():
    resposta = entrada.get()
    if resposta == f2palavra:
        rotulo_resultado.config(text="Parabéns! Você acertou!", fg="green")
        entrada.config(state=tk.DISABLED)
        botao.config(state=tk.DISABLED)
        botao_novo.config(state=tk.NORMAL)
    else:
        rotulo_resultado.config(text="Errado! Tente novamente.", fg="red")
        entrada.config(state=tk.DISABLED)
        botao.config(state=tk.DISABLED)
        botao_novo.config(state=tk.NORMAL)


def fasep3():
    mjogo_label.place_forget()
    fasesp.place_forget()
    fasep1_button.place_forget()
    fasep2_button.place_forget()
    fasep3_button.place_forget()
    voltar2.place_forget()
    if tam.get() == "640x360":
        boxp.config(width=85, height=19, bg="black")
    else:
        boxp.config(width=85, height=38, bg="black")
    boxp.place(relx=0.5, rely=0.57, anchor=tk.CENTER)
    voltar3.place(relx=0.05, rely=0.05)
    label.place(relx=0.5, rely=0.35, anchor=tk.CENTER)
    entry.place(relx=0.5, rely=0.6, anchor=tk.CENTER)
    button_verificar.place(relx=0.5, rely=0.75, anchor=tk.CENTER)
    button_restart.place(relx=0.5, rely=0.9, anchor=tk.CENTER)


def restart_p3():
    global palav, tries, win, correct, acertos, nao_tem, possui_up
    palav = random.choice(words)
    tries = 0
    win = False
    correct = []
    acertos = ["_"] * 5
    nao_tem.clear()
    possui_up.clear()
    label["text"] = "Tente adivinhar a palavra de 5 letras"
    entry.config(state=tk.NORMAL)
    button_verificar.config(state=tk.NORMAL)
    button_restart.config(state=tk.DISABLED)


def check():
    global palav, tries, win, correct, nao_tem, possui_up
    guess = entry.get()
    possui_up.clear()
    entry.delete(0, tk.END)
    tries += 1
    if guess == palav:
        win = True
        label["text"] = f"Parabéns! Você acertou a palavra {palav} em {tries} tentativas!"
        entry.config(state=tk.DISABLED)
        button_verificar.config(state=tk.DISABLED)
        button_restart.config(state=tk.NORMAL)
    else:
        label["text"] = f"Você errou! Tente novamente!\n"
        label["text"] += f"PALAVRA: "
        for i in range(5):
            if guess[i] == palav[i]:
                acertos[i] = guess[i]
        for letra in acertos:
            label["text"] += f"{letra}   "


        for letra in guess:
            if letra not in palav:
                nao_tem.append(letra)
            else:
                possui_up.append(letra)
        nao_tem = list(set(nao_tem))
        possui_up = list(set(possui_up))

        label["text"] += f"\nNão tem: {' '.join(nao_tem)}"
        label["text"] += f"\nUltima Palavra: {' '.join(guess)}"
        label["text"] += f"\nTem da Ultima Palavra: {' '.join(possui_up)}"


def numeros_option():
    tipo.place_forget()
    palavras_button.place_forget()
    numeros_button.place_forget()
    voltar1.place_forget()
    voltar4.place_forget()
    boxn.place_forget()
    instructions.place_forget()
    guess.place_forget()
    result.place_forget()
    check_button.place_forget()
    restart_button.place_forget()
    label_question.place_forget()
    entry_answer.place_forget()
    button_send.place_forget()
    label_result.place_forget()
    label_score.place_forget()
    obs_button1.place_forget()
    obs.place_forget()
    obs_button2.place_forget()
    fasen3cm.place_forget()
    mjogo_label.place(relx=0.5, rely=0.35, anchor=tk.CENTER)
    voltar2.place(relx=0.05, rely=0.05)
    fasesn.place(relx=0.5, rely=0.55, anchor=tk.CENTER)
    fasen1_button.place(relx=0.3, rely=0.7, anchor=tk.CENTER)
    fasen2_button.place(relx=0.5, rely=0.7, anchor=tk.CENTER)
    fasen3_button.place(relx=0.7, rely=0.7, anchor=tk.CENTER)


def fasen1():
    voltar2.place_forget()
    mjogo_label.place_forget()
    fasesn.place_forget()
    fasen1_button.place_forget()
    fasen2_button.place_forget()
    fasen3_button.place_forget()
    if tam.get() == "640x360":
        boxn.config(width=85, height=20, bg="black")
    else:
        boxn.config(width=85, height=36, bg="black")
    boxn.place(relx=0.5, rely=0.572, anchor=tk.CENTER)
    voltar4.place(relx=0.05, rely=0.05)
    instructions.place(relx=0.5, rely=0.3, anchor=tk.CENTER)
    guess.place(relx=0.5, rely=0.46, anchor=tk.CENTER)
    result.place(relx=0.5, rely=0.58, anchor=tk.CENTER)
    check_button.place(relx=0.5, rely=0.73, anchor=tk.CENTER)
    restart_button.place(relx=0.5, rely=0.9, anchor=tk.CENTER)


def check_guess():
    global secret, attempts, guess, result

    value = guess.get()
    try:
        number = int(value)
        if number == secret:
            result["text"] = "Parabéns! Você acertou!"
            result["fg"] = "green"
            guess["state"] = tk.DISABLED
            restart_button["state"] = tk.NORMAL
        else:
            if number < secret:
                result["text"] = "Errou! O número é maior."
                result["fg"] = "red"
            else:
                result["text"] = "Errou! O número é menor."
                result["fg"] = "red"
            attempts -= 1
            if attempts == 0:
                result["text"] = f"Você perdeu! O número era {secret}."
                guess["state"] = tk.DISABLED
                restart_button["state"] = tk.NORMAL
    except ValueError:
        result["text"] = "Digite um número inteiro válido!"
        result["fg"] = "red"
        guess.delete(0, tk.END)


def restart():
    global secret, attempts, guess, result

    secret = random.randint(1, max_number)
    attempts = 10
    guess.delete(0, tk.END)
    guess["state"] = tk.NORMAL
    result["text"] = ""
    restart_button["state"] = tk.DISABLED


def fasen2():
    voltar2.place_forget()
    mjogo_label.place_forget()
    fasesn.place_forget()
    fasen1_button.place_forget()
    fasen2_button.place_forget()
    fasen3_button.place_forget()
    if tam.get() == "640x360":
        boxn.config(width=21, height=16, bg="black")
    else:
        boxn.config(width=28, height=28, bg="black")
    boxn.place(relx=0.5, rely=0.548, anchor=tk.CENTER)
    voltar4.place(relx=0.05, rely=0.05)
    label_question.place(relx=0.5, rely=0.3, anchor=tk.CENTER)
    entry_answer.place(relx=0.5, rely=0.4, anchor=tk.CENTER)
    button_send.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    label_result.place(relx=0.5, rely=0.6, anchor=tk.CENTER)
    label_score.place(relx=0.5, rely=0.7, anchor=tk.CENTER)
    obs_button1.place(relx=0.5, rely=0.8, anchor=tk.CENTER)


def generate_question():
    global num1, num2, operator
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)

    operators = ["+", "-", "x", "/"]
    operator = random.choice(operators)
    question.set(f"{num1} {operator} {num2} = ?")


def check_answer():
    global num1, num2, operator
    answer = entry_answer.get()
    entry_answer.delete(0, tk.END)

    if operator == "+":
        conta = float(num1) + float(num2)
        if conta % 1 == 0:
            correct_answer = int(num1) + int(num2)
        else:
            correct_answer = round(conta, 2)
    elif operator == "-":
        conta = float(num1) - float(num2)
        if conta % 1 == 0:
            correct_answer = int(num1) - int(num2)
        else:
            correct_answer = round(conta, 2)
    elif operator == "x":
        conta = float(num1) * float(num2)
        if conta % 1 == 0:
            correct_answer = int(num1) * int(num2)
        else:
            correct_answer = round(conta, 2)
    elif operator == "/":
        conta = float(num1) / float(num2)
        if conta % 1 == 0:
            correct_answer = float(num1) / float(num2)
        else:
            correct_answer = round(conta, 2)

    if answer == str(correct_answer):
        resultado.set("Certo!")
        score.set(score.get() + 1)
    else:
        resultado.set("Errado!")
        score.set(score.get() - 1)
    generate_question()


generate_question()


def obs1():
    obs.place(relx=0.5, rely=0.12, anchor=tk.CENTER)
    obs_button1.place_forget()
    obs_button2.place(relx=0.5, rely=0.8, anchor=tk.CENTER)


def obs2():
    obs.place_forget()
    obs_button1.place(relx=0.5, rely=0.8, anchor=tk.CENTER)
    obs_button2.place_forget()


def fasen3():
    voltar2.place_forget()
    mjogo_label.place_forget()
    fasesn.place_forget()
    fasen1_button.place_forget()
    fasen2_button.place_forget()
    fasen3_button.place_forget()
    if tam.get() == "640x360":
        boxn.config(width=37, height=22, bg="black")
    else:
        boxn.config(width=37, height=22, bg="black")
    boxn.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    voltar4.place(relx=0.05, rely=0.05)
    fasen3cm.place(relx=0.5, rely=0.5, anchor=tk.CENTER)


def place_mines():
    global board, mines
    count = 0

    while count < mines:
        i = random.randint(0, size - 1)
        j = random.randint(0, size - 1)
        if board[i][j] != -1:
            board[i][j] = -1
            count += 1


def calculate_numbers():
    global board, size

    for i in range(size):
        for j in range(size):
            if board[i][j] != -1:
                count = 0
                for di in range(-1, 2):
                    for dj in range(-1, 2):
                        if di != 0 or dj != 0:
                            ni = i + di
                            nj = j + dj
                            if ni >= 0 and ni < size and nj >= 0 and nj < size:
                                if board[ni][nj] == -1:
                                    count += 1
                board[i][j] = count


place_mines()
calculate_numbers()


def reveal(i, j):
    global board, buttons, size

    button = buttons[i][j]
    number = board[i][j]

    if button["text"] == "  ":
        if number == -1:
            button["text"] = "💣"
            button["fg"] = "red"
            for row in buttons:
                for button in row:
                    button["state"] = tk.DISABLED
            restart_cm["state"] = tk.NORMAL
            tk.messagebox.showinfo("Campo Minado", "Você perdeu!")
        elif number == 0:
            button["text"] = "   "
            button["bg"] = "green"
            for di in range(-1, 2):
                for dj in range(-1, 2):
                    if di != 0 or dj != 0:
                        ni = i + di
                        nj = j + dj
                        if ni >= 0 and ni < size and nj >= 0 and nj < size:
                            reveal(ni, nj)
        else:
            button["text"] = str(number)
            button["fg"] = "blue"
    check_win()


def check_win():
    global buttons, mines
    count = 0
    for row in buttons:
        for button in row:
            if button["text"] == "  ":
                count += 1
    if count == mines:
        for row in buttons:
            for button in row:
                button["state"] = tk.DISABLED
        restart_cm["state"] = tk.NORMAL
        tk.messagebox.showinfo("Campo Minado", "Parabéns, você venceu!")


def restart_n3cm():
    global board, buttons, mines
    for i in range(size):
        for j in range(size):
            board[i][j] = 0
            button = buttons[i][j]
            button["text"] = "  "
            button["fg"] = "black"
            button["bg"] = "white"
            button["state"] = tk.NORMAL
    place_mines()
    calculate_numbers()
    restart_cm["state"] = tk.DISABLED


restart_cm["command"] = restart_n3cm


def command(i, j):
    return lambda: reveal(i, j)


for i in range(size):
    for j in range(size):
        button = buttons[i][j]
        button["command"] = command(i, j)


def show_options():
    start_button.place_forget()
    options_button.place_forget()
    exit_button.place_forget()
    mjogo_label.place(relx=0.5, rely=0.4, anchor=tk.CENTER)
    tamanho1.place(relx=0.4, rely=0.6, anchor=tk.CENTER)
    tamanho2.place(relx=0.6, rely=0.6, anchor=tk.CENTER)
    back_button.place(relx=0.5, rely=0.75, anchor=tk.CENTER)


def erase_label(label):
    label.destroy()

window.mainloop()

