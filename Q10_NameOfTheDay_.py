day = int(input())
days = {
    1: "Sunday",
    2: "Monday",
    3: "Tuesday",
    4: "Wednesday",
    5: "Thursday",
    6: "Friday",
    7: "Saturday"
}
if 1 <= day<= 7:
    print("yes", days[day])
else:
    print("no")
