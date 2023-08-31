import pygame
import random

#jo comments maine hindi mai likhe hai vo smjle aur vo kardena baki english wale chordena samjne mai assan hoga

class SnakeGame:
    #construtor hai yeh 
    def __init__(self):
        # intialize pygame ki modules
        pygame.init()
        
        # Colors
        self.white = (255, 255, 255)  # rgb format
        self.red = (255, 0, 0)
        self.cyan = (204, 204, 255)   #yeh cyan nhi hai purple hai isko purple kardena har jagah code mai
        self.black = (0, 0, 0)
        self.Ivor= (255, 255, 240)

        # Creating window
        self.screen_width = 900
        self.screen_height = 600
        self.gameWindow = pygame.display.set_mode((self.screen_width, self.screen_height))
        
        # Game Title
        pygame.display.set_caption("Snake's Game")
        pygame.display.update()     #jo bhi tune kiya hai usko update karta aur content visible karta
        self.clock = pygame.time.Clock()        #frame rate control karta
        self.font = pygame.font.SysFont(None, 50)       #font text size vagera
        
    def text_screen(self, text, color, x, y):
        screen_text = self.font.render(text, True, color)   #idhar vo self.font is this.font(jo tune choose kiya) usko parameter denge text
        # true boolean curved smooth edge kai liye and color
        self.gameWindow.blit(screen_text, [x, y])
        #self.gamewindow tune ek varibale banaya hai screen hai teri yeh usmai position kar rha tu screen_text
    def plot_snake(self, color, snk_list, snake_size):
        #snake draw karta    
        #har possible x,y pair mai jayega from snk_list se
        for x, y in snk_list:
            pygame.draw.rect(self.gameWindow, color, [x, y, snake_size, snake_size])
            
    def gameloop(self):
        #yeh sare intial varibale hai jaisa naam vaise hi kaam hai inka
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
        fps = 60  # fps = frames per second
        
        while not exit_game:
            #agar game khatam hogya toh
            if game_over:
                #yeh vo last screen harne kai baad
                self.gameWindow.fill(self.cyan)
                self.text_screen("Game Over! Press Enter To Continue", self.red, 100, 230)
                self.text_screen("Created By : ", self.black, 630, 430)
                self.text_screen("1.Rohit Verma", self.black, 630, 480)
                self.text_screen("2.Nipun Tiwari", self.black, 630, 520)
                self.text_screen("3.Pramith", self.black, 630, 560)
                #event handling har possible operation se kya karna vo batata
                for event in pygame.event.get():
                    #quit kar rha
                    if event.type == pygame.QUIT:
                        exit_game = True
                    #if event.type == pygame.KEYDOWN:  
                    #yeh keydown ka matlab hai ki koi key press hori
                    #yeh line mat hatana abhi aise hi rakhe rehne de yeh line game force quit karte jaise humko infite loop mai aata na vaise hi
                    #enter button daba rha 
                    if event.key == pygame.K_RETURN:
                        self.gameloop()     #khud kai funtion ko vapis bulara yani game restart
            else:
                for event in pygame.event.get():
                    #force quit kai liye hai vo cross button wala
                    if event.type == pygame.QUIT:
                        exit_game = True
                    #yeh keydown aur normal down arrow alag hai
                    #yeh keydown ka matlab hai ki koi key press hori
                    #yeh vo arrow wali bas DOWN hoti 
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RIGHT:
                            #agar right button dabayega toh init_Velcoty x ki taraf hogi
                            #aur doosra wala 0 hoga kyuki 1D motion hai
                            velocity_x = init_velocity
                            velocity_y = 0
                        if event.key == pygame.K_LEFT:
                            #agar right button dabayega toh init_Velcoty -x ki taraf hogi
                            #aur doosra wala 0 hoga kyuki 1D motion hai
                            velocity_x = -init_velocity
                            velocity_y = 0
                        if event.key == pygame.K_UP:
                            #agar up button dabayega toh init_Velcoty - y  ki taraf hogi
                            #aur doosra wala 0 hoga kyuki 1D motion hai
                            velocity_y = -init_velocity
                            velocity_x = 0
                        if event.key == pygame.K_DOWN:
                            #aur doosra wala 0 hoga kyuki 1D motion hai
                            #agar down button dabayega toh init_Velcoty y ki taraf hogi
                            velocity_y = init_velocity
                            velocity_x = 0
                            
                snake_x = snake_x + velocity_x
                snake_y = snake_y + velocity_y
                
                if abs(snake_x - food_x) < 10 and abs(snake_y - food_y) < 10:
                    score += 1
                    #yeh ranfomly place food
                    food_x = random.randint(20, self.screen_width - 30)
                    food_y = random.randint(60, self.screen_height - 30)
                    #length badhadeta hai
                    snk_length += 5
                #yeh screen hai game khelte vakt ki
                self.gameWindow.fill(self.Ivor)
                #yeh upar score dikhata
                self.text_screen("Score: " + str(score * 10), self.black, 5, 5)
                #rectangle banataa screen pe 
                pygame.draw.rect(self.gameWindow, self.red, [food_x, food_y, snake_size, snake_size])
                #yeh line keech rha 5 thickennes and vo 0 40 starting 900 40 vo starting ending hai 
                pygame.draw.line(self.gameWindow, self.red, (0, 40), (900, 40), 5)
                #snake head store karta ki movements
                head = []
                head.append(snake_x)
                head.append(snake_y)
                #snake position store karta list of list
                snk_list.append(head)
                
                if len(snk_list) > snk_length:
                    del snk_list[0]
                #khud se takar ra gya tab game over    
                if head in snk_list[:-1]:
                    game_over = True
                #yeh screen kai andar hai na head vo check karta varna game over
                if snake_x < 0 or snake_x > self.screen_width - 20 or snake_y < 50 or snake_y > self.screen_height - 20:
                    game_over = True
                #snake draw karta
                self.plot_snake(self.black, snk_list, snake_size)
            #har event kai baad window update karta
            pygame.display.update()
            #frame rate ya clock rate set karta
            self.clock.tick(fps)
        #module quit karata
        pygame.quit()
        #interpreter exit hora auto close hota agar vo upar ek line likhi hai vo na use ho toh 73 dekh line number
        quit()

# Create an object of the SnakeGame class
game = SnakeGame()
# Start the game
game.gameloop()
