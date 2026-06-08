import pandas as pd

def analyze_materials(file_path):
    """
    Automates the analysis of construction materials from a data file.
    """
    try:
        # Load project data
        data = pd.read_csv(file_path)
        
        # Perform Data Analysis
        summary = {
            "Total Items": len(data),
            "Total Estimated Budget": data['Cost'].sum(),
            "Most Expensive Item": data.loc[data['Cost'].idxmax(), 'Material'],
            "Average Material Cost": data['Cost'].mean()
        }
        
        print("--- Construction Project Analysis Summary ---")
        for key, value in summary.items():
            print(f"{key}: {value}")
            
        return summary

    except Exception as e:
        print(f"Error processing data: {e}")

if __name__ == "__main__":
    # Example usage:
    # In a real scenario, this script would process a large CSV file of materials.
    print("Construction Data Analyzer Tool is ready.")
