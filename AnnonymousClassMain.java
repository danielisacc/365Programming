import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.List;

public class AnnonymousClassMain {

	public static void main(String[] args) {
		
		List<Employee> emps = new ArrayList<>();
		emps.add(new Employee("John","Cameron",29));
		emps.add(new Employee("Ken","Brown",49));
		emps.add(new Employee("Kelly","Dounter",28));
		emps.add(new Employee("Jennifer","Johnson",34));
		emps.add(new Employee("Jerry","Jackson",50));
		
		//Anonymous class that implements the Comparator Interface
		Comparator<Employee> comp = new Comparator<Employee>(){

			@Override
			public int compare(Employee i, Employee j) {
				if(i.age > j.age)
					return 1;
				else 
					return -1;
				
			}
		};
		
		Collections.sort(emps, comp);
		System.out.println(emps);
	}

}
