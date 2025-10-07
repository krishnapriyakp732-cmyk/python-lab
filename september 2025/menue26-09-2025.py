while True:
    print("\nMenu:")
    print("1.Word occurrence count")
    print("2.Character frequency count")
    print("3.Display factors of a number")
    print("4.Exit")
    choice=input("Enter your choice (1-4): ")
    if choice=='1':
        text=input("Enter text: ")
        words=text.split()
        freq={}
        for word in words:
            word=word.lower()
            if word in freq:
                freq[word]+=1
            else:
                freq[word]=1
        print("Word occurrence:")
        for word, count in freq.items():
            print(f"{word}: {count}")
    elif choice=='2':
        text=input("Enter text: ")
        freq={}
        for char in text:
            if char.isalnum():
                char=char.lower()
                if char in freq:
                    freq[char]+=1
                else:
                    freq[char]=1
        print("Character frequencies:")
        for char, count in freq.items():
            print(f"{char}: {count}")
    elif choice=='3':
        num_str=input("Enter a number: ")
        if num_str.isdigit():
            num = int(num_str)
            factors=[]
            for i in range(1,num+1):
                if num%i==0:
                    factors.append(i)
            print(f"Factors of {num}: {factors}")
        else:
            print("Please enter a valid integer.")

    elif choice=='4':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please select from 1 to 4.")
