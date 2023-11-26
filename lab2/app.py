from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample data as a dictionary keyed by book ID
books = {
    1: {"id": 1, "title": "Book 1", "author": "Author 1"},
    2: {"id": 2, "title": "Book 2", "author": "Author 2"},
    3: {"id": 3, "title": "Book 3", "author": "Author 3"},
}

# Sample data as a dictionary keyed by user ID
members = {
    123: {"id": 123, "name": "User 1", "email": "user1@example.com"},
    456: {"id": 456, "name": "User 2", "email": "user2@example.com"},
}

loan = {
    1: {"id": 1, "book_id": 1, "member_id": 123, "date": "2020-01-01", "r_date": "2020-01-01"},
}

# Sample data as a dictionary keyed by loan ID
loans = {}

# Generate unique IDs for new items
def generate_id(dictionary):
    return max(dictionary.keys(), default=0) + 1

# CRUD operations for books

@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(list(books.values()))

@app.route('/books', methods=['POST'])
def create_book():
    data = request.get_json()
    new_book_id = generate_id(books)
    new_book = {
        "id": new_book_id,
        "title": data["title"],
        "author": data["author"]
    }
    books[new_book_id] = new_book
    return jsonify(new_book), 201

@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = books.get(book_id)
    if book is None:
        return "Book not found", 404
    return jsonify(book)

@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    data = request.get_json()
    book = books.get(book_id)
    if book is None:
        return "Book not found", 404
    book["title"] = data["title"]
    book["author"] = data["author"]
    return jsonify(book)

@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    book = books.pop(book_id, None)
    if book is None:
        return "Book not found", 404
    return "Book deleted", 204

# CRUD operations for members

@app.route('/members', methods=['GET'])
def get_members():
    return jsonify(list(members.values()))

@app.route('/members', methods=['POST'])
def create_members():
    data = request.get_json()
    new_members_id = generate_id(members)
    new_members = {
        "id": new_members_id,
        "name": data["name"],
        "email": data["email"]
    }
    members[new_members_id] = new_members
    return jsonify(new_members), 201

@app.route('/members/<int:member_id>', methods=['GET'])
def get_member(member_id):
    member = members.get(member_id)
    if member is None:
        return "Member not found", 404
    return jsonify(member)

@app.route('/members/<int:member_id>', methods=['PUT'])
def update_member(member_id):
    data = request.get_json()
    member = members.get(member_id)
    if member is None:
        return "ember not found", 404
    member["name"] = data["name"]
    member["email"] = data["email"]
    return jsonify(member)

@app.route('/members/<int:member_id>', methods=['DELETE'])
def delete_member(member_id):
    member = members.pop(member_id, None)
    if member is None:
        return "Member not found", 404
    return "Member deleted", 204

# crude loan
@app.route('/loans', methods=['GET'])
def get_loans():
    return jsonify(list(loans.values()))

@app.route('/loans', methods=['POST'])
def create_loans():
    data = request.get_json()
    new_loans_id = generate_id(loans)
    new_loans = {
        "id": new_loans_id,
        "book_id": data["book_id"],
        "member_id": data["member_id"],
        "date": data["date"],
        "r_date": data["r_date"],
    }
    loans[new_loans_id] = new_loans
    return jsonify(new_loans), 201

@app.route('/loans/<int:loan_id>', methods=['GET'])
def get_loan(loan_id):
    loan = loans.get(loan_id)
    if loan is None:
        return "Loan not found", 404
    return jsonify(loan)

@app.route('/loans/<int:loan_id>', methods=['PUT'])
def update_loan(loan_id):
    data = request.get_json()
    loan = loans.get(loan_id)
    if loan is None:
        return "ember not found", 404
    loan["book_id"] = data["book_id"]
    loan["member_id"] = data["member_id"]
    loan["date"] = data["date"]
    loan["r_date"] = data["r_date"]
    return jsonify(loan)

@app.route('/loans/<int:loan_id>', methods=['DELETE'])
def delete_loan(loan_id):
    loan = loans.pop(loan_id, None)
    if loan is None:
        return "Loan not found", 404
    return "Loan deleted", 204

if __name__ == '__main__':
    app.run(debug=True)
