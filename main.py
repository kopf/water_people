from graphics import *

SEGMENT_SQUARE_COUNT = 8 # number of squares that make up an individual segment
SPACING = 10 # spacing between squares within a segment
SEGMENT_WIDTH = SEGMENT_SQUARE_COUNT * SPACING * 2 # width of a segment
SEGMENTS_PER_ROW = ROW_COUNT = 13
START_X = START_Y = SPACING
WINDOW_SIZE = (2 * START_X) + ((SEGMENTS_PER_ROW + 1) * SEGMENT_WIDTH) / 2


def generate_segment(x1, y1):
    x2 = x1 + SEGMENT_WIDTH
    y2 = y1 + SEGMENT_WIDTH
    for level in range(SEGMENT_SQUARE_COUNT):
        offset = (level * SPACING)
        rect = Rectangle(Point(x1 + offset, y1 + offset),
                         Point(x2 - offset, y2 - offset))
        rect.setFill('white')
        if level > 3:
            rect.setWidth(2)
        yield rect
    yield Line(Point(x1, y1), Point(x2, y2))
    yield Line(Point(x1, y2), Point(x2, y1))


def generate_row(row_idx):
    row = []
    y_offset = row_idx * SEGMENT_WIDTH / 2
    for i in range(SEGMENTS_PER_ROW):
        x_offset = i * SEGMENT_WIDTH / 2
        segment = []
        for element in generate_segment(START_X + x_offset, START_Y + y_offset):
            segment.append(element)
        row.append(segment)
    return row


def generate_crosshairs():
    midway = ((SEGMENT_WIDTH / 2) * (SEGMENTS_PER_ROW / 2)) + (SEGMENT_WIDTH / 4)
    yield Line(Point(START_X + midway, START_Y), Point(START_X + midway, START_Y + (midway * 2)))
    yield Line(Point(START_X, START_Y + midway), Point(START_X + (midway * 2), START_Y + midway))


def alternating_iterator(iterable, last_first=True):
    exhausted = False
    indexes = (-1, 0) if last_first else (0, -1)
    while not exhausted:
        try:
            for idx in indexes:
                yield iterable.pop(idx)
        except IndexError:
            exhausted = True


def main():
    win = GraphWin("Water People", WINDOW_SIZE, WINDOW_SIZE)
    for row_idx in alternating_iterator(list(range(ROW_COUNT))):
        row = generate_row(row_idx)
        for segment in alternating_iterator(row):
            for square in segment:
                if not square.canvas:
                    square.draw(win)
    for line in generate_crosshairs():
        line.draw(win)
    win.getMouse() # Pause for click
    win.close()


if __name__ == '__main__':
    main()