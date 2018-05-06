import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.net.ServerSocket;
import java.net.Socket;

public class MainServer {
	public static void main(String[] args) throws IOException {
		System.out.println("Turn On Server");
		int hi;
		ServerSocket s_socket = new ServerSocket(5000);
		while(true) {
			Socket c_socket = null;
			try {

				c_socket = s_socket.accept();
				InputStream input_data = c_socket.getInputStream();
				OutputStream output_data = c_socket.getOutputStream();
				byte[] hihello = new byte[1024];
				while ((hi = input_data.read(hihello)) != -1) {
					output_data.write(hihello, 0, hi);
				}

				output_data.close();

				System.out.println(c_socket + ": 연결 종료");
			}catch(Exception e) {
				e.printStackTrace();
			}finally {
				try {
					if(c_socket != null) {
						c_socket.close();
					}
				}catch(Exception e) {
					e.printStackTrace();
				}
			}
		}
	}
}
