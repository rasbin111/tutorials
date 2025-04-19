import graphene


class Book(graphene.ObjectType): # Type
    title = graphene.String() # Field
    author = graphene.String() # Field


class Query(graphene.ObjectType):
    hello_world = graphene.String() # Field
    books = graphene.List(Book) # Field added

    def resolve_hello_world(self, info): # resolver function
        return "Hello World from graphene"

    def resolve_books(self, info): # resolver for books added
        import gc # garbace collector

        # dummy objects
        b1 = Book(title="Seto Dharti", author="Amar Neuapane")
        b2 = Book(title="Karnali Blues", author="Buddhi Sagar")

        obj_list = []
        for obj in gc.get_objects():
            if isinstance(obj, Book):
                obj_list.append(obj)

        return obj_list


class CreateBook(graphene.Mutation):
    class Arguments:
        title = graphene.String() # arguemnt
        author = graphene.String() # argument

    book = graphene.Field(Book)

    def mutate(self, info, title, author):
        book = Book(title=title, author=author)
        return CreateBook(book=book)


class Mutation(graphene.ObjectType):
    create_book = CreateBook.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)
