# Name: GraphingCalculator.py
# Author: Rodrigo Nevarez Escobar
# Modification date: February 11th, 2022
# Description: A graphing calculator that displays curves on a canvas.

from PIL import Image, ImageDraw

class GraphingCalculator():
  '''Overall class to manage calculator assets and behavior.'''

  def __init__(self):
    '''Initialize the calculator and create the calculator resources'''
    # Construct drawing canvas
    self.image = Image.new("1", (800,600), color=0)
    self.surface = ImageDraw.Draw(self.image)

  def preview(self):
    '''Display preview of the image generated on canvas.'''
    self.image.show()

  def test(self):
    '''Draw a gray cross over the canvas'''
    self.surface.line((0, 0) + self.image.size, fill=128)
    self.surface.line((0, self.image.size[1], self.image.size[0], 0), fill=128)

  def line(self, i_xy, f_xy):
    '''
    Brief: Draw a line over the canvas
    Param i_xy: Tuple containing initial coordinates.
    Param f_xy: Tuple containing final coordinates.
    ''' 

if __name__ == "__main__":
  # Make a calculator instance, run the calculator
  gc = GraphingCalculator()
  gc.test()
  gc.preview()
