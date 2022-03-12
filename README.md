# Conway's game of life

## Description

This is my attempt to code the "zero-player game", [Conway's Game of Life.](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life)

![gosper_glider_gun](https://conwaylife.com/w/images/b/b6/Gosperglidergun.gif)

The game is displayed as a grid of 1s and 0s in the console. A feature to be added is an easier-to-view UI.

## Rules of the "game"
In a grid of cells..

- Each cell with one or no neighbours dies, as if by solitude
- Each cell with four or more neighbours dies, as if by overpopulation
- Each cell with two or three neighbors survives.
- Each cell with three neighbours becomes populated.

## Usage

Navigate to the project directory, start the python3 console and load up the "tabletop".

```bash
python3 -i tabletop.py
```

---

To save a game setup, pass the arguments to the Game class:

 - width of board 
 - height of board
 - start positions (2D array of indices, each represents a live cell start position)

```python
# This will generate grid 18 wide and 11 cells high with starting positions triggering an oscillator pattern!

game_setup = Game(18, 11, [
  [4,6], [4,11], 
  [5,4], [5,5], [5,7], [5,8], [5,9], [5,10], [5,12], [5,13],
  [6,6], [6,11]
]) 
```

To start the game, simply call the `.play()` method on the game setup with the following arguments

- steps (how many "frames" you want the game to run for)
- time interval in seconds (default is 0.1 seconds)

```python
# This will step through 75 frames at a rate of 0.2 seconds per frame

game_setup.play(75, 0.2) 
```
---

There are some demo presets available (while in the python3 console)

To see a glider move across a continuous 5x5 grid, run:

```python
glider_demo()
```

Discovered by Bill Gosper in 1970, the ["Gosper Glider Gun"](https://en.wikipedia.org/wiki/Gun_(cellular_automaton)#:~:text=Bill%20Gosper%20discovered%20the%20first,other%20rules%20had%20smaller%20guns.). Significant in that this led to the later discovery that Conway's game of life is in fact, function as a Turing Machine.
```python
gosper_gun_demo()
```
To view an example of an 'oscillator' class, "Kok's Galaxy", run:

```python
koks_galaxy_demo()
```

# Technology

Written in Python 3.9

Testing framework: unittest
