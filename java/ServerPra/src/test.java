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

public class test{  

	public static void main(String[] args) throws Exception {

		int port = 9990;
		ServerSocket s_socket = new ServerSocket(port);

		while (true) {

			Socket clientSocket = s_socket.accept();

			BufferedReader in = new BufferedReader(new InputStreamReader(clientSocket.getInputStream())); 
			PrintWriter out = new PrintWriter(new BufferedWriter(new OutputStreamWriter(clientSocket.getOutputStream())), true);   

			String s;
			while ((s = in.readLine()) != null) {
				System.out.println(s);
				out.write("HTTP/1.0 200 OK\r\n");
				out.write("Date: Fri, 31 Dec 1999 23:59:59 GMT\r\n");
				out.write("Server: Apache/0.8.4\r\n");
				out.write("Content-Type: text/html\r\n");
				out.write("Content-Length: 59\r\n");
				out.write("Expires: Sat, 01 Jan 2000 00:59:59 GMT\r\n");
				out.write("Last-modified: Fri, 09 Aug 1996 14:21:40 GMT\r\n");
				out.write("\r\n");
			}
			out.close();
			in.close();
			clientSocket.close();
		}
	}
}