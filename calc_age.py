def calc_age(age):
    your_age = int(input('How old are you: '))
    if your_age > 1: 
      your_days = your_age *365
      your_days = str(your_days)
      print('You have '+ your_days + ' days')
      
    else:
        print('Tell me your real age: ')
	 

if __name__ == '__main__':
   calc_age('age')	