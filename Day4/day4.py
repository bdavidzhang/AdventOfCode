def test_case(cmd,result):
    assert cmd == result, f"Should be {result}, is {cmd}"
    
def compare_ranges(range1,range2):
    r1 = [int(el) for el in range1.split("-")]
    r2 = [int(el) for el in range2.split("-")]

    if ((r1[0] >= r2[0]) & (r1[1] <= r2[1])):
        return True
    elif ((r1[0] <= r2[0]) & (r1[1] >= r2[1])):
        return True
    else:
        return False

def compare_intersections(range1,range2):
    r1 = [int(el) for el in range1.split("-")]
    r2 = [int(el) for el in range2.split("-")]
   
    l1 = [i for i in range(r1[0],r1[1]+1)] 
    l2 = [i for i in range(r2[0],r2[1]+1)]
    s1 = set(l1)
    s2 = set(l2)
    
    if not s1.intersection(s2):
        return False
    else:
        return True

print(test_case(compare_ranges("1-3","2-5"),False))
print(test_case(compare_ranges("1-6","2-5"),True))

print(test_case(compare_intersections("6-10","1-5"),False))
print(test_case(compare_intersections("1-6","2-5"),True))

   
def camp_cleanup(input_file):
    with open(input_file,"r+") as f:
        ranges = [line.split(",") for line in f.readlines()]

        fully_contain = [compare_ranges(r[0],r[1]) for r in ranges]

        return sum(fully_contain)

def camp_cleanup2(input_file):
    with open(input_file,"r+") as f:
        ranges = [line.split(",") for line in f.readlines()]

        contain = [compare_intersections(r[0],r[1]) for r in ranges]
        
        return sum(contain)

print(camp_cleanup('Day4/day4.in'))
print(camp_cleanup2('Day4/day4.in'))