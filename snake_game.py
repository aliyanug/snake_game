from random import randint
import pygame

SCREEN_WIDTH, SCREEN_HEIGHT = 640, 480
GRID_SIZE = 20
GRID_WIDTH = SCREEN_WIDTH // GRID_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // GRID_SIZE

UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

BOARD_BACKGROUND_COLOR = (0, 0, 0)
APPLE_COLOR = (255, 0, 0)
SNAKE_COLOR = (0, 255, 0)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)
pygame.display.set_caption('И з г р и б  П и т о н а')

clock = pygame.time.Clock()


class GameObject:
    """Базовый класс, от которого наследуются другие игровые объекты."""

    def __init__(self, body_color=None):
        """Инициализирует базовые атрибуты объекта: позицию и цвет."""
        self.position = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        self.body_color = body_color

    def draw(self):
        """Абстрактный метод для отрисовки объекта на экране."""
        raise NotImplementedError(
            'Метод draw должен быть переопределен в дочернем классе.'
        )


class Apple(GameObject):
    """Класс, описывающий яблоко и действия с ним."""

    def __init__(self, body_color=APPLE_COLOR):
        """Инициализирует яблоко заданным цветом и случайной позицией."""
        super().__init__(body_color)
        self.randomize_position()

    def randomize_position(self):
        """Устанавливает случайное положение яблока на игровом поле."""
        self.position = (
            randint(0, GRID_WIDTH - 1) * GRID_SIZE,
            randint(0, GRID_HEIGHT - 1) * GRID_SIZE,
        )

    def draw(self):
        """Отрисовывает яблоко на игровой поверхности."""
        rect = pygame.Rect(self.position, (GRID_SIZE, GRID_SIZE))
        pygame.draw.rect(screen, self.body_color, rect)
        pygame.draw.rect(screen, (50, 50, 50), rect, 1)


class Snake(GameObject):
    """Класс, описывающий змейку и ее поведение."""

    def __init__(self, body_color=SNAKE_COLOR):
        """Инициализирует начальное состояние змейки."""
        super().__init__(body_color)
        self.reset()

    def reset(self):
        """Сбрасывает змейку в начальное состояние."""
        self.length = 1
        self.positions = [(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)]
        self.direction = RIGHT
        self.next_direction = None
        self.last = None

    def update_direction(self):
        """Обновляет направление движения змейки."""
        if self.next_direction:
            self.direction = self.next_direction
            self.next_direction = None

    def move(self):
        """Обновляет позицию змейки (координаты каждой секции)."""
        head_x, head_y = self.get_head_position()
        dir_x, dir_y = self.direction
        new_head = (
            (head_x + dir_x * GRID_SIZE) % SCREEN_WIDTH,
            (head_y + dir_y * GRID_SIZE) % SCREEN_HEIGHT,
        )
        if new_head in self.positions[1:]:
            screen.fill(BOARD_BACKGROUND_COLOR)
            self.reset()
            return
        
        self.positions.insert(0, new_head)
        if len(self.positions) > self.length:
            self.last = self.positions.pop()
        else:
            self.last = None

    def draw(self):
        """Отрисовывает змейку на экране, затирая след."""
        head_rect = pygame.Rect(
            self.get_head_position(), (GRID_SIZE, GRID_SIZE)
        )
        pygame.draw.rect(screen, self.body_color, head_rect)
        pygame.draw.rect(screen, (50, 50, 50), head_rect, 1)
        
        if self.last:
            last_rect = pygame.Rect(self.last, (GRID_SIZE, GRID_SIZE))
            pygame.draw.rect(screen, BOARD_BACKGROUND_COLOR, last_rect)

    def get_head_position(self):
        """Возвращает позицию головы змейки (первый элемент)."""
        return self.positions[0]


def handle_keys(snake):
    """Обрабатывает нажатия клавиш для изменения направления движения."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake.direction != DOWN:
                snake.next_direction = UP
            elif event.key == pygame.K_DOWN and snake.direction != UP:
                snake.next_direction = DOWN
            elif event.key == pygame.K_LEFT and snake.direction != RIGHT:
                snake.next_direction = LEFT
            elif event.key == pygame.K_RIGHT and snake.direction != LEFT:
                snake.next_direction = RIGHT


def main():
    """Основная функция игры, содержащая главный игровой цикл."""
    pygame.init()
    snake = Snake()
    apple = Apple()
    screen.fill(BOARD_BACKGROUND_COLOR)

    while True:
        clock.tick(20)
        handle_keys(snake)
        snake.update_direction()
        snake.move()
        
        if snake.get_head_position() == apple.position:
            snake.length += 1
            apple.randomize_position()
            
        apple.draw()
        snake.draw()
        pygame.display.update()


if __name__ == '__main__':
    main()
