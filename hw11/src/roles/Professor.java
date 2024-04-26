package roles;

import java.util.ArrayList;
import courses.Course;

//using inheritance property of OOP to extend a User base class with a PROFESSOR

public class Professor extends User {
	
	//array to store all professors in the system 
	
	public static ArrayList<Professor> PROFESSORS = new ArrayList<Professor>();

	
	// constructor
	
	public Professor(String name, String id, String userName, String password) {
		this.name = name;
		this.id = id;
		this.userName = userName;
		this.password = password;
	}
	

	/**
	 * Retrieves the list of courses taught by the professor.
	 *
	 * @return An ArrayList of courses taught by the professor.
	 */
	public ArrayList<Course> getCourseList() {
	    // Create an ArrayList to store the courses taught by the professor
	    ArrayList<Course> courseList = new ArrayList<>();

	    // Iterate over the list of all courses
	    for (Course course : Course.COURSELIST) {
	        // Check if the professor is teaching the course
	        if (this.getName().equals(course.getLecturer())) {
	            // If yes, add the course to the list
	            courseList.add(course);
	        }
	    }

	    return courseList;
	}

	
	/**
	 * Checks if a professor username is already in the list of professors.
	 *
	 * @param proUN The professor username to check.
	 * @return True if the username is occupied, otherwise false.
	 */
	public static boolean isUserNameOccupied(String proUN) {
	    // Set the initial value to false
	    boolean isUserNameOccupied = false;

	    // Iterate over the list of professors
	    for (Professor professor : Professor.professors_list) {
	        // Check if the username matches
	        if (professor.getUserName().equals(proUN)) {
	            // If the username is occupied, set the flag to true and break the loop
	            isUserNameOccupied = true;
	            break;
	        }
	    }

	    return isUserNameOccupied;
	}

	
	/**
	 * Checks if a professor ID is already in the list of professors.
	 *
	 * @param proID The professor ID to check.
	 * @return True if the ID is occupied, otherwise false.
	 */
	public static boolean isIDOccupied(String proID) {
	    // Set the initial value to false
	    boolean isIDOccupied = false;

	    // Iterate over the list of professors
	    for (Professor professor : Professor.professors_list) {
	        // Check if the ID matches
	        if (professor.getId().equals(proID)) {
	            // If the ID is occupied, set the flag to true and break the loop
	            isIDOccupied = true;
	            break;
	        }
	    }

	    return isIDOccupied;
	}

	

	
	
	
}