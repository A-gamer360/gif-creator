# gif-creator
gif creation helper made for the CookieRun Wiki

# Requirements
Requires, Git,  Python and imagemagick to be on your computer and PATH

# Main Options:
 * -l, --label LABEL    Label of the type of gif
 * -fps FPS             framerate of the gif from plist 'please add three numbers after the dot maximum'
 * -o, --output OUTPUT  Output name

# Tutorial

The spritesheet needs to be already spliced with a tool like [Boofunpack](https://github.com/syrupyy/boofunpack). the option of group_by_animations is recomanded to be used.

once the spritesheet already cropped into smaller pieces, everything needs to be put into the input folder.

After cloning the repo, use the following syntax

```python main.py -l <name after the cookie id> -fps <the number of frame per second as indicated in the associated.plist under <key> and <fps> -o <the name of the output file, with underscores>```
