from Quiz_question import quiz
score = 0
    
for item in quiz:
    print(item["question"])
    for key, value in item["options"].items():
        print(f"{key}:{value}")
        
    user_choice = input("Enter your answer: ").lower()

    if user_choice == item["answer"]:
        
        print("RIGHT ANSWER")
        
        score += 1
    
    
    else:
        correct_answer = item["answer"]
        
        print(f"WRONG ANSWER. The correct answer is {correct_answer}")
    
print(f"Your final score is: {score}/{len(quiz)}")
        
        
    





#car.update({"color": "blue"})

# car.pop("color")

# car.popitem()




