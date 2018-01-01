![alt text](https://github.com/FabriceCastel/gvcci/blob/master/resources/gvcci-title.png "gvcci logo")

## About

This project was developed as an alternative to the commonly used tool ```wal``` which was used by many in the UNIX community to extract colors from images in order to create terminal themes that matched their wallpapers.

The main flaw with ```wal``` is that it often missed smaller pops of differentiated color within an image, leaving its results monotone & uninteresting. This project aims to remedy that by using clustering algorithms on an image's colours so that small pockets of highly differentiated colours get picked up and have a shot at making it into the final colour palette.

For some examples, check out: http://fabricecastel.github.io/colors/examples.html

The project is still very much a work in progress, with background color logic in the works so that you can choose between light, dark & custom background colors. Feel free to join in the discussion via the github issues page, or the thread on /r/unixporn [here](https://www.reddit.com/r/unixporn/comments/77iagc/writing_a_new_tool_to_extract_terminal_colour/)

## Screenshots

![alt text](https://imgur.com/RxhkRTi.jpg "sample 1")
![alt text](https://imgur.com/easDsSY.jpg "sample 2")
![alt text](https://imgur.com/RhYelGp.jpg "sample 3")
![alt text](https://imgur.com/K7Xk7RX.jpg "sample 4")

## Setup

This program has the following dependencies:

* python3
* numpy
* scikit-learn
* scikit-image
* hasel
* pystache

To setup the project and dependencies:

1. If you don't have python3 installed, you should download it here: https://www.python.org/downloads/ (3.6.3 is the most up to date version as of the writing of this readme)
2. Download & Extract (or clone) the source files from the github repo: https://github.com/FabriceCastel/gvcci
3. ```cd``` into your local copy of the git repository
4. ```./install_dependencies.sh``` will download the required python libraries and initialize the git submodules
5. ```./gvcci.sh path/to/image.jpg``` to run the program

Running the program will print the generated color palette, generate an examples.html file with some previews that you can open in any web browser and a theme package in ```~/.gcvvi/themes/``` containing the image and the filled out templates.

## Options

`--background [auto|light|dark|<hex>]` - Defaults to `auto`, which can pick either a light or dark background depending on the image. The `light` and `dark` options have it pick either a light or a dark color from the image as the background, and `<hex>` allows you to specify a hex code to use as background color.

`--template [file|directory]` - Defaults to `./templates`. Specify which template to use when generating the output. If your argument is a file, that template file will be used. If it's a directory, all files in that directory will be used as templates. For more information regarding templates, refer to the Templates section below.

`--print-output` - If enabled, will output only the filled out template(s) to stdout.

`--symlink-wallpaper` - If enabled, the wallpaper image will be saved as a symlink rather than as a copy of the file under `~/.gvcci/themes/`.

## macOS iTerm users

You're in luck because that's my setup and I've made it easy to use `gvcci` with it. You can run ```./iterm_lazy.sh [img_path]``` for an easy one-step extract palette + generate iTerm profile + update iTerm profile + update wallpaper. You will need a recent version of iTerm (one that supports dynamic profiles) for this to work.

## Roadmap/TODO List

- [X] Output a foreground color
- [X] Assign adequately dark color to the ANSI 'Black' color value
- [X] Improve background color selection for light themes
- [X] Fix light themes resulting in dull grey background colors
- [X] Improve theme bundling
- [X] Improve syntax colors for light themes
- [X] Map the generated colors to their nearest ANSI counterpart (ie. the ANSI red should be the most "red" of the generated colors etc)
- [X] Refactor the codebase and modularize it where appropriate
- [X] Add the ability to use output templates
- [ ] Integrate theme generation and apply scripts (add params in config to apply?)
- [ ] Generalize script? (ie. be able to request X light colors, Y dark colors and Z variants on each color)
- [ ] Store generated color theme in ~./gvcci/themes/.../ to allow for easy reuse with other templates rather than recompute the colors every time
- [ ] Add commandline params to specify min/max contrast levels between light and dark colours, min/max saturation values, etc

## Templates

When writing a template, you have access to the following colors:

```
background
foreground
bold
cursor
selection
selected-text
ansi-black-normal
ansi-black-bright
ansi-red-normal
ansi-red-bright
ansi-green-normal
ansi-green-bright
ansi-yellow-normal
ansi-yellow-bright
ansi-blue-normal
ansi-blue-bright
ansi-magenta-normal
ansi-magenta-bright
ansi-cyan-normal
ansi-cyan-bright
ansi-white-normal
ansi-white-bright
```

You can also use `wallpaper` to insert the wallpaper's filename.

For each color, you have access to the following variants:

```
<color>-[red|green|blue]-255 (a value for the rgb components in the [0, 255] range)
<color>-[red|green|blue]-float (a value for the rgb components in the [0, 1] range)
<color>-hex (the hex code of the color)
```

Here's the "hello world" of `gvcci` templates:

```
Background: {{background-hex}}
Foreground RGB: [{{foreground-red-255}}, {{foreground-green-255}}, {{foreground-blue-255}}]
Wallpaper: {{wallpaper}}
```

If you had a pure black background with pure red foreground, this would yield

```
Background: #000000
Foreground RGB: [255, 0, 0]
```
