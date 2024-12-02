from site import Site

class Treasury(Site):
    def __init__(self, name):
        super().__init__(name)
        self.sub_menu = {
            "Back": 'back',
            "Spending": self.spending_report,
            "Edit": super().edit()
            }
        
    def spending_report(self):
        print("Treasury spending report")