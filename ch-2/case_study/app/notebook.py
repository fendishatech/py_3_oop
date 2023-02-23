import datetime

# globally stored id for notes
last_id = 0


class Note:
    """
    Represent a note ADT in the notebook. 
    :methods
    constructor instantiates a note with id, the memo, optional tags and the creation_date
    match matches if the filter provided to it is inside the memo text or tags.
    """

    def __init__(self, memo, tags=""):
        """
        Initialize a note with memo and optional space=separated tags. 
        Automatically set the note's creation date and a unique id.
        """
        global last_id
        last_id += 1
        self.id = last_id
        self.memo = memo
        self.tags = tags
        self.creation_date = datetime.date.today()

    def match(self, filter):
        """
        Determine if the note matches the filter text. 
        Return true if it matches, false otherwise.

        Search is case sensitive and matches meme text and tags.
        """

        return filter in self.memo or filter in self.tags


class NoteBook:
    """
    Represent a collection of notes that can be tagged, modifies and filtered
    :methods
    constructor
    new_notes
    modify_memo
    modify_tags
    search
    _find_note
    """

    def __init__(self) -> None:
        self.notes = []

    def new_note(self, memo, tags=""):
        """
        Create a new note and add it to the list.
        """
        self.notes.append(Note(memo, tags))

    def modify_memo(self, note_id, memo):
        """
        Find the note with the given id and change its memo to the given value.
        """
        note = self._find_note(note_id)
        if note:
            note.memo = memo
            return True

        return False

    def modify_tags(self, note_id, tags):
        """
        Find the note with the given id and change its tags to the given value.
        """
        note = self._find_note(note_id)
        if note:
            note.tags = tags
            return True

        return False

    def search(self, filter):
        """
        Find all notes that match the given filter
        """
        return [note for note in self.notes if note.match(filter)]

    def _find_note(self, note_id):
        """
        Locate the note with the given id.
        """
        for note in self.notes:
            if str(note.id) == str(note_id):
                return note

        return None
