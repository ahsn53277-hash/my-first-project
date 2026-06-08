import pandas as pd

class ConstructionEstimator:
    """
    An automation tool for calculating concrete quantities 
    and estimating costs for construction projects.
    """
    def __init__(self, project_name):
        self.project_name = project_name
        self.data = []

    def add_element(self, element_name, length, width, depth, unit_price):
        """Adds a new construction element."""
        volume = length * width * depth
        cost = volume * unit_price
        
        entry = {
            "Element": element_name,
            "Volume (m3)": round(volume, 2),
            "Estimated Cost ($)": round(cost, 2)
        }
        self.data.append(entry)
        print(f"Successfully added: {element_name}")

    def generate_report(self):
        """Generates a data report and exports it to a CSV file."""
        df = pd.DataFrame(self.data)
        df.to_csv(f"{self.project_name}_report.csv", index=False)
        print(f"\nReport generated successfully: {self.project_name}_report.csv")
        return df

if __name__ == "__main__":
    my_project = ConstructionEstimator("Building_Foundation_Project")
    
    # Adding sample data
    my_project.add_element("Slab", 5.0, 4.0, 0.25, 120.0)
    my_project.add_element("Column", 0.4, 0.4, 3.0, 150.0)
    
    # Generating report
    report = my_project.generate_report()
    print(report)
