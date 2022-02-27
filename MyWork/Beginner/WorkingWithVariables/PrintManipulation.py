# print("Hello World!\nHello World!\nHello World!")  # Hello World!
                                                     #  Hello World!
                                                     #  Hello World!

# print("Hello" + "Rich")  # HelloRich
# print("Hello" + " Rich")  # Hello Rich
# print("Hello" + " " + "Rich")  # Hello Rich

 print("Hello" + " " + "Rich")  # line 9
                                  #     print("Hello" + " " + "Rich")  # Hello Rich
                                  #     ^
                                  # IndentationError: unexpected indent
