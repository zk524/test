import cairosvg

svg_file = 'favicon.svg'
png_file = 'favicon.png'
ico_file = 'favicon.ico'
cairosvg.svg2png(url=svg_file, write_to=png_file)
cairosvg.svg2png(url=svg_file, write_to=ico_file, output_width=256, output_height=256)
