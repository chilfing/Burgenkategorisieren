package random;

import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;

public class TextWriter {
	public static void main(String[] args) throws Exception {
		String line;
		
		try {

	        BufferedReader bufferreader = new BufferedReader(new FileReader("./burgen.txt"));
	        FileWriter fw = new FileWriter("./burgenEdit.txt");  


	        while (true) { 
	        	line = bufferreader.readLine();
	        	if (line == null) {
	        		break;
	        	}
	        	fw.write("* " + line + " => kein passender Wikidata Eintrag gefunden!");
	        	fw.write(System.lineSeparator());
	        	
	        }
	        fw.close();

	    } catch (FileNotFoundException ex) {
	        ex.printStackTrace();
	    } catch (IOException ex) {
	        ex.printStackTrace();
	    }
		
	}
}
