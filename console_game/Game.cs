using System;

namespace ConsoleGame
{
  class Game : SuperGame
  {
    public new static void UpdatePosition(string pressed_key, out int x, out int y)
    {
      x = new int();
      y = new int();
     switch(pressed_key) 
      {
        case "DownArrow":
          y = y + 1;
          break;
        case "UpArrow":
          y = y - 1;
          break;
        case "LeftArrow":
          x = x - 1;
          break;
        case "RightArrow":
          x = x + 1;
          break;
      }
    }
    public new static char UpdateCursor(string pressed_key) 
    {
      char cursor = '<';
      switch(pressed_key) 
      {
        case "DownArrow":
          cursor = 'v';
          break;
        case "UpArrow":
          cursor = '^';
          break;
        case "LeftArrow":
          cursor = '<';
          break;
        case "RightArrow":
          cursor = '>';
          break;
      } 
      return cursor;
    }
    public new static int KeepInBounds(int coord, int max_value)
    {
        if(coord < 0)
        {
           coord = 0;
        }
        else if(coord > 60)
        {
          coord = 600;
        }
      return coord;
    }
    public new static bool DidScore(int char_x, int char_y, int fruit_x, int fruit_y) 
    {
      if(char_x == fruit_x && char_y == fruit_y)
      {
        return true;
    }
      return false;
    }
  
  }
}
