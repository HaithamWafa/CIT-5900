package roles;

import static org.junit.jupiter.api.Assertions.*;

import java.util.HashMap;
import java.util.Map;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import courses.Course;
import files.FileInfoReader;

class AdminTest {
	
	@BeforeEach
	void setUp() throws Exception {
		FileInfoReader.setAdminInfo();
		 FileInfoReader.setCourseInfo();
		 FileInfoReader.setStudentInfo();
		 FileInfoReader.setProfessorInfo();
	}

	@Test
	void testAddProfessor() {
		// the old size of professor list
		assertEquals(32, Professor.professors_list.size());
		// add a new professor
		Professor p = new Professor("Newton", "100", "Oldton", "password590");
		Admin.addProfessor(p);
		// the new size of professor list
		assertEquals(33, Professor.professors_list.size());
		
		Student.students_list.clear();
		Professor.professors_list.clear();
		Admin.admins_list.clear();
		Course.COURSELIST.clear();
	}
	
	
	@Test
	void testDelProfessor() {
		// the old size of professor list
		assertEquals(32, Professor.professors_list.size());
		Admin.delProfessor("001");
		// the new size of professor list
		assertEquals(31, Professor.professors_list.size());
				
		Student.students_list.clear();
		Professor.professors_list.clear();
		Admin.admins_list.clear();
		Course.COURSELIST.clear();
		}
	
	
	@Test
	void testAddStudent() {
		// the old size of student list
		assertEquals(2, Student.students_list.size());
		// create a new student
		Map<String, String> courseList = new HashMap<String, String>();
		courseList.put("CIS545", "A+");
		Student newStudent = new Student("003", "student03", "teststudent03", "012345", courseList);
	
		Admin.addStudent(newStudent);
		// the new size of student list
		assertEquals(3, Student.students_list.size());
		
		Student.students_list.clear();
		Professor.professors_list.clear();
		Admin.admins_list.clear();
		Course.COURSELIST.clear();
	}
	
	
	@Test
	void testDelStudent() {
		// the old size of student list
		assertEquals(2, Student.students_list.size());
		Admin.delStudent("001");
		// the new size of student list
		assertEquals(1, Student.students_list.size());
				
			Student.students_list.clear();
			Professor.professors_list.clear();
			Admin.admins_list.clear();
			Course.COURSELIST.clear();
		}
	
	
	
	@Test
	void testAddCourse() {
		// this only considers the legal situation, the other illegal ones will be excluded in the Controller
		// Or we will test the methods independently, such as noTimeConflict() and checkEndTime();
		// the old size of course list
		assertEquals(50, Course.COURSELIST.size());
		Course c = new Course("CIT900", "Web", "Ives", "MW", "14:30", "15:30", "120");
		Admin.addCourse(c);
		// the new size of course list
		assertEquals(51, Course.COURSELIST.size());
		
		Student.students_list.clear();
		Professor.professors_list.clear();
		Admin.admins_list.clear();
		Course.COURSELIST.clear();
		
	}
	
	@Test
	void testDelCourse() {
		// the old size of course list
		assertEquals(50, Course.COURSELIST.size());
		Admin.delCourse("CIS557");
		// the new size of student list
		assertEquals(49, Course.COURSELIST.size());
				
			Student.students_list.clear();
			Professor.professors_list.clear();
			Admin.admins_list.clear();
			Course.COURSELIST.clear();
		}
	
	@Test
	void testcheckEndTime() {
		
		 Admin a = Admin.admins_list.get(0);
		// endTime is later than startTime, return True;
		
		// endTime is earlier than startTime, return False;
	}
	
	
	
	
	
}