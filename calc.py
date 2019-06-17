i=1
while i==1:    
     try:
          a=input("Enter the first value:")
          i=i+1
   #  break
     except:
         print("Oops!")
         print("Run again.")
         break
     try:
        b=eval(input("Enter the second value:"))
        i=i+1
    # break
     except:
        print("Oops!") 
        print("Run again.")
        break
     print("1.Addition\n2.Subraction\n3.Division\n4.Multipication\n5.power")
     opt=float(input("Enter Your Choice"))
     opt=round(opt)
     if opt ==1:
            print("the Added value is: ",(a+b))
     elif opt ==2:
                print("the subracted value is: ",a-b)
     elif opt ==3:
                    if a or b == 0 :
                     print("invalid option")
                    else:    
                     print("The Divided value is: ",a/b)
     elif opt ==4:
            print("The multiplied value is",a*b)
     elif opt ==5:
            print(a,"power",b,"is: ",a**b)  
     else:
            print("Invalid option selected")
     break
