import time
import random
class Obj_creator:
    creature_def_health=60
    Hero_exp_points=0
    # Hero default attribute values
    def_health=100
    def_defense=10
    def_damage=50
    def_crt=10       
    def_penet=15       
    
    #boss default attributes
    B_def_health=250
    B_def_defense=30
    B_def_damage=25
    def __init__(self,name,health,defense,damage,level=1,exp=0,critical=10,penetrate=15):
        self.name=name
        self.level=level  
        self.exp=exp
        self.health=health
        self.defense=defense
        self.damage=damage
        self.critical=critical
        self.penetrate=penetrate
      # shouldve made one function , huge fault
    def Boss_attacks(self,obj):
        print("Boss attacks.")
        obj.health=obj.health-(self.damage-obj.defense)
        print(f'{obj.name} has {obj.health} health left.')
        
    def Hero_attacks(self,obj):
        ran = random.randint(5,20)
        print("Hero has attacked")
        if Hero.critical>=ran:
            if Hero.penetrate>=ran:
                print("Hero Struck critically and penetrated shield.")
                obj.health=obj.health-(self.damage)*2
            else:
                print("Hero struck critically.")
                obj.health=obj.health-(self.damage-obj.defense)*2
        else:
            if Hero.penetrate>=ran:
                print("Hero penetrated shield.")
                obj.health=obj.health-(self.damage)
            else:
                obj.health=obj.health-(self.damage-obj.defense)
            
        print(f"{obj.name} has {obj.health} health left.")
        
    def Creature_attacks(self,obj):
        ran = random.randint(0,20)
        print("Creature has attacked")
        if Creature.critical>=ran:
            if Creature.penetrate>=ran:
                print("Creature Struck critically and penetrated shield.")
                obj.health=obj.health-(self.damage)*2
            else:
                print("Creature struck critically.")
                obj.health=obj.health-(self.damage-obj.defense)*2
        else:
            if Creature.penetrate>=ran:
                print("Creature penetrated shield.")
                obj.health=obj.health-(self.damage)
            else:
                obj.health=obj.health-(self.damage-obj.defense)
            
        print(f"Hero has {Hero.health} health left.")
    def increase_bossLevel(Boss):
        Boss.level+=1
        Boss.health=Boss.B_def_health+250
        Boss.B_def_health=Boss.health
                
        Boss.defense=Boss.B_def_defense+5
        Boss.B_def_defense=Boss.defense
                
        Boss.damage=Boss.B_def_damage+10
        Boss.B_def_damage=Boss.damage
        
        print("Boss slayed. Next boss stats and level increased.")
          
    def increase_level(self):
        
        
        self.level+=1
        print("""
              1.health,
              2.defense,
              3.damage,
              4.critical,
              5.penetrate
              """)
        choice=int(input("Level increase possible.Which performance to increase?"))
        match choice:
            case 1:
                self.health= self.def_health+100
                self.def_health=self.health
                print(f'Now you have {self.health} health.')
            case 2:
                self.defense=self.def_defense+10
                self.def_defense=self.defense
                print(f'Now you have {self.defense} defense')
            case 3:
                self.damage=self.def_damage+4
                self.def_damage=self.damage
                print(f'Now you have {self.damage} damage.')
            case 4:
                self.critical=self.def_crt+2
                self.def_crt=self.critical
                print(f"Now you have {self.critical} % critical chance.")
            case 5:
                self.penetrate=self.def_penet+3
                self.def_penet=self.penetrate
                print(f'Now you have {self.penetrate} % penetration chance.')
            case _:
                print('Wrong input!')
        
    def attack_creature(self,obj):
        creature_no = int(input("Number of creature you want to fight?"))
        version= int(input(""" Pick an option :
                           1.Show Details 
                           2.Hide Details 
                           """))
        creatures_killed=0
        if version==1:
            while self.health >0 and obj.health >0 :
                Hero.exp=0
                input("Press Enter to attack.")
                Hero.Hero_attacks(Creature)
                time.sleep(2)
                if Creature.health >0 and creature_no>0:
                    for i in range(creature_no):
                        Creature.Creature_attacks(Hero)
                    time.sleep(2)
                    print("  ")
                    if Hero.health >0 :
                        
                        #Hero.attack_creature(Creature)
                        continue
                    else:
                        print(f"Your hero has died. hero health {Hero.health}")
                elif Creature.health <=0 and creature_no>0:
                    creature_no-=1
                    creatures_killed+=1
                    print(f"You killed {creatures_killed} enemy(ies).Enemies left {creature_no}")
                    if creature_no>0:
                        Creature.health=self.creature_def_health
                        for i in range(creature_no):
                            Creature.Creature_attacks(Hero)
                        time.sleep(2)
                        print("  ")
                        if Hero.health >0 :
                            #Hero.attack_creature(Creature)
                            continue
                        else:
                            print("Your hero has died.")
                    else:
                        print(f"Your hero has won. Creature health= {Creature.health}")    
                        Hero.exp+= (50*creatures_killed)
                        self.Hero_exp_points+=Hero.exp
                        while self.Hero_exp_points >0 :
                            if self.Hero_exp_points>= (Hero.level*100):
                                self.Hero_exp_points-= (Hero.level*100)
                                Hero.increase_level()
                                print(f'exp points left : {self.Hero_exp_points}')
                                print(f'Hero level {Hero.level}')
                                ch= input('Do you want to attack creatures again? Y or N')
                                if ch=='Y':
                                    Creature.health=60
                                    Hero.attack_creature(Creature)
                                    
                                else:
                                    break
                            else:
                                #continue
                                print(f'exp points left : {self.Hero_exp_points}')
                                print(f'Hero level {Hero.level}')
                                ch= input('Do you want to attack creatures again? Y or N')
                                if ch=='Y':
                                    Creature.health=60
                                    Hero.attack_creature(Creature)
                                
                                else:
                                    break
                else:
                        print(f"Your hero has won. Creature health= {Creature.health}")
                        Hero.exp+= (50*creatures_killed)
                        self.Hero_exp_points+=Hero.exp
                        while self.Hero_exp_points >0 :
                            if self.Hero_exp_points>= (Hero.level*100):
                                self.Hero_exp_points-= (Hero.level*100)
                                print(f'exp points left: {Hero.Hero_exp_points}')
                                print(f'Hero level {Hero.level}')
                                Hero.increase_level()
                            else:
                                #continue
                                print(f'exp points left: {Hero.Hero_exp_points}')
                                print(f'Hero level {Hero.level}')
                                ch= input('Do you want to attack creatures again? Y or N')
                                if ch=='Y':
                                    
                                    Hero.attack_creature(Creature)
                                else:
                                    break
                                

        elif version==2:
            while self.health >0 and obj.health >0 :
                Hero.Hero_attacks(Creature)
                if Creature.health >0 and creature_no>0:
                    for i in range(creature_no):
                        Creature.Creature_attacks(Hero)

                    if Hero.health >0 :
                        
                        #Hero.attack_creature(Creature)
                        continue
                    else:
                        print(f"Your hero has died. hero health {Hero.health}")
                elif Creature.health <=0 and creature_no>0:
                    creature_no-=1
                    print(f"You killed an enemy.Enemies left {creature_no}")
                    if creature_no>0:
                        Creature.health=self.creature_def_health
                        for i in range(creature_no):
                            Creature.Creature_attacks(Hero)
                            
                        print("  ")
                        if Hero.health >0 :
                            #Hero.attack_creature(Creature)
                            continue
                    else:
                        print(f"Your hero has won. Creature health= {Creature.health}")    
                else:
                        print(f"Your hero has won. Creature health= {Creature.health}")
    
    def attack_boss(self,Boss):
    
        print("Showing Hero vs Boss attributes:")
        print("Hero   -   Boss")
        print(f'{Hero}')
        print(f"""Showing Hero vs Boss attributes:
              Hero  -  Boss
    Health:  {Hero.health}       {Boss.health}
    Defense: {Hero.defense}        {Boss.defense}
    Damage:  {Hero.damage}        {Boss.damage}  
    Critical:{Hero.critical}        {Boss.critical}
    Penet % :{Hero.penetrate}        {Boss.penetrate}
              
              
              """)
        
              
        while(self.health >0 and Boss.health >0):
            input('Press enter to attack')
            time.sleep(2)
            self.Hero_attacks(Boss)
            if Boss.health >0 :
                time.sleep(2)
                Boss.Boss_attacks(Hero)
                if self.health>0:
                    continue
                else:
                    print(f'You were killed by the boss.  Hero health {self.health} ')
            else:
                print(f'You killed the boss. Boss health {Boss.health}')  
                Boss.increase_bossLevel()
                
                
         
        
Hero = Obj_creator("Hero",150,10,50)
Creature= Obj_creator("Creature",60,10,10)
Boss = Obj_creator("Boss",250,30,25)
"""
print(Creature.health)
Hero.attacks(Creature)
print(Creature.health)
"""
choice=int(input(" Pick an option:1.Attack creature 2.Attack bosses"))
if choice==1:
    Hero.attack_creature(Creature)
elif choice==2:
    Hero.attack_boss(Boss)