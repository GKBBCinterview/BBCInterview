Notes on design:

Grid is initialised based on defining certain coordinates as containing cells. Two options are present, one for a glider and one for a blinker, which can be activated by commenting out the appropriate lines. Improved functionality may include a more user friendly way to input initial cells, or having more predefined patterns to load.

The grid is taken as infinite and loops at the edges. This could be improved by allowing user to choose between the infinite looping grid and a "dead-zone" or similar around the edges.

The output prints a simple textual representation of the grid to the console at each iteration. This could be expanded to have an automatically generated, animated graphical output, or enabling time controls between iterations to more clearly see how the patterns evolve.

The rules of the game are applied on line 59. This one line summarises all the potential outcomes and gives the appropriate result. This has the benefit of brevity but a construct such as a series of if-else statements may improve readability and more flexibility if, for example, a user wished to change or add additional rules.