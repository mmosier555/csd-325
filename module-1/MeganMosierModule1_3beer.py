"""
Megan Mosier
Module 1.3 Beer Bottle Countdown

This program asks the user how many bottles of beer are on the wall, then passes
that number to a function that counts down to 1.
The function will print the correct lyrics for each number.
Once countdown is completed, the program reminds the user to buy more beer.
"""

def countdown(bottles):
    """
    This funtion receives the starting number of bottles then counts down to 1.
    It prints lyrics based on number received.
    """
    while bottles>1:
        print(f"{bottles} bottles of beer on the wall, {bottles} bottles of beer. Take one down and pass it around. {bottles -1} bottles of beer on the wall")
        bottles -= 1
        
    # Handle the final bottle
    print("1 bottle of beer on the wall, 1 bottle of beer. Take it down and pass it around.")
    
def main():
    print("Welcome to the Beer Bottle Countdown Program!\n")
    
    #Get user input
    num = int(input("How many bottles of beer are on the wall? "))
    
    #Call the countdown function
    countdown(num)
    
    #Final message
    print("\nTime to buy more beer!")
    
#Run the program
if __name__ == "__main__":
    main()
    
    