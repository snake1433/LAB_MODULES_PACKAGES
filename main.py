# LAB_MODULES_PACKAGES

from library import librarian
import dateOP
dateOP.current_time()

# Bonus

library = {}
# add_book()
librarian.add_book(library, "The Catcher in the Rye",
                   "J.D. Salinger", "9780316769174")
librarian.add_book(library, "To Kill a Mockingbird",
                   "Harper Lee", "9780446310789")
librarian.add_book(library, "1984", "George Orwell", "9780451524935")

librarian.remove_book(library, "9780451524935")
# librarian.check_out_book(library,"9780446310789")
# librarian.return_book(library,"9780446310789")
librarian.display_books(library)
