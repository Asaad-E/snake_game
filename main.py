# -*- coding: utf-8 -*-
import pygame
from utils import *
from snake import Snake

from random import randint

# pygame setup

pygame.init()
pygame.font.init() 

screen = pygame.display.set_mode((screen_width, screen_heigth))
pygame.display.set_caption('Snake')


programIcon = pygame.image.load('icon.png')
pygame.display.set_icon(programIcon)


clock = pygame.time.Clock()



snake = Snake()

game_stage = {
    'game_over': False,
    'score': 0,
    'max_score': 0
}


running = True
game_over = False
frame_count = 1

def random_food():
    
    while True:
        x = randint(0, grid_w-1)
        y = randint(0, grid_h-1)
        
        if not snake.check_chollision((x, y)):
            return [x, y]
    
def text(screen, text, pos, size=30):
    font = pygame.font.Font('Retro Gaming.ttf', size)
    text_surface = font.render(text, False, white_color)
    
    rect = text_surface.get_rect()
    rect.center = (pos[0], pos[1])
    
    screen.blit(text_surface, rect)    
    

def add_score():
    
    game_stage['score'] += 1;
    
    if game_stage['score'] > game_stage['max_score']:
        game_stage['max_score'] = game_stage['score']

def reset_game():
    global game_stage, snake, frame_count, food
    game_stage = {
        'game_over': False,
        'score': 0,
        'max_score': game_stage['max_score']
    }    
    snake = Snake()
    frame_count = 1
    food = random_food()


def main():
    global game_stage, snake, frame_count, food, running
    
    food = random_food()
    while running:
        # Poll for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    snake.change_dir(-1, 0)
                if event.key == pygame.K_RIGHT:
                    snake.change_dir(1, 0)
                if event.key == pygame.K_UP:
                    snake.change_dir(0, -1)
                if event.key == pygame.K_DOWN:
                    snake.change_dir(0, 1)                        
                
                if game_stage['game_over'] == True and event.key == pygame.K_RETURN:
                    print('reset')
                    reset_game()

        # fill the background
        
        screen.fill(background_color)
        
        # update snake
        
        if frame_count % frame_span == 0 and game_stage['game_over'] == False:
            check = snake.move_snake()
            
            if check == False:
                game_stage['game_over'] = True
                
        if snake.eat(food):
            food = random_food()
            add_score()
        
        # draw snake
        
        for segment in snake.body_pos:
            row = segment[0]
            column = segment[1]
            pygame.draw.rect(screen,snake_color,(row*span_w, column*span_h, span_w, span_h))
        
        # draw food
        
        pygame.draw.rect(screen,food_color,(food[0]*span_w, food[1]*span_h, span_w, span_h))
        
        
        # draw grid
        for row in range(grid_w):
            for column in range(grid_h):
                pygame.draw.rect(screen,border_color,(row*span_w, column*span_h, span_w, span_h), width = 1)
        
        
        # draw UI
        score = f'Score: {game_stage['score']}'
        text(screen, score, (screen_width//4, game_heigth + ui_heigth//2))
        
        score = f'Max Score: {game_stage['max_score']}'
        text(screen, score, ((3*screen_width)//4 - 20, game_heigth + ui_heigth//2))        
        
        # draw gameover screen
        if game_stage['game_over']:
            rect = pygame.Rect(0, 0, 350, 100)
            rect.center = (screen_width//2, screen_heigth//2)
            
            pygame.draw.rect(screen, background_color, rect)
            pygame.draw.rect(screen, border_color, rect, width=3)
            
            text(screen, 'GameOver', (screen_width//2, screen_heigth//2 - 20))
            text(screen, 'Pres Start to start again', (screen_width//2, screen_heigth//2 + 20), size=20)
        
        # end frame
        pygame.display.flip()
        clock.tick(fps)
        frame_count += 1
        
        


if __name__ == '__main__':
    main()
    pygame.quit()