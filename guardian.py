class MinorMintGuardian:
    def __init__(self):
        self.prohibited = ["poker", "bet", "gamble", "vape", "wine", "casino"]
    def analyze_request(self, item_name):
        name = item_name.lower()
        if any(w in name for w in self.prohibited):
            return False, "سياسة الأمان تمنع مشتريات القمار."
        return True, "شراء آمن ومعتمد."
      
