#include <iostream>
#include <fstream>
using namespace std;

class Student {
private:
    string name;
    int rollNo;
    float marks;

public:
    void getDetails() {
        cout << "Enter Name: ";
        cin >> name;
        cout << "Enter Roll Number: ";
        cin >> rollNo;
        cout << "Enter Marks: ";
        cin >> marks;
    }

    void displayDetails() {
        cout << "Name: " << name << endl;
        cout << "Roll Number: " << rollNo << endl;
        cout << "Marks: " << marks << endl;
    }

    void saveToFile() {
        ofstream file("student.txt", ios::out);
        if (file.is_open()) {
            file << name << endl;
            file << rollNo << endl;
            file << marks << endl;
            file.close();
            cout << "Details saved to file successfully!" << endl;
        } else {
            cout << "Unable to open file!" << endl;
        }
    }

    void readFromFile() {
        ifstream file("student.txt", ios::in);
        if (file.is_open()) {
            getline(file, name);
            file >> rollNo >> marks;
            file.close();
            cout << "Details read from file successfully!" << endl;
        } else {
            cout << "Unable to open file!" << endl;
        }
    }
};

int main() {
    Student s;
    s.getDetails();
    s.saveToFile();
    s.readFromFile();
    s.displayDetails();
    return 0;
}
