#include <iostream>
using namespace std;

class Book {
private:
    string title;
    string author;

public:
    void getDetails() {
        cout << "Enter Title: ";
        cin >> title;
        cout << "Enter Author: ";
        cin >> author;
    }

    void displayDetails() {
        cout << "Title: " << title << ", Author: " << author << endl;
    }
};

int main() {
    int n;
    cout << "Enter the number of books: ";
    cin >> n;

    Book* books = new Book[n];

    for (int i = 0; i < n; i++) {
        cout << "Enter details for book " << i + 1 << ":" << endl;
        books[i].getDetails();
    }

    cout << "\nBook Details:\n";
    for (int i = 0; i < n; i++) {
        cout << "Book " << i + 1 << ": ";
        books[i].displayDetails();
    }

    delete[] books;
    return 0;
}
