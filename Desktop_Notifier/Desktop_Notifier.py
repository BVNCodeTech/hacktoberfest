def Desktop_Notifier():
	from win10toast import ToastNotifier
	import time
	Notifying = True
	while Notifying == True:
		Toaster = ToastNotifier()
		title = "Take a brake"
		message = "It has been whole 20 minutes since you have been straying at the screen continuously take a 20 seconds brake by look at something away from the computer"
		icon_path = "Desktop_Notifier/clock.ico"
		Toaster.show_toast(title, message, icon_path)
		time.sleep(60*20)


Desktop_Notifier()
