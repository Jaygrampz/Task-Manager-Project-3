def reg_user():
    #print("This Functionality is only for User with admin priveleges")

        if (username == "admin" and password == "adm1n"): #Validate admin credentials
               
            new_username = input("Enter a new username: ")
            new_password = input("Enter a new password: ")                
                        
            with open("user.txt", 'r+') as f2: #User file is opened to write new data to the file.
                data = f2.readlines() #Lines of the file are read and stored in this variable

                for line in data: 
                    if line.startswith(new_username): #Function to verify if the new_username does not match any of the lines in 'data'
                        print("This username already exists. Please try again")
                        reg_user()
                        
                f2.write(f"{new_username}, {new_password}\n")
                        
                        
        else:
            print("You do not have permission to do this!")
         
               
def add_task():
    with open('tasks.txt', 'a+') as f5:#The task file is opened
        task_list = []
        #The username, task of the title, task description, date assigned and due date are appened to the variable "task list" in respective order.
        
        username = input("Enter your username: ")
        task_list.append(username)

        task_title = input("What task are you assigning to the user?: ")
        task_list.append(task_title)

        task_description = input("What duties should the user need to fulfill?: ")
        task_list.append(task_description)

        date_assigned = input("Enter the date the task was assigned to the user: ")
        task_list.append(date_assigned)

        due_date = input("Enter the due date for the task: ")
        task_list.append(due_date)

        task_status = "No"
        task_list.append(task_status)

        task_list_write = ", ".join(task_list) #The lists are joined together and are written to the file
        f5.write(task_list_write + "\n")

        return print("Task has been successfully added!")

def view_all():
    with open('tasks.txt', 'r') as f6: #The file is opened in read mode
        data = [] #The lines of the file are stored in the variable called data and then displayed to the user
        
        for lines in f6:
            data.append(lines.replace("\n", ""))
            
        print("User: " + " " + "Task: " + " " + "Description: " + " " + "Date Assigned: " + " " + "Due Date: ")
        
        for i in data: #'i' represents the lines stored in the variable data
            print(i)

def vm_view():
    with open('tasks.txt', 'r') as f7:
        task_data = [] 
        
        for lines in f7:
            task_data.append(lines) #The lines in f7 will be appended to task_data

        username = input("Enter your username: ")      
        for lines in task_data:
            if lines.startswith(username): #Once the user inputs their user name, it will display their respective tasks
                print("User: " + " " + "Task: " + " " + "Description: " + " " + "Date Assigned: " + " " + "Due Date: ")
                return print(lines)
            
#This function is to change the task status, whether the task is complete or not
def vm_completion():
    with open('tasks.txt', 'r+') as file_2:
        user_tasks = []
        task_edit = []
        
        for lines in file_2:
            user_tasks.append(lines.replace("\n", "")) #All the tasks of this file are appended into 'user_tasks'

        username = input("Enter your username: ")
        for lines in user_tasks: #The lines that are present of user_tasks
            if lines.startswith(username): #The username of the specific user will be entered and thier tasks will be appended to 'task_edit'
                task_edit.append(lines.split(", "))

        completion = input("Has the task been completed? (Yes/No)\n Enter here: ")   
        for line in task_edit:
            line[5] = completion #Completion is the input of the user. It is either Yes/No and the 5th index of the list is changed
            to_write = ", ".join(line) #The lists are joined together and written to the file
            file_2.write("\n" + to_write)

        
        
#This function chnages the due date of the tasks assigned to a specific user
def vm_due_date():
    with open('tasks.txt', 'r+') as file_3:
        user_tasks = []
        task_edit = []
        
        for lines in file_3: #All the tasks of this file are appended into 'user_tasks'
            user_tasks.append(lines.replace("\n", ""))

        
        username = input("Enter your username: ") 
        for lines in user_tasks: #The lines that are present of user_tasks
            if lines.startswith(username): #The username of the specific user will be entered and thier tasks will be appended to 'task_edit'
                task_edit.append(lines.split(", "))
                

        due_date = input("Enter the new due date: ")
        for line in task_edit:
            line[4] = due_date #Due_date is the input of the user. The new date replaces the 4th index of the list
            to_write = ", ".join(line) #The lists are joined together and written to the file
            file_3.write(to_write)

        

#This function assigns an existing task to a new user
def vm_user():
    with open('tasks.txt', 'r+') as file_4:
        user_tasks = []
        task_edit = []
        
        for lines in file_4: #All the tasks of this file are appended into 'user_tasks'
            user_tasks.append(lines.replace("\n", ""))

        username = input("Enter your username: ")
        for lines in user_tasks: #The lines that are present of user_tasks
            if lines.startswith(username): #The username of the specific user will be entered and thier tasks will be appended to 'task_edit'
                task_edit.append(lines.split(", "))

        new_user = input("Enter the new username: ")
        for line in task_edit:
            line[0] = new_user #new_user is the input of the user. The new username replaces the 0th index of the list
            to_write = ", ".join(line) #The lists are joined together and written to the file
            file_4.write(to_write)

#The task overview funtions
def task_generation():
    with open("tasks.txt", 'r+') as file_in1:
        tasks = []

        for lines in file_in1: #The tasks in the tasks.txt are appended in to the list 'tasks'
            tasks.append(lines.replace("\n", "").split(", "))

    num_of_tasks = int(len(tasks)) #The number of lists is determined and cast into an integer

    with open('task_overview.txt', 'w') as file_out1:
        file_out1.write("The number of tasks generated by task manager: " + str(num_of_tasks)) #The number of lists = number of tasks
        
#This function retrieves the task that are incomplete
def task_incomplete():
    with open('tasks.txt', 'r+') as file_in2:
        data = []
        incomplete_tasks = []

        for lines in file_in2: #The tasks in the tasks.txt are appended in to the list 'data'
            data.append(lines.replace("\n", ""))

        for line in data:
            answer = "No"
            if line.endswith(answer): #This function reads the last element of the line, whether task is complete or not ie. Yes or No.
                incomplete_tasks.append(line) #The incomplete tasks are appended the to variable 'incomplete_tasks'


    number = int(len(incomplete_tasks)) #The number of lists present in 'incomplete_tasks' is determined and cast as an integer

    with open('task_overview.txt', "w") as file_out2:
        file_out2.write('\n' + "The total number of tasks incomplete: " + str(number))#The number of lists = number of tasks incomplete
    
#This function retrieves the task that are complete
def task_complete():
    with open('tasks.txt', 'r+') as file_in3:
        data = []
        complete_tasks = []

        for lines in file_in3: #The tasks in the tasks.txt are appended in to the list 'data'
            data.append(lines.replace("\n", ""))

        for line in data:
            answer = "Yes"
            if line.endswith(answer): #This function reads the last element of the line, whether task is complete or not ie. Yes or No.
                complete_tasks.append(line) #The incomplete tasks are appended the to variable 'complete_tasks'


    number = int(len(complete_tasks)) #The number of lists present in 'complete_tasks' is determined and cast as an integer

    with open('task_overview.txt', "w") as file_out3:
        file_out3.write('\n' + "The total number of tasks complete: " + str(number)) #The number of lists = number of tasks complete

#This function determines the percentage of tasks incomplete
def percentage_inc():
    with open('tasks.txt', 'r+') as filein4:
        data = []
        incomplete_tasks = []

        for lines in filein4:
            data.append(lines.replace("\n", "")) #The tasks are appended to 'data'

        for line in data:
            neg_answer = "No" #The incomplete tasks end with 'No'. These lines are appended to 'incomplete tasks'
            if line.endswith(neg_answer):
                incomplete_tasks.append(line)

    total_numbers = int(len(data)) #All the tasks, whether or not they've been completed, are stored in 'data'. The number of tasks is determined
    number = int(len(incomplete_tasks)) #The number of lists in 'incomplete_tasks" is determined

    percentage = (number / total_numbers) * 100 #Math calculation to determine the percentage


    with open("task_overview.txt", "w") as fileout4: #Written to task.txt
        fileout4.write('\n' + "Percentage tasks that are incomplete: " + str(percentage) + '%')
        
#User overview functions begin from here
        
#The number of users registered       
def user_estimate():
    with open('user.txt', 'r+') as filein5:
        user_creds = []

        for lines in filein5: #The user credentials are appended to user_creds
            user_creds.append(lines.replace('\n', ''))

        reg_user = int(len(user_creds)) #Number of lists in 'user_creds' is determined

        with open("user_overview.txt", "a") as fileout5: 
            fileout5.write("The number of users registered in Task Manager: " + str(reg_user)) #the number of lists in 'user_creds' = number of users

#The number of tasks assigned to a specific user
def tasks_assigned(username):
    with open('tasks.txt', 'r+') as filein6:
        data = []
        user_specific = []

        for lines in filein6: #The tasks are appended to 'data'
            data.append(lines.replace("\n", ""))

        for line in data:
            if line.startswith(username): #The functions looks for the line(s) that start with the username entered
                user_specific.append(line) #The results are appended to 'user_specific

        user_tasks = int(len(user_specific)) #The number of lists in 'user_specific'

        with open('user_overview.txt', 'w') as fileout6:
            fileout6.write("\n" + f"The number of tasks assigned to {username}: " + str(user_tasks)) #The number of tasks in 'user_specific' = The number of tasks assigned to the username

#The percentage of all tasks assigned to the specific user
def user_percentage(username):
    with open('tasks.txt', 'r+') as filein7:
        data = []
        user_specific = []

        for lines in filein7: #The tasks are appended to 'data'
            data.append(lines.replace("\n", ""))

        for line in data:
            if line.startswith(username): #The functions looks for the line(s) that start with the username entered
                user_specific.append(line) #The results are appended to 'user_specific

        total_tasks = int(len(data)) #The numbers of tasks is determined
        user_tasks = int(len(user_specific)) #The number of tasks to the specific user is determined
        percentage = (user_tasks / total_tasks) * 100 #Math calculation to determine the percentage

        with open('user_overview.txt', 'w') as fileout7:
            fileout7.write("\n" + f"The percentage of all tasks assigned to {username}: " + str(percentage))

#The percentage of the tasks assigned to the user that have been completed       
def user_specific_complete(username):
    with open('tasks.txt', 'r+') as filein7:
        data = []
        user_specific = []
        completed = []

        for lines in filein7: #The tasks are appended to 'data'
            data.append(lines.replace("\n", ""))

        for line in data:
            if line.startswith(username): #The functions looks for the line(s) that start with the username entered
                user_specific.append(line) #The results are appended to 'user_specific'

        for lines in user_specific:
            answer = "Yes"
            if lines.endswith(answer): #The functions looks for the line(s) that ends with the answer "Yes"
                completed.append(lines) #The results are appended to 'completed'
                

        total_tasks = int(len(user_specific)) #The numbers of tasks assigned that are specific to the user is determined
        user_tasks_completed = int(len(completed)) #The numbers of tasks completed by the specific user is determined
        percentage = (user_tasks_completed / total_tasks) * 100 #Math calculation to determine the percentage

        with open('user_overview.txt', 'w') as fileout8:
            fileout8.write("\n" + f"The percentage of tasks completed by {username}: " + str(percentage))


#The percentage of the tasks assigned to the user that are incomplete
def user_specific_incomplete(username):
    with open('tasks.txt', 'r+') as filein9:
        data = []
        user_specific = []
        incomplete = []

        for lines in filein9: #The tasks are appended to 'data'
            data.append(lines.replace("\n", ""))

        for line in data:
            if line.startswith(username): #The functions looks for the line(s) that start with the username entered
                user_specific.append(line) #The results are appended to 'user_specific'

        for lines in user_specific:
            answer = "No"
            if lines.endswith(answer): #The functions looks for the line(s) that ends with the answer "No"
                incomplete.append(lines) #The results are appended to 'incomplete'
                

        total_tasks = int(len(user_specific)) #The numbers of tasks assigned that are specific to the user is determined
        user_tasks_incomplete = int(len(incomplete)) #The numbers of tasks incomplete by the specific user is determined
        percentage = (user_tasks_incomplete / total_tasks) * 100 #Math calculation to determine the percentage

        with open('user_overview.txt', 'w') as fileout9: 
            fileout9.write("\n" + f"The percentage of tasks incomplete by {username}: " + str(percentage))


def task_overview():
    with open('task_overview.txt', 'r+') as ov1:
        data = []

        for lines in ov1: #Lines in the file ov2 are appended to 'data'
            data.append(lines.replace("\n", ""))

        for line in data:
            print(line) #Lines in data are displayed. These are the lines of task_overview


def user_overview():
    with open('user_overview.txt', 'r+') as ov2:
        data = []

        for lines in ov2: #Lines in the file ov2 are appended to 'data'
            data.append(lines.replace("\n", ""))

        for line in data:
            print(line) #Lines in data are displayed. 
        


def main_menu():
    print("r - register user")
    print("a - add task")
    print("va - view all tasks")
    print("vm - view my tasks")
    print("gr - generate reports")
    print("ds - display statistics")
    print("e - exit")
    

    

#ALL the functions have been defined. The task manager program starts from here


f1 = open('user.txt', 'r')
raw_data = []

for lines in f1:
    raw_data.append(lines.replace("\n", "").split(", ")) #Passowrd and username are added to the variable 'raw_data'

#The user inputs their credentials
username = input("Enter your username: ")
password = input("Enter your password: ")
#Boolean was created to validate the login
login = False


while login == False: #while loop created for the login
    for data in raw_data: #data represents the credentials found in raw_data
        
        if (username and password in data):
            login = True
            
    if (login == False): #User is asked to type their credentials again if they were not found in the file
        print("Your username or password is incorrect! Please enter the correct crdentials")
        username = input("Enter username: ")
        password = input("Enter password: ")
    
f1.close()
 

while login == True: #loop for successful login and access to the task manager
    main_menu()
    user_choice = input("Please select one of the above options: ")

    if (user_choice == "r"): #register a new user (admin-only)
        
        reg_user()
        print("User registered successfully!")

                               
    elif (user_choice == "a"): #This choice adds a new task
        print("Add tasks here and assign them to specific users")

        add_task()
        print("Task registered successfully!")
        

    elif (user_choice == "va"): #This selection is to view all tasks for every user
        print("You are now viewing the tasks for all users.")

        view_all()

    elif (user_choice == "vm"): #This selection is ti view the task specific to a user

        vm_view()

        vm_choice = input("Press (1) if you would like to edit your task\n Press(-1) to exit\n Enter your selection: ")

        if (vm_choice == "1"):
            edit_choice = input("tc - Task completion\n nu - New user\n dd - Due date change\n Enter your selection: ")
            if (edit_choice == "tc"):
                vm_completion()
                print("Your completion has been registered!")

            elif (edit_choice == "nu"):
                vm_user()
                print("User changed successfully!")

            elif (edit_choice == "dd"):
                vm_due_date()
                print("Due Date chnaged successfully!")

#Functions called to generate the overview reports
    elif (user_choice == "gr"):
        task_generation()
        task_incomplete()
        task_complete()
        percentage_inc()
        print('Task overview report generated!')

        username = input("Enter the username to generate a report on a specific user: ")
        user_estimate()
        task_generation()
        tasks_assigned(username)
        user_percentage(username)
        user_specific_complete(username)
        user_specific_incomplete(username)
        print('User overview report generated!')
        print("To display the results of the report, in the main menu select \"ds\" which will display the statistics.")

#Functions called to display the overview reports
    elif (user_choice == "ds"):
        print("The results of the task overview report are as follows: ")
        task_overview()

        print("The results of the user overview report are as follows: ")
        user_overview()
                         
                               
    elif (user_choice == "e"): #This option is for the user to exit the program
        exit()
        
            
        
            
            
                
            
            
            
            
            
            

    




            
   
    
