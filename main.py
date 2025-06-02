#تحليل بيانات موظفين الشركه
import pandas as pd
import matplotlib.pyplot as plt 

#بيانات مواظفين الشركه
data = pd.read_csv("employees.csv")

#Exploratory
print("First ten rows of data:\n")
print(data.head(10))
print("\nInformation about columns:\n")
print(data.info())

#عدد الموظفين في كل قسم
counts_employees = (
    data.groupby("department")["name"]
    .count()
    .sort_values(ascending=False)
    .reset_index() 
                    )

#متوسط الرواتب حسب القسم
average_salary_department = (
    data.groupby("department")["salary"]
    .mean()
    .round(2)
    .sort_values(ascending=False)
    .reset_index() 
                             )

#الموظفين اللي مرتباتهم اعلي من المتوسط
average_salary = data['salary'].mean()
print(f"\nArithmetic average: {average_salary:.2f}")
employees_above_avg = (
    data[(data['salary'] > average_salary)]
    .sort_values(by="salary",ascending=False)
    .reset_index()
    )

# من اكتر واحد راتبه؟
highest_salary  = data[(data['salary'] == data["salary"].max())]

#تقارير اكسل فيه تحليل
with pd.ExcelWriter("Analyze_employee_data.xlsx") as writer:
    counts_employees.to_excel(writer,sheet_name="counts_employees",index=False)
    average_salary_department.to_excel(writer,sheet_name="average_salary_department",index=False)
    employees_above_avg.to_excel(writer,sheet_name="employees_above_avg",index=False)
    highest_salary.to_excel(writer,sheet_name="highest_salary",index=False)
    data.to_excel(writer,sheet_name="row_data",index=False)

#رسم بياني عمودي لي رواتب حسب شهر
avg_dept_salaries= data.groupby("department")["salary"].mean()
ax = avg_dept_salaries.plot(kind="bar",figsize=(10,6))

ax.bar_label(ax.containers[0])
ax.set_xlabel("Departments")
ax.set_ylabel("Salaries")
plt.title("Average salaries by department")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("Department_salary.png",bbox_inches="tight",dpi=300)
plt.show() 


#ارفع الكود