from django.apps import AppConfig

class BookprojectConfig(AppConfig):
    name = 'bookproject'

    #load from masterdata
    def ready(self):
        from .models import Book
        Book.objects.all().delete()
        books = {}
        import csv
        with open("bookproject/master_list.csv") as tsv:
            tsv.__next__()
            for line in csv.reader(tsv, delimiter="\t"):
                book = books.get(line[0] + line[1], Book(title = line[0], author = line[1], recommendationCount = 0))
                book.recommendationCount += 1
                books[line[0] + line[1]] = book

        Book.objects.bulk_create(list(books.values()))
