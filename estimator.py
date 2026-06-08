import pandas as pd

class ConstructionEstimator:
    """
    أداة لأتمتة حساب كميات الخرسانة وتقدير التكلفة للمشاريع الإنشائية.
    """
    def __init__(self, project_name):
        self.project_name = project_name
        self.data = []

    def add_element(self, element_name, length, width, depth, unit_price):
        """إضافة عنصر إنشائي جديد (سقف، قاعدة، عمود)."""
        volume = length * width * depth
        cost = volume * unit_price
        
        entry = {
            "Element": element_name,
            "Volume (m3)": round(volume, 2),
            "Estimated Cost ($)": round(cost, 2)
        }
        self.data.append(entry)
        print(f"تمت إضافة: {element_name} بنجاح.")

    def generate_report(self):
        """إنشاء تقرير البيانات وتصديره إلى ملف CSV."""
        df = pd.DataFrame(self.data)
        df.to_csv(f"{self.project_name}_report.csv", index=False)
        print(f"\nتم إنشاء التقرير بنجاح: {self.project_name}_report.csv")
        return df

# --- تجربة الكود ---
if __name__ == "__main__":
    my_project = ConstructionEstimator("Building_Foundation_Project")
    
    # إضافة بيانات افتراضية
    my_project.add_element("Slab", 5.0, 4.0, 0.25, 120.0)
    my_project.add_element("Column", 0.4, 0.4, 3.0, 150.0)
    
    # عرض التقرير
    report = my_project.generate_report()
    print(report)
