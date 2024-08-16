// debug.
mp.onButtonEvent(mp.MultiplayerButton.A, ControllerButtonEvent.Pressed, function (player2) {
    game.gameOver(true)
})
scene.setBackgroundImage(assets.image`scene`)
// Add players.
mp.setPlayerSprite(mp.playerSelector(mp.PlayerNumber.One), sprites.create(assets.image`1`, SpriteKind.Player))
mp.setPlayerSprite(mp.playerSelector(mp.PlayerNumber.Two), sprites.create(assets.image`2`, SpriteKind.Player))
mp.setPlayerSprite(mp.playerSelector(mp.PlayerNumber.Three), sprites.create(assets.image`3`, SpriteKind.Player))
mp.setPlayerSprite(mp.playerSelector(mp.PlayerNumber.Four), sprites.create(assets.image`4`, SpriteKind.Player))
// Set the players to be movable with buttons.
mp.moveWithButtons(mp.playerSelector(mp.PlayerNumber.One), 100, 100)
mp.moveWithButtons(mp.playerSelector(mp.PlayerNumber.Two), 100, 100)
mp.moveWithButtons(mp.playerSelector(mp.PlayerNumber.Three), 100, 100)
mp.moveWithButtons(mp.playerSelector(mp.PlayerNumber.Four), 100, 100)
