from matplotlib import pyplot as plt

def curses():
    curse_of_agony = (1044 + 300 / 3) / 24
    spellpower = .1 # shadow, frost, and fire damage
    caster_dps = 300 # average for cloth casters across a large variety of boss fights in raids # Includes MC, BWL, and AQ for Mages and Warlocks
    melee_dps = 210
    reck = []
    element = []
    agony = []
    armor = 3731 # armor of the boss # 
    ar = 100 / ( ( 467.5 * 60 - 22167.5 ) / armor + 1 ) # armor reduction as percent this is about 44% physical damage reduction from level 60 player
    ar_curse = 100 / ( ( 467.5 * 60 - 22167.5 ) / (armor - 640) + 1 ) # this is ar after adding the curse of recklessness
    print(ar, ar_curse, ar / (ar - ar_curse))
    for i in range(10):
        ap = - ar / (ar_curse - ar)
        spellboost = i * caster_dps * spellpower
        apboost = i * melee_dps * ap
        c = i * curse_of_agony
        reck.append(apboost)
        element.append(spellboost)
        agony.append(c)

    # plt.xlabel("Number of Players")
    # plt.ylabel("Increased Raid Damage Per Second")
    # plt.plot(reck, label='Curse of Recklessness')
    # plt.plot(element, label='Curse of the Elements / Shadow')
    # plt.plot(agony, label='Curse of Agony')
    # plt.legend()
    # plt.show()

curses()
