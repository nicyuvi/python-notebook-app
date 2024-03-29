import curses
from note import NoteController


def draw_menu(stdscr):
    k = 0
    cursor_x = 0
    cursor_y = 0

    # Clear and refresh the screen for a blank canvas
    stdscr.clear()
    stdscr.refresh()

    # Start colors in curses
    curses.start_color()
    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_WHITE)

    # Loop where k is the last character pressed
    while (k != ord('q')):

        # Initialization
        stdscr.clear()
        height, width = stdscr.getmaxyx()

        cursor_x = max(0, cursor_x)
        cursor_x = min(width-1, cursor_x)

        cursor_y = max(0, cursor_y)
        cursor_y = min(height-1, cursor_y)

        # Declaration of strings
        title = 'Note Manager'
        add_note_title = 'Add Note'
        view_notes_title = 'View Notes'
        update_note_title = 'Update Note'
        delete_note_title = 'Delete Note'

        statusbarstr = "Press 'q' to exit"

        # Centering calculations
        start_x_title = int(
            (width // 2) - (len(title) // 2) - len(title) % 2)
        start_x_options = int(
            (width // 2) - (len(title) // 2) - len(title) % 2)
        start_y = int((height // 2) - 2)

        # Render status bar
        stdscr.attron(curses.color_pair(3))
        stdscr.addstr(height-1, 0, statusbarstr)
        stdscr.addstr(height-1, len(statusbarstr), " " *
                      (width - len(statusbarstr) - 1))
        stdscr.attroff(curses.color_pair(3))

        # Turning on attributes for title
        stdscr.attron(curses.color_pair(2))
        stdscr.attron(curses.A_BOLD)

        # Rendering title
        stdscr.addstr(start_y, start_x_title, title)

        # Turning off attributes for title
        stdscr.attroff(curses.color_pair(2))
        stdscr.attroff(curses.A_BOLD)

        # Print rest of text
        stdscr.addstr(start_y + 1, (width // 2) - 4, '-' * 8)
        stdscr.addstr(start_y + 3, start_x_options - 4, '[1]')
        stdscr.addstr(start_y + 3, start_x_options + 4, add_note_title)

        stdscr.addstr(start_y + 4, start_x_options - 4, '[2]')
        stdscr.addstr(start_y + 4, start_x_options + 4, view_notes_title)

        stdscr.addstr(start_y + 5, start_x_options - 4, '[3]')
        stdscr.addstr(start_y + 5, start_x_options + 4, update_note_title)

        stdscr.addstr(start_y + 6, start_x_options - 4, '[4]')
        stdscr.addstr(start_y + 6, start_x_options + 4, delete_note_title)

        # starts cursor in top left
        stdscr.move(cursor_y, cursor_x)

        note = NoteController()
        notes = note.load_notes()

        # options logic here
        if k == ord('1'):
            stdscr = curses.initscr()
            stdscr.clear()

            curses.echo()
            stdscr.addstr(2, 3, 'Note title: ')
            stdscr.refresh()
            input_title = stdscr.getstr(3, 3, 20)

            stdscr.addstr(5, 3, 'Note desc: ')
            stdscr.refresh()
            input_desc = stdscr.getstr(6, 3, 20)

            note.add_note(input_title, input_desc, notes)
        elif k == ord('2'):
            note.view_note(stdscr, notes)
        elif k == ord('3'):
            note.update_note(curses, stdscr, notes)
        elif k == ord('4'):
            note.delete_note(curses, stdscr, notes)

        # Refresh the screen
        stdscr.refresh()

        # Wait for next input
        k = stdscr.getch()


def main():
    curses.wrapper(draw_menu)


if __name__ == "__main__":
    main()
