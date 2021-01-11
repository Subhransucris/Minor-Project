#code to track COVID-19 using Python

for i in range(0,100):
    print(" ")

    #importing covid module
    from covid import Covid
    print("COVID TRACKER:-")
    
    #creating a object for operation using COVID module for Web Data Analysis
    cv=Covid()

    #Global Results as well as Country Results with the help of preddefined functions
    #assigned variables to the predefined function

    act=cv.get_total_active_cases()
    rec=cv.get_total_recovered()
    death=cv.get_total_deaths()
    con=cv.get_total_confirmed_cases()

    print("1.Global Count")
    print("2.Active Cases")
    print("3.Confirmed Cases")
    print("4.Recovered Cases")
    print("5.Deceased")
    print("6.Get COVID Updates By Country Name")

    choice=input("Enter a Number of Your Choice :")

    #if-elif-else ststements used on the basis of Decision Tree

    if choice == '1':
        print("Active Cases :",act,"\nConfirmed Cases :",con,"\nRecovered Cases :",rec,"\nDeseased :",death)

    elif choice == '2' :
        print("Active Cases :",act)

    elif choice == '3' :
        print("Confirmed Cases :",con)

    elif choice == '4' :
        print("Recovered Cases :",rec)

    elif choice == '5' :
        print("Deceased :",death)

    elif choice == '6' :
        str = i = input("Enter Country Name :")       #Get the status COVID 19 in a perticular country
        cname = cv.get_status_by_country_name(i)
        print(cname)

    else :
        print("Invalid Option")


#End of Program

                                #Thank you#