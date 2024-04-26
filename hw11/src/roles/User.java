package roles;

import java.util.ArrayList;

import courses.Course;

/**
 * This represents the abstract class for the user who can access this system
 * which can be extended to be be student, professor or, an adminstrator 
 */

public abstract class User {
	//every user has the following attributes
	String name;
	String id;
	String userName;
	String password;
	
	//getter methods
	public String getName() {
		return name;
	}
	
	public String getId() {
		return id;
	}

	public String getUserName() {
		return userName;
	}

	public String getPassword() {
		return password;
	}
	
//the following method can be used by all users to print their courses
	public void viewAllCourses() {
		for (Course course : Course.COURSELIST) {
	        System.out.println(course);
	    }
	}
}