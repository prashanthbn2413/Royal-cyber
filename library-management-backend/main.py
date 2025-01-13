from fastapi import FastAPI, Request
import mysql.connector
from fastapi.responses import JSONResponse

app = FastAPI()

# MySQL Database Connection
def get_db_connection():
    return mysql.connector.connect(
        host="127.0.0.1",  # Your MySQL host
        user="root",       # Your MySQL user
        password="root",   # Your MySQL password
        database="library_db"  # Your database name
    )

# Home route for testing the server
@app.get("/")
def home():
    return {"message": "Library Bookstore API is Running!"}

# Dialogflow Webhook Integration
@app.post("/webhook")
async def dialogflow_webhook(request: Request):
    payload = await request.json()
    
    # Debug: Print the entire payload for checking the incoming request
    print("Incoming request payload:")
    print(payload)

    intent = payload["queryResult"]["intent"]["displayName"]
    parameters = payload["queryResult"]["parameters"]

    # Check the intent and call corresponding functions
    if intent == "ListBooks":  # Ensure this matches exactly with your Dialogflow intent
        return list_books()
    elif intent == "OrderBook":
        book_name = parameters.get("book_name")  # Fixed parameter name
        quantity = parameters.get("quantity")
        return order_book(book_name, quantity)
    else:
        return JSONResponse(content={"fulfillmentText": "Sorry, I couldn't understand your request."})

# List all books available in the database
def list_books():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT title, author, genre, published_year, availability FROM books;")
    books = cursor.fetchall()
    connection.close()

    if books:
        # Format the list of books for response
        books_list = "\n".join([f"• {book['title']} by {book['author']} - {book['genre']}, Published: {book['published_year']}, Availability: {'Available' if book['availability'] else 'Not Available'}" for book in books])
        return JSONResponse(content={"fulfillmentText": f"Here are the available books:\n{books_list}"})
    else:
        return JSONResponse(content={"fulfillmentText": "No books available at the moment."})

# Order a book based on title and author
def order_book(book_name, quantity):
    if not quantity or quantity <= 0:
        return JSONResponse(content={"fulfillmentText": "Please specify a valid quantity for the book."})

    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT title, author, availability FROM books WHERE title = %s;", (book_name,))
    book = cursor.fetchone()
    connection.close()

    if book:
        if book["availability"]:
            return JSONResponse(content={"fulfillmentText": f"The book '{book_name}' is available for purchase."})
        else:
            return JSONResponse(content={"fulfillmentText": f"'{book_name}' is currently out of stock."})
    else:
        return JSONResponse(content={"fulfillmentText": f"'{book_name}' is not available in our store."})

# Run the FastAPI Server
if __name__ == "__main__":  # Corrected the condition
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
