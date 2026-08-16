from pathlib import Path
path=Path("./login_attempts.txt")
fail_counts={}
with open(path,"r",encoding="utf-8") as File:
    for line in File:
        if "FAILED" in line:
            parts=line.split(",")
            user_part=parts[0]
            username=user_part.split(":")[1].strip()

            if username in fail_counts:
                fail_counts[username]+=1
            else:
                fail_counts[username]=1

# --- new part starts here ---
print("Suspicious users (2+ failed attempts):")

for username, count in fail_counts.items():
    if count >= 2:
        print(f"  {username} — {count} failed attempts")