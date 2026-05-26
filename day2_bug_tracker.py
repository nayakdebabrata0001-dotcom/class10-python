print("=== Bug Severity Checker ===")
bug = input("Bug type: syntax/logic/crash: ")
severity = int(input("Severity 1-5: "))

if bug == "crash" and severity >= 4:
    print("P0 - Fix now! Call senior dev")
elif bug == "logic" and severity >= 3:
    print("P1 - Fix today")
elif bug == "syntax":
    print("P2 - Easy fix")
else:
    print("P3 - Backlog it")
