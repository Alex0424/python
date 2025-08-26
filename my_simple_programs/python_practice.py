from typing import Iterable, Tuple, Set


def quiz_category(title: str, answers: Iterable[str]) -> Tuple[int, int]:
    """Ask the user to name the given category's types.

    Returns (correct_count, total_in_category).
    """
    remaining: Set[str] = {a.lower() for a in answers}
    seen: Set[str] = set()
    total = len(remaining)

    plural = "types" if total != 1 else "type"
    print(f"\nWhat are the {total} {title} {plural}?")

    for i in range(1, total + 1):
        ans = input(f"{i}: ").strip().lower()

        if ans in remaining:
            remaining.remove(ans)
            seen.add(ans)
            print("✅ Correct")
        elif ans in seen:
            print("💀💀💀💀💀 Already entered that.")
        else:
            print("💀 None of them")

    if remaining:
        missed = ", ".join(sorted(remaining))
        print(f"Missed: {missed}")
        return total - len(remaining), total

    print("All correct! ✨")
    return total, total


def main() -> None:
    categories = [
        ("numeric", ["int", "float", "complex"]),
        ("boolean", ["bool"]),
        ("text sequence", ["str"]),
        ("sequence (non-text)", ["list", "tuple", "range"]),
        ("set", ["set", "frozenset"]),
        ("binary sequence", ["bytes", "bytearray", "memoryview"]),
        ("mapping", ["dict"]),
        ("null/sentinel", ["None"]),
    ]

    total_correct = 0
    total_possible = 0

    print("Python Built-in Types Quiz")
    print("-" * 28)

    for title, answers in categories:
      correct, possible = quiz_category(title, answers)
      total_correct += correct
      total_possible += possible

    print("\nDone.")
    print(f"Score: {total_correct}/{total_possible}")


if __name__ == "__main__":
    main()
