from codecs import decode, encode
import json
from typing import List, Optional


class Note:
    def __init__(self, title: str, desc: str):
        self.title = title
        self.desc = desc


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

    def add_note(self, title: bytes, desc: bytes, notes):
        # implement with decode. then see if Note instance works

        # new_note = Note(title, desc)
        decode_title = decode(title)
        decode_desc = decode(desc)

        # new_note = {new_title, new_desc}
        new_note = {'title': decode_title, 'desc': decode_desc}
        notes.append(new_note)
        # print(notes)

        with open('notes.json', 'w') as file:
            json.dump(notes, file, indent=4)

    def view_note(self, stdscr, notes: List[Note]):
        print(notes)
        # if empty array, render 'no notes ...'
        # if not notes:
        #     stdscr.addstr(0, 0, 'No notes...')
        # else:
        #     # else loop through and display
        #     for index, note in enumerate(notes):
        #         stdscr.addstr(0, index, note.title)
        #         stdscr.addstr(0, index + 1, note.desc)
