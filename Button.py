import pygame


# The Button class is a class that creates a button object that can be drawn to the screen
class Button:
    # Constructor
    def __init__(self, pos_x, pos_y, width, height):
        """
        The function takes in the position of the object, the width and height of the object, and then creates a rectangle
        object with the given parameters

        :param pos_x: The x position of the top left corner of the rectangle
        :param pos_y: The y-coordinate of the top of the rectangle
        :param width: The width of the rectangle
        :param height: The height of the rectangle
        """
        self.rect = pygame.Rect(pos_x, pos_y, width, height)
        self.rect.center = (pos_x, pos_y)

    # Drawing button
    def draw(self, surface, color, thickness, corner, font, text_size, text_color, text):
        """
        This function draws a button with a given color, thickness, corner, font, text size, text color, and text

        :param surface: the surface you want to draw the button on
        :param color: the color of the button
        :param thickness: the thickness of the button outline
        :param corner: the radius of the rounded corners
        :param font: The font of the text
        :param text_size: The size of the text on the button
        :param text_color: The color of the text on the button
        :param text: the text that will be displayed on the button
        """
        # drawing button outline
        pygame.draw.rect(surface, color, self.rect, thickness, corner)

        # text for button
        button_font = pygame.font.SysFont(font, text_size)
        text_width, text_height = button_font.size(text)

        button_name = button_font.render(text, True, text_color)

        text_x = self.rect.x + ((self.rect.width - text_width) / 2)
        text_y = self.rect.y + ((self.rect.height - text_height) / 2)

        # drawing the button and button text
        surface.blit(button_name, (text_x, text_y))


# import pygame
#
#
# class Button:
#     # Constructor
#     def __init__(self, pos_x, pos_y, width, height):
#         self.rect = pygame.Rect(pos_x, pos_y, width, height)
#         self.rect.center = (pos_x, pos_y)
#
#     # Drawing button
#     def draw(self, surface, color, thickness, corner, font, text_size, text_color, text):
#         # drawing button outline
#         pygame.draw.rect(surface, color, self.rect, thickness, corner)
#
#         # text for button
#         button_font = pygame.font.SysFont(font, text_size)
#         text_width, text_height = button_font.size(text)
#
#         button_name = button_font.render(text, True, text_color)
#
#         text_x = self.rect.x + ((self.rect.width - text_width) / 2)
#         text_y = self.rect.y + ((self.rect.height - text_height) / 2)
#
#         # drawing the button and button text
#         surface.blit(button_name, (text_x, text_y))
