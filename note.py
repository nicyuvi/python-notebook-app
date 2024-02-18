from codecs import decode
import json
from typing import Dict, TypeAlias
from uuid import uuid4

Notes: TypeAlias = list[Dict[str, str]]


class NoteId():
    def __init__(self):
        self.uid = uuid4().hex


class Note:
    def __init__(self, id: str, title: str, desc: str):
        self.id = id
        self.title = title
        self.desc = desc

    def to_dict(self):
        return {'id': self.id, 'title': self.title, 'desc': self.desc}


class NoteController:
    def load_notes(self):
        try:
            with open('notes.json', 'r') as file:
                notes = json.load(file)
        except FileNotFoundError:
            notes = []
        return notes

    def add_note(self, title: bytes, desc: bytes, notes: Notes):
        note_id = NoteId()
        note = Note(note_id.uid, decode(title), decode(desc))
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
                stdscr.addstr(counter, 0, note['id'])
                stdscr.addstr(counter, len(note['id']) + 2, note['title'])
                stdscr.addstr(counter, len(
                    note['id']) + len(note['title']) + 4, note['desc'])
                counter += 2

    def update_note(self):
        print('update note')

    def delete_note(self, curses, stdscr, notes: Notes):
        curses.echo()
        stdscr.addstr(2, 3, 'Note ID: ')
        stdscr.refresh()
        note_id = stdscr.getstr(3, 3, 40)

        for index, note in enumerate(notes):
            if note['id'] == decode(note_id):
                notes.pop(index)
                with open('notes.json', 'w') as file:
                    json.dump(notes, file, indent=4)
