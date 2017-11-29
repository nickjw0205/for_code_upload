import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.DataOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.io.OutputStreamWriter;
import java.io.PrintWriter;
import java.net.ServerSocket;
import java.net.Socket;

public class test1{  

	public static void main(String[] args) throws Exception {

		ServerSocket s_socket = new ServerSocket(9992);

		while (true) {
			Socket c_socket = s_socket.accept();
			
			BufferedReader in = new BufferedReader(new InputStreamReader(c_socket.getInputStream())); 
			PrintWriter out = new PrintWriter(new BufferedWriter(new OutputStreamWriter(c_socket.getOutputStream())), true);
			


			
			String s;
			int i = 0;
			System.out.println("HTTP/1.0 200 OK\r\n");
			out.println("HTTP/1.1 200 OK\r\n");
			out.flush();

			while (!(s = in.readLine()).equals("")) {
				System.out.println(s);
				out.println(s);
				out.flush();

			}

			try {
				out.close();
				in.close();
				c_socket.close();
				s_socket.close();
			}catch(Exception e) {
				
			}

		}

	}
}