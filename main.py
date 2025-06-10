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
    def __init__(self):
        """
        Inicializa a cobra com um número inicial de segmentos (BODY_PARTS),
        todos começando na posição (0,0). Cada parte do corpo é desenhada
        como um retângulo verde no canvas.
        """
        self.body_size = BODY_PARTS
        self.coordinates = []
        self.squares = []

        for i in range(0, BODY_PARTS):
            self.coordinates.append([0, 0])

        for x, y in self.coordinates:
            square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE,
                                             fill=SNAKE_COLOR,
                                             tags='snake')
            self.squares.append(square)


# Classe que representará a comida do jogo
class Food:
    def __init__(self):
        """
        Inicializa a comida em uma posição aleatória do canvas, alinhada à grade do jogo.
        A comida é representada por um círculo vermelho desenhado no canvas.
        """
        x = random.randint(0, (GAME_WIDTH // SPACE_SIZE) - 1) * SPACE_SIZE
        y = random.randint(0, (GAME_HEIGHT // SPACE_SIZE) - 1) * SPACE_SIZE

        self.coordinates = [x, y]

        canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOR, tags='food')


# Função que será chamada a cada "turno" do jogo
def next_turn(snake, food):
    """
    Atualiza a posição da cobra de acordo com a direção atual.
    Move a cabeça da cobra, desenha o novo segmento, remove o último e chama a si mesma novamente após o intervalo SPEED.
    """
    x, y = snake.coordinates[0]

    if direction == 'up':
        y -= SPACE_SIZE
    elif direction == 'down':
        y += SPACE_SIZE
    elif direction == 'left':
        x -= SPACE_SIZE
    elif direction == 'right':
        x += SPACE_SIZE

    snake.coordinates.insert(0, (x, y))
    square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR)
    snake.squares.insert(0, square)

    # Verifica se houve colisão com a parede ou o próprio corpo
    if check_collision(snake):
        pass

    # Verifica se a comida foi comida
    if x == food.coordinates[0] and y == food.coordinates[1]:
        global score
        score += 1
        label.config(text=f'Score:{score}')
        canvas.delete('food')
        food = Food()
    else:
        # Remove a última parte da cobra para simular o movimento
        del snake.coordinates[-1]
        canvas.delete(snake.squares[-1])
        del snake.squares[-1]

    # Chama o próximo turno
    window.after(SPEED, next_turn, snake, food)


# Função que altera a direção da cobra
def change_direction(new_direction):
    """
    Altera a direção global da cobra. Evita mudança direta para a direção oposta.
    """
    global direction

    if new_direction == 'left' and direction != 'right':
        direction = new_direction
    elif new_direction == 'right' and direction != 'left':
        direction = new_direction
    elif new_direction == 'up' and direction != 'down':
        direction = new_direction
    elif new_direction == 'down' and direction != 'up':
        direction = new_direction


# Função que verifica colisões
def check_collision(snake):
    """
    Verifica se a cobra colidiu com a parede ou com o próprio corpo.
    Retorna True em caso de colisão, False caso contrário.
    """
    pass



# Função que finaliza o jogo
def game_over():
    """
    Exibe mensagem de fim de jogo e limpa o canvas.
    """
    pass



# ==== INICIALIZAÇÃO DA INTERFACE GRÁFICA ====

# Criação da janela principal
window = Tk()
window.title('Snake game')  # Título da janela
window.resizable(False, False)  # Impede redimensionamento

# Inicializa placar e direção
score = 0
direction = 'down'

# Cria rótulo do placar
label = Label(window, text=f'Score:{score}', font=('consolas', 40))
label.pack()

# Cria o canvas onde o jogo será desenhado
canvas = Canvas(window, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()

# Atualiza a janela antes de centralizar
window.update()

# Centraliza a janela na tela do usuário
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = int((screen_width / 2) - (window_width / 2))
y = int((screen_height / 2) - (window_height / 2))
window.geometry(f'{window_width}x{window_height}+{x}+{y}')

# Define os controles do teclado
window.bind('<Left>', lambda event: change_direction('left'))
window.bind('<Right>', lambda event: change_direction('right'))
window.bind('<Up>', lambda event: change_direction('up'))
window.bind('<Down>', lambda event: change_direction('down'))

# Instancia a cobra e a comida
snake = Snake()
food = Food()

# Inicia o loop principal do jogo
next_turn(snake, food)

# Inicia o loop da interface
window.mainloop()
