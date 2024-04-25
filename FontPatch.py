import os
import getpass

old = ['GothamSSm-Black.otf', 'GothamSSm-Bold.otf', 'GothamSSm-Book.otf', 'GothamSSm-Medium.otf']
new = ['BuilderSans-ExtraBold.otf', 'BuilderSans-Bold.otf', 'BuilderSans-Regular.otf', 'BuilderSans-Medium.otf']
usr = getpass.getuser()

os.system("cls")
print("[Roblox Font Patcher]")
print("Out with the new, and in with the old.")
print("Patch your Roblox fonts today!")
input("\nPress ENTER to get started. ")

os.system("cls")
print("[Client Detector]")
print("Only clients with installed Roblox versions will be detected.")
if os.path.exists(f"C:/Users/{usr}/AppData/Local/Roblox/Versions"):
    if len(os.listdir(f"C:/Users/{usr}/AppData/Local/Roblox/Versions")) > 0:
        print("  - Roblox Player detected.")
if os.path.exists(f"C:/Users/{usr}/AppData/Local/Bloxstrap/Versions"):
    if len(os.listdir(f"C:/Users/{usr}/AppData/Local/Bloxstrap/Versions")) > 0:
        print("  - Bloxstrap detected.")
client = input("\nWhich client should be patched? ")
if "bloxstrap" in client.lower():
    if len(os.listdir(f"C:/Users/{usr}/AppData/Local/Bloxstrap/Versions")) == 0:
        input("ERROR: No valid Roblox version was detected. ")
        exit()
    versionId = os.listdir(f"C:/Users/{usr}/AppData/Local/Bloxstrap/Versions")[0]
    versionPath = f"C:\\\\Users\\\\{usr}\\\\AppData\\\\Local\\\\Bloxstrap\\\\Versions\\\\{versionId}\\\\content\\\\fonts"
elif "roblox" in client.lower():
    if len(os.listdir(f"C:/Users/{usr}/AppData/Local/Roblox/Versions")) == 0:
        input("ERROR: No valid Roblox version was detected. ")
        exit()
    versionId = os.listdir(f"C:/Users/{usr}/AppData/Local/Roblox/Versions")[0]
    versionPath = f"C:\\\\Users\\\\{usr}\\\\AppData\\\\Local\\\\Bloxstrap\\\\Versions\\\\{versionId}\\\\content\\\\fonts"

os.system("cls")
print("Patching fonts...\n")

# If renamed Gotham fonts are present in the "Patch" folder, use this code!
# Also use this if Roblox removes their old fonts (but they probably won't!)
#os.system(f"copy .\\Patch\\BuilderSans-Regular.otf {versionPath} /Y >NUL 2>&1")
#os.system(f"copy .\\Patch\\BuilderSans-Medium.otf {versionPath} /Y >NUL 2>&1")
#os.system(f"copy .\\Patch\\BuilderSans-Bold.otf {versionPath} /Y >NUL 2>&1")
#os.system(f"copy .\\Patch\\BuilderSans-ExtraBold.otf {versionPath} /Y >NUL 2>&1")
#input("Done patching fonts! ")

os.system(f"copy {versionPath}\\{old[0]} {versionPath}\\{new[0]} /Y >NUL 2>&1")
print("Copied font 1/4")
os.system(f"copy {versionPath}\\{old[1]} {versionPath}\\{new[1]} /Y >NUL 2>&1")
print("Copied font 2/4")
os.system(f"copy {versionPath}\\{old[2]} {versionPath}\\{new[2]} /Y >NUL 2>&1")
print("Copied font 3/4")
os.system(f"copy {versionPath}\\{old[3]} {versionPath}\\{new[3]} /Y >NUL 2>&1")
print("Copied font 4/4")
input("\nDone patching fonts! ")