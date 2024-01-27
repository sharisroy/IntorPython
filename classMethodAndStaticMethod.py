class ClassTest:
    def instance_method(self):
        print(f"Called instance_method of {self}")

    @classmethod
    def class_method(cls):
        print(f"Called class_method of {cls}")

    @staticmethod
    def static_method():
        print("Called static_method")


# test = ClassTest()
# test.instance_method()  # instance method net object to call the method
# ClassTest.instance_method(test)  # instance method net object to call the method


# ClassTest.class_method()

ClassTest.static_method()

print("------------------------------------- Example of Class Method -------------------------------------")


class Book:
    TYPES = ("hardcover", "paperback")

    def __init__(self, name, book_type, weight):
        self.name = name
        self.book_type = book_type
        self.weight = weight

    def __repr__(self):
        return f"Book Name: {self.name},\tType: {self.book_type},\tWeight: {self.weight}"

    @classmethod
    def hardcover(cls, name, page_weight):
        return Book(name, Book.TYPES[0], page_weight + 100)

    @classmethod
    def paperback(cls, name, page_weight):
        return Book(name, Book.TYPES[1], page_weight)


hardCoverBook = Book.hardcover("Python Hard Cover Book", 1500)
paperCoverBook = Book.paperback("Python Paper Cover Boom", 1000)

print(hardCoverBook)
print(paperCoverBook)
