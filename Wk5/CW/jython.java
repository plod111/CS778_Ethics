// jython.java: Demonstrating Jython, allowing Python in Java.
//
// 2024 FA - CSCI 77800 - Edgar E. Troudt, Ph.D.

import org.python.util.PythonInterpreter;
import org.python.core.PyObject;

public class jython {

	public static void main ( String args[] ) {
		PythonInterpreter p = new PythonInterpreter( );
		// PyObject result = p.eval( "..."); // more advanced
		p.exec( "print(\"Hello world\");" );
	}

}
