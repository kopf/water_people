from graphics import *

SEGMENT_SQUARE_COUNT = 8 # number of squares that make up an individual segment
SPACING = 10 # spacing between squares
SEGMENT_WIDTH = SEGMENT_SQUARE_COUNT * SPACING * 2 # width of an individual segment
SEGMENTS_PER_ROW = ROW_COUNT = 13
START_X = START_Y = SPACING


def generate_segment(x1, y1):
    x2 = x1 + 160
    y2 = y1 + 160
    for level in range(SEGMENT_SQUARE_COUNT):
        offset = (level * SPACING)
        rect = Rectangle(Point(x1 + offset, y1 + offset),
                         Point(x2 - offset, y2 - offset))
        rect.setFill('white')
        yield rect


def generate_row():
    line = []
    for i in range(SEGMENTS_PER_ROW):
        offset = i * SEGMENT_WIDTH / 2
        segment = []
        for square in generate_segment(START_X + offset, START_Y):
            segment.append(square)
        line.append(segment)
    return line


def main():
    win = GraphWin("Water People", 1140, 800)
    line = generate_row()
    for i in range(int(SEGMENTS_PER_ROW / 2) + 1):
        for segment in (line[-i], line[i]):
            for square in segment:
                if not square.canvas:
                    square.draw(win)
    win.getMouse() # Pause to view result
    win.close()    # Close window when done


if __name__ == '__main__':
    main()