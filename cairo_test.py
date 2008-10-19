import cairo

WIDTH, HEIGHT = 400, 400

# Setup Cairo
surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
ctx = cairo.Context(surface)

# Set thickness of brush
ctx.set_line_width(15)

# Draw out the triangle using absolute coordinates
ctx.move_to(200, 100)
ctx.line_to(300, 300)
ctx.rel_line_to(-200, 0)
ctx.close_path()

# Apply the ink
ctx.stroke()

# Output a PNG file
surface.write_to_png("triangle.png")
