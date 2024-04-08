from PIL import ImageFont, Image, ImageDraw


def create_gradient(width, height, color1, color2):
    # Создаем новое изображение
    gradient = Image.new('RGB', (width, height), color1)

    # Создаем объект ImageDraw
    draw = ImageDraw.Draw(gradient)

    # Создаем градиентный прямоугольник
    for y in range(height):
        # Вычисляем цвет пикселя в строке с использованием линейного градиента между color1 и color2
        alpha = y / height
        r = int(color1[0] * (1 - alpha) + color2[0] * alpha)
        g = int(color1[1] * (1 - alpha) + color2[1] * alpha)
        b = int(color1[2] * (1 - alpha) + color2[2] * alpha)
        color = (r, g, b)

        # Рисуем горизонтальную линию пикселей с цветом color
        draw.line((0, y, width, y), fill=color)

    return gradient


def create_card_with_two_image(book_image_path_1: str, book_image_path_2: str, main_title: str, type_of_book: str,
                               class_info: str,
                               age_or_class: str, output_path: str,  quantity: int = 0):
    #  BACKGROUND
    width = 1200
    height = 1600
    color1 = (172, 222, 255)  # фиолетовый
    color2 = (135, 215, 228)
    fill1 = (136, 197, 206)

    # color1 = (100, 124, 200) # немного темно синий
    # color2 = (120, 85, 150)
    fill2 = (150, 148, 200)

    # Создаем градиентное изображение
    gradient_image = create_gradient(width, height, color1, color2)
    # Сохраняем изображение
    gradient_image.save("two_image/gradient.png")

    #  BOOK picture
    X = 160
    image_path_2= book_image_path_2
    book_image_2 = Image.open(image_path_2).convert('RGBA')
    book_width, book_height = book_image_2.size
    print(f"Width = {book_width}, Height = {book_height}")
    book_image_resized_2 = book_image_2.resize((3 * X, 4 * X), resample=Image.LANCZOS)

    # Создание макета коллажа
    MAIN_PAGE = gradient_image

    # Размещение изображений на макете
    MAIN_PAGE.paste(book_image_resized_2, (540, 630))

    MAIN_PAGE_rot = MAIN_PAGE.rotate(-7, expand=True, resample=Image.BICUBIC)
    cropped_image = MAIN_PAGE_rot.crop((250, 200, 1150, 1400))

    font_main_title = ImageFont.truetype(
        '/Users/rrkhikmatullin/Downloads/Oswald,Roboto_Condensed/Oswald/Oswald-VariableFont_wght.ttf',
        size=80)

    font_class = ImageFont.truetype(
        '/Users/rrkhikmatullin/Library/Fonts/Roboto_Condensed/RobotoCondensed-Italic-VariableFont_wght.ttf',
        size=140)

    font_class_text = ImageFont.truetype(
        '/Users/rrkhikmatullin/Library/Fonts/Roboto_Condensed/RobotoCondensed-Italic-VariableFont_wght.ttf',
        size=70)

    font_type_of_book = ImageFont.truetype(
        '/Users/rrkhikmatullin/Library/Fonts/Roboto_Condensed/RobotoCondensed-Italic-VariableFont_wght.ttf',
        size=55,)

    draw = ImageDraw.Draw(cropped_image)

    ## second image
    image_path_1 = book_image_path_1
    book_image_1 = Image.open(image_path_1).convert('RGBA')
    book_width, book_height = book_image_1.size
    print(f"Width = {book_width}, Height = {book_height}")
    book_image_resized_1 = book_image_1.resize((3 * X, 4 * X), resample=Image.LANCZOS)

    # Размещение изображения 2 на макете
    cropped_image.paste(book_image_resized_1, (70, 350))


    # main title
    draw.multiline_text((450, 70), f"{main_title}", font=font_main_title, align='center', anchor='mm')
    # rectangle for type of book
    rectangle_height_1 = 130
    rectangle_height_2 = 230
    draw.rounded_rectangle((40, rectangle_height_1, 860, rectangle_height_2), radius=20, fill=fill1)
    draw.multiline_text((450, (rectangle_height_1 + rectangle_height_2)//2), f"{type_of_book}", font=font_type_of_book,
                        align='center', anchor='mm')
    print(quantity)
    ## Komplekt
    if quantity:
        draw.rounded_rectangle((200, rectangle_height_2 + 20, 700, rectangle_height_2 + 100), radius=20, fill=fill2)
        draw.multiline_text((450, rectangle_height_2 + 60), f"{int(quantity)} КОМПЛЕКТОВ",
                            font=font_type_of_book,
                            align='center', anchor='mm')
    # class info
    class_height = 350
    draw.text((800, class_height), f"{class_info}", font=font_class, align='center', anchor='mm')
    draw.text((800, class_height + 100), f"{age_or_class}", font=font_class_text, align='center', anchor='mm')

    # icon
    # icon_image = Image.open('/Users/rrkhikmatullin/Desktop/Снимок экрана 2024-04-06 в 16.14.38.png')
    # print(icon_image.size)
    # cropped_image.paste(icon_image, (0, 0))

    cropped_image.save(f"finish/2/{output_path}.png")


if __name__ == '__main__':
    book_1 = "two_image/1_part.png"
    book_2 = "two_image/2_part.png"
    main_title = "ОКРУЖАЮЩИЙ МИР"
    type_of = "Рабочая тетрадь"
    class_info = "2"
    age_or_class = "класс"
    output_path = "two_image/finish"
    # book_image = Image.open(book_1).convert('RGBA')
    # book_width, book_height = book_image.size
    # print(f"Width = {book_width}, Height = {book_height}")
    create_card_with_two_image(book_1, book_2, main_title, type_of, class_info, age_or_class, output_path, 10)