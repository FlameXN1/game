board_art = """ 1 | 2 | 3
---+---+---
 4 | 5 | 6
---+---+---
 7 | 8 | 9 """
is_running=True
positions = [
    1, 2, 3,
    4, 5, 6,
    7, 8, 9
]

print(f"{positions[0]} {positions[1]} {positions[2]}\n{positions[3]} {positions[4]} {positions[5]}\n{positions[6]} {positions[7]} {positions[8]}")

used_positions=[]

while is_running:
    if positions[0] == positions[1] == positions[2]:
        print(f"{positions[0]} wins!")
        is_running = False
    elif positions[3] == positions[4] == positions[5]:
        print(f"{positions[3]} wins!")
        is_running = False
    elif positions[6] == positions[7] == positions[8]:
        print(f"{positions[6]} wins!")
        is_running = False

    # vertical
    elif positions[0] == positions[3] == positions[6]:
        print(f"{positions[0]} wins!")
        is_running = False
    elif positions[1] == positions[4] == positions[7]:
        print(f"{positions[1]} wins!")
        is_running = False
    elif positions[2] == positions[5] == positions[8]:
        print(f"{positions[2]} wins!")
        is_running = False

    # diagonal
    elif positions[0] == positions[4] == positions[8]:
        print(f"{positions[0]} wins!")
        is_running = False
    elif positions[2] == positions[4] == positions[6]:
        print(f"{positions[2]} wins!")
        is_running = False
    positionx=input("Enter the position of x you want to enter: ")
    if not positionx.isdigit():
        print("You can only input a number from 1 to 9")
        continue
    positionx=int(positionx)
    if positionx<1 or positionx>9:
        print("You can only input a number from 1 to 9")
        continue
    elif positionx in used_positions:
        print(f"Position {positionx} is already used!")
        continue
    x="x"
    New=True
    if New:
        positions[int(positionx)-1]=x
        

        print(f"{positions[0]} {positions[1]} {positions[2]}\n{positions[3]} {positions[4]} {positions[5]}\n{positions[6]} {positions[7]} {positions[8]}")
        used_positions.append(positionx)
        # horizontal
    if positions[0] == positions[1] == positions[2]:
        print(f"{positions[0]} wins!")
        is_running = False
        break
    elif positions[3] == positions[4] == positions[5]:
        print(f"{positions[3]} wins!")
        is_running = False
        break
    elif positions[6] == positions[7] == positions[8]:
        print(f"{positions[6]} wins!")
        is_running = False
        break

    # vertical
    elif positions[0] == positions[3] == positions[6]:
        print(f"{positions[0]} wins!")
        is_running = False
        break
    elif positions[1] == positions[4] == positions[7]:
        print(f"{positions[1]} wins!")
        is_running = False
        break
    elif positions[2] == positions[5] == positions[8]:
        print(f"{positions[2]} wins!")
        is_running = False
        break

    # diagonal
    elif positions[0] == positions[4] == positions[8]:
        print(f"{positions[0]} wins!")
        is_running = False
        break
    elif positions[2] == positions[4] == positions[6]:
        print(f"{positions[2]} wins!")
        is_running = False
        break

    positiono=input("Enter the position of o you want to enter: ")
    if not positiono.isdigit():
        print("You can only input a number from 1 to 9")
        continue
    positiono=int(positiono)
    if positiono<1 or positiono>9:
        print("You can only input a number from 1 to 9")
        continue
    elif positiono in used_positions:
        print(f"Position {positiono} is already used!")
        continue
    o="o"
    New=True
    if New:
        positions[int(positiono)-1]=o
        

        print(f"{positions[0]} {positions[1]} {positions[2]}\n{positions[3]} {positions[4]} {positions[5]}\n{positions[6]} {positions[7]} {positions[8]}")
        used_positions.append(positiono)
    #horizontal
    # horizontal
    if positions[0] == positions[1] == positions[2]:
        print(f"{positions[0]} wins!")
        is_running = False
        break
    elif positions[3] == positions[4] == positions[5]:
        print(f"{positions[3]} wins!")
        is_running = False
        break
    elif positions[6] == positions[7] == positions[8]:
        print(f"{positions[6]} wins!")
        is_running = False
        break

    # vertical
    elif positions[0] == positions[3] == positions[6]:
        print(f"{positions[0]} wins!")
        is_running = False
        break
    elif positions[1] == positions[4] == positions[7]:
        print(f"{positions[1]} wins!")
        is_running = False
        break
    elif positions[2] == positions[5] == positions[8]:
        print(f"{positions[2]} wins!")
        is_running = False
        break

    # diagonal
    elif positions[0] == positions[4] == positions[8]:
        print(f"{positions[0]} wins!")
        is_running = False
        break
    elif positions[2] == positions[4] == positions[6]:
        print(f"{positions[2]} wins!")
        is_running = False
        break
