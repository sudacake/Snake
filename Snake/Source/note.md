# main
### missions
* ##### Initialize the **pygame**
* ##### Initialize **screen** size and caption
* ##### Enter the **game loop**
***

* Initialize the **pygame**
```python
pygame.init()
```
* Initialize **screen** size and caption
```python
screen = pygame.display.set_mode((GameState.screen_width, GameState.screen_height))
```
* Enter the **game loop**
```python
pygame.display.set_caption('Snake')
```

## the game loop
* #### missions
* ##### get **pygame event**
* ##### **erase screen**
* ##### **update the contents of the entire display**
***

* get **pygame event**
See check_events() in functions

* **erase screen**
See update_screen(screen) in functions

* **update the contents of the entire display**
```python
pygame.display.flip()
```

# settings
### missions
* ##### Set **game parameters** and Serving **game_state**
***
* screen
```python
screen_width = 800
screen_height = 800
screen_background_color = 255, 255, 255
```

# game_state
##### missions:
Get a copy of the **Settings** at the beginning of the game
My approach is to **GameState** inherit **Settings**
**In the game, we will not make any changes to the data in the settings, the changes are implemented in the game_state**
***
```python
from settings import Settings


class GameState(Settings):
    pass
```
So, its code is very simple.

# functions
##### missions: Handling game events
* ##### check_events()
* ##### update_screen(screen)
***
* check_events()
```python
def check_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
```

* update_screen(screen)
```python
def update_screen(screen):
    screen.fill(GameState.screen_background_color)
```