import subprocess

# Get metadata of saved Wi-Fi profiles
data = subprocess.check_output(
    ["netsh", "wlan", "show", "profiles"],
    stderr=subprocess.DEVNULL
).decode("utf-8", errors="ignore").split("\n")

profiles = []

# Extract profile names
for line in data:
    if "All User Profile" in line:
        profiles.append(line.split(":")[1].strip())

print("{:<30} | {:<}".format("Wi-Fi Name", "Password"))
print("-" * 50)

# Loop through profiles and get passwords
for profile in profiles:
    try:
        results = subprocess.check_output(
            ["netsh", "wlan", "show", "profile", profile, "key=clear"],
            stderr=subprocess.DEVNULL
        ).decode("utf-8", errors="ignore").split("\n")

        password = ""

        for line in results:
            if "Key Content" in line:
                password = line.split(":")[1].strip()
                break

        print("{:<30} | {:<}".format(profile, password))

    except Exception:
        print("{:<30} | {:<}".format(profile, "ERROR"))
