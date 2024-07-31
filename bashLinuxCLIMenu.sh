#!/bin/bash

#this is the main function that allows the user to navigate to the different parts of the code
main(){
	#the choice variable contains the menubox and will assign the input that the user provides to choice
	choice=$(dialog --backtitle "MAIN MENU" \
	--title "WELCOME TO THE MAIN MENU" \
	--menu "" 0 0 0 \
	1 "Date/time" \
	2 "Calendar" \
	3 "Delete" \
	4 "System configuration" \
	5 "Exit" --stdout)
	#above is the attributes of the box with the list of options
	#switch case to allow the user to navigate to the different options
	case $choice in 
		#calls the date_time
		1) date_time;;	
		#calls the show_calendar function
		2) show_calendar;;	
		#calls function to delete a file	
		3) delete_file;;		
		#this calls the system configuration menu	
		4) system_config_menu;;			
		#this outputs a info box saying shutting down, and will kill the program in two seconds	
		5) dialog --infobox "Shutting down..." 0 0 ; sleep 2;;				
	esac #closes cases
}


#date_time function
date_time() {
	#this assigns the date to the date_and_time variable
	date_and_time=$(date)
	#this prints the date and time as an infobox, so it will only pop up for 2 seconds
	dialog --infobox "$date_and_time" 5 35 ; sleep 2;
	#this goes back to the main function
	main
}


#show_calendar function
show_calendar() {
	#outputs a calendar that can be interacted with in a dialog box
	dialog --title "Calendar" --calendar "Use TAB to switch to different areas of the box" 0 0
	main	
}


#delete file function
delete_file() {
	#assigns the path that the user inputs to this variable
	path=$(dialog --title "Remove File" --inputbox "What is the path?" 10 50 --stdout)
	#goes to the path that the user has chosen
	cd $path
	#this assigns the users input to this variable
	f=$(dialog --title "Remove File" --inputbox "What file do you want to delete" 10 50 --stdout)
	
	if [ -f $f ] 	#if the file is a file
	then
		prompt=$(dialog --title "Remove File" --inputbox "Are you sure you want to delete file? [y/n]" 10 30 --stdout)
		if [ $prompt == "y" ]; then
			rm $f #removes file
			dialog --title "Remove File" --infobox "$path: $f file deleted." 10 50 ; sleep 2 ;
			#outputs the path of the file and that its been removed5
		elif [ $prompt == "n" ]; then
			main
		fi
	else
		dialog --title "Remove File" --infobox "$f is not a file." 10 50 ; sleep 2 ;
		#outputs that the user input isnt a file
	fi 
	main
}

#results function
display_result() {
  	dialog --title "$1" \	#first arguement is passed as the title
    --no-collapse \
    --msgbox "$result" 0 0	#result is the thing i keep redefining to pass through commands
}
#system config menu
system_config_menu() {
	#this assigns the users choice from the menu box to the variable choice
	choice=$(dialog --backtitle "SYSTEM MENU" \
	--title "WELCOME TO THE SYSTEM CONFIGURATION MENU" \
	--menu "" 0 0 0 \
	1 "Operating System Type" \
	2 "CPU" \
	3 "Memory" \
	4 "Hard Disk" \
	5 "File System" --stdout)
	#above is the attributes of the box with the list of options
}
	
	#switch cases
	case $choice in
	1) 
	platform='unknown'
    unamestr=`uname`	#uname checks the platform type to determine the OS
    if [[ "$unamestr" == 'Linux' ]]; then
   	    platform='linux'
	elif [[ "$unamestr" == 'FreeBSD' ]]; then
        platform='freebsd'
	fi
	result=$(echo "Your platform is $platform")	#the if statement above checks uname which is built in on linux and free bsd
	display_result "Here is your platform"
      ;;
    2)
	result=$(lscpu)		#gets general cpu information can use cat /proc/cpuinfo for more info on each core
	display_result "CPU info"
	;;
	3)
	result=$(cat /proc/meminfo)	#gets memory information from the processes folder
    display_result "Your memory information"
    ;;
    4)
	result=$(lsblk)		#lsblk is a functo=ion that is used in order to obtain hard disc information without using sudo
	display_result "Your hard disk information"
	;;
	5)
	result=$(findmnt)		#gets mounted file system information so that you can see the files in a tree like format
    display_result "Files in a mounted way"
	;;
	esac
	main
}
main
