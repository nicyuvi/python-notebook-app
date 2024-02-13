import json
from typing import List, Optional


class Note:
    def __init__(self, title: str, desc: str):
        self.title = title
        self.desc = desc


class NoteController:
    def load_notes(self) -> Optional[List[Note]]:
        try:
            with open('notes.json', 'r') as file:
                notes = json.load(file)
        except FileNotFoundError:
            notes = []
        return notes

    def add_note(self, stdscr):
        add_note_str = 'add note'
        stdscr.addstr(0, 0, add_note_str)
        # Create instances of the Note class
        # note = Note(title="user_input", desc=user_input)

    def view_note(self, stdscr, notes: Optional[List[Note]]):
        # if empty array, render 'no notes ...'
        if not notes:
            stdscr.addstr(0, 0, 'No notes...')
        else:
            # else loop through and display
            for index, note in enumerate(notes):
                stdscr.addstr(0, index, note.title)
                stdscr.addstr(0, index + 1, note.desc)
