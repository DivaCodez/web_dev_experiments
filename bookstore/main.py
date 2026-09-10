from fastapi import FastAPI, HTTPException 
from pydantic import BaseModel

app = FastAPI()

books = [
    {"id": 1, "title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "is_offer": True},
    {"id": 2, "title": "1984", "author": "George Orwell", "is_offer": False},
    {"id": 3, "title": "To Kill a Mockingbird", "author": "Harper Lee", "is_offer": False},
    {"id": 4, "title": "Pride and Prejudice", "author": "Jane Austen", "is_offer": True}
]


@app.get("/")
def read_root():
	return {"message": "Welcome to the Mini Bookstore API!"}

@app.get("/books")
def get_books():
	if books:
		return books
	raise HTTPException (status_code=404, detail="No books found")

@app.get("/books/{id_book}")
def get_book(id_book : int):
	book = next((b for b in books if b["id"] == id_book), None) 

	if book is None:
		raise HTTPException  (status_code=404, detail="Wrong id")
	else: 
		return book
	
class Book (BaseModel):
	id : int
	title : str
	author : str
	is_offer : bool = False


@app.post("/books")
def create_book(book : Book):
	if not book:
		raise HTTPException  (status_code=404, details="book not recieved")
	books.append(book)
	return {"message": "book créé avec succès !", 
		"data_received": book.model_dump(),}

@app.put("/books/{id_book}")
def update_book(id_book : int, updated_fields : Book):
	existing_book = next((b for b in books if b["id"] == id_book), None)
	if existing_book is None:
		raise HTTPException  (status_code=404, details="book not recieved")
		
	existing_book["title"] = updated_fields.title
	existing_book["author"] = updated_fields.author
	existing_book["is_offer"] = updated_fields.is_offer
	
	return {"message": "Book updated with success !"}
