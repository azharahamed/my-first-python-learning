# Chapter 8 - Exercises 5 - Start

# import sys

def workout_coach(lift_name, wt):
    print("Time to", lift_name, wt, "pounds! You got this!")

def main():
    # sys.setExecutionLimit(120000) # keep program from timing out
    lifts = ["squat", "bench", "deadlift"]
    for lift in lifts:
        weight = 10
        user_input = "Yes"
        while user_input == 'Yes' or user_input == 'yes':
            if lift == "bench" and weight > 200:
                break
            else:
                workout_coach(lift, weight)
                weight += 10
            user_input = input("Keep doing the " + lift + "? Enter yes for the next set.")

    # Your code here

if __name__ == "__main__":
    main()
# Chapter 8 - Exercises 5 - End
# import sys

# def workout_coach(lift_name, wt):
#     print("Time to", lift_name, wt, "pounds! You got this!")

# def main():
#     # sys.setExecutionLimit(120000)
#     lifts = ["squat", "bench", "deadlift"]
#     for lift in lifts:
#         keep_lifting = "yes"
#         weight = 0
#         input_prompt = "Keep doing the " + lift + "? Enter yes for the next set."
#         while keep_lifting == "yes":
#             weight = weight + 10
#             if lift == "bench" and weight > 200:
#                 break
#             else:
#                 workout_coach(lift, weight)
#             keep_lifting = input(input_prompt)

# if __name__ == "__main__":
#     main()




# Chapter 8  - Exercises 6 

# from PIL import Image

# img = Image.open("cy.png")

# for row in range(img.height):
#     for col in range(img.width):
#         r,g,b = img.getpixel((col,row))
#         img.putpixel((col,row),(0, g, b))
# img.show()


# Chapter 8  - Exercises 6  End

# img.draw(win)
# win.exitonclick()



# from PIL import Image ImageWin

# img = Image.open('cy.png')
# win = Image.ImageWin(img.getwidth(),img.getHeight())
# img.draw(win)
# img.setDelay(1, 15)

# for row in range(img.getHeight()):
#   for col in range(img.getwidth()):
#     p=img.getPixel(col,row)

#     r = p.getRed()
#     g = p.getGreen()
#     b = p.getBlue()

#     grey = (r+g+b / 3)
#     new_r = new_g = new_b = grey
    
#     new_pixel = image.Pixel(new_r,new_g,new_b)

#     img.setPixel(col, row, new_pixel)
    
# img.draw(win)
# win.exitonclick()







    