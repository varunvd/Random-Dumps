import java.util.StringTokenizer;
 import java.io.*; 
class Check
{
	public static void main(String args[])
	{
		 BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
			String message = new String();
		try{ 
				message = br.readLine(); 
			} catch(IOException e) { 
			System.out.print("Error");
			} 
		 String str = new String();
        String b = new String();
        str=message;
        StringTokenizer tokens = new StringTokenizer(str, " ");
        String[] splited = new String[tokens.countTokens()];
        int index = 0;
        int z=1;
        if(str.charAt(str.length()-1) == '4')
        {
            while(tokens.hasMoreTokens()){
                splited[index] = tokens.nextToken();
                ++index;
            }
            int j=0;
            for(j=0; j<index-1; j++)
            {
                b=b+splited[j];
                b=b+" ";
            }
            message=b;
        }
        else
        {
            str=str.replace("and", "");
            str=str.replace("of", "");
            str=str.replace("with", "");
            str = str.replaceAll("( )+", " ");
            StringTokenizer token = new StringTokenizer(str, " ");
            while(token.hasMoreTokens()){
                splited[index] = token.nextToken();
                ++index;
            }
            int j=0;
            if(splited[index-1].charAt(0) == '1')
            {
                for(j=0; j<index-1; j++)
                {
                    if(splited[j].charAt(1) == '+' || splited[j].charAt(1)=='#' || splited[j].charAt(1)=='.')
                        b=b+splited[j];
                    else
                        b=b+splited[j].charAt(0);

                }
                message=b;
            }
            if(splited[index-1].charAt(0) == '2')
            {
                if(index>=4)
                {
                    for(j=0; j<index-1; j++)
                    {
                        if(splited[j].charAt(1)=='+' || splited[j].charAt(1)=='#' || splited[j].charAt(1)=='.')
                            b=b+splited[j];
                        else{
                            if(splited[j].length()<1)
                                b=b+splited[j];
                            else
                            b=b+splited[j].charAt(0)+splited[j].charAt(1);
                    }}
                    message=b;
                }
                else if(index==3)
                {
                    for(j=0; j<index-1; j++)
                    {
                        if(splited[j].charAt(1) == '+' || splited[j].charAt(1)=='#' || splited[j].charAt(1)=='.')
                            b=b+splited[j];
                        else {
                            if (splited[j].length() <= 2)
                                b = b + splited[j];
                            else
                            b = b + splited[j].charAt(0) + splited[j].charAt(1) + splited[j].charAt(2);
                        }

                    }
                    message=b;
                }
                else
                {
                    if(splited[0].length()-7<=0)
                        b=b+splited[0];
                    else{
                    for(j=0; j<splited[0].length()-6; j++)
                    {
                        b=b+splited[0].charAt(j);
                    }}
                    message=b;
                }

            }
            if(splited[index-1].charAt(0) == '3')
            {
                if(index>=4)
                {
                    for(j=0; j<index-1; j++)
                    {
                        if(splited[j].charAt(1)=='+' || splited[j].charAt(1)=='#' || splited[j].charAt(1)=='.')
                            b=b+splited[j];
                        else{
                            if(splited[j].length()<=3)
                                b=b+splited[j];
                            else
                            b=b+splited[j].charAt(0)+splited[j].charAt(1)+splited[j].charAt(2);
                    }}
                    message=b;
                }
                else if(index==3)
                {
                    for(j=0; j<index-1; j++)
                    {
                        if(splited[j].charAt(1) == '+' || splited[j].charAt(1)=='#' || splited[j].charAt(1)=='.'){
                            b=b+splited[j];}
                        else {
                            if (splited[j].length() < 4)
                                b = b+splited[j];
                            else
                                b = b + splited[j].charAt(0) + splited[j].charAt(1) + splited[j].charAt(2) + splited[j].charAt(3);
                        }
                    }
                    message=b;
                }
                else
                {
                    if(splited[0].length()-4<=0)
                        b=b+splited[0];
                    else{
                    for(j=0; j<splited[0].length()-3; j++)
                    {
                        b=b+splited[0].charAt(j);
                    }}
                    message=b;
                }

            }
        }
		System.out.println(message);
	}
}
