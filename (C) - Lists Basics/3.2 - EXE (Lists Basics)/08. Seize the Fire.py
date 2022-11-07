input_fires_in_list = input().split("#")
water_in_liters = int(input())
type_n_list = []
level_in_list = []
effort = 0
total_fire = 0
for element in input_fires_in_list:
    current_element = element.split(" = ")
    type_n_list.append(current_element[0])
    level_in_list.append(int(current_element[1]))
print("Cells:")
for index, value in enumerate(type_n_list):
    if value == "High" or value == "Medium" or value == "Low":
        if value == "High":
            if 81 <= level_in_list[index] <= 125:
                if water_in_liters - level_in_list[index] < 0:
                    continue
                else:
                    water_in_liters -= level_in_list[index]
                    effort += level_in_list[index] * 0.25
                    total_fire += level_in_list[index]
                    print(f"- {level_in_list[index]}")
            else:
                continue
        elif value == "Medium":
            if 51 <= level_in_list[index] <= 80:
                if water_in_liters - level_in_list[index] < 0:
                    continue
                else:
                    water_in_liters -= level_in_list[index]
                    effort += level_in_list[index] * 0.25
                    total_fire += level_in_list[index]
                    print(f"- {level_in_list[index]}")
            else:
                continue
        elif value == "Low":
            if 1 <= level_in_list[index] <= 50:
                if water_in_liters - level_in_list[index] < 0:
                    continue
                else:
                    water_in_liters -= level_in_list[index]
                    effort += level_in_list[index] * 0.25
                    total_fire += level_in_list[index]
                    print(f"- {level_in_list[index]}")
            else:
                continue
    else:
        continue
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")


# fireLevel = input().split("#")
# waterQty = int(input())
# effort = 0
# fireList = []
# for fire in fireLevel:
#     currentCell = fire.split(" = ")
#     typeOfFire = currentCell[0]
#     valueOfCell = int(currentCell[1])
#     if "High" in typeOfFire and 81 <= valueOfCell <= 125:
#         if waterQty - valueOfCell >= 0:
#             effort += valueOfCell * 0.25
#             waterQty -= valueOfCell
#             fireList.append(valueOfCell)
#         else:
#             continue
#     elif "Medium" in typeOfFire and 51 <= valueOfCell <= 80:
#         if waterQty - valueOfCell >= 0:
#             effort += valueOfCell * 0.25
#             waterQty -= valueOfCell
#             fireList.append(valueOfCell)
#         else:
#             continue
#     elif "Low" in typeOfFire and 1 <= valueOfCell <= 50:
#         if waterQty - valueOfCell >= 0:
#             effort += valueOfCell * 0.25
#             waterQty -= valueOfCell
#             fireList.append(valueOfCell)
#         else:
#             continue
#     else:
#         continue
# print(f"Cells:")
# for cell in fireList:
#     print(f" - {int(cell)}", end="\n")
# print(f"Effort: {effort:.2f}")
# print(f"Total Fire: {sum(fireList)}")
