from matplotlib import pyplot as plt

def curses():
    curse_agony = (1044 + 500 / 3) / 24 # 1044 is raw damage from agony, 500 is spellpower increase, the spellpower coefficient is 100% so we just divide by 3 per tick, then divide the whole by 24 for per second.
    curse_elements = .1 # increased shadow, frost, and fire damage. Even though this is labeled Elements we include Curse of Shadow since the attributes are the same.
    caster_dps = 300 # average dps for cloth casters across a large variety of boss fights in raids # Includes AQ for Mages and Warlocks
    melee_dps = 210
    curse_doom = (3200 + 500) / 60
    reck_list = []
    element_list = []
    agony_list = []
    doom_list = []
    armor = 3731 # armor of the boss # WoW Classic 1.12 values
    ar = 100 / ( ( 467.5 * 60 - 22167.5 ) / armor + 1 ) # armor reduction as percent this is about 38.8% physical damage reduction from level 60 player
    ar_curse = 100 / ( ( 467.5 * 60 - 22167.5 ) / (armor - 640) + 1 ) # this is ar after adding the curse of recklessness which is about 34.4%
    ap = ar / (ar - ar_curse) # The amount of increased damage after calculated the reduction of armor on the boss/mob
    for i in range(10):
        physical = i * melee_dps * ap / 100
        spell = i * caster_dps * curse_elements
        coa = i * curse_agony
        cod = i * curse_doom
        reck_list.append(physical)
        element_list.append(spell)
        agony_list.append(coa)
        doom_list.append(cod)

    plt.xlabel("Number of Players")
    plt.ylabel("Increased Raid Damage Per Second")
    plt.plot(reck_list, label='Curse of Recklessness')
    plt.plot(element_list, label='Curse of the Elements / Shadow')
    plt.plot(doom_list, label='Curse of Doom')
    plt.plot(agony_list, label='Curse of Agony')
    plt.title("Increased Damage of Warlock Curses")
    plt.legend()
    plt.show()

curses()
