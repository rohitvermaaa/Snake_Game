import pygame
import random


class SnakeGame:
    def __init__(self):
        pygame.init()
        
        self.white = (255, 255, 255)  
        self.red = (255, 0, 0)
        self.cyan = (204, 204, 255)   
        self.black = (0, 0, 0)
        self.Ivor= (255, 255, 240)

        self.screen_width = 900
        self.screen_height = 600
        self.gameWindow = pygame.display.set_mode((self.screen_width, self.screen_height))
        
        pygame.display.set_caption("Snake's Game")
        pygame.display.update()  
        self.clock = pygame.time.Clock()       
        self.font = pygame.font.SysFont(None, 50)       
        
    def text_screen(self, text, color, x, y):
        screen_text = self.font.render(text, True, color)   
        self.gameWindow.blit(screen_text, [x, y])
        
    def plot_snake(self, color, snk_list, snake_size):
        for x, y in snk_list:
            pygame.draw.rect(self.gameWindow, color, [x, y, snake_size, snake_size])
            
    def gameloop(self):
        exit_game = False
        game_over = False
        snake_x = 45
        snake_y = 55
        velocity_x = 0
        velocity_y = 0
        snk_list = []
        snk_length = 1
        food_x = random.randint(20, self.screen_width - 20)
        food_y = random.randint(60, self.screen_height - 20)
        score = 0
        init_velocity = 4
        snake_size = 30
        fps = 60  
        
        while not exit_game:
            if game_over:
                self.gameWindow.fill(self.cyan)
                self.text_screen("Game Over! Press Enter To Continue", self.red, 100, 230)
                self.text_screen("Created By : ", self.black, 630, 430)
                self.text_screen("1.Rohit Verma", self.black, 630, 480)
                self.text_screen("2.Nipun Tiwari", self.black, 630, 520)
                self.text_screen("3.Pramith", self.black, 630, 560)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        exit_game = True
                    if event.key == pygame.K_RETURN:
                        self.gameloop()    
            else:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        exit_game = True
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RIGHT:
                            velocity_x = init_velocity
                            velocity_y = 0
                        if event.key == pygame.K_LEFT:
                            velocity_x = -init_velocity
                            velocity_y = 0
                        if event.key == pygame.K_UP:
                            velocity_y = -init_velocity
                            velocity_x = 0
                        if event.key == pygame.K_DOWN:
                            velocity_y = init_velocity
                            velocity_x = 0
                            
                snake_x = snake_x + velocity_x
                snake_y = snake_y + velocity_y
                
                if abs(snake_x - food_x) < 10 and abs(snake_y - food_y) < 10:
                    score += 1
                    food_x = random.randint(20, self.screen_width - 30)
                    food_y = random.randint(60, self.screen_height - 30)
                    snk_length += 5
                self.gameWindow.fill(self.Ivor)
                self.text_screen("Score: " + str(score * 10), self.black, 5, 5)
                pygame.draw.rect(self.gameWindow, self.red, [food_x, food_y, snake_size, snake_size])
                pygame.draw.line(self.gameWindow, self.red, (0, 40), (900, 40), 5)
                head = []
                head.append(snake_x)
                head.append(snake_y)
                snk_list.append(head)
                
                if len(snk_list) > snk_length:
                    del snk_list[0]
                if head in snk_list[:-1]:
                    game_over = True
                if snake_x < 0 or snake_x > self.screen_width - 20 or snake_y < 50 or snake_y > self.screen_height - 20:
                    game_over = True
                self.plot_snake(self.black, snk_list, snake_size)
            pygame.display.update()
            self.clock.tick(fps)
        pygame.quit()
        quit()

game = SnakeGame()
game.gameloop()
