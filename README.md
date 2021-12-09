# pyglphys
A OpenGL based game engine in Python

# What is it?
pyglphys is a package that has classes to create and interact with objects, and draw them with pyOpenGL.
As of now, it only supports basic ortholinear 2d objects. Most of the physics have to be implemented manually.

## How do I use it?
You will need pyOpenGL package. You can get it from the documentation [here](http://pyopengl.sourceforge.net/documentation/index.html), or use `pip`.
After that, drag the `pyglphys` folder into your working directory, and import as a package. 
You can look at some of the examples to understand how the package is used.

## What can it do?
Right now, not very much, but do feel free to modify and improve the(honestly terrible) code. For major changes, raise a issue and create a new pull request.

### Functionality
>class `particle2d` - A basic 2d point object, drawn as a GL_POINTS entity. It has 7 attributes- `x`, `y`, `vx`, `vy`, `ax`, `ay`, and `size` . THeese are the conponents of position, velocity and acceleration respectively|

>class `paddle2d` - Simple 2d rectagular body, with center position, x and y sizes ad attributes, aside from the same motion parameters as in `particle2d`. Used in much the same way, only drawn very differently|
