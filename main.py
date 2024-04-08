import math

from PIL import Image, ImageDraw, ImageFont
import pandas as pd

from one_image.one_image import create_card_with_one_image
from two_image.two_image import create_card_with_two_image
from downloading import download_image


def read_excel(excel_path: str):
    df = pd.read_excel(excel_path)
    df['class_info'] = df['class_info'].fillna("")
    df['age_or_class'] = df['age_or_class'].fillna("")
    df['quantity'] = df['quantity'].fillna("")

    return df


if __name__ == "__main__":
    excel_path = "Тест_книги (1) (1).xlsx"
    # book_image_path = "/Users/rrkhikmatullin/Downloads/2.png"
    # main_title = "АНГЛИЙСКИЙ ЯЗЫК\n Spotlight"
    # type_of_book = "Рабочая тетрадь"
    # output_path = 'card_picture.png'
    # class_info = '2'
    # create_card(book_image_path, main_title, type_of_book, class_info, age_or_class, output_path)
    df = read_excel(excel_path)
    for book_path_1, book_path_2, main_title, type_of_book, class_info, age_or_class, output_path, quantity, template in zip(
            df['book_path_1'],
            df['book_path_2'],
            df['main_title'],
            df['type_of_book'],
            df['class_info'],
            df['age_or_class'],
            df['output_path'],
            df['quantity'],
            df['template']):
        main_title = main_title.replace("\\n", "\n")
        type_of_book = type_of_book.replace("\\n", "\n")

        # # Example float value that may contain NaN
        # if math.isnan(quantity):
        #     # Handle the case where the value is NaN
        #     quantity = 0
        # else:
        #     # Convert the float value to an integer
        #     int_value = int(quantity)

        if "/Users/rrkhikmatullin" in book_path_1:
            if template == 1:
                create_card_with_one_image(book_path_1, main_title, type_of_book, class_info, age_or_class, output_path,
                                           quantity)
            if template == 2:
                create_card_with_two_image(book_path_1, book_path_2, main_title, type_of_book, class_info, age_or_class,
                                           output_path,
                                           quantity)
        if "https://basket" in book_path_1:
            file_path = f'src/{main_title}.png'
            download_image(book_path_1, file_path)
            book_path_1 = file_path

            if template == 1:
                create_card_with_one_image(book_path_1, main_title, type_of_book, class_info, age_or_class, output_path,
                                           quantity)
            if template == 2:
                create_card_with_two_image(book_path_1, book_path_2, main_title, type_of_book, class_info, age_or_class,
                                           output_path,
                                           quantity)
