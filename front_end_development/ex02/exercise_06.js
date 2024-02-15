let book = {
    isbn: null,
    name: null,
    authors: null,
    publicationDate: null,

    getAuthors: function() {
        return this.authors;
    },

    setAuthors: function(newAuthors) {
        this.authors = newAuthors;
    },

    getIsbn: function() {
        return this.isbn;
    },

    setIsbn: function(newIsbn) {
        this.isbn = newIsbn;
    },

};

function compareIsbn (book_1, book_2) {
    return book_1.isbn === book_2.isbn;
}

function compareBooks (book_1, book_2) {
    return book_1 === book_2;
}

let book_1 = {isbn: "978-3-16-148410-0", name: "The Catcher in the Rye", authors: "J.D. Salinger", publicationDate: "1951-07-16"};
let book_2 = {isbn: "978-3-16-148410-1", name: "To Kill a Mockingbird", authors: "Harper Lee", publicationDate: "1960-07-11"};

let book_same_1 = {isbn: "978-3-16-148410-0", name: "The Catcher in the Rye", authors: "J.D. Salinger", publicationDate: "1951-07-16"};
let book_same_2 = {isbn: "978-3-16-148410-0", name: "The Catcher in the Rye", authors: "J.D. Salinger", publicationDate: "1951-07-16"};

//console.log(book_1);
//console.log(book_2);
//console.log(compareIsbn(book_1, book_2));
console.log(compareBooks(book_same_1, book_same_2));
