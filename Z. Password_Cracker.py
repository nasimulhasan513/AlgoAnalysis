def passwordCracker(passwords, attempt):
    password_set = set(passwords)
    n = len(attempt)
    can_break = [False] * (n + 1)
    can_break[0] = True
    split_indices = [-1] * (n + 1)

    for i in range(1, n + 1):
        for pw in passwords:
            pw_len = len(pw)
            if i >= pw_len and can_break[i - pw_len] and attempt[i - pw_len:i] == pw:
                can_break[i] = True
                split_indices[i] = i - pw_len
                break

    if not can_break[n]:
        return "WRONG PASSWORD"

    result = []
    idx = n
    while idx > 0:
        prev_idx = split_indices[idx]
        result.append(attempt[prev_idx:idx])
        idx = prev_idx

    return ' '.join(result[::-1])

for _ in range(int(input().strip())):
    n = int(input().strip())
    passwords = input().strip().split()
    attempt = input().strip()
    print(passwordCracker(passwords, attempt))
