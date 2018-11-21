import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.io.PrintWriter;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.Statement;
import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

public class serv1 extends HttpServlet {

    protected void processRequest(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        response.setContentType("text/html;charset=UTF-8");
        PrintWriter out = response.getWriter();
        String age = request.getParameter("age").replaceAll(" ", "_");
        String gender = request.getParameter("gender").replaceAll(" ", "_");
        String occupation = request.getParameter("occupation").replaceAll(" ", "_");
        String location = request.getParameter("location").replaceAll(" ", "_");
        String monthly_income = request.getParameter("monthly_income").replaceAll(" ", "_");
        
        
//        out.println(age);
//        out.println(gender);
//        out.println(occupation);
//        out.println(location);
//        out.println(monthly_income);
        
		try{
//			Process p = Runtime.getRuntime().exec("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe");
			Process p = Runtime.getRuntime().exec("cmd /c python C:\\Users\\kaka\\Documents\\NetBeansProjects\\minor\\src\\python\\back_code3.py "+age+" "+occupation+" "+gender+" "+location);

//                        Process p = Runtime.getRuntime().exec("cmd /c python C:\\Users\\kaka\\Documents\\NetBeansProjects\\minor\\src\\python\\back_code.py 21 Student Male New_Delhi");
			
                        InputStream is = p.getInputStream();

			int i=0;
			StringBuffer sb = new StringBuffer();
                        
//                        OutputStream sb = new FileOutputStream("C:\\Users\\kaka\\Desktop\\outputfile.txt");
             
			while((i=is.read())!=-1)
			{
				sb.append((char)i);
//                                sb.write((char)i);
			}
//			out.println(sb.toString());
                    
                        String str = sb.toString();
                        String s = "";
                        for(int index = 0; index < str.length() - 2; index++){
                            if(!(str.charAt(index) == '[' || str.charAt(index) == ']' || str.charAt(index) == ' ')){
                                s += str.charAt(index);
                    
                            }
                            
                        }
                       
                        String strings[] = s.split(",");
//                        for(int k=0; k<strings.length; k++)
//                        {
//                            out.println(strings[k]+"<br>");
//                        }
                        
                        
                        int arr[] = new int[strings.length];
                        
                        for(int k=0; k<arr.length; k++)
                        {
                            arr[k] = Integer.parseInt(strings[k]);
                        }

                        for(int k=0; k<arr.length; k++)
                        {
                            out.println(arr[k]+"<br>");
                        }
                        
                        Class.forName("com.mysql.jdbc.Driver");
                        Connection con = DriverManager.getConnection("jdbc:mysql://localhost:3306/recommendation","root","kaka");
                        Statement stmt = con.createStatement();
                        ResultSet rs = stmt.executeQuery("select * from ex_survey where userid="+arr[0]);
                        while(rs.next())
                        {
                            String clothes_off = rs.getString(7);
                            String groceries_off = rs.getString(8);
                            String cosmetics_off = rs.getString(9);
                            String medicines_off = rs.getString(10);
                            String food_off = rs.getString(11);
                            
                            out.println(clothes_off+"<br>");
                            out.println(groceries_off+"<br>");
                            out.println(cosmetics_off+"<br>");
                            out.println(medicines_off+"<br>");
                            out.println(food_off+"<br>");
                        }
                        
                        
		}
		catch(Exception e){
			out.println(e);
		}
	}
        
    
    

    // <editor-fold defaultstate="collapsed" desc="HttpServlet methods. Click on the + sign on the left to edit the code.">
    /**
     * Handles the HTTP <code>GET</code> method.
     *
     * @param request servlet request
     * @param response servlet response
     * @throws ServletException if a servlet-specific error occurs
     * @throws IOException if an I/O error occurs
     */
    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        processRequest(request, response);
    }

    /**
     * Handles the HTTP <code>POST</code> method.
     *
     * @param request servlet request
     * @param response servlet response
     * @throws ServletException if a servlet-specific error occurs
     * @throws IOException if an I/O error occurs
     */
    @Override
    protected void doPost(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        processRequest(request, response);
    }

    /**
     * Returns a short description of the servlet.
     *
     * @return a String containing servlet description
     */
    @Override
    public String getServletInfo() {
        return "Short description";
    }// </editor-fold>

}
