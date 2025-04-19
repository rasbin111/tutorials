from schema import schema

query1 = '''
    query helloB{
        helloWorld
    }
'''

mutation1 = '''
    mutation bookCreator{
        createBook(title: "The Greate Gatsby", author: "Not Buddhi Sagar"){
            book {
                title
                author
            }
        }
    }
'''

query_books = '''
    query{
        books{
            title
            author
        }
    }
'''

result = schema.execute(query_books)
print(result.data)
