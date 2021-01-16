controller.A.onEvent(ControllerButtonEvent.Pressed, function on_a_pressed() {
    
    Wind_bullets = sprites.createProjectileFromSprite(img`
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . d d d . . . . . . . . . . 
                    . . . d d d d . . . . . . . . . 
                    . . . d d d d d d d . . . . . . 
                    . . . d d d d . . . . . . . . . 
                    . . . d d d . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . .
        `, bigBat, 200, 0)
})
sprites.onOverlap(SpriteKind.Projectile, SpriteKind.Enemy, function on_on_overlap(sprite: Sprite, otherSprite: Sprite) {
    otherSprite.destroy()
    sprite.destroy(effects.fire, 100)
    info.changeScoreBy(1)
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Enemy, function on_on_overlap2(sprite: Sprite, otherSprite: Sprite) {
    otherSprite.destroy()
    info.changeLifeBy(-1)
})
let crazyBat : Sprite = null
let Wind_bullets : Sprite = null
let bigBat : Sprite = null
bigBat = sprites.create(img`
        . . f f f . . . . . . . . f f f 
            . f f c c . . . . . . f c b b c 
            f f c c . . . . . . f c b b c . 
            f c f c . . . . . . f b c c c . 
            f f f c c . c c . f c b b c c . 
            f f c 3 c c 3 c c f b c b b c . 
            f f b 3 b c 3 b c f b c c b c . 
            . c 1 b b b 1 b c b b c c c . . 
            . c 1 b b b 1 b b c c c c . . . 
            c b b b b b b b b b c c . . . . 
            c b 1 f f 1 c b b b b f . . . . 
            f f 1 f f 1 f b b b b f c . . . 
            f f 2 2 2 2 f b b b b f c c . . 
            . f 2 2 2 2 b b b b c f . . . . 
            . . f b b b b b b c f . . . . . 
            . . . f f f f f f f . . . . . .
    `, SpriteKind.Player)
bigBat.setFlag(SpriteFlag.StayInScreen, true)
info.setLife(3)
controller.moveSprite(bigBat, 200, 200)
game.onUpdateInterval(500, function on_update_interval() {
    
    crazyBat = sprites.create(img`
            ........................
                    ........................
                    ........................
                    ..........ffff..........
                    ........ff1111ff........
                    .......fb111111bf.......
                    ......fbd1111111f.......
                    ......fdd1111111df......
                    ......fddd111111df......
                    ......fdddddd111df......
                    ......fdddddd111df......
                    ......fbddddddd1df......
                    ......ffbbddbfd1df......
                    .......fcbbdcfddbf......
                    .......fffbddccffff.....
                    .......ffffcfbbb1bcf....
                    ......ffffffffcd1b1f....
                    ...ffffffffff..fdfdf....
                    .....ffffff.....f.f.....
                    ........................
                    ........................
                    ........................
                    ........................
                    ........................
        `, SpriteKind.Enemy)
    crazyBat.setVelocity(-100, 0)
    crazyBat.left = scene.screenWidth()
    crazyBat.y = randint(0, scene.screenHeight())
    crazyBat.setFlag(SpriteFlag.AutoDestroy, true)
})
