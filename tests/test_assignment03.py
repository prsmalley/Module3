import subprocess
import sys

# Module 3 is about conditionals, so the autograder feeds specific inputs and
# checks that the correct branch runs. The program reads input in this order:
#   Task 1: dog age              (1 value)
#   Task 2: a number 1-20        (1 value)
#   Task 3: three side lengths   (3 values)
#   Task 4: num, then check      (2 values)
# Whole numbers are used so each value is valid for both int() and float().

def run(values):
    result = subprocess.run(
        [sys.executable, 'assignment03.py'],
        input="\n".join(values) + "\n",
        capture_output=True, text=True
    )
    return result.stdout, result.returncode

def test_runs_without_errors():
    _, returncode = run(["2", "5", "5", "5", "5", "10", "5"])
    assert returncode == 0, "Code crashed — remember to convert input() with int()/float() before comparing or doing math."

def test_all_sections_present():
    output, _ = run(["2", "5", "5", "5", "5", "10", "5"])
    for label in ('Task 01', 'Task 02', 'Task 03', 'Task 04'):
        assert label in output, f"Missing section: {label}."

def test_task01_dog_years():
    # A 2-year-old dog = 2 * 10.5 = 21.0 human years.
    output, _ = run(["2", "5", "6", "8", "12", "10", "5"])
    assert "21" in output, "Task 01: a 2-year-old dog should be 21.0 human years."

def test_task03_equilateral():
    output, _ = run(["2", "5", "5", "5", "5", "10", "5"])
    assert "equilateral" in output.lower(), "Task 03: sides 5, 5, 5 should be reported as equilateral."

def test_task03_scalene():
    output, _ = run(["2", "5", "6", "8", "12", "10", "3"])
    assert "scalene" in output.lower(), "Task 03: sides 6, 8, 12 should be reported as scalene."

def test_task04_divides_evenly():
    # 10 % 5 == 0, so the program should say it divides evenly.
    output, _ = run(["2", "5", "5", "5", "5", "10", "5"])
    assert "even" in output.lower(), "Task 04: 10 divided by 5 should be reported as dividing evenly."

if __name__ == '__main__':
    tests = [
        test_runs_without_errors,
        test_all_sections_present,
        test_task01_dog_years,
        test_task03_equilateral,
        test_task03_scalene,
        test_task04_divides_evenly,
    ]
    passed = 0
    for test in tests:
        try:
            test()
            print(f"  ✅ PASSED: {test.__name__}")
            passed += 1
        except AssertionError as e:
            print(f"  ❌ FAILED: {test.__name__} — {e}")

    print(f"\n{passed}/{len(tests)} checks passed.")
    if passed < len(tests):
        sys.exit(1)  # Causes the Action to show as failed in GitHub
