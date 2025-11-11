print("Student ulgerimin bakylau zhuyesi")
student_aty = input("Student aty-zhoni: ").strip()
pan_sany = int(input("Pander sany: ").strip())
pander = []
for i in range(pan_sany):
    pan_atau = input(f"{i+1}-pan atauy: ").strip()
    ball = int(input(f"{pan_atau} boyynsha ball (0-100): ").strip())
    pander.append((pan_atau, ball))
barlik_ballar = [b for _, b in pander]
ortasha_ball = sum(barlik_ballar) / len(barlik_ballar)
en_joqary = max(barlik_ballar)
en_tomen = min(barlik_ballar)
ozgeris_bar = (en_joqary - en_tomen) >= 20
otti_me = ortasha_ball >= 50
if ortasha_ball >= 90:
    gpa = 4.0
elif ortasha_ball >= 80:
    gpa = 3.0
elif ortasha_ball >= 70:
    gpa = 2.0
elif ortasha_ball >= 60:
    gpa = 1.0
else:
    gpa = 0.0
print("\n=== Bastapqy natizhe ===")
print("Student:", student_aty)
print("Ortascha ball:", round(ortasha_ball, 2))
print("GPA:", gpa)
pan_ataulary = [p[0] for p in pander]
print("\nPander tizimi:", pan_ataulary)
izdew_sozi = input("\nQandai pan izdeisin?: ").strip().lower()
bar = False
for pan, b in pander:
    if izdew_sozi in pan.lower():
        print(f"Tabyldy: {pan} ({b} ball)")
        bar = True
if not bar:
    print("Munday pan tabylmady")
pander_dict = {p[0]: p[1] for p in pander}
while True:
    print("\n=== MENIU ===")
    print("1 - bar panderdi korsetu")
    print("2 - jana pan qosyp, ball engizu")
    print("3 - ortasha ball esepteu")
    print("4 - en joqary men en tomen balldy korsetu")
    print("0 - shygu")
    tandau = input("Tandau: ").strip()
    if tandau == "1":
        if not pander_dict:
            print("Bos tizim")
        else:
            for atau, ball in pander_dict.items():
                print(f"{atau}: {ball} ball")
    elif tandau == "2":
        atau = input("Pan atauy: ").strip()
        ball = int(input("Ball (0-100): ").strip())
        pander_dict[atau] = ball
        print("Pan qosyldy")
    elif tandau == "3":
        if not pander_dict:
            print("Aldymen pander qosyńyz")
        else:
            ort = sum(pander_dict.values()) / len(pander_dict)
            print(f"Ortascha ball: {ort:.2f}")
    elif tandau == "4":
        if not pander_dict:
            print("Pander joq")
        else:
            en_joqary = max(pander_dict.values())
            en_tomen = min(pander_dict.values())
            print(f"En joqary ball: {en_joqary}, En tomen: {en_tomen}")
    elif tandau == "0":
        print("Sau bolynyz")
        break
    else:
        print("Durys emes tandau. Qaita engiziniz.")
        import csv
from typing import Dict, List, Tuple
Record = Dict[str, int]
Dataset = Dict[str, Record]
def add_record(db: Dataset, student: str, subject: str, score: int) -> None:
    if student not in db:
        db[student] = {}
    db[student][subject] = score
def remove_record(db: Dataset, student: str, subject: str) -> bool:
    if student in db and subject in db[student]:
        del db[student][subject]
        return True
    return False
def show_records(db: Dataset, student: str) -> List[Tuple[str, int]]:
    if student not in db:
        return []
    return sorted(db[student].items(), key=lambda x: x[0].lower())
def find_records(db: Dataset, student: str, query: str) -> List[Tuple[str, int]]:
    query = query.lower()
    return [(s, b) for s, b in show_records(db, student) if query in s.lower()]
def average_score(scores: List[int]) -> float:
    return sum(scores) / len(scores) if scores else 0.0
def sum_recursive(nums: List[int]) -> int:
    if not nums:
        return 0
    return nums[0] + sum_recursive(nums[1:])
def gpa_from_average(avg: float) -> float:
    if avg >= 90:
        return 4.0
    if avg >= 80:
        return 3.0
    if avg >= 70:
        return 2.0
    if avg >= 60:
        return 1.0
    return 0.0
def save_to_txt(db: Dataset, path: str) -> None:
    with open(path, "w", encoding="utf-8") as f:
        for student, rec in db.items():
            for subject, score in rec.items():
                f.write(f"{student} | {subject} | {score}\n")
def save_to_csv(db: Dataset, path: str) -> None:
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["student", "subject", "score"])
        for student, rec in db.items():
            for subject, score in rec.items():
                writer.writerow([student, subject, score])
def load_from_csv(path: str) -> Dataset:
    db: Dataset = {}
    try:
        with open(path, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                student = (row.get("student") or "").strip()
                subject = (row.get("subject") or "").strip()
                score_str = (row.get("score") or "").strip()
                if not (student and subject and score_str.isdigit()):
                    continue
                add_record(db, student, subject, int(score_str))
    except FileNotFoundError:
        return {}
    return db