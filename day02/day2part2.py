import os

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, "input.txt")
with open(filename, encoding="utf-8") as f:
    input_text = f.readlines()
    for index, item in enumerate(input_text):
        input_text[index] = item.strip()

total = 0
for report in input_text:
    report_items = report.split(" ")
    report_items = [int(x) for x in report_items]
    for x in range(len(report_items)):
        temp_report_items = report_items[:x] + report_items[x+1:]
        increasing = temp_report_items[1] > temp_report_items[0]
        for x in range(1, len(temp_report_items)):
            difference = abs(temp_report_items[x]-temp_report_items[x-1])
            if difference > 3 or difference == 0:
                break
            if increasing:
                if temp_report_items[x] < temp_report_items[x-1]:
                    break
            else:
                if temp_report_items[x] > temp_report_items[x-1]:
                    break
        else:
            total += 1
            break

print(total)
