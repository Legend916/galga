def on_a_pressed():
    global Wind_bullets
    Wind_bullets = sprites.create_projectile_from_sprite(img("""
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
        """),
        bigBat,
        200,
        0)
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_on_overlap(sprite, otherSprite):
    otherSprite.destroy()
    sprite.destroy(effects.fire, 100)
    info.change_score_by(1)
sprites.on_overlap(SpriteKind.projectile, SpriteKind.enemy, on_on_overlap)

def on_on_overlap2(sprite, otherSprite):
    otherSprite.destroy()
    info.change_life_by(-1)
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_on_overlap2)

crazyBat: Sprite = None
Wind_bullets: Sprite = None
bigBat: Sprite = None
bigBat = sprites.create(img("""
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
    """),
    SpriteKind.player)
bigBat.set_flag(SpriteFlag.STAY_IN_SCREEN, True)
info.set_life(3)
controller.move_sprite(bigBat, 200, 200)

def on_update_interval():
    global crazyBat
    crazyBat = sprites.create(img("""
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
        """),
        SpriteKind.enemy)
    crazyBat.set_velocity(-100, 0)
    crazyBat.left = scene.screen_width()
    crazyBat.y = randint(0, scene.screen_height())
    crazyBat.set_flag(SpriteFlag.AUTO_DESTROY, True)
game.on_update_interval(500, on_update_interval)
