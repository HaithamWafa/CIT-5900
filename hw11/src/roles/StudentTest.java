package roles;

import static org.junit.jupiter.api.Assertions.*;

import java.util.HashMap;
import java.util.Map;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import courses.Course;
import files.FileInfoReader;



class StudentTest {


	Student student;
	
	 @BeforeEach
	    void setUp() throws Exception {
		
		 FileInfoReader.setAdminInfo();
		 FileInfoReader.setCourseInfo();
		 FileInfoReader.setStudentInfo();
		 FileInfoReader.setProfessorInfo();
	      
	    }
	 
	 

	@Test
	void testAddEnrolledCourse() {
		
		
		Map<String, String> courseList = new HashMap<String, String>();
		
		courseList.put("CIS545", "A+");
		
		courseList.put("CBE554", "A+");
		
		Student newStudent = new Student("003", "student03", "teststudent03", "012345", courseList);
		
		// can not put course which are not in the list into the enrolled list (eg."CBE554")
		// can add course like "CIS545" which is on the course list
		newStudent.addEnrolledCourse();
		assertEquals(1, newStudent.getEnrolledCourses().size());	
		
		
		
		Student.students_list.clear();
		Professor.professors_list.clear();
		Admin.admins_list.clear();
		Course.COURSELIST.clear();
		
	}
	 
	

	@Test
	void testAddCourse() {
		
		
		student = Student.students_list.get(0);

		
		

		student.addEnrolledCourse();
		
		// add a course which had been selected before, should not get enrolled
		
		System.out.println(Course.COURSELIST.get(12).getAddStudent().size());
		student.addCourse("CIS191");
		assertEquals(2, student.getEnrolledCourses().size());
		
		// test whether the list of enrolled student is +1
		
		//add a course that dose not exist, should not get enrolled
		student.addCourse("CBE554");
		assertEquals(2, student.getEnrolledCourses().size());

		// add a course and successful
		student.addCourse("CIT594");
		assertEquals(3, student.getEnrolledCourses().size());
		
		// then get the add course and check the enrolledNum
		Course firstClass = student.getEnrolledCourses().get(2);
		assertEquals(1, firstClass.getEnrolledNum());
		
		// check the course's student list
		assertEquals(1, firstClass.addStudent.size());
		
		// and check the capacity
		assertEquals("72", firstClass.getCapacity());
		// make the course full and then check whether the student can add the course
		for (int i = 0; i < 71; i++) {
			firstClass.addEnrolledNum();
		}
		assertEquals(72, firstClass.getEnrolledNum());
		
		// then another student add the course, which should be failed
		Student student2 = Student.students_list.get(1);
		student2.addEnrolledCourse();
		//load the enrolled courses to the list of enrolledCourses
		assertEquals(2, student2.getEnrolledCourses().size());
		student2.addCourse("CIT594");
		// nothing changes
		assertEquals(2, student2.getEnrolledCourses().size());
		
		
		
		
		
		Student.students_list.clear();
		Professor.professors_list.clear();
		Admin.admins_list.clear();
		Course.COURSELIST.clear();
		
		
	}

	@Test
	void testDropCourse() {
		
		
		student = Student.students_list.get(1);

		student.addEnrolledCourse();
		
		
		// drop a course which had not been selected before, should not get dropped
		student.dropCourse("CIS191");
		assertEquals(2, student.getEnrolledCourses().size());
		
		
		// drop a course that dose not exist, should not get dropped
		student.dropCourse("CBE554");
		assertEquals(2, student.getEnrolledCourses().size());
		
		
		// drop a course and successful
		student.dropCourse("CIT592");
		assertEquals(1, student.getEnrolledCourses().size());
		
		
		Student.students_list.clear();
		Professor.professors_list.clear();
		Admin.admins_list.clear();
		Course.COURSELIST.clear();
		
		
	}
	
	@Test
	void testIsIDOccupied() {
		
	
		// 001 is occupied
		assertTrue(Student.isIDOccupied("001"));
		
		
		// 12345 is not occupied
		assertFalse(Student.isIDOccupied("12345"));
		
		Student.students_list.clear();
		Professor.professors_list.clear();
		Admin.admins_list.clear();
		Course.COURSELIST.clear();
		
	}

	@Test
	void testIsUserNameOccupied() {
		
		// testStudent01 is occupied
		assertTrue(Student.isUserNameOccupied("testStudent01"));
		
		// xinyangs is not occupied
		assertFalse(Student.isUserNameOccupied("xinyangs"));
		
		Student.students_list.clear();
		Professor.professors_list.clear();
		Admin.admins_list.clear();
		Course.COURSELIST.clear();
	}
	
	


}