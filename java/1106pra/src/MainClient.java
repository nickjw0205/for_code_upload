import java.io.InputStream;
import java.io.OutputStream;
import java.net.Socket;
import java.nio.charset.StandardCharsets;

public class MainClient {

	public static void main(String[] args) {
		Socket c_socket = null;
		try {
			c_socket = new Socket("127.0.0.1",5000);
			InputStream input_data = c_socket.getInputStream();
			OutputStream output_data = c_socket.getOutputStream();
			byte[] receiveBuffer = new byte[100];
			int hi;
			while ((hi = System.in.read(receiveBuffer)) != -1) {
				output_data.write(receiveBuffer, 0, hi);
				hi = input_data.read(receiveBuffer);
				System.out.write(receiveBuffer, 0, hi);
				}
			output_data.close();
			while ((hi = input_data.read(receiveBuffer)) != -1)
				System.out.write(receiveBuffer, 0, hi);
				System.out.println();
			input_data.read(receiveBuffer);
			
			System.out.println(new String(receiveBuffer, StandardCharsets.UTF_8));
			

			System.out.println(c_socket + ": 연결 종료");

		}catch(Exception e) {
			e.printStackTrace();
		}finally {
			try {
				c_socket.close();
			}catch(Exception e) {
				
			}
		}

	}

}
