grid = [
    ["C", "D", "N", "L", "O", "V", "E", "D", "M", "H", "C", "L", "O", "U", "D"],
    ["O", "R", "I", "I", "M", "C", "H", "E", "A", "N", "Y", "T", "D", "D", "S"],
    ["O", "A", "A", "R", "H", "D", "R", "E", "T", "M", "B", "H", "T", "C", "B"],
    ["L", "M", "H", "A", "D", "O", "O", "P", "H", "L", "E", "A", "T", "A", "I"],
    ["M", "A", "C", "H", "I", "N", "E", "L", "E", "A", "R", "N", "I", "N", "G"],
    ["A", "D", "K", "I", "N", "G", "S", "E", "M", "H", "S", "F", "S", "F", "D"],
    ["T", "S", "C", "B", "Y", "T", "E", "A", "A", "A", "E", "H", "T", "A", "A"],
    ["P", "D", "O", "L", "Y", "F", "T", "R", "T", "P", "C", "K", "A", "C", "T"],
    ["L", "Z", "L", "J", "F", "R", "K", "N", "I", "P", "U", "R", "T", "E", "A"],
    ["O", "T", "B", "H", "A", "R", "O", "I", "C", "Y", "R", "E", "I", "B", "W"],
    ["T", "S", "J", "H", "O", "H", "F", "N", "S", "S", "I", "M", "S", "O", "G"],
    ["L", "O", "Z", "W", "T", "S", "H", "G", "H", "G", "T", "S", "T", "O", "Q"],
    ["I", "Q", "T", "Y", "D", "G", "A", "N", "A", "L", "Y", "T", "I", "C", "S"],
    ["B", "E", "P", "A", "N", "D", "A", "S", "K", "K", "T", "L", "C", "Z", "D"],
    ["N", "Z", "R", "B", "L", "O", "C", "K", "C", "H", "A", "I", "S", "M", "F"]
]
start_r = 0
start_c = 0
current_r = 0
current_c = 0
searched_word = input("Enter word to find: ").upper() #accept lower and upper case letters
found = False
fail = True
for row in range(len(grid)):
    for column in range(len(grid[row])):
        if searched_word[0] == grid[row][column]: #search for 1st letter/letter with index 0
            found = True
            start_r = row
            start_c = column
            current_r = row
            current_c = column
            for i in range(len(searched_word)): #search for all letters of the searched word
                if current_c >= len(grid[row]) or current_c < 0 or current_r >= len(grid) or current_r <0 or \
                        searched_word[i] != grid[current_r][current_c]: #conditions if rows or columns are out of grid range or letter has not been found
                    found = False
                current_c += 1 # horizontal search, shift column by 1
            if found:
                print(f'{searched_word} has been found in position {start_r} {start_c} in → direction')
                fail = False

            #top to bottom
            found = True
            current_r = row
            current_c = column
            for i in range(len(searched_word)): #search for all letters of the searched word
                if current_c >= len(grid[row]) or current_c < 0 or current_r >= len(grid) or current_r < 0 or \
                        searched_word[i] != grid[current_r][current_c]: #conditions if rows or columns are out of grid range or letter has not been found
                    found = False
                current_r += 1 # vertical search top to bottom, shift row by 1
            if found:
                print(f'{searched_word} has been found in position {start_r} {start_c} in ↓ direction')
                fail = False

            #bottom to top
            found = True
            current_r = row
            current_c = column
            for i in range(len(searched_word)): #search for all letters of the searched word
                if current_c >= len(grid[row]) or current_c < 0 or current_r >= len(grid) or current_r < 0 or \
                        searched_word[i] != grid[current_r][current_c]: #conditions if rows or columns are out of grid range or letter has not been found
                    found = False
                current_r -= 1 # vertical search bottom to top, shift row by - 1
            if found:
                print(f'{searched_word} has been found in position {start_r} {start_c} in ↑ direction')
                fail = False

            #diagonal: top to bottom
            found = True
            current_r = row
            current_c = column
            for i in range(len(searched_word)): #search for all letters of the searched word
                if current_c >= len(grid[row]) or current_c < 0 or current_r >= len(grid) or current_r < 0 or \
                        searched_word[i] != grid[current_r][current_c]: #conditions if rows or columns are out of grid range or letter has not been found
                    found = False
                current_r += 1 # diagonal search top to bottom, shift row and column by 1
                current_c += 1
            if found:
                print(f'{searched_word} has been found in position {start_r} {start_c} in ⬊ direction')
                fail = False

            #diagonal: bottom to top
            found = True
            current_r = row
            current_c = column
            for i in range(len(searched_word)): #search for all letters of the searched word
                if current_c >= len(grid[row]) or current_c < 0 or current_r >= len(grid) or current_r < 0 or \
                        searched_word[i] != grid[current_r][current_c]: #conditions if rows or columns are out of grid range or letter has not been found
                    found = False
                current_r -= 1 # diagonal search bottom to top, shift row by - 1 and column by 1
                current_c += 1
            if found:
                print(f'{searched_word} has been found in position {start_r} {start_c} in ⬈ direction')
                fail = False

if fail: #search has not been successful, print out the message
    print(f'Oops, I could not find {searched_word} in the grid')



