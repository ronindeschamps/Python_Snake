import os 
import pygame as p
import random
import keyboard as keys

movement = p.USEREVENT + 1

class Snake():
  
  def __init__(self):
    self.positions = [(250, 250)]
    self.color = (0, 255, 255)

  def draw(self, screen):
    for position in self.positions:
      p.draw.rect(screen, self.color, (position[0], position[1], 10, 10))
      
  def gobble(self, dx, dy):
    head_x, head_y = self.positions[0]
    self.positions.insert(0, (head_x + dx, head_y + dy))
    
  def move(self, dx, dy, screen):
    head_x, head_y = self.positions[0]
    
    if head_x < 0 or head_x >= 500 or head_y < 0 or head_y >= 350:
      p.font.init()
      font = p.font.Font(None, 74)
      text = font.render('Game Over', True, (255, 0, 0))
      text_rect = text.get_rect(center=(screen.get_width()/2, screen.get_height()/2))
      screen.blit(text, text_rect)  
      p.display.update()   
      
    
    self.positions.insert(0, (head_x + dx, head_y + dy))
    self.positions.pop()
    
class Food():
  
  def __init__(self):
    self.positions = [((random.randint(0, 49)*10), (random.randint(0, 34)*10))]
    self.color = (255, 255, 0)

  def draw(self, screen):
    for position in self.positions:
      p.draw.rect(screen, self.color, (position[0], position[1], 10, 10))
      
  def regen(self):
    print(self.positions)
    self.positions.pop()
    self.positions.insert(0, ((random.randint(0, 49)*10), (random.randint(0, 34)*10)))
   
def main():
  
  p.init()
  clock = p.time.Clock()
  screen = p.display.set_mode((500, 350))
  p.display.set_caption("Snake")
  snake = Snake()
  food = Food()

  p.time.set_timer(movement, 100)

  score = 0
  
  running = True
  game_over = False
  while running:
    for event in p.event.get():

      if event.type == p.QUIT:
        running = False
        
      elif event.type == p.KEYDOWN:
        if 'lastkey' in locals(): 
          slastkey = lastkey
          lastkey = event.key
        else:
          lastkey = event.key
          
      if snake.positions[0] in snake.positions[1:]:
           
        p.font.init()
        font = p.font.Font(None, 74)
        text = font.render('Game Over', True, (255, 0, 0))
        text_rect = text.get_rect(center=(screen.get_width()/2, screen.get_height()/2))
        screen.blit(text, text_rect)  
        p.display.update()   
        game_over = True
        
      elif event.type == movement and game_over == False:
      
        screen.fill((0, 0, 0))  

        
        if snake.positions[0] == food.positions[0]:
          score += 1
          print(score)
          if lastkey == p.K_LEFT:
            snake.gobble(-10, 0)
            food.regen()
          if lastkey == p.K_RIGHT:
            snake.gobble(10, 0)
            food.regen()
          if lastkey == p.K_UP:
            snake.gobble(0, -10)
            food.regen()
          if lastkey == p.K_DOWN:
            snake.gobble(0, 10)
            food.regen()

        keys = p.key.get_pressed()
        if keys[p.K_LEFT]:
            snake.move(-10, 0, screen)
        elif keys[p.K_RIGHT]:
            snake.move(10, 0, screen)
        elif keys[p.K_UP]:
            snake.move(0, -10, screen)
        elif keys[p.K_DOWN]:
            snake.move(0, 10, screen)
            
        elif 'lastkey' in locals():
            if lastkey == p.K_LEFT:
              snake.move(-10, 0, screen)
              if 'slastkey' in locals():
                if slastkey == p.K_RIGHT:
                  p.font.init()
                  font = p.font.Font(None, 74) 
                  text = font.render('Game Over', True, (255, 0, 0))
                  text_rect = text.get_rect(center=(screen.get_width()/2, screen.get_height()/2))
                  screen.blit(text, text_rect) 
                  p.display.update()
                  game_over = True
                  
            if lastkey == p.K_RIGHT:
              snake.move(10, 0, screen)
              if 'slastkey' in locals():
                if slastkey == p.K_LEFT:
                  p.font.init()
                  font = p.font.Font(None, 74) 
                  text = font.render('Game Over', True, (255, 0, 0))
                  text_rect = text.get_rect(center=(screen.get_width()/2, screen.get_height()/2))
                  screen.blit(text, text_rect) 
                  p.display.update()
                  game_over = True                  
                
            if lastkey == p.K_UP:
              snake.move(0, -10, screen)
              if 'slastkey' in locals():              
                if slastkey == p.K_DOWN:
                  p.font.init()
                  font = p.font.Font(None, 74) 
                  text = font.render('Game Over', True, (255, 0, 0))
                  text_rect = text.get_rect(center=(screen.get_width()/2, screen.get_height()/2))
                  screen.blit(text, text_rect) 
                  p.display.update()
                  game_over = True
                  
            if lastkey == p.K_DOWN:
              snake.move(0, 10, screen)
              if 'slastkey' in locals():                            
                if slastkey == p.K_UP:
                  p.font.init()
                  font = p.font.Font(None, 74) 
                  text = font.render('Game Over', True, (255, 0, 0))
                  text_rect = text.get_rect(center=(screen.get_width()/2, screen.get_height()/2))
                  screen.blit(text, text_rect) 
                  p.display.update()
                  game_over = True             
                    
    snake.draw(screen)
    food.draw(screen)
    p.font.init()
    font = p.font.Font(None, 30)
    text = font.render(f'Score: {score}', True, (255, 0, 0))
    text_rect = text.get_rect()
    screen.blit(text, text_rect) 
    p.display.update()
    clock.tick(60)

  p.quit()

main()