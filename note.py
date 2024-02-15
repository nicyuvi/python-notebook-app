from codecs import decode
import json
from typing import Dict, List


class Note:
    def __init__(self, title: str, desc: str):
        self.title = title
        self.desc = desc

    def to_dict(self):
        return {'title': self.title, 'desc': self.desc}


class NoteController:
    def load_notes(self):
        try:
            with open('notes.json', 'r') as file:
                notes = json.load(file)
        except FileNotFoundError:
            notes = []
        return notes

    def save_notes(self, notes):
        with open('notes.json', 'w') as file:
            json.dump(notes, file, indent=4)

    def add_note(self, title: bytes, desc: bytes, notes: List[Dict[str, str]]):
        note = Note(decode(title), decode(desc))
        note_dict = note.to_dict()
        notes.append(note_dict)
        with open('notes.json', 'w') as file:
            json.dump(notes, file, indent=4)

    def view_note(self, stdscr, notes: List[Note]):
        print(type(notes))
        # if empty array, render 'no notes ...'
        # if not notes:
        #     stdscr.addstr(0, 0, 'No notes...')
        # else:
        #     # else loop through and display
        #     for index, note in enumerate(notes):
        #         stdscr.addstr(0, index, note.title)
        #         stdscr.addstr(0, index + 1, note.desc)
