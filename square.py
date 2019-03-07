class Square(object): 

    def __init__(self, North, East, South, West): 
        self.north = North 
        self.east = East 
        self.south = South 
        self.west = West

# =============================================================================
#     def ueberweisen(self, ziel, betrag):
#         if(self.Kontostand - betrag < -self.Kontokorrent):
#             # Deckung nicht genuegend
#             return False  
#         else: 
#             self.Kontostand -= betrag 
#             ziel.Kontostand += betrag 
#             return True
#  
#     def einzahlen(self, betrag): 
#        self.Kontostand += betrag 
#  
#     def auszahlen(self, betrag): 
#        self.Kontostand -= betrag 
#  
#     def kontostand(self): 
#         return self.Kontostand
# 
# =============================================================================
