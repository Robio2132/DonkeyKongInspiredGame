'''kong.py
Robbie Bennett
Project_10
CS151 Spring
Makes a video game that is similar Donkey Kong.
Artwork objects: https://gifer.com/en/ 
Artwork backgrounds --
https://www.deviantart.com/jaytoon81/art/Gotta-Go-Fast-Sonic-X-976094641
https://www.alamy.com/stock-photo/minions.html?sortBy=relevant
https://www.shutterstock.com/search/dungeon-background
'''

from abc import ABC, abstractmethod
import turtle

class Game(ABC):  
  
    class Button:

        def __init__(self, turtleDrawer: turtle.Turtle, topLeftX: int, topLeftY: int, bottomRightX: int, bottomRightY: int, buttonText: str, borderColor = "Black", fillColor = None, fontColor = None, fontSize: int = 12):
            '''Creates the instance vairiables for the button constructor.
            Paramaters:
            turtleDrawer -- Creates a turtle object
            TopLeftX -- The top left X position
            TopLeftY -- The top left Y position
            bottomRightX -- The top bottom Right x position
            BottomRightY -- The bottom Right Y position
            buttonText -- Creates the button texts
            borderColor -- Sets the Border color
            fillColor -- sets the fill color
            fontColor -- sets the font color
            fontSize -- sets the font size
            '''
            
            
            self.turt = turtleDrawer
            self.topLeftX = topLeftX
            self.topLeftY = topLeftY
            self.bottomRightX = bottomRightX
            self.bottomRightY = bottomRightY
            self.text = buttonText
            self.fill = fillColor
            self.font = ('Arial', fontSize, 'normal')
            self.fontColor = fontColor
            self.borderColor = borderColor
            self.draw()
        
        def draw(self):
            ''' This function draws the button using the turtleDrawer given in the constructor
            Paramaters:
            '''
            
            
            self.turt.goto(self.topLeftX, self.topLeftY)
            self.turt.setheading(0)
            oldColor = self.turt.color()
            oldWidth = self.turt.width()
            self.turt.color(self.borderColor)

            if self.fill: # Begins filling if fillColor was given in constructor
                self.turt.fillcolor(self.fill)
                self.turt.begin_fill()
            
            self.turt.pendown()
            self.turt.width(5)
            for i in range(2): # Draws the boundary of the button
                self.turt.forward(self.bottomRightX-self.topLeftX)
                self.turt.right(90)
                self.turt.forward(self.topLeftY - self.bottomRightY)
                self.turt.right(90)
            self.turt.penup()

            if self.fill:
                self.turt.end_fill()

            # Draws the text in the center of the box
            self.turt.goto(int((self.topLeftX + self.bottomRightX)/2), 
                           int((self.topLeftY + self.bottomRightY)/2) - self.font[1])
            self.turt.pencolor(self.fontColor)
            self.turt.write(self.text, align = "center", font = self.font)
            self.turt.pencolor(oldColor[0])
            self.turt.pencolor(oldColor[1])
            self.turt.width(oldWidth)

        def pointInside(self, pointX: int, pointY: int) -> bool:
            ''' This function returns True if the point given by (pointX, pointY) is within the 
                bounds of the button given in the constructor
                Paramaters:
                pointX -- creates a pointX int
                pointY -- creates a pointY int.'''
                
                
            return (pointX >= self.topLeftX
                and pointX <= self.bottomRightX
                and pointY >= self.bottomRightY
                and pointY <= self.topLeftY)
            
    class Game(ABC):
        def __init__(self):
            '''Creates the instance variables for the Game class.
            Paramaters:
            '''
            
            
            self.drawer = turtle.Turtle()
            self.drawer.hideturtle()
            self.drawer.penup()

      
class Title(Game):
        
    screen = turtle.Screen()
    turtleDrawer = turtle.Turtle()
        
    def __init__(self):
        '''Creates the instance variables for the intro screen
        Paramaters:
        '''
        
    
        super().__init__()
        self.turtleDrawer.hideturtle()
        self.background()
        self.Title()
        self.villain()
        self.createMainPlayer()
        self.barrel()  
        self.t = self.titleScreen()

    def barrel(self):
        '''Creates the barrel objects:
        Paramaters:
        ''' 
        
        
        barrel1 = turtle.Turtle()
        self.screen.register_shape('barrell.gif')
        barrel1.shape('barrell.gif')
        barrel1.penup()
        barrel1.goto(100,-310)
        
        barrel2 = turtle.Turtle()
        barrel2.shape('barrell.gif')
        barrel2.penup()
        barrel2.goto(-100,-310)
        
        barrel3 = turtle.Turtle()
        barrel3.shape('barrell.gif')
        barrel3.penup()
        barrel3.goto(-300,-310)
            
        self.barrel1 = barrel1 
        self.barrel2 = barrel2
        self.barrel3 = barrel3

    def createMainPlayer(self):
        ''' Creates a main player object.
        Paramaters:
        '''
        
        
        player = turtle.Turtle()
        self.screen.register_shape('sonic.gif')
        player.shape('sonic.gif')
        player.penup()
        player.goto(300,-310)
        self.p = player
        
    def background(self):
        '''Creates the background of the screen.
        Paramaters:
        '''
        
        
        self.bg = turtle.Turtle()
        self.screen.register_shape('gamebg.gif')
        self.bg.shape('gamebg.gif')
        self.bg.penup()
    
    def titleScreen(self):
        ''' Creates the title screen
        Paramaters:
        '''
            
            
        self.turtleDrawer.penup()
        #self.screen = turtle.Screen()
        self.screen.tracer(0)
            
        self.button = Game.Button(Title.turtleDrawer, 100, 100, 200, 0, "Click Me\nTo Start", borderColor="Red", 
            fillColor="Yellow", fontColor="Blue", fontSize=13)
        self.quitButton = Game.Button(Title.turtleDrawer, -200, 100, -100, 0, "Click Me\nTo Quit", borderColor="Red", 
            fillColor="Yellow", fontColor="Blue", fontSize=13)
        
    def villain(self):
        '''Creates the villain.
        Paramaters:
        '''


        villain = turtle.Turtle()
        self.screen.register_shape('minion.gif')
        villain.shape('minion.gif')
        villain.penup()
        villain.goto(-15,-70)
        self.villain = villain
        print("villain working")
        #return(self.barrel)
        
    def Title(self):
        '''Creates the title of the game.
        Paramaters:
        '''


        title = turtle.Turtle()
        title.penup()
        title.hideturtle()
        title.color('yellow')
        title.goto(-150, 200)
        title.write("Minion Escape!", True, 'left', ('Melted Monster', 50, 'normal'))
        print("villain working")
        
    def createTitleScreenEvents( mouse_X, mouse_Y):  
        '''Creates the Title Screen Events:
        Paramaters:
        mouse_X -- Gets the mouse x position
        mouse_Y -- Gets the mouse Y position
        '''
            
            
        button = Game.Button(Title.turtleDrawer, 100, 100, 200, 0, "Click Me\nTo Start", borderColor="Red", 
            fillColor="Green", fontColor="Blue", fontSize=13)
        quitButton = Game.Button(Title.turtleDrawer, -200, 100, -100, 0, "Click Me\nTo Quit", borderColor="Red", 
            fillColor="Green", fontColor="Blue", fontSize=13)
        if button.pointInside(mouse_X, mouse_Y):
            print("Button clicked!")
            Title.screen.clear()
            k = Kong()
            k.play()
        elif quitButton.pointInside( mouse_X, mouse_Y):
            Title.screen.exitonclick()
     
    def play(self):
        '''Creates the mainloop method.
        Paramters:
        '''
        
        
        self.screen.onclick(Title.createTitleScreenEvents)
        self.screen.listen()
        turtle.done()
        
class Kong(Game):
    def __init__(self):
        '''Creates the instance variables for the Kong Game Class
        Paramaters:
        '''
        
        
        super().__init__()
        self.barrel1 = turtle.Turtle()
        self.bar2 = turtle.Turtle()
        self.bar3 = turtle.Turtle()
        self.bar4 = turtle.Turtle()
        self.direction = 1
        self.direction2 = 1
        self.screen = Title.screen
        self.screen.tracer(0)
        self.width = 800
        self.height = 800
        self.screen.screensize(self.width,self.height, "Dark Grey")
        self.background()
        self.speed = 10
        self.turnRate = 10
        self.min_x = -200
        self.min_y = 200
        self.max_x = 200
        self.max_y = 300
        self.collision_radius = 40
        self.jump_radius = 40
        
        #Initial start screen events.
        self.c = self.createGamescene()
        self.l = self.ladder()
        self.p = self.createMainPlayer()
        self.v = self.villain()
        self.b = self.barrel()
        self.b2 = self.barrel2()
        self.createGameScreenEvents()
        
    def background(self):
        '''Creates the background image of the screen.
        Paramaters:
        '''
        
        
        self.bg = turtle.Turtle()
        self.screen.register_shape('gamebg.gif')
        self.bg.shape('gamebg.gif')
        self.bg.penup()
        
    def createMainPlayer(self):
        '''Creates the main player character
        Paramaters:
        '''
        
        
        player = turtle.Turtle()
        self.screen.register_shape('sonic.gif')
        self.screen.register_shape('leftsonic.gif')
        player.shape('sonic.gif')
        player.penup()
        player.goto(-550,-420)
        self.p = player
        return(self.p)
     
    def createGamescene(self):
        '''Creates the Game Scene.
        Paramaters:
        '''


        turt = turtle.Turtle()
        turt2 = turtle.Turtle()
        turt3 = turtle.Turtle()
        turt4 = turtle.Turtle()
        self.screen.register_shape('floor.gif')
        turt.shape('floor.gif')
        turt.penup()
        turt.goto(0,-455)
        self.ground = turt, turt2, turt3, turt4
        turt2.shape('floor.gif')
        turt2.penup()
        self.ground2 = turt2
        self.ground2.goto(0,-200)
        self.sc = 0 
        turt3.shape('floor.gif')
        turt3.penup()
        self.ground3 = turt3
        self.ground3.goto(0,50)
        turt4.shape('floor.gif')
        turt4.penup()
        self.ground4 = turt4
        self.ground4.goto(0,250)
        
        return self.ground 
    
    def ladder(self):
        '''Creates the ladders.
        Paramaters:
        '''
        
        
        ladder = turtle.Turtle()
        ladder2 = turtle.Turtle()
        ladder3 = turtle.Turtle()
        #ladder 1
        self.screen.register_shape('ladder.gif')
        ladder.shape('ladder.gif')
        ladder.penup()
        ladder.goto(550,-330)
        #ladder 2
        ladder2.shape('ladder.gif')
        ladder2.penup()
        ladder2.goto(-550,-75)
        #ladder 3
        ladder3.shape('ladder.gif')
        ladder3.penup()
        ladder3.goto(550,150)
    
        self.l1 = ladder
        self.l2 = ladder2
        self.l3 = ladder3
        self.l = ladder, ladder2, ladder3
        return(self.l)

    def play(self):
        '''Creates the play main loop method.
        Paramaters:
        '''
        
        
        print("play working")
        self.screen.listen()
        self.screen.update()
        self.screen.mainloop()      
          
    def villain(self):
        '''Creates the villains
        Paramaters:
        '''
        
        
        villain = turtle.Turtle()
        self.screen.register_shape('minion.gif')
        villain.shape('minion.gif')
        villain.penup()
        villain.goto(-395,340)
        self.villain = villain
        return(self.villain)
    
    def barrel(self):
        '''Creates the barrel objects:
        Paramaters:
        ''' 
        
        
        barrel = self.barrel1
        self.screen.register_shape('barrell.gif')
        barrel.shape('barrell.gif')
        barrel.penup()        
        barrel.goto(-150,290)
        self.barrel = barrel
        
        return(self.barrel)  
    
    def barrel2(self):
        '''Creates the barrel objects:
        Paramaters:
        ''' 
        
        
        barrel2 = self.bar2
        self.screen.register_shape('barrell.gif')
        barrel2.shape('barrell.gif')
        barrel2.penup()        
        barrel2.goto(-150,290)
        self.barrel2 = barrel2
        return(self.barrel2)  
            
    def createGameScreenEvents(self):
        '''Creates the game screen events.
        Paramaters:
        '''
        
        
        self.screen.onkeypress(self.moveright, "Right")
        self.screen.onkeypress(self.runEnd, "q")
        self.screen.onkeypress(self.runWin, "r")
        self.screen.onkeypress(self.moveleft, "Left") 
        self.screen.onkeypress(self.jump, "Up") 
        self.screen.onkeypress(self.jump, "space") 
        self.screen.ontimer(self.player_collide_ladder, 50) 
        self.screen.update()
     
    def runEnd(self):
        '''Runs the end screen event.
        Paramaters
        '''
        
        
        self.screen.clear()
        e = End()
        e.play()
        
    def runWin(self):
        '''Runs the end screen event.
        Paramaters
        '''
        
        
        self.screen.clear()
        t = WinScreen()
        t.play()
        
    
    def moveright(self):
        '''Moves the player character right.
        Paramaters:
        '''
        
        
        self.p.setheading(0)
        self.p.forward(self.speed)
    
    def moveleft(self):
        '''Moves the player character left
        Paramaters:
        '''
        
        
        self.p.setheading(180)
        self.p.forward(self.speed)
        
    def jump(self):
        '''Makes the player character jump.
        Paramaters:
        '''
        
        
        self.p.setheading(90)
        self.p.forward(80)
        self.screen.ontimer(self.jump_down, 2000)
        
    def jump_down(self):
        '''Moves the player character down after the jump.
        Paramaters:
        '''
        
        
        self.p.setheading(270)
        self.p.forward(80)
    
    def player_collide_ladder(self):
        '''Moves the characters and objects movements when they collide with the ladder objects.
        Paramaters:
        '''
    
    
        b = self.b.pos()   
        b2 = self.b2.pos()
        self.b.goto(b[0]+self.direction*20,b[1])
        self.b2.goto(b2[0]+self.direction2*50,b2[1])
        
        #Change player shape
        if self.p.heading()==0:
            self.p.shape('sonic.gif')
        elif self.p.heading()== 180:
            self.p.shape('leftsonic.gif')

        #Player collisions with the ladder
        if self.p.pos() == (550, -420):
            self.p.shape('leftsonic.gif')
            self.p.goto(550, -155)
        elif self.p.pos() == (-550.00, -155.00):
            self.p.shape('sonic.gif')
            self.p.goto(-550, 85)
        elif self.p.pos() == (550.00, 85.00):
            self.p.shape('leftsonic.gif')
            self.p.goto(550.00, 290.00)
        elif self.p.pos() == (600, -155):
            self.p.shape('sonic.gif')
            self.p.goto(500, -420)
        elif self.p.pos() == (-600.00, 85.00):
            self.p.goto(-400.00, -155)
        elif self.p.pos() == (600, 290):
            self.p.goto(550, 85)

        #Player barrel collision.
        if self.p.distance(self.b) <= self.collision_radius or self.p.distance(self.b2) <= self.collision_radius:
            self.screen.clear()
            e = End()
            e.play()
       
        #Player collision with Villain.
        if self.p.pos() == (-390,290): 
            self.screen.clear()
            w = WinScreen()
            w.play()
            
        #barrel collision with ladder.
        if self.b.pos() == (-550, 85):
            self.b.goto(-550, -155)
            self.direction = self.direction * -1
        elif self.b.pos() == (550, -155):
            self.b.goto(550, -420)
            self.direction = self.direction * -1
        elif self.b.pos() == (-550, -420):
            self.b.goto(-150,290)
            self.direction = self.direction * -1   
        elif self.b.pos() == (550, 290):
            self.b.goto(550, 85)
            self.direction = self.direction * -1
        elif self.b.pos() == (550, 290):
            self.b.goto(550, 85)
            self.direction = self.direction * -1 
        elif self.b.pos() == (-550, 85):
            self.b.goto(-550, -155)
            self.direction = self.direction * -1
        elif self.b.pos() == (550, -155):
            self.b.goto(550, -420)
            self.direction = self.direction * -1
        elif self.b.pos() == (-550, -420):
            self.b.goto(-150,290)
            self.direction = self.direction * -1  
        elif self.b.pos() == (550, 290):
            self.b.goto(550, 85)
            self.direction = self.direction * -1
            
        #barrel2 collision with ladder
        if self.b2.pos() == (-550, 85):
            self.b2.goto(-550, -155)
            self.direction2 = self.direction2 * -1
        elif self.b2.pos() == (550, -155):
            self.b2.goto(550, -420)
            self.direction2 = self.direction2 * -1
        elif self.b2.pos() == (-550, -420):
            self.b2.goto(-150,290)
            self.direction2 = self.direction2 * -1
        elif self.b2.pos() == (550, 290):
            self.b2.goto(550, 85)
            self.direction2 = self.direction2 * -1
        elif self.b2.pos() == (550, 290):
            self.b2.goto(550, 85)
            self.direction2 = self.direction2 * -1  
        elif self.b2.pos() == (-550, 85):
            self.b2.goto(-550, -155)
            self.direction2 = self.direction2 * -1
        elif self.b2.pos() == (550, -155):
            self.b2.goto(550, -420)
            self.direction2 = self.direction2 * -1
        elif self.b2.pos() == (-550, -420):
            self.b2.goto(-150,290)
            self.direction2 = self.direction2 * -1  
        elif self.b2.pos() == (550, 290):
            self.b2.goto(550, 85)
            self.direction2 = self.direction2 * -1
        self.screen.ontimer(self.player_collide_ladder, 250)    
        self.screen.update() 
         
class End(Game):
    screen = Title.screen
    turtleDrawer = turtle.Turtle()
        
    def __init__(self):
        '''Creates the instance variables for the end screen class.
        Paramaters:
        '''
        
        
        super().__init__()
        self.background()
        self.t = self.titleScreen()
        
    def background(self):
        '''Creates the background of the screen.
        Paramaters:
        '''
        
        
        self.bg = turtle.Turtle()
        self.screen.register_shape('loosescreen.gif')
        self.bg.shape('loosescreen.gif')
        self.bg.penup()
           
    def titleScreen(self):
        '''Creates the title screen.
        Paramaters:
        '''
            
            
        self.turtleDrawer.penup()
        self.screen.bgcolor("red")
        self.screen.tracer(0)   
        self.button = Game.Button(Title.turtleDrawer, 100, 100, 200, 0, "Click Me\nTo Start", borderColor="Red", 
            fillColor="Yellow", fontColor="Blue", fontSize=13)
        self.quitButton = Game.Button(Title.turtleDrawer, -200, 100, -100, 0, "Click Me\nTo Quit", borderColor="Red", 
            fillColor="Yellow", fontColor="Blue", fontSize=13)

    def createTitleScreenEvents( mouse_X, mouse_Y):  
        '''Creates the title screen events.
        Paramaters:
        '''
            
            
        button = Game.Button(Title.turtleDrawer, 100, 100, 200, 0, "Click Me\nTo Start Over", borderColor="Red", 
            fillColor="Green", fontColor="Blue", fontSize=13)
        quitButton = Game.Button(Title.turtleDrawer, -200, 100, -100, 0, "Click Me\nTo Quit", borderColor="Red", 
            fillColor="Green", fontColor="Blue", fontSize=13)
        if button.pointInside(mouse_X, mouse_Y):
            print("Button clicked!")
            End.screen.clear()
            e = End()
            e.screen
        elif quitButton.pointInside( mouse_X, mouse_Y):
            Title.screen.exitonclick()

    def play(self):
        '''Creates the play main loop method.
        Paramaters:
        '''
        
        
        self.screen.onclick(Title.createTitleScreenEvents)
        self.screen.listen()
        turtle.done()
          
class WinScreen(Game):
    screen = Title.screen
    turtleDrawer = turtle.Turtle()
        
    def __init__(self):
        '''Creates the instance variables for the end screen class.
        Paramaters:
        '''
        
        
        super().__init__()
        self.background()
        self.t = self.titleScreen()

    def titleScreen(self):
        '''Creates the title screen.
        Paramaters:
        '''
            
            
        self.turtleDrawer.penup()
        self.screen.bgcolor("yellow")
        self.screen.tracer(0)   
        self.button = Game.Button(Title.turtleDrawer, 100, 100, 200, 0, "Click Me\nTo Start", borderColor="Red", 
            fillColor="Yellow", fontColor="Blue", fontSize=13)
        self.quitButton = Game.Button(Title.turtleDrawer, -200, 100, -100, 0, "Click Me\nTo Quit", borderColor="Red", 
            fillColor="Yellow", fontColor="Blue", fontSize=13)

    def createTitleScreenEvents( mouse_X, mouse_Y):  
        '''Creates the title screen events.
        Paramaters:
        '''
            
            
        button = Game.Button(Title.turtleDrawer, 100, 100, 200, 0, "Click Me\nTo Start Over", borderColor="Red", 
            fillColor="Green", fontColor="Blue", fontSize=13)
        quitButton = Game.Button(Title.turtleDrawer, -200, 100, -100, 0, "Click Me\nTo Quit", borderColor="Red", 
            fillColor="Green", fontColor="Blue", fontSize=13)
        if button.pointInside(mouse_X, mouse_Y):
            print("Button clicked!")
            End.screen.clear()
            e = End()
            e.screen
        elif quitButton.pointInside( mouse_X, mouse_Y):
            Title.screen.exitonclick()

    def play(self):
        '''Creates the play main loop method.
        Paramaters:
        '''
        
        
        self.screen.onclick(Title.createTitleScreenEvents)
        self.screen.listen()
        turtle.done()
    
    def background(self):
        '''Creates the background of the screen.
        Paramaters:
        '''
        
        
        self.bg = turtle.Turtle()
        self.screen.register_shape('winscreen.gif')
        self.bg.shape('winscreen.gif')
        self.bg.penup()
                   
if __name__ == "__main__":
    #creates and makes the game.
    
   l = Title()
   l.play()
   