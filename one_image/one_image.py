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


def create_card_with_one_image(book_image_path: str, main_title: str, type_of_book: str, class_info: str,
                               age_or_class: str, output_path: str):
    #  BACKGROUND
    width = 1200
    height = 1600
    color1 = (240, 124, 223)  # фиолетовый
    color2 = (120, 85, 150)
    fill1 = (217, 148, 230)

    # color1 = (100, 124, 200) # немного темно синий
    # color2 = (120, 85, 150)
    fill2 = (150, 148, 200)

    # Создаем градиентное изображение
    gradient_image = create_gradient(width, height, color1, color2)
    # Сохраняем изображение
    gradient_image.save("gradient.png")

    #  BOOK picture
    X = 180
    image_path = book_image_path
    book_image = Image.open(image_path).convert('RGBA')
    book_width, book_height = book_image.size
    print(f"Width = {book_width}, Height = {book_height}")
    book_image_resized = book_image.resize((3 * X, 4 * X), resample=Image.LANCZOS)

    # Создание макета коллажа
    MAIN_PAGE = gradient_image

    # Размещение изображений на макете
    MAIN_PAGE.paste(book_image_resized, (230, 530))

    MAIN_PAGE_rot = MAIN_PAGE.rotate(5, expand=True, resample=Image.BICUBIC)
    cropped_image = MAIN_PAGE_rot.crop((150, 200, 1050, 1400))

    font_main_title = ImageFont.truetype(
        '/Users/rrkhikmatullin/Downloads/Oswald,Roboto_Condensed/Oswald/Oswald-VariableFont_wght.ttf',
        size=80)

    font_class = ImageFont.truetype(
        '/Users/rrkhikmatullin/Library/Fonts/Roboto_Condensed/RobotoCondensed-Italic-VariableFont_wght.ttf',
        size=130)

    font_class_text = ImageFont.truetype(
        '/Users/rrkhikmatullin/Library/Fonts/Roboto_Condensed/RobotoCondensed-Italic-VariableFont_wght.ttf',
        size=70)

    font_type_of_book = ImageFont.truetype(
        '/Users/rrkhikmatullin/Library/Fonts/Roboto_Condensed/RobotoCondensed-Italic-VariableFont_wght.ttf',
        size=55)

    draw = ImageDraw.Draw(cropped_image)
    # main title
    draw.multiline_text((450, 100), f"{main_title}", font=font_main_title, align='center', anchor='mm')
    # rectangle for type of book
    draw.rounded_rectangle((40, 220, 860, 320), radius=20, fill=fill1)
    draw.multiline_text((450, 270), f"{type_of_book}", font=font_type_of_book, align='center', anchor='mm')
    # class info
    draw.text((800, 400), f"{class_info}", font=font_class, align='center', anchor='mm')
    draw.text((800, 500), f"{age_or_class}", font=font_class_text, align='center', anchor='mm')

    # icon
    # icon_image = Image.open('/Users/rrkhikmatullin/Desktop/Снимок экрана 2024-04-06 в 16.14.38.png')
    # print(icon_image.size)
    # cropped_image.paste(icon_image, (0, 0))

    cropped_image.save(f"{output_path}.png")
