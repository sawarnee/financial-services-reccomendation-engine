<%-- 
    Document   : serv1
    Created on : 2 Nov, 2018, 11:34:08 AM
    Author     : kaka
--%>

<%@page import="java.sql.PreparedStatement"%>
<%@page import="java.util.ArrayList"%>
<%@page import="java.sql.ResultSet"%>
<%@page import="java.sql.Statement"%>
<%@page import="java.sql.DriverManager"%>
<%@page import="java.sql.Connection"%>
<%@page import="java.io.InputStream"%>
<%@page contentType="text/html" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
    <head>
            <title>RESULT</title>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1">
    <!--===============================================================================================-->	
            <link rel="icon" type="image/png" href="images/icons/favicon.ico"/>
    <!--===============================================================================================-->
            <link rel="stylesheet" type="text/css" href="vendor/bootstrap/css/bootstrap.min.css">
    <!--===============================================================================================-->
            <link rel="stylesheet" type="text/css" href="fonts/font-awesome-4.7.0/css/font-awesome.min.css">
    <!--===============================================================================================-->
            <link rel="stylesheet" type="text/css" href="vendor/animate/animate.css">
    <!--===============================================================================================-->
            <link rel="stylesheet" type="text/css" href="vendor/select2/select2.min.css">
    <!--===============================================================================================-->
            <link rel="stylesheet" type="text/css" href="vendor/perfect-scrollbar/perfect-scrollbar.css">
    <!--===============================================================================================-->
            <link rel="stylesheet" type="text/css" href="css/util.css">
            <link rel="stylesheet" type="text/css" href="css/main.css">
    <!--===============================================================================================-->
    </head>
    <body>
        
	<div class="limiter">
		<div class="container-table100">
                            <h1>RECOMMENDED ARE THE FOLLOWING....</h1>

			<div class="wrap-table100">
                    <h1>OFFLINE SHOPS</h1>                            
				<div class="table100 ver1 m-b-100">
					<div class="table100-head">
						<table>
							<thead>
								<tr class="row100 head">
									<th class="cell100 column1">Clothes</th>
									<th class="cell100 column2">Groceries</th>
									<th class="cell100 column3">Cosmetics</th>
									<th class="cell100 column4">Medicines</th>
									<th class="cell100 column5">Food</th>
								</tr>
							</thead>
						</table>
					</div>
                                    
					<div class="table100-body js-pscroll">
						<table>
							<tbody>
								<tr class="row100 body">
                                                                    <%
                                                                        
            String age = request.getParameter("age").replaceAll(" ", "_");
            String gender = request.getParameter("gender").replaceAll(" ", "_");
            String occupation = request.getParameter("occupation").replaceAll(" ", "_");
            String location = request.getParameter("location").replaceAll(" ", "_");
            String monthly_income = request.getParameter("monthly_income").replaceAll(" ", "_");
            
		try{
			Process p = Runtime.getRuntime().exec("cmd /c python C:\\Users\\kaka\\Documents\\NetBeansProjects\\minor\\src\\python\\back_code3.py "+age+" "+occupation+" "+gender+" "+location);

                        InputStream is = p.getInputStream();

			int i=0;
			StringBuffer sb = new StringBuffer();
                        
			while((i=is.read())!=-1)
			{
				sb.append((char)i);
			}
                    
                        String str = sb.toString();
                        String s = "";
                        for(int index = 0; index < str.length() - 2; index++){
                            if(!(str.charAt(index) == '[' || str.charAt(index) == ']' || str.charAt(index) == ' ')){
                                s += str.charAt(index);
                    
                            }
                            
                        }
                       
                        String strings[] = s.split(",");
                        
                        int arr[] = new int[strings.length];
                        
                        for(int k=0; k<arr.length; k++)
                        {
                            arr[k] = Integer.parseInt(strings[k]);
                        }

                        Class.forName("com.mysql.jdbc.Driver");
                        Connection con = DriverManager.getConnection("jdbc:mysql://localhost:3306/recommendation","root","kaka");
                        PreparedStatement stmt = con.prepareStatement("select * from ex_survey where userid=?");
                        for(int k=0; k<5; k++)
                        {
                            stmt.setInt(1, arr[k]);
                            ResultSet rs = stmt.executeQuery();
                            while(rs.next())
                            {
                                String clothes = rs.getString(7);
                                String groceries = rs.getString(8);
                                String cosmetics = rs.getString(9);
                                String medicines = rs.getString(10);
                                String food = rs.getString(11);
                                
                                %>
                                <td class="cell100 column1"><%= clothes %></td>
                                <td class="cell100 column2"><%= groceries %></td>
                                <td class="cell100 column3"><%= cosmetics %></td>
                                <td class="cell100 column4"><%= medicines %></td>
                                <td class="cell100 column5"><%= food %></td>
                                                                </tr>
                                
                                <%
                                
                            }
                        }
                        %>
                                                        </tbody>
                                                </table>
                                        </div>
                                </div>
                        </div>
                </div>
        </div>
                                                                                                               
	<div class="limiter">
		<div class="container-table100">
			<div class="wrap-table100">
                            <h1>ONLINE PORTALS</h1>
                            	<div class="table100 ver1 m-b-100">
					<div class="table100-head">
						<table>
							<thead>
								<tr class="row100 head">
									<th class="cell100 column1">Clothes</th>
									<th class="cell100 column2">Groceries</th>
									<th class="cell100 column3">Cosmetics</th>
									<th class="cell100 column4">Medicines</th>
									<th class="cell100 column5">Food</th>
								</tr>
							</thead>
						</table>
					</div>
                                    
					<div class="table100-body js-pscroll">
						<table>
							<tbody>
								<tr class="row100 body">
                                                                    <%
                        stmt = con.prepareStatement("select * from ex_survey where userid=?");
                        for(int k=0; k<5; k++)
                        {
                            stmt.setInt(1, arr[k]);
                            ResultSet rs = stmt.executeQuery();
                            while(rs.next())
                            {
                                String clothes = rs.getString(13);
                                String groceries = rs.getString(14);
                                String cosmetics = rs.getString(15);
                                String medicines = rs.getString(16);
                                String food = rs.getString(17);
                                
                                %>
                                <td class="cell100 column1"><%= clothes %></td>
                                <td class="cell100 column2"><%= groceries %></td>
                                <td class="cell100 column3"><%= cosmetics %></td>
                                <td class="cell100 column4"><%= medicines %></td>
                                <td class="cell100 column5"><%= food %></td>
                                                                </tr>
                                
                                <%
                                
                            }
                        }
                                                        
                                                        
                        
		}
		catch(Exception e){
			out.println(e);
		}
                                                                                    
                                                                        %>
<!--===============================================================================================-->	
	<script src="vendor/jquery/jquery-3.2.1.min.js"></script>
<!--===============================================================================================-->
	<script src="vendor/bootstrap/js/popper.js"></script>
	<script src="vendor/bootstrap/js/bootstrap.min.js"></script>
<!--===============================================================================================-->
	<script src="vendor/select2/select2.min.js"></script>
<!--===============================================================================================-->
	<script src="vendor/perfect-scrollbar/perfect-scrollbar.min.js"></script>
	<script>
		$('.js-pscroll').each(function(){
			var ps = new PerfectScrollbar(this);

			$(window).on('resize', function(){
				ps.update();
			})
		});
			
		
	</script>
<!--===============================================================================================-->
	<script src="js/main.js"></script>
            

    </body>
</html>
