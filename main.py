from init import *


# Цикл игры
running = True
while running:
    # держим цикл на правильной скорости
    clock.tick(FPS)

    # Название окна
    pygame.display.set_caption('Simon')

    if game:
        if tile_table.check():
            tile_table.clear()
            game_round = False
            level += 1
            tile_table.create_picture(level)

        if not game_round:
            if showing_timer == 0:
                showing_timer = 180
                level_message.set_message("LEVEL: " + str(level))
            if showing_timer == 179:
                tile_table.show()
            if showing_timer == 1:
                tile_table.hide()
                game_round = True
            showing_timer -= 1

    # Ввод процесса (события)
    for event in pygame.event.get():
        # проверить закрытие окна
        if event.type == pygame.QUIT:
            running = False
        if showing_timer == 0:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if game:
                    tile_panel.choose_color(event)
                    chosen_color_ind = tile_panel.get_chosen_color()
                    game = tile_table.choose_tile(event, chosen_color_ind)
                else:
                    if yes_message.rect.collidepoint(event.pos):
                        level = 0
                        tile_table.clear()
                        game = True
                    elif no_message.rect.collidepoint(event.pos):
                        running = False

    # Обновление
    all_sprites.update()
    screen.fill(LIGHT_GREY)
    all_sprites.draw(screen)
    if tile_panel.chosen_color is not None:
        tile_panel.frame.draw(tile_panel.chosen_color.rect.topleft)
    if not game:
        gio_message.draw()
        pa_message.draw()
        yes_message.draw()
        no_message.draw()
        yes_message.update(PURPLE)
        no_message.update(PURPLE)
    level_message.set_message("LEVEL: " + str(level))
    level_message.draw()

    # Визуализация (сборка)
    pygame.display.flip()

pygame.quit()
