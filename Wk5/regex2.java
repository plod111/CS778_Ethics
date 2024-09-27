// regex2.java: Demonstrates using a regular expression to evaluate if keyboard input has an email address.
//
// CSCI 77800 -- 2024 FA -- Edgar E. Troudt, Ph.D.
//
//
// Good reference for how to use Pattern Matching:
//	https://download.java.net/java/early_access/valhalla/docs/api/java.base/java/util/regex/Pattern.html
// Example modified by Edgar Troudt to be more illustrative and work with email addresses.

import java.util.regex.Pattern;
import java.util.regex.Matcher;
import java.util.Scanner;

public class regex2 {
	public static void main ( String args[] ) {
		// RE string taken from: https://www.geeksforgeeks.org/write-regular-expressions/
		Scanner read = new Scanner ( System.in );
		String my_re = """
			       ([a-zA-Z0-9_\\-\\.]+)@([a-zA-Z0-9_\\-\\.]+)\\.([a-zA-Z]{2,5})\
			       """;
		System.out.println( "The regular expression that we are using is: " + my_re );

		Pattern p = Pattern.compile( my_re );
		while ( true ) {
			System.out.print ("Enter an email: " );
			String input = read.nextLine();
			Matcher m = p.matcher( input );
			boolean b = m.matches();

			System.out.println( "Does it match? " + b );
		}
	}
}
