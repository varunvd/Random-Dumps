import java.io.*;
import java.net.*;
public class DailyAdviceClient {
public void go() {
try {
	Socket s = new Socket("192.168.43.96", 8000);
	InputStreamReader streamReader = new InputStreamReader(s.getInputStream());
	BufferedReader reader = new BufferedReader(streamReader);
	String advice = reader.readLine();
	System.out.println("Today your advice is:" + " " + advice);
	reader.close();
	} catch(IOException ex) {
		ex.printStackTrace();
	}
	}
public static void main(String[] args) {
	DailyAdviceClient client = new DailyAdviceClient();
	client.go();
}
}


