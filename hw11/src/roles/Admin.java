package roles;

import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Date;

import courses.Course;

//using inheritance property of OOP to extend a User base class with an ADMIN

public class Admin extends User{
	
//array to store all admins in the system
	public static ArrayList<Admin> admins_list = new ArrayList<Admin>();
	
	//Admin class constructor
	
	/**
	 * creates an admin and initializes his/her credentials
	 * @param name
	 * @param id
	 * @param userName
	 * @param password
	 */
	
	public Admin(String name, String id, String userName, String password) {
		this.name = name;
		this.id = id;
		this.userName = userName;
		this.password = password;
		
	}
	
	//adding a student
		public static void addStudent(Student student) {
			
			
			try {
				Student.students_list.add(student);
				}
				catch(Exception e) {
					System.out.println("Unable to add student");
				}

			System.out.println("Successfully added the new student " + student.getName() + " with ID " + student.getId());
		}
		
		
		//deleting a student using his/her ID
		public static void delStudent(String studentID) {
			
		//searching for the student ID
			for(int i = 0; i < Student.students_list.size(); i++) {
					
					if(Student.students_list.get(i).getId() == studentID) {
						try {
							Student.students_list.remove(i);
							}
							catch(Exception e) {
								System.out.println("Unable to remove student");
							}
						System.out.println("Successfully removed the student " +  Student.students_list.get(i).getName() + " with ID " + Student.students_list.get(i).getId());
						
					}
				}
		}
		
	//adding new professor
	public static void addProfessor(Professor professor) {
		
		try {
			Professor.professors_list.add(professor);
			}
			catch(Exception e) {
				System.out.println("Unable to add professor");
			}
		System.out.println("Successfully added the new professor " + professor.getName() + " with ID " + professor.getId());
		
	}
	//deleting an existing professor
	
	public static void delProfessor(String proID) {
		
		//seaching for professor using his/her ID
		
		for(int i = 0; i < Professor.professors_list.size(); i++) {
			
			if(Professor.professors_list.get(i).getId() == proID){
				
				System.out.println("Successfully remove the professor: " + Professor.professors_list.get(i).getId() + " " + Professor.professors_list.get(i).getName());
				
				try {
					Professor.professors_list.remove(i);
					}
					catch(Exception e) {
						System.out.println("Unable to remove professor");
					}
				System.out.println("Successfully removed the professor " + Professor.professors_list.get(i).getName() + " with ID " + Professor.professors_list.get(i).getId());
			}
		}
		
	}
	
	//adding a new course 
	
	public static void addCourse(Course course) {
		try {
			Course.COURSELIST.add(course);
			}
			catch(Exception e) {
				System.out.println("Unable to add course");
			}
		
		System.out.println("Successfully added the course: " + course);
		
	}

	//deleting an existing course using course ID
	
	public static void delCourse(String courseID) {
		// finding the course 
		for(int i = 0; i < Course.COURSELIST.size(); i++) {
	
				if(Course.COURSELIST.get(i).getId() == courseID) {
					try {
						Course.COURSELIST.remove(i);
						}
						catch(Exception e) {
							System.out.println("Unable to remove course");
						}
					
					System.out.println("Successfully removed the course: " + Course.COURSELIST.get(i).getId() + " " + Course.COURSELIST.get(i).getName());

				}
			}
		
	}
		
	//checking endtime violation
	
	public boolean checkEndTime(String start, String end) {
	    SimpleDateFormat sdf = new SimpleDateFormat("hh:mm");
	    try {
	        Date startTime = sdf.parse(start);
	        Date endTime = sdf.parse(end);
	        return endTime.after(startTime);
	    } catch (ParseException e) {
	        e.printStackTrace();
	        return false;
	    }
	}
	

}