import java.io.*;
public class BufferedReaderDemo {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader_input = new BufferedReader(  
            new InputStreamReader(System.in));
        System.out.print("請輸入一串文字，可以包括空白字元 : ");
        String text = bufferedReader_input.readLine();
        System.out.println("你輸入的文字:"+text);
    }
    
}
