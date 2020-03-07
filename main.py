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


def generate_row(row_idx):
    row = []
    y_offset = row_idx * SEGMENT_WIDTH / 2
    for i in range(SEGMENTS_PER_ROW):
        x_offset = i * SEGMENT_WIDTH / 2
        segment = []
        for square in generate_segment(START_X + x_offset, START_Y + y_offset):
            segment.append(square)
        row.append(segment)
    return row


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
    win = GraphWin("Water People", 1140, 800)
    for row_idx in alternating_iterator(list(range(ROW_COUNT))):
        row = generate_row(row_idx)
        for segment in alternating_iterator(row):
            for square in segment:
                if not square.canvas:
                    square.draw(win)
    win.getMouse() # Pause to view result
    win.close()    # Close window when done


if __name__ == '__main__':
    main()