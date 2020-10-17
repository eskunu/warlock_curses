from matplotlib import pyplot as plt

def curses():
    curse_of_agony = (1044 + 300 / 3) / 24 # 1044 is raw damage from agony, 300 is spellpower increase, the spellpower coefficient is 100% so we just divide by 3 per tick, then divide the whole by 24 for per second.
    curse_elements = .1 # increased shadow, frost, and fire damage. Even though this is labeled Elements we include Curse of Shadow since the attributes are the same.
    caster_dps = 300 # average for cloth casters across a large variety of boss fights in raids # Includes AQ for Mages and Warlocks
    melee_dps = 210
    reck_list = []
    element_list = []
    agony_list = []
    armor = 3731 # armor of the boss # WoW Classic 1.12 values
    ar = 100 / ( ( 467.5 * 60 - 22167.5 ) / armor + 1 ) # armor reduction as percent this is about 44% physical damage reduction from level 60 player
    ar_curse = 100 / ( ( 467.5 * 60 - 22167.5 ) / (armor - 640) + 1 ) # this is ar after adding the curse of recklessness
    print(ar, ar_curse, ar / (ar - ar_curse))
    for i in range(10):
        ap = - ar / (ar_curse - ar)
        spellboost = i * caster_dps * curse_elements
        apboost = i * melee_dps * ap / 100
        c = i * curse_of_agony
        reck_list.append(apboost)
        element_list.append(spellboost)
        agony_list.append(c)

    plt.xlabel("Number of Players")
    plt.ylabel("Increased Raid Damage Per Second")
    plt.plot(reck_list, label='Curse of Recklessness')
    plt.plot(element_list, label='Curse of the Elements / Shadow')
    plt.plot(agony_list, label='Curse of Agony')
    plt.legend()
    plt.show()

curses()
