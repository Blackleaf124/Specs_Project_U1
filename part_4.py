### Step 1 - Input function

## Create five input statements to gather user's book they want to input to the system. After that be sure to turn it into a function.

def create_new_book_1():
    title = input("What is the title of your book? ")
    author = input("Who is the author of the book? ")
    year = input("What year was the book published? ")
    rating = input("What rating would you give it out of 5? ")
    pages = input("How many pages are in the book? - ")

    book_dictionary = {
        "title": title,
        "author": author,
        "year": year,
        "rating": rating,
        "pages": pages
    }

    return print(book_dictionary)

# create_new_book_1()

### Step 2 - Type conversion

## Now convert the proper data-types front strings to either floats or ints depending on what it is. Feel free to comment out your old function so you don't get an error, or copy/paste and give it a new name.

def create_new_book_2():
    title = input("What is the title of your book? ")
    author = input("Who is the author of the book? ")
    year = int(input("What year was the book published? "))
    rating = float(input("What rating would you give it out of 5? "))
    pages = int(input("How many pages are in the book? - "))

    book_dictionary = {
        "title": title,
        "author": author,
        "year": year,
        "rating": rating,
        "pages": pages
    }

    return print(book_dictionary)



### Step 3 - Error handling

## Now take your previous function, and handle potential errors should the user type an answer that doesn't convert data-type properly.

def create_new_book_3():
    title = input("What is the title of your book? ")
    author = input("Who is the author of the book? ")
    try:
        year = int(input("What year was the book published? "))
    except:
        year = int(input("Please type a number for the year. "))
    rating = float(input("What rating would you give it out of 5? "))
    pages = int(input("How many pages are in the book? - "))

    book_dictionary = {
        "title": title,
        "author": author,
        "year": year,
        "rating": rating,
        "pages": pages
    }

    return print(book_dictionary)



### Step 4 - if/elif/else

## Now create a main menu function that gives the user options. Handle their choices with if/elif/else statements.
condition = True
def main_menu():
    print("MAIN MENU")
    print("Type SEE to see all the currently stored books.")
    print("Type ADD to add a new book.")
    print("Type EXIT to close the app.")
    choice = input("What do you want to do?")

    if choice == "ADD":
        print("Adding books.")
    elif choice == "SEE":
        print("Seeing Books.")
    elif choice == "EXIT":
        condition = False
    else:
        print("What you typed was not a valid response. Try again please.")
        


### Step 5 - while loops

## Now add a while loop to your main menu to keep it alive, and continually asking for input until the user chooses to exit the program. Call the main menu to ensure it functions properly.

while condition == True:
    main_menu()

