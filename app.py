from game_pkg.visual_class import *
village_man = Visual("village_man")
title = Visual("title")
warning = Visual("warning")
guide = Visual("guide")
warrior_title = Visual("warrior")
endtitle = Visual("end")

termcheck()
warning.show_image("midcenter")
time.sleep(3)
title.expandmidborder(.025, .2, .025,
                      "------------------ Press Enter to Continue ------------------")
input()
title.image_exit_border(.025, "right")


time.sleep(2)
guide.image_enter_border(.025, "left")
time.sleep(1)
scrolltext("The Guide:", .025)
print("\n")
scrolltext(
    "Welcome Adventurer.", .025)
time.sleep(1)
print("\n")
scrolltext(
    "This realm is but merely a test, and I am here to guide you through this test.", .025)
print("\n")
print("Press Enter to Continue".center(columns))
input()
guide.image_exit_border(.025, "right")
time.sleep(1)
warrior_title.image_enter_border(.025, "right")
time.sleep(1)
scrolltext("The Guide:", .025)
print("\n")
scrolltext(
    "The Warrior role is one of many roles that you will be able to choose from", .025)
scrolltext("once I actually get around to creating them.", .025)
print("\n")
print("Press Enter to Continue".center(columns))
input()
warrior_title.image_exit_border(.025, "right")
time.sleep(.5)
village_man.image_enter_border(.025, "left")
time.sleep(.5)
scrolltext("The Guide:", .025)
print("\n")
scrolltext(
    "This is a Villager that you will either eventually save or kill.", .025)
time.sleep(.5)
scrolltext("It all depends on what type of Adventurer you'd like to be.", .025)
print("\n")
print("Press Enter to Continue".center(columns))
input()
time.sleep(1)
village_man.show_image_border()
scrolltext("The Villager:", .025)
print("\n")
# time.sleep(.5)
scrolltext(
    "Please don't kill me mister... I'm just trying to feed my children...", .025)
print('\n')
print("Press Enter to Continue".center(columns))
input()
village_man.image_exit_border(.025, "left", 5)
guide.image_enter_border(.025, "left", 5)
time.sleep(.5)
scrolltext("The Guide:", .025)
print("\n")
scrolltext("Don't mind him, he's just being dramatic", .025)
print("\n")
print("Press Enter to Continue".center(columns))
input()
guide.show_image_border()
scrolltext("The Guide:", .025)
time.sleep(.5)
print("\n")
scrolltext(
    "I hope you enjoyed this guide through the realm of World of Python", .025)
time.sleep(1)
scrolltext("Hopefully the next time you come we will have more to offer.", .025)
print("\n")
print("Press Enter to Continue".center(columns))
input()
guide.image_exit_border(.025, "right")
time.sleep(.5)
endtitle.image_enter_border(.025, "right")
print("\n")
print("\n")
print("Press enter to exit".center(columns))
input()
