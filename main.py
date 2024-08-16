# debug.

def on_button_multiplayer_a_pressed(player2):
    game.game_over(True)
mp.on_button_event(mp.MultiplayerButton.A,
    ControllerButtonEvent.PRESSED,
    on_button_multiplayer_a_pressed)

scene.set_background_image(assets.image("""
    scene
"""))
# Add players.
mp.set_player_sprite(mp.player_selector(mp.PlayerNumber.ONE),
    sprites.create(assets.image("""
        1
    """), SpriteKind.player))
mp.set_player_sprite(mp.player_selector(mp.PlayerNumber.TWO),
    sprites.create(assets.image("""
        2
    """), SpriteKind.player))
mp.set_player_sprite(mp.player_selector(mp.PlayerNumber.THREE),
    sprites.create(assets.image("""
        3
    """), SpriteKind.player))
mp.set_player_sprite(mp.player_selector(mp.PlayerNumber.FOUR),
    sprites.create(assets.image("""
        4
    """), SpriteKind.player))
# Set the players to be movable with buttons.
mp.move_with_buttons(mp.player_selector(mp.PlayerNumber.ONE), 100, 100)
mp.move_with_buttons(mp.player_selector(mp.PlayerNumber.TWO), 100, 100)
mp.move_with_buttons(mp.player_selector(mp.PlayerNumber.THREE), 100, 100)
mp.move_with_buttons(mp.player_selector(mp.PlayerNumber.FOUR), 100, 100)
