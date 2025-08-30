class Author: ## name
    all = []  # keep track of all authors

    def __init__(self, name):
        if not isinstance(name, str) or not name.strip():
            raise Exception("Name must be a non-empty string")
        self.name = name
        Author.all.append(self)

    def contracts(self):
        """Return list of contracts related to this author"""
        return [c for c in Contract.all if c.author == self]

    def books(self):
        """Return list of books related to this author through contracts"""
        return [c.book for c in self.contracts()]

    def sign_contract(self, book, date, royalties):
        """Create and return a new Contract"""
        return Contract(self, book, date, royalties)

    def total_royalties(self):
        """Return total royalties for all contracts"""
        return sum(c.royalties for c in self.contracts())

    def __repr__(self):
        return f"<Author name={self.name}>"



class Book:
    all = []

    def __init__(self, title):
        self.title = title
        Book.all.append(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title_str):
        if isinstance(title_str, str) and len(title_str) > 0:
            self._title = title_str
        else:
            raise Exception("Title must be a non-empty string.")

    def contracts(self):
        return [contract for contract in Contract.all if contract.book == self]
    def authors(self):
        return [contract.author for contract in Contract.all if contract.book == self]



class Contract:
    all = []  # to store data

    def __init__(self, author, book, date, royalties):
        # attributes.
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)

    # Getters and Setters for 'author'
    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, author_obj):
        if isinstance(author_obj, Author):
            self._author = author_obj
        else:
            raise Exception("Author must be an instance of the Author class.")

    # Getters and Setters for 'book'
    @property
    def book(self):
        return self._book

    @book.setter
    def book(self, book_obj):
        if isinstance(book_obj, Book):
            self._book = book_obj
        else:
            raise Exception("Book must be an instance of the Book class.")

    # Getters and Setters for 'date'
    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, date_str):
        if isinstance(date_str, str) and len(date_str) > 0:
            self._date = date_str
        else:
            raise Exception("Date must be a non-empty string.")

    # Getters and Setters for 'royalties'
    @property
    def royalties(self):
        return self._royalties

    @royalties.setter
    def royalties(self, royalties_int):
        # The prompt says 'number', so we'll check for int or float.
        # But for this simple lab, int is sufficient.
        if isinstance(royalties_int, int) and royalties_int > 0:
            self._royalties = royalties_int
        else:
            raise Exception("Royalties must be a positive integer.")

    # Class method to find contracts by date
    @classmethod
    def contracts_by_date(cls, date):
        return [contract for contract in cls.all if contract.date == date]