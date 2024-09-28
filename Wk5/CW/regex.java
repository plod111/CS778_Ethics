// regex.java: Demonstrates the replaceAll function.
//
// Edgar Troudt - CSCI 70900 - 2024 FA
public class regex {

	public static void main ( String args[] ) {
		String s = "This is a string that has a sentence.";
		System.out.println( s );
		String t = s.replaceAll( "a", "A" );
		t = t.replaceAll( "e", "E" );
		t = t.replaceAll( "i", "I" );
		t = t.replaceAll( "o", "O" );
		t = t.replaceAll( "u", "U" );
		System.out.println( t );
	}

}
