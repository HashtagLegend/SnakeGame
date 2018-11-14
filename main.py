from sense_hat import SenseHat
from time import sleep
sense = SenseHat()

sense.clear()
direction = "up"

A = (255,0,0)
B = (0,0,0)


x = 3
y = 3
play = True

sense.set_pixel(x,y,(A))

def movement(a,b):
  while True:
    global x
    global y
    x = a
    y = b
    
    while direction == "up":
      sense.set_pixel(x,y,(B))
      x=x-1
      if x < 0:
        sense.show_message("GAME OVER")
        play = False
      
      sense.set_pixel(x,y,(A))
      sleep(1)
      break
        
 
    while direction == "down":
      sense.set_pixel(x,y,(B))
      x=x+1
      if x > 7:
        sense.show_message("GAME OVER")
        play = False
     
      sense.set_pixel(x,y,(A))
      sleep(1) 
      break
    
    while direction == "left":
      sense.set_pixel(x,y,(B))
      y=y+1
      if y > 7:
        sense.show_message("GAME OVER")
        play = False
      
      sense.set_pixel(x,y,(A))
      sleep(1)
      break
    
    while direction == "right":
      sense.set_pixel(x,y,(B))
      y=y-1
      if y < 0:
        sense.show_message("GAME OVER")
        play = False
      
      sense.set_pixel(x,y,(A))
      sleep(1)
      break
    break

while play:
  for event in sense.stick.get_events():
    
    if event.action == "pressed":
      if event.direction == "up":
        direction = "up"
        movement(x,y)
      if event.direction == "left":
        direction = "left"
        movement(x,y)
      if event.direction == "right":
        direction = "right"
        movement(x,y)
      if event.direction == "down":
        direction = "down"
        movement(x,y)

  


      


    
sense.clear()    