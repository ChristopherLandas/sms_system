from matplotlib import rcParams
import matplotlib.pyplot as plt
import datetime

class graphs():
    def show_graph(salary_arr):
        def add_label(salary):
            for i in range(len(salary)):
                plt.text(i,salary[i],salary[i])  
    
        def total_count(salary):
            total = 0
            for i in salary:
                total = total + i
            return total
    
        def date_time():
            date = datetime.datetime.now()
            return date.strftime("%y%m%d_%H%M%S")
                 
        rcParams['toolbar']='None'
        #disable toolbar

        metadata_dict = {
            "Title" : "Summary Report",
            "Author": "USER",
            "Creation Time" : f"{date_time()}"
        }
    
        figure_setup = plt.get_current_fig_manager()
        figure_setup.window.wm_iconbitmap("image/search.ico")
        figure_setup.set_window_title("Summary Reports")
        figure_setup.resize(1000,500)

        salary = salary_arr
        label = ['Low', 'Medium', 'High', 'Very High']
        total = f'Total = {total_count(salary)}'
             
        plt.subplot(1,2,1)
        plt.pie(salary, labels= label, autopct="%.2f%%", explode=[0.1,0.1,0.1,0.1],
                colors=["#FF6464", "#FAAB78","#BCE29E","#579BB1"],)
        plt.title('Salary Pie Chart')
        plt.text(-0.5,-1.85, 'Low - 0 - 9,999\nMid - 10,000 - 19,999\nHigh - 20,000 - 49,999\nVery High - 50,000 Above' )
 
        plt.subplot(1,2,2) 
        plt.bar(label, salary, color=["#54BAB9"])
        add_label(salary)
        plt.title('Salary Bar Graph ')
        plt.ylabel('Number of People' )
        plt.xlabel('Salary Range\n\n'+ total)

        plt.subplots_adjust(left=0.08, bottom=0.186,right=0.92,top=0.85, wspace=0.45, hspace=0.2)
        plt.savefig(f"reports/{date_time()}_Summary_Records.png", dpi=180, pad_inches= 0.5, bbox_inches='tight', 
                    metadata = metadata_dict)
        plt.show()
        
        
# [COUNT LOW INCOME, COUNT MID INCOME, COUNT HIGH INCOME, COUNT VHIGH INCOME]
# TAKES ARRAY PARAMETER 
#x = [1, 3, 5, 94]   
#graphs.show_graph(x)
