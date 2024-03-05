
public class Employee {
	
	public String firstName;
	public String lastName;
	public Integer age;
	
	
	public Employee(String firstName, String lastName, Integer age) {
		this.firstName = firstName;
		this.lastName = lastName;
		this.age = age;
	}
	
	public int getAge() {
		return this.age;
	}
	
	@Override
	public String toString() {
		return String.format(
				  "\nFirst Name: %s\n"
				+ "Last Name: %s\n"
				+ "Age: %d\n", firstName, lastName, age);
	}
}
