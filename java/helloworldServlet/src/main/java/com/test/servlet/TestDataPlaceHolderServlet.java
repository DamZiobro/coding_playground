package com.test.servlet;

import java.io.IOException;
import java.io.PrintWriter;

import javax.servlet.Servlet;
import javax.servlet.ServletConfig;
import javax.servlet.ServletContext;
import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;

/**
 * Servlet implementation class TestDataPlaceHolder
 */
/**
 * @author preetham
 *
 */
public class TestDataPlaceHolderServlet extends HttpServlet {
	private static final long serialVersionUID = 1L;
       
    /**
     * @see HttpServlet#HttpServlet()
     */
    public TestDataPlaceHolderServlet() {
        super();
        System.out.println("TestDataPlaceHolderServlet servlet constructor called");
    }

    /**
	 * @see Servlet#init(ServletConfig)
	 */
	public void init(ServletConfig config) throws ServletException {
		System.out.println("TestDataPlaceHolderServlet \"Init\" method called");
	}

	/**
	 * @see Servlet#destroy()
	 */
	public void destroy() {
		System.out.println("TestDataPlaceHolderServlet \"Destroy\" method called");
	}


    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException,IOException
    {
    	System.out.println("TestDataPlaceHolderServlet doGet method called");
    	doPost(request,response);
    	
    }
	/**
	 * @see HttpServlet#doPost(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		System.out.println("TestDataPlaceHolderServlet servlet doPost method called");
		PrintWriter out = response.getWriter();
		out.write("<html><body><h4>Check console to understand the flow</h4></body></html>");
		//get the value from the request
		String requestValue= (String)request.getAttribute("requestKey");
		if(requestValue!=null)
		{
			out.write("<html><body><h1>Value stored in request is "+ requestValue+" </h1></body></html>");
			out.write("<html><body><h5><i> The data in request scope was sent from dataPlaceHolder.jsp(DataPlaceHolderServlet) to TestDataPlaceHolderServlet. The data in request scope will be present for forthcoming servlets. For new requests this data will not be present</i> </h5></body></html>");
		}
		
		//get the exisitng session
		HttpSession session = request.getSession(false);
		if(session!=null)
		{
			//get the value from the session
			String sessionValue=(String) session.getAttribute("sessionKey");
			System.out.println("Value stored in session is "+ sessionValue);
			out.write("<html><body><h1>Value stored in session is "+ sessionValue+"</h1></body></html>");
			
		}
		else{
			out.write("<html><body><h1>Session not present</h1></body></html>");
		}
		
		ServletContext context = request.getServletContext();
		//get the value from the servlet context
		String contextValue = (String)context.getAttribute("servletContextKey");
		if(contextValue!=null)
		{
			out.write("<html><body><h1>Value stored in servlet context is "+ contextValue+"</h1></body></html>");
		}
		out.write("<html><body><p>&copy 2016 Preetham</p></body></html>");
	}

}
