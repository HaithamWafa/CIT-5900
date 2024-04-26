package roles;

import java.util.ArrayList;
import java.util.Iterator;
import java.util.Map;
import java.util.Map.Entry;
import courses.Course;

//using inheritance property of OOP to extend a User base class with a STUDENT

public class Student extends User {
	
	//array to store all students in the system
	public static ArrayList<Student> students_list = new ArrayList<Student>();
	
	//attributes
	
	// (course, grade) map for each student
	private Map<String, String> courseMap;
	
	//student's courses 
	private ArrayList<Course> enrolledCourses = new ArrayList<Course>();
	
	// constructor to initialize student records
	
	public Student( String name, String id, String userName, String password, Map<String, String> courseMap) {
		
		this.name = name;
		this.id = id;
		this.userName = userName;
		this.password = password;
		this.courseMap = courseMap;
		
	}


	
	public ArrayList<Course> getEnrolledCourses() {
		return enrolledCourses;
	}
	
	public Map<String, String> getCourseMap() {
		return courseMap;
	}
	


	
	
	/**
	 * Adds a course for the student.
	 * 
	 * @param courseID The ID of the course to add.
	 */
	public void addCourse(String courseID) {

	    // Flag to track if the course exists
	    boolean exists = false;

	    // Check if the course is in the course list
	    for (Course course : Course.COURSELIST) {
	        if (course.getId().equals(courseID)) {
	            // The course exists
	            exists = true
	            		
	            // Check if the course has already been taken
	            boolean taken = false;
	            for (Course enrolledCourse : enrolledCourses) {
	                if (enrolledCourse.getId().equals(courseID)) {
	                    System.out.println("The course you selected is already in your list.");
	                    taken = true;
	                    break;
	                }
	            }

	            if (!taken) {
	                // Check for time conflicts
	                if (!course.noTimeConflict(this, course)) {
	                    System.out.println("The course you selected has time conflict with other courses: ");
	                    for (Course conflictCourse : course.getConflictCourses()) {
	                        System.out.println(conflictCourse.getId() + " " + conflictCourse.getName());
	                    }
	                } else {
	                    // Check course capacity
	                    if (course.CourseIsFull()) {
	                        System.out.println("This course is overloaded, so you cannot register for it");
	                    } else {
	                        // No time conflict and course is not full, add the course
	                        System.out.println("Course added successfully.");
	                        enrolledCourses.add(course);
	                        courseMap.put(courseID, null);
	                        course.addEnrolledNum();
	                        if (!course.addStudent.contains(this)) {
	                            course.addStudent.add(this);
	                            course.setAddStudent(course.addStudent);
	                        }
	                    }
	                }
	                break;
	            }
	        }
	    }

	    // Print message if the course doesn't exist
	    if (!exists) {
	        System.out.println("Course not found.");
	    }
	}

	
	
	/**
	 * Drops the specified course for the student.
	 *
	 * @param courseID The ID of the course to be dropped.
	 */
	public void dropCourse(String courseID) {
	    // Set a boolean value to track if the course exists or not
	    boolean exists = false;

	    // Iterate over all courses in the course list to check if the course is present
	    for (Course course : Course.COURSELIST) {
	        if (course.getId().equals(courseID)) {
	            // Change the exists value to true
	            exists = true;

	            // Use a boolean value to track if the course has been selected
	            boolean taken = false;

	            // Iterate over the enrolled courses ArrayList to check if the course has been enrolled before
	            for (Course enrolledCourse : enrolledCourses) {
	                // If the course already exists in the enrolled courses ArrayList
	                if (enrolledCourse.getId().equals(courseID)) {
	                    System.out.println("Course dropped successfully.");

	                    // Delete this student from the course's student list
	                    enrolledCourse.removeStudent(this);

	                    // Remove this course from the enrolled courses list
	                    enrolledCourses.remove(enrolledCourse);

	                    // Remove the course from the courseMap
	                    courseMap.remove(courseID);

	                    // Change the taken value to true
	                    taken = true;
	                    break;
	                }
	            }

	            // If this course has not been chosen before
	            if (!taken) {
	                // Can't drop the course
	                System.out.println("Course not enrolled, cannot be dropped.");
	            }
	            break;
	        }
	    }

	    // If the course does not exist, print out a message
	    if (!exists) {
	        System.out.println("Course not found.");
	    }
	}
	

	

	public void addEnrolledCourse() {
	    // Iterate over each course ID in the student's course map
	    for (String cID : this.courseMap.keySet()) {
	        // Search for the course in the COURSELIST
	        for (Course course : Course.COURSELIST) {
	            // If the course ID matches, add the student to the course,
	            // add the course to the student's enrolled courses,
	            // and increase the enrolled number of the course
	            if (course.getId().equals(cID)) {
	                enrolledCourses.add(course);
	                course.addStudent(this);
	                course.addEnrolledNum();
	                break; // No need to continue searching
	            }
	        }
	    }
	}
	
	/**
	 * Displays the enrolled courses for the student.
	 */
	public void viewEnrolledCourses() {
	    // Iterate over the enrolled courses list and print out each course
	    for (Course course : enrolledCourses) {
	        // Print out the information for each course
	        System.out.println(course);
	    }
	}


	/**
	 * Displays the grades for the student.
	 */
	public void viewGrade() {
	    // Iterate through the courseMap and print out the grades for each course
	    for (Map.Entry<String, String> entry : courseMap.entrySet()) {
	        System.out.println("Grade of " + entry.getKey() + ": " + entry.getValue());
	    }
	}

	
	/**
	 * Checks if the student ID is already occupied.
	 *
	 * @param stuID The student ID to be checked.
	 * @return true if the student ID is occupied, false otherwise.
	 */
	
	/**
	 * Checks if the username is already occupied.
	 *
	 * @param stuUN The username to be checked.
	 * @return true if the username is occupied, false otherwise.
	 */
	public static boolean isUserNameOccupied(String stuUN) {
	    // Iterate over the list of students
	    for (Student student : Student.students_list) {
	        // If the username is occupied
	        if (student.getUserName().equals(stuUN)) {
	            return true;
	        }
	    }
	    // If the username is not occupied
	    return false;
	}

	

	public static boolean isIDOccupied(String stuID) {
	    // Iterate over the list of students
	    for (Student student : Student.students_list) {
	        // If the ID is occupied
	        if (student.getId().equals(stuID)) {
	            return true;
	        }
	    }
	    // If the ID is not occupied
	    return false;
	}

	

}