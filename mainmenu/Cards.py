class Mobster():
    def __init__(self, type, name, origin, hp1, hp2, hp3, img):
        self.type = type
        self.name = name
        self.origin = origin
        self.hp1 = hp1
        self.hp2 = hp2
        self.hp3 = hp3
        self.img = img
        
    def display(self):
        rimg = loadImage(self.img)
        scale(0.3)
        image(rimg, 100, 100)
        
class Origin():
    def __init__(self, type, name, img):
        self.type = type
        self.name = name
        self.img = img
        
    def display(self):
        rimg = loadImage(self.img)
        scale(0.3)
        image(rimg, 100, 100)
        
class TrapJob():
    def __init__(self, type, name, hp1, hp2, effect, img):
        self.type = type
        self.name = name
        self.hp1 = hp1
        self.hp2 = hp2
        self.effect = effect
        self.img = img
        
    def display(self):
        rimg = loadImage(self.img)
        scale(0.3)
        image(rimg, 100, 100)

test_card = Mobster("testType", "TestName", "TestOrigin", 0, 0, 0, "settingsicon2.png")

#Mobsters
aivd1 = Mobster("Mobster", "AIVD1", "Netherlands", 6, 6, 6, "AIVD1.jpg")
aivd2 = Mobster("Mobster", "AIVD2", "Netherlands", 7, 9, 6, "AIVD2.jpg")
aivd3 = Mobster("Mobster", "AIVD3", "Netherlands", 0, 10, 5, "AIVD3.jpg")
aivd4 = Mobster("Mobster", "AIVD4", "Netherlands", 0, 11, 0, "AIVD4.jpg")
bratva1 = Mobster("Mobster", "Bratva1", "Russia", 7, 8, 8, "Bratva1.jpg")
bratva2 = Mobster("Mobster", "Bratva2", "Russia", 0, 9, 9, "Bratva2.jpg")
bratva3 = Mobster("Mobster", "Bratva3", "Russia", 0, 9, 10, "Bratva3.jpg")
bratva4 = Mobster("Mobster", "Bratva4", "Russia", 0, 10, 10, "Bratva4.jpg")
cosaNosta1 = Mobster("Mobster", "CosaNostra1", "Italy", 7, 6, 9, "CosaNostra1.jpg")
cosaNosta2 = Mobster("Mobster", "CosaNostra2", "Italy", 0, 9, 10, "CosaNostra2.jpg")
cosaNosta3 = Mobster("Mobster", "CosaNostra3", "Italy", 0, 4, 5, "CosaNostra3.jpg")
cosaNosta4 = Mobster("Mobster", "CosaNostra4", "Italy", 0, 11, 0, "CosaNostra4.jpg")
dni1 = Mobster("Mobster", "DNI1", "Colombia", 5, 6, 6, "DNI1.jpg")
dni2 = Mobster("Mobster", "DNI2", "Colombia", 0, 9, 5, "DNI2.jpg")
dni3 = Mobster("Mobster", "DNI3", "Colombia", 0, 10, 4, "DNI3.jpg")
dni4 = Mobster("Mobster", "DNI4", "Colombia", 0, 3, 0, "DNI4.jpg")
farmer1 = Mobster("Mobster", "Farmer1", "Netherlands", 7, 9, 7, "Farmer1.jpg")
farmer2 = Mobster("Mobster", "Farmer2", "Netherlands", 6, 6, 6, "Farmer2.jpg")
farmer3 = Mobster("Mobster", "Farmer3", "Netherlands", 0, 10, 5, "Farmer3.jpg")
farmer4 = Mobster("Mobster", "Farmer4", "Netherlands", 0, 11, 0, "Farmer4.jpg")
fsb1 = Mobster("Mobster", "FSB1", "Russia", 7, 8, 8, "FSB1.jpg")
fsb2 = Mobster("Mobster", "FSB2", "Russia", 0, 9, 9, "FSB2.jpg")
fsb3 = Mobster("Mobster", "FSB3", "Russia", 0, 9, 10, "FSB3.jpg")
fsb4 = Mobster("Mobster", "FSB4", "Russia", 0, 10, 10, "FSB4.jpg")
CaliKartel1 = Mobster("Mobster", "CaliKartel1", "Colombia", 5, 6, 6, "KaliKartel1.jpg")
CaliKartel2 = Mobster("Mobster", "CaliKartel2", "Colombia", 0, 9, 5, "KaliKartel2.jpg")
CaliKartel3 = Mobster("Mobster", "CaliKartel3", "Colombia", 0, 4, 10, "KaliKartel3.jpg")
CaliKartel4 = Mobster("Mobster", "CaliKartel4", "Colombia", 0, 3, 0, "KaliKartel4.jpg")
mss1 = Mobster("Mobster", "MSS1", "China", 8, 8, 8, "MSS1.jpg")
mss2 = Mobster("Mobster", "MSS2", "China", 5, 6, 7, "MSS2.jpg")
mss3 = Mobster("Mobster", "MSS3", "China", 0, 9, 4, "MSS3.jpg")
mss4 = Mobster("Mobster", "MSS4", "China", 0, 3, 0, "MSS4.jpg")
psia1 = Mobster("Mobster", "PSIA1", "Japan", 8, 6, 7, "PSIA1.jpg")
psia2 = Mobster("Mobster", "PSIA2", "Japan", 8, 6, 9, "PSIA2.jpg")
psia3 = Mobster("Mobster", "PSIA3", "Japan", 7, 7, 7, "PSIA3.jpg")
psia4 = Mobster("Mobster", "PSIA4", "Japan", 0, 3, 0, "PSIA4.jpg")
sismi1 = Mobster("Mobster", "SISMI1", "Italy", 7, 6, 9, "SISMI1.jpg")
sismi2 = Mobster("Mobster", "SISMI2", "Italy", 0, 5, 4, "SISMI2.jpg")
sismi3 = Mobster("Mobster", "SISMI3", "Italy", 0, 10, 9, "SISMI3.jpg")
sismi4 = Mobster("Mobster", "SISMI4", "Italy", 0, 11, 0, "SISMI4.jpg")
triad1 = Mobster("Mobster", "Triad1", "China", 8, 8, 8, "Triad1.jpg")
triad2 = Mobster("Mobster", "Triad2", "China", 5, 6, 7, "Triad2.jpg")
triad3 = Mobster("Mobster", "Triad3", "China", 0, 9, 4, "Triad3.jpg")
triad4 = Mobster("Mobster", "Triad4", "China", 0, 3, 0, "Triad4.jpg")
yakuza1 = Mobster("Mobster", "Yakuza1", "Japan", 6, 8, 7, "Yakuza1.jpg")
yakuza2 = Mobster("Mobster", "Yakuza2", "Japan", 6, 8, 9, "Yakuza2.jpg")
yakuza3 = Mobster("Mobster", "Yakuza3", "Japan", 7, 7, 7, "Yakuza3.jpg")
yakuza4 = Mobster("Mobster", "Yakuza4", "Japan", 0, 3, 0, "Yakuza4.jpg")

#origins
origin_China_Red = Origin("Origin", "Origin_China_Red", "OriginChina.jpg")
origin_China_Blue  = Origin("Origin", "Origin_China_Blue", "OriginChinaFED.jpg")
origin_Japan_Red = Origin("Origin", "Origin_Japan_Red", "OriginJapan.jpg")
origin_Japan_Blue = Origin("Origin", "Origin_Japan_Blue", "OriginJapanFED.jpg")
origin_Colombia_Red = Origin("Origin", "Origin_Colombia_Red", "OriginColombia.jpg")
origin_Colombia_Blue = Origin("Origin", "Origin_Colombia_Blue", "OriginColombiaFED.jpg")
origin_Italy_Red = Origin("Origin", "Origin_Italy_Red", "OriginItaly.jpg")
origin_Italy_Blue = Origin("Origin", "Origin_Italy_Blue", "OriginItalyFED.jpg")
origin_Netherlands_Red = Origin("Origin", "Origin_Netherlands_Red", "OriginNetherlands.jpg")
origin_Netherlands_Blue = Origin("Origin", "Origin_Netherlands_Blue", "OriginNetherlandsFED.jpg")
origin_Russia_Red = Origin("Origin", "Origin_Russia_Red", "OriginRussia.jpg")
origin_Russia_Blue = Origin("Origin", "Origin_Russia_Blue", "OriginRussiaFED.jpg")

#Jobs
anti_Hit_Red1 = TrapJob("Job","Anti_Hit_Red", 1, 0, "-2 dmg", "JobAnti-Hit.jpg")
anti_Hit_Red2 = TrapJob("Job","Anti_Hit_Red", 1, 0, "-2 dmg", "JobAnti-Hit.jpg")
anti_Hit_Blue1 = TrapJob("Job","Anti_Hit_Blue", 1, 0, "-2 dmg", "JobAnti-HitFED.jpg")
anti_Hit_Blue2 = TrapJob("Job","Anti_Hit_Blue", 1, 0, "-2 dmg", "JobAnti-HitFED.jpg")
clairevoyance_Red1 = TrapJob("Job","Clairevoyance_Red", 1, 0, "Reveal 2 cards", "JobClairevoyance.jpg")
clairevoyance_Red2 = TrapJob("Job","Clairevoyance_Red", 1, 0, "Reveal 2 cards", "JobClairevoyance.jpg")
clairevoyance_Blue1 = TrapJob("Job","Clairevoyance_Blue", 1, 0, "Reveal 2 cards", "JobClairevoyanceFED.jpg")
clairevoyance_Blue2 = TrapJob("Job","Clairevoyance_Blue", 1, 0, "Reveal 2 cards", "JobClairevoyanceFED.jpg")
prophecy_Red1 = TrapJob("Job","Prophecy_Red", 1, 0, "Save 1 rolled dice value", "JobProphecy.jpg")
prophecy_Red2 = TrapJob("Job","Prophecy_Red", 1, 0, "Save 1 rolled dice value", "JobProphecy.jpg")
prophecy_Blue1 = TrapJob("Job","Prophecy_Blue", 1, 0, "Save 1 rolled dice value", "JobProphecyFED.jpg")
prophecy_Blue2 = TrapJob("Job","Prophecy_Blue", 1, 0, "Save 1 rolled dice value", "JobProphecyFED.jpg")
reroll_Red1 = TrapJob("Job","Reroll_Red", 1, 0, "can reroll a second time", "JobReroll.jpg")
reroll_Red2 = TrapJob("Job","Reroll_Red", 1, 0, "can reroll a second time", "JobReroll.jpg")
reroll_Blue1 = TrapJob("Job","Reroll_Blue", 1, 0, "can reroll a second time", "JobRerollFED.jpg")
reroll_Blue2 = TrapJob("Job","Reroll_Blue", 1, 0, "can reroll a second time", "JobRerollFED.jpg")
retaliate_Red1=  TrapJob("Job","Retaliate_Red", 1, 0, "Take back a card and fully heal it", "JobRetaliate.jpg")
retaliate_Red2 = TrapJob("Job","Retaliate_Red", 1, 0, "Take back a card and fully heal it", "JobRetaliate.jpg")
retaliate_Blue1 = TrapJob("Job","Retaliate_Blue", 1, 0, "Take back a card and fully heal it", "JobRetaliateFED.jpg")
retaliate_Blue2 = TrapJob("Job","Retaliate_Blue", 1, 0, "Take back a card and fully heal it", "JobRetaliateFED.jpg")
reveal_Red1 = TrapJob("Job","Reveal_Red", 1, 0, "Reveal the enemy trap", "JobReveal.jpg")
reveal_Red2 = TrapJob("Job","Reveal_Red", 1, 0, "Reveal the enemy trap", "JobReveal.jpg")
reveal_Blue1 = TrapJob("Job","Reveal_Blue", 1, 0, "Reveal the enemy trap", "JobRevealFED.jpg")
reveal_Blue2 = TrapJob("Job","Reveal_Blue", 1, 0, "Reveal the enemy trap", "JobRevealFED.jpg")
sacrifice_Red1 = TrapJob("Job","Sacrifice_Red", 1, 0, "Sacrifice a non damaged Mobster to kill an enemy Mobster", "JobSacrifice.jpg")
sacrifice_Red2 = TrapJob("Job","Sacrifice_Red", 1, 0, "Sacrifice a non damaged Mobster to kill an enemy Mobster", "JobSacrifice.jpg")
sacrifice_Blue1 = TrapJob("Job","Sacrifice_Blue", 1, 0, "Sacrifice a non damaged Mobster to kill an enemy Mobster", "JobSacrificeFED.jpg")
sacrifice_Blue2 = TrapJob("Job","Sacrifice_Blue", 1, 0, "Sacrifice a non damaged Mobster to kill an enemy Mobster", "JobSacrificeFED.jpg")
small_Hit_Red1 = TrapJob("Job","Small_Hit_Red", 1, 0, "+2 dmg", "JobSmallHit.jpg")
small_Hit_Red2 = TrapJob("Job","Small_Hit_Red", 1, 0, "+2 dmg", "JobASmallHit.jpg")
small_Hit_Blue1 = TrapJob("Job","Small_Hit_Blue", 1, 0, "+2 dmg", "JobSmallHitFED.jpg")
small_Hit_Blue2 = TrapJob("Job","Small_Hit_Blue", 1, 0, "+2 dmg", "JobSmallHitFED.jpg")
stun_Red1 = TrapJob("Job","Stun_Red", 1, 0, "Your enemy can't attack with their dice next turn", "JobStun.jpg")
stun_Red2 = TrapJob("Job","Stun_Red", 1, 0, "Your enemy can't attack with their dice next turn", "JobStun.jpg")
stun_Blue1 = TrapJob("Job","Stun_Blue", 1, 0, "Your enemy can't attack with their dice next turn", "JobStunFED.jpg")
stun_Blue2 = TrapJob("Job","Stun_Blue", 1, 0, "Your enemy can't attack with their dice next turn", "JobStunFED.jpg")
the_Odds_Are_Against_You_Red1 = TrapJob("Job","The_Odds_Are_Against_You_Red", 1, 0, "Move one of your ringcontainers to your enemy", "JobTheoddsareagainstyou.jpg")
the_Odds_Are_Against_You_Red2 = TrapJob("Job","The_Odds_Are_Against_You_Red", 1, 0, "Move one of your ringcontainers to your enemy", "JobTheoddsareagainstyou.jpg")
the_Odds_Are_Against_You_Blue1 = TrapJob("Job","The_Odds_Are_Against_You_Blue", 1, 0, "Move one of your ringcontainers to your enemy", "JobTheoddsareagainstyouFED.jpg")
the_Odds_Are_Against_You_Blue2 = TrapJob("Job","The_Odds_Are_Against_You_Blue", 1, 0, "Move one of your ringcontainers to your enemy", "JobTheoddsareagainstyouFED.jpg")

#Traps
ambushed_Red1 = TrapJob("Trap", "Ambushed_Red", 1, 1, "When the enemy plays a job, it will be placed in your hand", "TrapAmbushed.jpg")
ambushed_Red2 = TrapJob("Trap", "Ambushed_Red", 1, 1, "When the enemy plays a job, it will be placed in your hand", "TrapAmbushed.jpg")
ambushed_Blue1 = TrapJob("Trap", "Ambushed_Blue", 1, 1, "When the enemy plays a job, it will be placed in your hand", "TrapAmbushedFED.jpg")
ambushed_Blue2 = TrapJob("Trap", "Ambushed_Blue", 1, 1, "When the enemy plays a job, it will be placed in your hand", "TrapAmbushedFED.jpg")
dodge_Red1 = TrapJob("Trap", "Dodge_Red", 1, 1, "Your mobster is immune to every 1 cost action when it takes damage", "TrapDodge.jpg")
dodge_Red2 = TrapJob("Trap", "Dodge_Red", 1, 1, "Your mobster is immune to every 1 cost action when it takes damage", "TrapDodge.jpg")
dodge_Blue1 = TrapJob("Trap", "Dodge_Blue", 1, 1, "Your mobster is immune to every 1 cost action when it takes damage", "TrapDodgeFED.jpg")
dodge_Blue2 = TrapJob("Trap", "Dodge_Blue", 1, 1, "Your mobster is immune to every 1 cost action when it takes damage", "TrapDodgeFED.jpg")
revive_Red1 = TrapJob("Trap", "Revive_Red", 1, 1, "When a mobster dies, revive it", "TrapRevive.jpg")
revive_Red2 = TrapJob("Trap", "Revive_Red", 1, 1, "When a mobster dies, revive it", "TrapRevive.jpg")
revive_Blue1 = TrapJob("Trap", "Revive_Blue", 1, 1, "When a mobster dies, revive it", "TrapReviveFED.jpg")
revive_Blue2 = TrapJob("Trap", "Revive_Blue", 1, 1, "When a mobster dies, revive it", "TrapReviveFED.jpg")
ricochet_Red1 = TrapJob("Trap", "Ricochet_Red", 1, 1, "When you are attacked, you can attack with the same value or +1 bonus/-1 damage", "TrapRicochet.jpg")
ricochet_Red2 = TrapJob("Trap", "Ricochet_Red", 1, 1, "When you are attacked, you can attack with the same value or +1 bonus/-1 damage", "TrapRicochet.jpg")
ricochet_Blue1 = TrapJob("Trap", "Ricochet_Blue", 1, 1, "When you are attacked, you can attack with the same value or +1 bonus/-1 damage", "TrapRicochetFED.jpg")
ricochet_Blue2 = TrapJob("Trap", "Ricochet_Blue", 1, 1, "When you are attacked, you can attack with the same value or +1 bonus/-1 damage", "TrapRicochetFED.jpg")
sniped_Red1 = TrapJob("Trap", "Sniped_Red", 1, 1, "When the enemy plays a Mobster, damage one of his hp", "TrapSniped.jpg")
sniped_Red2 = TrapJob("Trap", "Sniped_Red", 1, 1, "When the enemy plays a Mobster, damage one of his hp", "TrapSniped.jpg")
sniped_Blue1 = TrapJob("Trap", "Sniped_Blue", 1, 1, "When the enemy plays a Mobster, damage one of his hp", "TrapSnipedFED.jpg")
sniped_Blue2 = TrapJob("Trap", "Sniped_Blue", 1, 1, "When the enemy plays a Mobster, damage one of his hp", "TrapSnipedFED.jpg")
