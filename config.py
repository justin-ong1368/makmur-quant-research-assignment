from pathlib import Path
class ProjectPaths:
    def __init__(self):
        self.root = Path(__file__).parent
        self.data = self.root / "assets"
        self.outputs = self.root / "outputs"

        self.ownership_data= self.data /"ownership-data"
        self.brokerage_data = self.data /"brokerage-data"
        self.marked_trades_data = self.data /"marked-trades-data"

    def get_data_file(self, filename):
        """Get path to data file as a string"""
        return str(self.data / filename)
PATHS = ProjectPaths()