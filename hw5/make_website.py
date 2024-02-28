def read_file(filename):
    """
    1. Opens and reads a file.

    Args:
        path (str): file path
    Returns:
        list: all lines in file
    """
    with open(filename, "r") as f:
        lines = f.readlines()
    return lines
def get_name(resume):
    """
    1. Removes leading or trailing whitespace.
    2. Checks if the first letter in 'name' is uppercase.
    Args:
        resume (str): the name of resume
    Returns:
        str: "Invalid Name" if 'name' is invalid,
            otherwise 'name' without leading or trailing whitespace
    """
    name = resume[0].strip()
    if(name[0].isupper()):
        return name
    else:
        return "Invalid Name"
def get_email(resume):
    """
    1. Searches for email using the @ identifier in the resume
    2. Removes leading or trailing whitespace.
    3. Checks if 'email' is in a valid format.

    Args:
        resume (str): name of the resume 
    Returns:
        str: empty string if 'email' is invalid,
            otherwise 'email' without leading or trailing whitespace
    """
    identifier = '@'
    for line in resume:
        if(identifier in line): #check for an identifier hit
            email = line.strip() #remove whitespaces
            idx = email.index("@") + 1 #index right after the @
            allowed_extensions = [".edu", ".com"] #a list of all allowed extensions (can be edited for future use)
            extension_idx = -4 
            if email[extension_idx:] not in allowed_extensions: #checking invalid extension
                return ""
            if not email[idx].islower():  #checking invalid uppercase letter after the @
                return ""
            for ch in email:  #checking if there is a digit in the email (invalid)
                if(ch.isdigit()):
                    return ""
            return email
    return ""    
def get_courses(resume):
    """
    1. Searches the resume for the courses.
    2. Removes leading or trailing whitespace.

    Args:
        resume (str): name of the resume
    Returns:
        list: empty list if no courses are found or all the courses if it is found
    """
    identifier = "Courses"
    for line in resume:
        if(identifier in line):  #check for an identifier hit
            courses = line.strip()[len(identifier):]  #remove whitespaces
            idx = 0
            for i, ch in enumerate(courses):
                if ch.isalpha():  #finding the index of the first course
                    idx = i
                    break
            if idx == 0:  #if no courses are listed, return empty list
                courses = []
                return courses
            else:
                courses = courses[idx:].split(",")  #otherwise, separate at the ',' and return courses
                courses = [course.strip() for course in courses]
                return courses
    return []
def get_projects(resume):
    """
    1. Searches for the Projects in the resume until the end line
    2. Removes empty projects.
    3.  Removes leading or trailing whitespaces.
    Args:
        resume (str): name of the resume
    Returns:
        list: projects
    """
    projects_list = []
    end = 0
    identifier = "Projects"
    for i in range(len(resume)):
        if(identifier in resume[i]): #check for an identifier hit
            i+=1 #increment to get the next line after "Projects"
            while(end == 0): #a flag to signal the end line after the projects section
                projects_list.append(resume[i]) #adding a project line by line in the loop
                i+=1 
                if("-" * 10  in resume[i]): #condition to signal a flag for the end line and stop the loop
                 end = 1
           # print(projects_list)  
    return [project.strip() for project in projects_list if project.strip()] #removing whitespaces and empty projects using list comprehension

    

def surround_block(tag, text):
    """
    Surrounds the given text with the given html tag and returns the string.
    """

    return f"<{tag}>{text}</{tag}>"

def create_email_link(email_address):
    """
    Creates an email link with the given email_address.
    To cut down on spammers harvesting the email address from the webpage,
    displays the email address with [aT] instead of @.

    Example: Given the email address: lbrandon@wharton.upenn.edu
    Generates the email link: <a href="mailto:lbrandon@wharton.upenn.edu">lbrandon[aT]wharton.upenn.edu</a>

    Note: If, for some reason the email address does not contain @,
    use the email address as is and don't replace anything.
    """

    if '@' in email_address:
        formatted_email = '<a href="mailto:{}">{}</a>'.format(email_address, email_address.replace('@', '[aT]'))
    else:
        formatted_email = '<a href="mailto:{}">{}</a>'.format(email_address, email_address)

    return formatted_email

def generate_html(txt_input_file, html_output_file):
    """
    Loads given txt_input_file,
    gets the name, email address, list of projects, and list of courses,
    then writes the info to the given html_output_file.

    # Hint(s):
    # call function(s) to load given txt_input_file
    # call function(s) to get name
    # call function(s) to get email address
    # call function(s) to get list of projects
    # call function(s) to get list of courses
    # call function(s) to write the name, email address, list of projects, and list of courses to the given html_output_file
    """

    resume = read_file(txt_input_file) #reading the resume
    name = get_name(resume) #fetching name
    email = get_email(resume) #fetching email
    courses = get_courses(resume) #fetching courses
    projects = get_projects(resume) #fetching projects

    #writing the fetched info in html
    with open(html_output_file, "w") as html_file:
        html_file.write("<html>\n<head>\n</head>\n<body>\n")
        html_file.write(surround_block("div", surround_block("h1", name)))
        html_file.write(surround_block("p", f"Email: {create_email_link(email)}"))
        html_file.write(surround_block("div", surround_block("h2", "Projects") + surround_block("ul", '\n'.join([f"<li>{project}</li>" for project in projects]))))
        html_file.write(surround_block("div", surround_block("h3", "Courses") + f"<span>{', '.join(courses)}</span>"))
        html_file.write("</div>\n</body>\n</html>")
def main():
   ## uncomment for testing
  #  resume = read_file("resume.txt")
   # name = get_name(resume)
   # print(name)
   # email = get_email(resume)
   # print(email)
   # courses = get_courses(resume)
   # print(courses)
   # projects = get_projects(resume)
   # print(projects)

    # DO NOT REMOVE OR UPDATE THIS CODE
    # generate resume.html file from provided sample resume.txt
    generate_html('resume.txt', 'resume.html')

    # DO NOT REMOVE OR UPDATE THIS CODE.
    # Uncomment each call to the generate_html function when you’re ready
    # to test how your program handles each additional test resume.txt file
    generate_html('TestResumes/resume_bad_name_lowercase/resume.txt', 'TestResumes/resume_bad_name_lowercase/resume.html')
    generate_html('TestResumes/resume_courses_w_whitespace/resume.txt', 'TestResumes/resume_courses_w_whitespace/resume.html')
    generate_html('TestResumes/resume_courses_weird_punc/resume.txt', 'TestResumes/resume_courses_weird_punc/resume.html')
    generate_html('TestResumes/resume_projects_w_whitespace/resume.txt', 'TestResumes/resume_projects_w_whitespace/resume.html')
    generate_html('TestResumes/resume_projects_with_blanks/resume.txt', 'TestResumes/resume_projects_with_blanks/resume.html')
    generate_html('TestResumes/resume_template_email_w_whitespace/resume.txt', 'TestResumes/resume_template_email_w_whitespace/resume.html')
    generate_html('TestResumes/resume_wrong_email/resume.txt', 'TestResumes/resume_wrong_email/resume.html')

    # If you want to test additional resume files, call the generate_html function with the given .txt file
    # and desired name of output .html file

if __name__ == '__main__':
    main()