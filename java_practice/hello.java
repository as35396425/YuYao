/**
 * hello 如果要使用javac時可以註解，需要使用編碼utf8  指令為:javac =encoding utf-8 hello.java
 */
public class hello //class後面要等於檔案名稱  大括號裡面可以看成body//
{  
    public static void main(String[] args) //此串即是起始點//
    {
        String yuyao = "hello yuyao" ;  //宣告一個物件 String 名字叫yuyao 內容為"hello yuyao"

        System.out.printf("Hello world hi YuYao %s \n ",yuyao);//如何把文字物件化呢??
        System.out.println(yuyao);     //println不能使用上面的 %s精準化輸出String
    }   
}//再物件裡面定義，程式的起始點//   