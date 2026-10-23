{\rtf1\ansi\ansicpg1251\cocoartf2868
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 from random import randint\
import pygame\
\
SCREEN_WIDTH, SCREEN_HEIGHT = 640, 480\
GRID_SIZE = 20\
GRID_WIDTH = SCREEN_WIDTH // GRID_SIZE\
GRID_HEIGHT = SCREEN_HEIGHT // GRID_SIZE\
\
UP = (0, -1)\
DOWN = (0, 1)\
LEFT = (-1, 0)\
RIGHT = (1, 0)\
\
BOARD_BACKGROUND_COLOR = (0, 0, 0)\
APPLE_COLOR = (255, 0, 0)\
SNAKE_COLOR = (0, 255, 0)\
\
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)\
pygame.display.set_caption('\uc0\u1048 \u1079 \u1075 \u1080 \u1073  \u1055 \u1080 \u1090 \u1086 \u1085 \u1072 ')\
\
clock = pygame.time.Clock()\
\
\
class GameObject:\
    """\uc0\u1041 \u1072 \u1079 \u1086 \u1074 \u1099 \u1081  \u1082 \u1083 \u1072 \u1089 \u1089 , \u1086 \u1090  \u1082 \u1086 \u1090 \u1086 \u1088 \u1086 \u1075 \u1086  \u1085 \u1072 \u1089 \u1083 \u1077 \u1076 \u1091 \u1102 \u1090 \u1089 \u1103  \u1076 \u1088 \u1091 \u1075 \u1080 \u1077  \u1080 \u1075 \u1088 \u1086 \u1074 \u1099 \u1077  \u1086 \u1073 \u1098 \u1077 \u1082 \u1090 \u1099 ."""\
\
    def __init__(self, body_color=None):\
        """\uc0\u1048 \u1085 \u1080 \u1094 \u1080 \u1072 \u1083 \u1080 \u1079 \u1080 \u1088 \u1091 \u1077 \u1090  \u1073 \u1072 \u1079 \u1086 \u1074 \u1099 \u1077  \u1072 \u1090 \u1088 \u1080 \u1073 \u1091 \u1090 \u1099  \u1086 \u1073 \u1098 \u1077 \u1082 \u1090 \u1072 : \u1087 \u1086 \u1079 \u1080 \u1094 \u1080 \u1102  \u1080  \u1094 \u1074 \u1077 \u1090 ."""\
        self.position = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)\
        self.body_color = body_color\
\
    def draw(self):\
        """\uc0\u1040 \u1073 \u1089 \u1090 \u1088 \u1072 \u1082 \u1090 \u1085 \u1099 \u1081  \u1084 \u1077 \u1090 \u1086 \u1076  \u1076 \u1083 \u1103  \u1086 \u1090 \u1088 \u1080 \u1089 \u1086 \u1074 \u1082 \u1080  \u1086 \u1073 \u1098 \u1077 \u1082 \u1090 \u1072  \u1085 \u1072  \u1101 \u1082 \u1088 \u1072 \u1085 \u1077 ."""\
        raise NotImplementedError(\
            '\uc0\u1052 \u1077 \u1090 \u1086 \u1076  draw \u1076 \u1086 \u1083 \u1078 \u1077 \u1085  \u1073 \u1099 \u1090 \u1100  \u1087 \u1077 \u1088 \u1077 \u1086 \u1087 \u1088 \u1077 \u1076 \u1077 \u1083 \u1077 \u1085  \u1074  \u1076 \u1086 \u1095 \u1077 \u1088 \u1085 \u1077 \u1084  \u1082 \u1083 \u1072 \u1089 \u1089 \u1077 .'\
        )\
\
\
class Apple(GameObject):\
    """\uc0\u1050 \u1083 \u1072 \u1089 \u1089 , \u1086 \u1087 \u1080 \u1089 \u1099 \u1074 \u1072 \u1102 \u1097 \u1080 \u1081  \u1103 \u1073 \u1083 \u1086 \u1082 \u1086  \u1080  \u1076 \u1077 \u1081 \u1089 \u1090 \u1074 \u1080 \u1103  \u1089  \u1085 \u1080 \u1084 ."""\
\
    def __init__(self, body_color=APPLE_COLOR):\
        """\uc0\u1048 \u1085 \u1080 \u1094 \u1080 \u1072 \u1083 \u1080 \u1079 \u1080 \u1088 \u1091 \u1077 \u1090  \u1103 \u1073 \u1083 \u1086 \u1082 \u1086  \u1079 \u1072 \u1076 \u1072 \u1085 \u1085 \u1099 \u1084  \u1094 \u1074 \u1077 \u1090 \u1086 \u1084  \u1080  \u1089 \u1083 \u1091 \u1095 \u1072 \u1081 \u1085 \u1086 \u1081  \u1087 \u1086 \u1079 \u1080 \u1094 \u1080 \u1077 \u1081 ."""\
        super().__init__(body_color)\
        self.randomize_position()\
\
    def randomize_position(self):\
        """\uc0\u1059 \u1089 \u1090 \u1072 \u1085 \u1072 \u1074 \u1083 \u1080 \u1074 \u1072 \u1077 \u1090  \u1089 \u1083 \u1091 \u1095 \u1072 \u1081 \u1085 \u1086 \u1077  \u1087 \u1086 \u1083 \u1086 \u1078 \u1077 \u1085 \u1080 \u1077  \u1103 \u1073 \u1083 \u1086 \u1082 \u1072  \u1085 \u1072  \u1080 \u1075 \u1088 \u1086 \u1074 \u1086 \u1084  \u1087 \u1086 \u1083 \u1077 ."""\
        self.position = (\
            randint(0, GRID_WIDTH - 1) * GRID_SIZE,\
            randint(0, GRID_HEIGHT - 1) * GRID_SIZE,\
        )\
\
    def draw(self):\
        """\uc0\u1054 \u1090 \u1088 \u1080 \u1089 \u1086 \u1074 \u1099 \u1074 \u1072 \u1077 \u1090  \u1103 \u1073 \u1083 \u1086 \u1082 \u1086  \u1085 \u1072  \u1080 \u1075 \u1088 \u1086 \u1074 \u1086 \u1081  \u1087 \u1086 \u1074 \u1077 \u1088 \u1093 \u1085 \u1086 \u1089 \u1090 \u1080 ."""\
        rect = pygame.Rect(self.position, (GRID_SIZE, GRID_SIZE))\
        pygame.draw.rect(screen, self.body_color, rect)\
        pygame.draw.rect(screen, (50, 50, 50), rect, 1)\
\
\
class Snake(GameObject):\
    """\uc0\u1050 \u1083 \u1072 \u1089 \u1089 , \u1086 \u1087 \u1080 \u1089 \u1099 \u1074 \u1072 \u1102 \u1097 \u1080 \u1081  \u1079 \u1084 \u1077 \u1081 \u1082 \u1091  \u1080  \u1077 \u1105  \u1087 \u1086 \u1074 \u1077 \u1076 \u1077 \u1085 \u1080 \u1077 ."""\
\
    def __init__(self, body_color=SNAKE_COLOR):\
        """\uc0\u1048 \u1085 \u1080 \u1094 \u1080 \u1072 \u1083 \u1080 \u1079 \u1080 \u1088 \u1091 \u1077 \u1090  \u1085 \u1072 \u1095 \u1072 \u1083 \u1100 \u1085 \u1086 \u1077  \u1089 \u1086 \u1089 \u1090 \u1086 \u1103 \u1085 \u1080 \u1077  \u1079 \u1084 \u1077 \u1081 \u1082 \u1080 ."""\
        super().__init__(body_color)\
        self.reset()\
\
    def reset(self):\
        """\uc0\u1057 \u1073 \u1088 \u1072 \u1089 \u1099 \u1074 \u1072 \u1077 \u1090  \u1079 \u1084 \u1077 \u1081 \u1082 \u1091  \u1074  \u1085 \u1072 \u1095 \u1072 \u1083 \u1100 \u1085 \u1086 \u1077  \u1089 \u1086 \u1089 \u1090 \u1086 \u1103 \u1085 \u1080 \u1077 ."""\
        self.length = 1\
        self.positions = [(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)]\
        self.direction = RIGHT\
        self.next_direction = None\
        self.last = None\
\
    def update_direction(self):\
        """\uc0\u1054 \u1073 \u1085 \u1086 \u1074 \u1083 \u1103 \u1077 \u1090  \u1085 \u1072 \u1087 \u1088 \u1072 \u1074 \u1083 \u1077 \u1085 \u1080 \u1077  \u1076 \u1074 \u1080 \u1078 \u1077 \u1085 \u1080 \u1103  \u1079 \u1084 \u1077 \u1081 \u1082 \u1080 ."""\
        if self.next_direction:\
            self.direction = self.next_direction\
            self.next_direction = None\
\
    def move(self):\
        """\uc0\u1054 \u1073 \u1085 \u1086 \u1074 \u1083 \u1103 \u1077 \u1090  \u1087 \u1086 \u1079 \u1080 \u1094 \u1080 \u1102  \u1079 \u1084 \u1077 \u1081 \u1082 \u1080  (\u1082 \u1086 \u1086 \u1088 \u1076 \u1080 \u1085 \u1072 \u1090 \u1099  \u1082 \u1072 \u1078 \u1076 \u1086 \u1081  \u1089 \u1077 \u1082 \u1094 \u1080 \u1080 )."""\
        head_x, head_y = self.get_head_position()\
        dir_x, dir_y = self.direction\
        new_head = (\
            (head_x + dir_x * GRID_SIZE) % SCREEN_WIDTH,\
            (head_y + dir_y * GRID_SIZE) % SCREEN_HEIGHT,\
        )\
        if new_head in self.positions[1:]:\
            screen.fill(BOARD_BACKGROUND_COLOR)\
            self.reset()\
            return\
        self.positions.insert(0, new_head)\
        if len(self.positions) > self.length:\
            self.last = self.positions.pop()\
        else:\
            self.last = None\
\
    def draw(self):\
        """\uc0\u1054 \u1090 \u1088 \u1080 \u1089 \u1086 \u1074 \u1099 \u1074 \u1072 \u1077 \u1090  \u1079 \u1084 \u1077 \u1081 \u1082 \u1091  \u1085 \u1072  \u1101 \u1082 \u1088 \u1072 \u1085 \u1077 , \u1079 \u1072 \u1090 \u1080 \u1088 \u1072 \u1103  \u1089 \u1083 \u1077 \u1076 ."""\
        head_rect = pygame.Rect(\
            self.get_head_position(), (GRID_SIZE, GRID_SIZE)\
        )\
        pygame.draw.rect(screen, self.body_color, head_rect)\
        pygame.draw.rect(screen, (50, 50, 50), head_rect, 1)\
        if self.last:\
            last_rect = pygame.Rect(self.last, (GRID_SIZE, GRID_SIZE))\
            pygame.draw.rect(screen, BOARD_BACKGROUND_COLOR, last_rect)\
\
    def get_head_position(self):\
        """\uc0\u1042 \u1086 \u1079 \u1074 \u1088 \u1072 \u1097 \u1072 \u1077 \u1090  \u1087 \u1086 \u1079 \u1080 \u1094 \u1080 \u1102  \u1075 \u1086 \u1083 \u1086 \u1074 \u1099  \u1079 \u1084 \u1077 \u1081 \u1082 \u1080  (\u1087 \u1077 \u1088 \u1074 \u1099 \u1081  \u1101 \u1083 \u1077 \u1084 \u1077 \u1085 \u1090 )."""\
        return self.positions[0]\
\
\
def handle_keys(snake):\
    """\uc0\u1054 \u1073 \u1088 \u1072 \u1073 \u1072 \u1090 \u1099 \u1074 \u1072 \u1077 \u1090  \u1085 \u1072 \u1078 \u1072 \u1090 \u1080 \u1103  \u1082 \u1083 \u1072 \u1074 \u1080 \u1096  \u1076 \u1083 \u1103  \u1080 \u1079 \u1084 \u1077 \u1085 \u1077 \u1085 \u1080 \u1103  \u1085 \u1072 \u1087 \u1088 \u1072 \u1074 \u1083 \u1077 \u1085 \u1080 \u1103  \u1076 \u1074 \u1080 \u1078 \u1077 \u1085 \u1080 \u1103 ."""\
    for event in pygame.event.get():\
        if event.type == pygame.QUIT:\
            pygame.quit()\
            raise SystemExit\
        elif event.type == pygame.KEYDOWN:\
            if event.key == pygame.K_UP and snake.direction != DOWN:\
                snake.next_direction = UP\
            elif event.key == pygame.K_DOWN and snake.direction != UP:\
                snake.next_direction = DOWN\
            elif event.key == pygame.K_LEFT and snake.direction != RIGHT:\
                snake.next_direction = LEFT\
            elif event.key == pygame.K_RIGHT and snake.direction != LEFT:\
                snake.next_direction = RIGHT\
\
\
def main():\
    """\uc0\u1054 \u1089 \u1085 \u1086 \u1074 \u1085 \u1072 \u1103  \u1092 \u1091 \u1085 \u1082 \u1094 \u1080 \u1103  \u1080 \u1075 \u1088 \u1099 , \u1089 \u1086 \u1076 \u1077 \u1088 \u1078 \u1072 \u1097 \u1072 \u1103  \u1075 \u1083 \u1072 \u1074 \u1085 \u1099 \u1081  \u1080 \u1075 \u1088 \u1086 \u1074 \u1086 \u1081  \u1094 \u1080 \u1082 \u1083 ."""\
    pygame.init()\
    snake = Snake()\
    apple = Apple()\
    screen.fill(BOARD_BACKGROUND_COLOR)\
\
    while True:\
        clock.tick(20)\
        handle_keys(snake)\
        snake.update_direction()\
        snake.move()\
        if snake.get_head_position() == apple.position:\
            snake.length += 1\
            apple.randomize_position()\
        apple.draw()\
        snake.draw()\
        pygame.display.update()\
\
\
if __name__ == '__main__':\
    main()}
