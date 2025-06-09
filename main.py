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
        self.body_size = BODY_PARTS            # Tamanho inicial do corpo da cobra
        self.coordinates = []                  # Lista de coordenadas de cada segmento do corpo
        self.squares = []                      # Lista de objetos gráficos (retângulos) no canvas

        # Inicializa as coordenadas com todos os segmentos sobrepostos em (0,0)
        for i in range(0, BODY_PARTS):
            self.coordinates.append([0, 0])

        # Para cada coordenada, desenha um retângulo correspondente à parte da cobra
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
        Sua posição é armazenada como uma lista [x, y] em self.coordinates.
        """

        # Gera uma posição aleatória múltipla de SPACE_SIZE dentro da largura do jogo
        x = random.randint(0, (GAME_WIDTH // SPACE_SIZE) - 1) * SPACE_SIZE

        # Gera uma posição aleatória múltipla de SPACE_SIZE dentro da altura do jogo
        y = random.randint(0, (GAME_HEIGHT // SPACE_SIZE) - 1) * SPACE_SIZE

        # Armazena as coordenadas da comida como uma lista
        self.coordinates = [x, y]

        # Desenha a comida no canvas como um círculo vermelho
        canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOR, tags='food')


# Função que será chamada a cada "turno" do jogo (movimento da cobra, atualização da tela, etc.)
def next_turn(snake, food):
    """
    Atualiza a posição da cobra de acordo com a direção atual.
    Move a cabeça da cobra, desenha o novo segmento, remove o último e chama a si mesma novamente após o intervalo SPEED.
    """
    # Obtém a posição atual da cabeça da cobra
    x, y = snake.coordinates[0]

    # Atualiza a posição com base na direção global
    if direction == 'up':
        y -= SPACE_SIZE
    elif direction == 'down':
        y += SPACE_SIZE
    elif direction == 'left':
        x -= SPACE_SIZE
    elif direction == 'right':
        x += SPACE_SIZE

    # Insere a nova posição da cabeça na frente da lista de coordenadas
    snake.coordinates.insert(0, (x, y))

    # Desenha o novo segmento no canvas
    square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR)

    # Adiciona o retângulo à lista de partes da cobra
    snake.squares.insert(0, square)

    # Remove a última parte da cobra (a cauda) para simular o movimento
    del snake.coordinates[-1]
    canvas.delete(snake.squares[-1])
    del snake.squares[-1]

    # Chama novamente a função após um intervalo (loop do jogo)
    window.after(SPEED, next_turn, snake, food)


# Função que altera a direção da cobra de acordo com o input do usuário
def change_direction(new_direction):
    """
    Altera a direção global da cobra. Ainda precisa implementar verificação para evitar reversão direta.
    """
    global direction

    if new_direction == 'left':
        if direction != 'right':
            direction = new_direction
    if new_direction == 'right':
        if direction != 'left':
            direction = new_direction
    if new_direction == 'up':
        if direction != 'down':
            direction = new_direction
    if new_direction == 'down':
        if direction != 'up':
            direction = new_direction


# Função para verificar se houve colisão (com a parede ou consigo mesma)
def check_collision():
    """
    Verifica se a cobra colidiu com a parede ou com ela mesma.
    """
    pass  # Ainda será implementado


# Função que finaliza o jogo
def game_over():
    """
    Finaliza o jogo, possivelmente mostrando uma mensagem e desativando a movimentação.
    """
    pass  # A lógica será implementada depois


# ==== INICIALIZAÇÃO DA INTERFACE ====

# Criação da janela principal do jogo
window = Tk()
window.title('Snake game')         # Define o título da janela
window.resizable(False, False)     # Impede redimensionamento da janela

# Inicialização da pontuação e da direção inicial
score = 0
direction = 'down'

# Rótulo que exibe a pontuação atual
label = Label(window, text=f'Score:{score}', font=('consolas', 40))
label.pack()

# Canvas onde a cobra e a comida são desenhadas
canvas = Canvas(window, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()

# Atualiza a janela antes de centralizar
window.update()

# Cálculo para centralizar a janela na tela do usuário
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width / 2) - (window_width / 2))
y = int((screen_height / 2) - (window_height / 2))

# Define a posição da janela
window.geometry(f'{window_width}x{window_height}+{x}+{y}')

window.bind('<Left>', lambda event: change_direction('left'))
window.bind('<Right>', lambda event: change_direction('right'))
window.bind('<Up>', lambda event: change_direction('up'))
window.bind('<Down>', lambda event: change_direction('down'))

# Instancia a cobra e a comida
snake = Snake()
food = Food()

# Inicia o loop do jogo chamando a função next_turn
next_turn(snake, food)

# Inicia o loop principal da interface gráfica
window.mainloop()
