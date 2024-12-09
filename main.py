from gui import Display
from grid import Grid


display = Display()
game = Grid()


def event_handler(event):
    if game.is_paused:
        if event.keysym == 'space':
            game.new_grid()
            game.unpause()
            display.update_numbers(game.grid)
            display.text.hide()
        return

    if game.merge_numbers(event.keysym):
        game.spawn_number()
        game.check_milestone()

    if game.is_stuck():
        game.pause()
        display.text.show()
        print("Game Over! Press SPACE to play again.")

    display.update_numbers(game.grid)
        

display.bind_handler(event_handler)
display.update_numbers(game.grid)
display.mainloop()
