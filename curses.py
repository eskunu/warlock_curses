from matplotlib import pyplot as plt

def debuffs():
    # Curses
    curse_agony     = (1044 + 500 / 3) / 24 # 1044 is raw damage from agony, 500 is spellpower increase, the spellpower coefficient is 100% so we just divide by 3 per tick, then divide the whole by 24 for per second. 
    curse_elements  = .1                    # increased shadow, frost, and fire damage. Even though this is labeled Elements we include Curse of Shadow since the attributes are the same.
    curse_doom      = (3200 + 500) / 60     # Base damage is 3200 plus 500 spellpower at 100% coefficient divided by 60 seconds

    # Damage per Second
    dps_caster      = 300 # average dps for cloth casters across a large variety of boss fights in raids # Includes AQ for Mages and Warlocks
    dps_melee       = 300 # average dps for physical dealers across a large variety of boss fights in raids # Includes AQ for hunters, rogues, warriors

    # Plotting coordindate arrays
    list_reck       = []
    list_element    = []
    list_agony      = []
    list_doom       = []
    list_sunder     = []
    list_faerie     = []
    list_expose     = []
    list_expose_imp = []
    list_full_sa    = []
    list_full_iea   = []

    # Boss stats
    boss_armor           = 3731                                                # armor of the boss # WoW Classic 1.12 values
    boss_armor_reduction = 100 / ( ( 467.5 * 60 - 22167.5 ) / boss_armor + 1 ) # armor reduction as percent this is about 38.8% physical damage reduction from level 60 player

    # Calculations for armor reduction changes (result will be % of physical damage reduction for the boss)
    ar_reck     = 100 / ( ( 467.5 * 60 - 22167.5 ) / (boss_armor - 640) + 1 )                 # this is ar after adding the curse of recklessness which is about 34.4% (Reck)
    ar_ff       = 100 / ( ( 467.5 * 60 - 22167.5 ) / (boss_armor - 505) + 1 )                 # faerie fire (FF)
    ar_sa       = 100 / ( ( 467.5 * 60 - 22167.5 ) / (boss_armor - 450 * 5) + 1 )             # sunder armor (SA)
    ar_ea       = 100 / ( ( 467.5 * 60 - 22167.5 ) / (boss_armor - 1700) + 1 )                # expose armor (EA)
    ar_ea_imp   = 100 / ( ( 467.5 * 60 - 22167.5 ) / (boss_armor - 2550) + 1 )                # improved expose armor (IEA)
    ar_full_sa  = 100 / ( ( 467.5 * 60 - 22167.5 ) / (boss_armor - 640 - 450 * 5 - 505) + 1 ) # FF+Reck+SA
    ar_full_iea = 100 / ( ( 467.5 * 60 - 22167.5 ) / (boss_armor - 640 - 2550 - 505) + 1 )    # FF+Reck+IEA

    # Calculate the damange increases (just shows % dmg increased over the original reduction e.g. 38.8% -> 34.4% = 4.4% for ap_reck)
    # The amount of increased damage after calculating the reduction of armor on the boss/mob
    ap_reck     = boss_armor_reduction - ar_reck
    ap_ff       = boss_armor_reduction - ar_ff
    ap_sa       = boss_armor_reduction - ar_sa
    ap_ea       = boss_armor_reduction - ar_ea
    ap_ea_imp   = boss_armor_reduction - ar_ea_imp
    ap_full_sa  = boss_armor_reduction - ar_full_sa
    ap_full_iea = boss_armor_reduction - ar_full_iea

    # Generate plots for up to 10 players gaining the benefits
    for i in range(10):
        # result = player * dps * mitigation %
        reck     = i * dps_melee * ( ap_reck / 100 )
        spell    = i * dps_caster * curse_elements
        coa      = i * curse_agony
        cod      = i * curse_doom
        ff       = i * dps_melee * ( ap_ff / 100 )
        sa       = i * dps_melee * ( ap_sa / 100 )
        ea       = i * dps_melee * ( ap_ea / 100 )
        ea_imp   = i * dps_melee * ( ap_ea_imp / 100 )
        full_sa  = i * dps_melee * ( ap_full_sa / 100 )
        full_iea = i * dps_melee * ( ap_full_iea / 100 )
        
        list_reck.append(reck)
        list_element.append(spell)
        list_agony.append(coa)
        list_doom.append(cod)
        list_sunder.append(sa)
        list_faerie.append(ff)
        list_expose.append(ea)
        list_expose_imp.append(ea_imp)
        list_full_sa.append(full_sa)
        list_full_iea.append(full_iea)
        #print(full_sa)


    # Create chart
    plt.xlabel("Number of Players")
    plt.ylabel("Increased Raid Damage Per Second")
    plt.plot(list_reck,       label="Curse of Recklessness")
    plt.plot(list_element,    label="Curse of the Elements / Shadow")
    plt.plot(list_sunder,     label="Sunder Armor")
    plt.plot(list_faerie,     label="Faerie Fire")
    plt.plot(list_expose,     label="Expose Armor")
    plt.plot(list_expose_imp, label="Imp Expose Armor")
    plt.plot(list_doom,       label="Curse of Doom")
    plt.plot(list_agony,      label="Curse of Agony")
    plt.plot(list_full_sa,    label="Full w/ Sunder Armor")
    plt.plot(list_full_iea,   label="Full w/ Imp Expose Armor")
    plt.title("Increased Damage of Warlock Curses")
    plt.legend()
    plt.show()

debuffs()
