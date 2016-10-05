package ssw567.team2.assignment2;

/*
 *  This file shows some simple (and buggy) python code to solve the Triangles assignment.
 *  The primary goal of this file is to demonstrate a simple pyghon program and use of the
 *  unittest package.
 */
 
public class ImprovedTriangle {

	public String classifyTriangle(int a, int b, int c) {
		/*
		 * This function returns a string with the type of triangle from three integer values
		 * corresponding to the lengths of the three sides of the Triangle.
		 * 
		 * Return:
		 *  - If any side is not between 0 and 200, return "InvalidInput"
		 *  - If all three sides are equal, return 'Equilateral' 
		 *	- If exactly one pair of sides are equal, return 'Isosceles'
		 *  - If not a valid triangle, then return 'NotATriangle'
		 *  - If all sides are different, then return 'Scalene'
		 *  - If the sum of the square of any two sides equals the square of the third side, then return 'Right' in addition to the triangle type 
		 *
		 */
 
		// require that the input values be > 0 and <= 200 
		if (a > 200 || b > 200 || c > 200) { 
			return "InvalidInput";
		}
		
		if (a <= 0 || b <= 0 || c <= 0) { 
			return "InvalidInput";
		}
		
		/*
		  
		  verify that all 3 inputs are integers 
		  Python's "isinstance(object,type) returns True if the object is of the specified type

		  Python is a dynamic typed language and Java is a strong typed language.
		  Meaning that Python gives you the tools like the isinstance method below for you to
		  check variable types, but doesn't force it upon you. So, in Python, you could compile the program
		  using incorrect variables that would throw an error at runtime

          if (not(isinstance(a,int) and isinstance(b,int) and isinstance(c,int)) {
			return "InvalidInput";
		  }
	
		 */
		
		/*
		   This information was not in the requirements spec but is important for correctness
		   the sum of any two sides must be strictly less than the third side
		   of the specified shape is not a triangle
		*/
		if ((a >= (b+c)) || (b >= (c+a)) || (c >= (a + b))) { 
			return "NotATriangle";
		}
		
		String triType = "";

		// now we know that we have a valid triangle
		if ((a==b) && (b==c)) {
			triType = "Equilateral"; 
		}
		else if ((a == b) || (b == c) || (a == c)) { 
			triType = "Isosceles";  
		}
		else {
			triType = "Scalene"; 
		}

		if ((Math.pow(a, 2) + Math.pow(b, 2) == Math.pow(c, 2)) 
				|| (Math.pow(b, 2) + Math.pow(c, 2) == Math.pow(b, 2)) 
				|| (Math.pow(c, 2) + Math.pow(a, 2) == Math.pow(b, 2))) {
			return "Right "+triType;
		} 
		else {
			return triType;
		}			

	}

	// Run classifyTriangle
	public static void runClassifyTriangle (int a, int b, int c) {
		ImprovedTriangle t1 = new ImprovedTriangle();
		
		System.out.println("classifyTriangle(" + a + "," + b + "," + c + ") = " + t1.classifyTriangle(a, b, c)); // Scott - Corrected a, b, c from a, b, b	
	
	}
	
	
	// Invoke ImprovedTriangle with the original BuggyTriangle and Extended arguments and print the results
	public static void main(String[] args) {
		
		/*
		 * Original BuggyTriangle input values used
		 */
		int[][] originalValues = {
				{1, 2, 3}, 
                {1, 1, 1},
                {3, 4, 5}
        	};
		
		System.out.println("Original BuggyTriangle Input Values");
		System.out.println("------------------------------------");
		
		for(int i = 0; i < originalValues.length; i++) {
			ImprovedTriangle.runClassifyTriangle(originalValues[i][0], originalValues[i][1], originalValues[i][2]); 
		}
		
		/*
		 * Extended input values for additional scenarios
		 */
		int[][] extendedValues = {
				{0, 3, 4},
                {4, 4, -4},
                {3, 3, 3},
                {3, 3, 5},
                {6, 5, 4}
        	};

		System.out.println("\n\nExtended ImprovedTriangle Input Values");
		System.out.println("------------------------------------");

		for(int i = 0; i < extendedValues.length; i++) {
			ImprovedTriangle.runClassifyTriangle(extendedValues[i][0], extendedValues[i][1], extendedValues[i][2]);
		}

	}	

}
