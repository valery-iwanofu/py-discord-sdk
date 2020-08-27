import time

import discordsdk as dsdk


# we get the application id from a file
with open("application_id.txt", "r") as file:
    applicationId = int(file.read())

# we create the discord instance
app = dsdk.Discord(applicationId,  dsdk.CreateFlags.Default)
userManager = app.GetUserManager()


# events
def onCurrentUserUpdate():
    print("[onCurrentUserUpdate]")
    user = userManager.GetCurrentUser()
    print(f"hello, {user.Username}#{user.Discriminator}!")

    premiumType = userManager.GetCurrentUserPremiumType()
    if premiumType == dsdk.PremiumType.None_:
        print("you are not a nitro subscriber :(")
    elif premiumType == dsdk.PremiumType.Tier1:
        print("you are a nitro classic subscriber!")
    elif premiumType == dsdk.PremiumType.Tier2:
        print("you are a nitro subscriber!")

    if userManager.CurrentUserHasFlag(dsdk.UserFlag.HypeSquadHouse1):
        print("you are a member of house bravery")
    if userManager.CurrentUserHasFlag(dsdk.UserFlag.HypeSquadHouse2):
        print("you are a member of house brillance")
    if userManager.CurrentUserHasFlag(dsdk.UserFlag.HypeSquadHouse3):
        print("you are a member of house balance")


# bind events
userManager.OnCurrentUserUpdate = onCurrentUserUpdate


def callback(result, user):
    if result != dsdk.Result.Ok:
        print("we failed to get user (result " + str(result) + ")")
    else:
        print("we have found the user! " + str(user.Username) + "#" + str(user.Discriminator))


# we search for the owner of the repo
userManager.GetUser(336834315130503169, callback)

while 1:
    time.sleep(1/10)
    app.RunCallbacks()
