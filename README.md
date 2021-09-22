# RadioTide

This was an old simple map generation project I dug up from many years ago,
originally I intended to create some type of rpg/strategy game, but I never
continued it. Still the concept and code is quite interesting, so I've left
it here for now with the intention of maybe having a look at it again in
future.

To play, simply run the shell file at the root of the project, on a Linux/Unix
based environment. There are two versions, one shell and one curses, the shell
allows for more modification of the topography density.

Running the shell version should display an output similar to below, only
in colours (if available)

```
Which version do you want? (s)hell version or (c)urses version? (c/s) s

RadTide
======

tx.Hx^x^^^..t+tTT+x^tt^..x.^^x+^^++..hxHx^h+h^^^..xx+txxHTTh
hH....^th^^....H.Ht^^^^^^...^^x^^^tT.....^T++^^^.....TtHhTtT
H.............+....^^^^^^^...x+t^^^+t....+Tt+..^.....HHhxt+T
.............+.+......^^.......hT^.^^.....t+....^^^....H~tHh
..............T........^.........^^....^^^^Tt....^^^....~+th
...............................T.^......xx^^T..x..^^..~...~~
...x..H...................+..............^Ht+.....^^+.~.....
..............^............t.....h........H~~~~h...+...~~~..
...........~~~~~~~~~...^^.................hh~~~~~^^^......~.
~~~.........~~~~~~~~~~~~~~~.......^..........~~~~~^^h~~..~~~
~~~~~~~~....~~~~~~~~~~~~~~~~~~~~..............~~~~~h^~H~~~~~
~~~~~~~~~..~..~~~~~~~~~~~~~~~~~~~~.x...........~~~~THx~Hh~~~
~~~~~~~~.~~.~~~~~~~~~~~~~~~~~~~~~~~~HH..........~~~~~~~~~~~~
~~~~~~~^.....~~~~~~~~~~~~~~~~~~~~~~~~Hh..........~~~~~~~~~~~
~~~~~~~^.....~~~~~~~~~~~~~~~~~~~~~~~~~~~..........~~~~~~~~~~
~~~~~~~^......~~~~~~~~~~~~~~~~~~~~~~~~~~~~...h...~~~~~~~~~~~
~~~~~~~~x......~~~~~~~~~~~~~~~~~~~~~~~~~~~......~~~~~~~~~~~~
~~~~~~~~Th......~~~~~~~~~~~~~~~~~~~~~~~~~~~....~..~~~~~~~~~~
~~~~~~~~~~......~~~~~~~~~~~~~~~~~~~~~~~~~~~~H...~~~~~~~~~~~~
~~~~~~~~~~~........~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~...........~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~.T.......~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~^....~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~...~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~T..~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Dimensions
height: 25 tiles
width: 60 tiles
Density
=======
density of water: 40%
density of urban: 10%
density of elevation: 35%
density of wilderness: 50%
density of foliage: 25%

Accept this map? (y)
or change density percentage? (enter density name)
or press any key to regenerate using the same values
or change dimension? (enter dimension name)
```

Todo
====
- create some standard value templates for generating certain things, i.e.
  more trees, less trees, less water, more water etc...
- there are multiple iterations of map creation, first is blatting random
  things down on the map, this does not include path (tracks, roads etc),
  the second iteration of the map should add paths, find a few spots on
  the top of the map, then go down to the next row, continue the path
  occasionally forking off and changing directions, if it encounters
  another path of the same type, then it will skip and this one will stop.
