package roles;

import static org.junit.jupiter.api.Assertions.*;

import java.util.ArrayList;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import courses.Course;
import files.FileInfoReader;

class ProfessorTest {
	

	@BeforeEach
	void setUp() throws Exception {
		
		FileInfoReader.setAdminInfo();
		 FileInfoReader.setCourseInfo();
		 FileInfoReader.setStudentInfo();
		 FileInfoReader.setProfessorInfo();
	}

	@Test
	void testGetCourseList() {
		// pro should be Greenberg
		Professor pro = Professor.professors_list.get(0);
		ArrayList<Course> givenCourses = pro.getCourseList();
		// the lecturer of course in list is equal to Clayton Greenberg
		assertEquals("Clayton Greenberg", givenCourses.get(0).getLecturer());
		// the first course should be CIT592
		assertEquals("CIT592", givenCourses.get(0).getId());
		
		Student.students_list.clear();
		Professor.professors_list.clear();
		Admin.admins_list.clear();
		Course.COURSELIST.clear();
		
	}
	
	@Test
	void testIsIDOccupied() {
		
		// 001 is occupied
		assertTrue(Professor.isIDOccupied("001"));
	
		// 12345 is not occupied
		assertFalse(Professor.isIDOccupied("12345"));
		

		Student.students_list.clear();
		Professor.professors_list.clear();
		Admin.admins_list.clear();
		Course.COURSELIST.clear();
		
	}
	
	
	@Test
	void testIsUserNameOccupied() {
		
		// testStudent01 is occupied
		assertTrue(Professor.isUserNameOccupied("Greenberg"));
		
		// curry is not occupied
		assertFalse(Professor.isUserNameOccupied("curry"));
		
		Student.students_list.clear();
		Professor.professors_list.clear();
		Admin.admins_list.clear();
		Course.COURSELIST.clear();
	}
	
	


}