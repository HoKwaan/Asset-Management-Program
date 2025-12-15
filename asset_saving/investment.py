import csv


class Investment:
    def __init__(self, asset, amount, completed=False):
        self.asset = asset
        self.amount = amount
        self.completed = completed




def save_investments(filepath, investments):
    with open(filepath, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["asset", "amount", "completed"])
        for inv in investments:
            writer.writerow([inv.asset, int(inv.amount), inv.completed])