#Task 1
class Publication:
    def __init__(self,name_publication):
        self.name_publication = name_publication

class Book(Publication):
    def __init__(self,name_publication,author,page_no):
        super().__init__(name_publication)
        self.author = author
        self.page_no = page_no
    
    def print_information(self):
        print("Book Info:")
        print(f"Pubilcation Name:{self.name_publication}\nAuthor:{self.author}\nPages:{self.page_no}")

class Magazine(Publication):
    def __init__(self,name_publication,chief_editor):
        super().__init__(name_publication)
        self.chief_editor = chief_editor

    def print_information(self):
        print("Magazine Info:")
        print(f"Pubilcation Name:{self.name_publication}\nChief Editor:{self.chief_editor}")

object1 = Magazine("Donald Duck","Aki Hyyppä")
object2 = Book("Compatment No. 6","Rosa Liksom",192)
object1.print_information()
object2.print_information()