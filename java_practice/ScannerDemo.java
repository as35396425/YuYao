import java.util.Scanner;
//示範如何使用Scanner取得使用者輸入，Scanner取得輸入，不得包括空白字元，若想取得空白字元可以使用"BufferedReader" 取得輸入
public class ScannerDemo 
{
    public static void main(String[] args) 
    {
        Scanner my_input = new Scanner(System.in); //新增一個Scanner物件叫做 my_input   new 表示要新增物件Scanner 且Scanner需要System.in取得輸入
        //Scanner為System.in的支援者
        System.out.printf("請輸入數字:");
        System.out.printf("哈囉！ %d !\n", my_input.nextInt()); //  使用Scanner工具中的next()功能來取得使用者輸入的字串  
                                                                //  也可以輸入nextInt取得int型態的整數   //
    }
}
