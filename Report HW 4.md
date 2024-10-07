# Report
# Kelsey Edinborough
# Fall 2024 

Please answer the questions below. Make sure to ask questions if you have them. 


For all these questions, it is recommended youthe python interpreter and try out the code.  You can also use the python visualizer to help you visualize the code.  You can find the visualizer here: [http://www.pythontutor.com/visualize.html#mode=edit](http://www.pythontutor.com/visualize.html#mode=edit)


1. Correct the following loop.
   ```python
   value = None
   while value == "quit":
       value = input("Enter a value or quit: ")
       print(value)
   ```
    ```python
    ## put your corrected code below this line
    value = None
    while value != "quit":
        value = input("Enter a value or quit: ")
        print(value)
    ```

2. The above code uses a None value to initialize the input variable. This works because python can let a variable be multiple types, but in some languages, you would have to match the type. Assuming you had to match the type (str), what would be a good default input value, that could never cause the loop to not run at least once? Provide reasoning for your logic as there are multiple correct answers. With that said, there is one that is more 'standard' than the rest, so feel free to openly discuss options that come to mind (you do not have to come up with the standard answer, but try to!).  When testing with different input values that are strings, I came up with any string value was acceptable in going through the loop at least once. If a coding language requires match type to continue through the loop at least once using and word in a string format would allow the loop to run because it does not equal "quit", and it is the same variable type (string). An empty string will also work because it's in string format and again doesn't equal "quit". Using the empty string may be more standard than using any word inside a string. 
   

3. Write a small loop that will keep repeating until someone 
   enters a number greater than 0, and less than 5. It has to be
   whole numbers (hint: look up .isnumeric() from the team activity).

 Source used to help understand: (Gomez, 2021)

   ```python
   while True: 

    number_entered = input("Enter a value x in the following range 0 < x < 5: ")
    done = "great job!"
    again = "that number is not in the range, enter another one"
    if number_entered.isnumeric():
        int_input = int(number_entered)

        if int_input > 0 and int_input < 5: 
            print(done)
            break 

        else:  
            print(again)

    else:   
        print("you did not enter a whole number, try again")



   ```

4. Draw a flow diagram for your solution to #3

5. Looking back at homework #2, we actually had a type of 'loop' in the provided code (look near the main function). First copy the bit of code that causes the loop.
    ```python

    again = input("Run again (y or n)? ")
    if again.strip().lower() == 'y':
        main()  
    else: 
        print("Good luck on the move!")

    ```
    Now: what would be some of the pros and cons of looping in such a way (think about 'frames' you see in the python visualizer)?  One pro is that the user has say over how many times the program loops. A con to that is that it's not efficient though, because the user has to intiate each loop. Each time the user selects 'y', main() is called in a separate frame, which is a pro and also could be a con in terms of space. 

6. Thinking about edge cases, it is very common to get an off-by-one (OB1) error with loops. 
   Create two test cases (just as examples/inputs) for the following code. They 
   should both be 'correct' cases, but one of them should uncover the error in the code.

   ```python
    def count_backwards(value: int) -> None:
        """ Counts from value to 0, printing even values until 10 (including 10), and 
        then odd values."""
       counter = value
       while counter >= 0:
          if counter > 10:
            if counter % 2 == 0:
                print(counter)
          else:
            if counter % 2 == 1:
                print(counter)
          counter -= 1
   ```
   * Example test one: count_backwards(0), this runs and prints nothing as it should 
   
   * Example test two: count_backwards(12), the code is supposed to include 10 as it counts down. However, this skips 10 and goes straight to 9. In the code it should be if counter >= 10: 

 7. When thinking of these edge cases and OB1 errors, it is common to say one should test
    every condition plus-minus 1. In your opinion, is this beneficial? Why or why not? I think it is beneficial because even though it can be time consuming and difficult to figure out what the edge cases should be, it provides the following benefits: checking to make sure our code isn't causing an off by one error, which makes sure our code is applicable and runs correctly for the user, also, when I've had to figure out edge-cases in my own code, it makes me think and review what I'm actually trying to do with my code, what my final goal is, and this helps me also catch errors in my code. 


## Deeper Thinking

Reflection is a powerful tool that has been **repeatedly** documented to help computer scientists learn languages, concepts, and improve their problem solving skills. There is even research that shows CS majors who spend time reflecting often do better at technical interviews, and long term studies show those reflective students also tend to get higher paying jobs over time. It is also a great way to help you learn how to learn.

Take a moment to reflect on the design of jailbreak.py (just the one file). Was it
a design you would have come up with given the problem? Did breaking concepts up into
functions help as compared to one loop? Also take a moment to reflect on your development process in general. What are topics you need to work on? What are some topics you really enjoy?  You should write a paragraph reflection using *PROSE* (don't bullet point). We often return reflections that are bullet points, and there is a reason you should use prose as it forces you to consolidate and solidify your thoughts. 

Given the design of jailbreak.py, I think this early on in coding, I can't say I would have come up with this design myself. Breaking up the concepts into functions definitely helped me wrap my head around my goal with the code. I found that most of my time on Jailbreak was spent mapping out the code using flowcharts and trying to write the unlock_pattern_lock function. I need more practice using loops with strings such as this function. It took me several hours to figure out where my errors in the code were. The hint to write a function to create the pattern first was very helpful, as was rewatching the homework help from Thursday on how to build shapes. I would like to get better at understanding how to effectively use a loop, especially the counters. I had difficulty with understanding how to reverse the counters correctly when building the top part of the X pattern after building the bottom portion. I actually really enjoyed the concept of this homework, especially the video explaining an example of our goal. More specifically, I like breaking down the code into separate functions and seeing the end result when all of it comes together. 
