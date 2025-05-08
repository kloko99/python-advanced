"""
you are tasked with designing a class structure for a bookstore application.
The application should allow users to search for books using different search
engines (e.g., Google Books, Amazon Books). Your goal is to implement
dependency injection to achieve loose coupling between the application and
search engines.

1) Create an abstract class called BookSearchEngine with an abstract method search
that takes a search query as input and returns a list of books. This class
represents the search engine interface.

2) Implement two concrete search engines: GoogleBooksSearch and AmazonBooksSearch.
Each search engine should inherit from BookSearchEngine and implement the
search method with the respective search engine's logic.

3) Create a class called Bookstore that takes a search engine as a dependency
during initialization. The Bookstore class should have a method called
search_books that delegates the book search to the injected search engine and
returns the list of books.

4) In the client code, create instances of the BookSearchEngine implementations
(e.g., GoogleBooksSearch, AmazonBooksSearch) and use them to create a Bookstore
object. Then, use the Bookstore object to search for books and print the
results.

!!!!!
the methods should only print the name of the search engine,
no real search logic is needed.

"""

from abc import ABC, abstractmethod


# Step 1: Define the BookSearchEngine class with abstract method search

# Step 2: Implement concrete search engines with
# concrete search method


# Step 3: Implement the Bookstore class
# in init method take a search engine as a dependency
class Bookstore:
    pass


# Step 4: Client code
if __name__ == "__main__":
    # Create instances of search engines
    # google_search = GoogleBooksSearch()
    # amazon_search = AmazonBooksSearch()

    # Create a Bookstore with Google Books search engine
    # bookstore = Bookstore(google_search)

    # Search for books using the Bookstore
    # result = bookstore.search_books("Python Programming")
    # print("Books found using Google Books:", result)

    # Create a Bookstore with Amazon Books search engine
    # bookstore = Bookstore(amazon_search)
    #
    # Search for books using the Bookstore
    # result = bookstore.search_books("Python Programming")
    # print("Books found using Amazon Books:", result)
