# Importação dos módulos necessários
from tkinter import *  # Importa todas as classes e funções do módulo tkinter (interface gráfica)
import random  # Importa o módulo random para gerar posições aleatórias para a comida

# Constantes do jogo
GAME_WIDTH = 700           # Largura da área de jogo (canvas)
GAME_HEIGHT = 700          # Altura da área de jogo (canvas)
SPEED = 50                 # Intervalo entre os frames do jogo (em milissegundos)
SPACE_SIZE = 50            # Tamanho de cada "bloco" da cobra e da comida
BODY_PARTS = 3             # Número inicial de partes do corpo da cobra
SNAKE_COLOR = '#00FF00'    # Cor da cobra (verde)
FOOD_COLOR = '#FF0000'     # Cor da comida (vermelha)
BACKGROUND_COLOR = '#000000'  # Cor de fundo do canvas (preto)

# Classe que representará a cobra
class Snake:
    pass  # A implementação será feita nas próximas etapas

# Classe que representará a comida
class Food:
    pass  # A implementação será feita nas próximas etapas

# Função que será chamada a cada "turno" do jogo (movimento da cobra, atualização da tela, etc.)
def next_turn():
    pass  # Lógica será implementada posteriormente

# Função que altera a direção da cobra de acordo com o input do usuário
def change_direction(new_direction):
    pass  # Lógica será implementada posteriormente

# Função para verificar se houve colisão (com a parede ou consigo mesma)
def check_collision():
    pass  # Lógica será implementada posteriormente

# Função que finaliza o jogo
def game_over():
    pass  # Lógica será implementada posteriormente

# Criação da janela principal do jogo
window = Tk()
window.title('Snake game')         # Define o título da janela
window.resizable(False, False)     # Impede que a janela seja redimensionada

# Inicialização da pontuação e da direção inicial da cobra
score = 0
direction = 'down'

# Rótulo (label) que exibe a pontuação
label = Label(window, text=f'Score:{score}', font=('consolas', 40))
label.pack()  # Adiciona o rótulo à janela

# Canvas (área gráfica) onde o jogo será desenhado
canvas = Canvas(window, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()  # Adiciona o canvas à janela

window.update()  # Atualiza a janela para que possamos pegar os tamanhos corretos dela

# Centraliza a janela na tela do usuário
window_width = window.winfo_width()             # Largura da janela
window_height = window.winfo_height()           # Altura da janela
screen_width = window.winfo_screenwidth()       # Largura da tela do monitor
screen_height = window.winfo_screenheight()     # Altura da tela do monitor

x = int((screen_width / 2) - (window_width / 2))   # Posição horizontal centralizada
y = int((screen_height / 2) - (window_height / 2)) # Posição vertical centralizada

# Define a geometria da janela e a posiciona centralizada na tela
window.geometry(f'{window_width}x{window_height}+{x}+{y}')

# Inicia o loop principal da interface gráfica
window.mainloop()


