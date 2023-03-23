points = {1:"AEIOULNSTRАВЕИНОРСТ",
                2:"DGДКЛМПУ",
                3:"BCMPБГЁЬЯ",
                4:"FHVWYЙЫ",
                5:"KЖЗХЦЧ",
                8:"JXШЭЮ",
                10:"QZФЩЪ"}
count = 0
word = input().upper()
for i in word:
    for k, v in points.items():
        if i in v:
            count+=k
print(count)


