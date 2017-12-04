package Proxy;

import java.net.*;
import java.io.*;

public class ProxyServer {
    public static void main(String[] args) throws IOException {
        ServerSocket s_socket = null;
        boolean listening = true;

        int port = 8888;	//setting server 
        try {
            port = Integer.parseInt(args[0]);
        } catch (Exception e) {
            // catching exception
        }

        try {
            s_socket = new ServerSocket(port);
            System.out.println("Started on: " + port);
        } catch (IOException e) {
            System.err.println("Could not listen on port: " + args[0]);
            System.exit(-1);
        }

        while(listening) {
            new ProxyThread(s_socket.accept()).start();
        }
        s_socket.close();
    }
}