1. Iterate through an array without repeting the elements.
-> e.g: lst1 = [101,102,103,104]
        for i in range(len(lst1)):
            for j in range(i+1,len(lst1))
            print(lst1[i] , lst[j])

2.Palindrome int checker question
->  x % 10 gives the last digit of integer x [but it doent remove that last digit from it]
    x // 10 removes the last digit of integer x
    new_number * 10 + last_digit this formula adds that last digit to new digit

        if x < 0:
            return False 
        new_number = 0
        old_x = x
        while x != 0:
            new_digit = x % 10
            new_number = new_number * 10  + new_digit
            x = x // 10
        return new_number == old_x