from codecs import decode
import json
from typing import Dict, TypeAlias

Notes: TypeAlias = list[Dict[str, str]]


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

    def add_note(self, title: bytes, desc: bytes, notes: Notes):
        note = Note(decode(title), decode(desc))
        note_dict = note.to_dict()
        notes.append(note_dict)
        with open('notes.json', 'w') as file:
            json.dump(notes, file, indent=4)

    def view_note(self, stdscr, notes: Notes):
        if not notes:
            stdscr.addstr(0, 0, 'No notes...')
        else:
            counter = 0
            for note in notes:
                stdscr.addstr(counter, 0, note['title'])
                stdscr.addstr(counter, len(note['title']) + 2, note['desc'])
                counter += 2
