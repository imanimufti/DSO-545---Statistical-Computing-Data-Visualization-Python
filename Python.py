## % cell
hours= float(input('How many hours have you fasted:'))
if hours < 2:
    print('You need to fast at least 2 hours to perform this test')

bloodsugar = float(input('What is your blood sugar level:'))

if 2<=hours<8 and bloodsugar > 140:
    print('Your blood sugar level is high')
elif 2<=hours<8 and bloodsugar < 140:
    print('Your blood sugar level is normal')
elif hours >=8 and bloodsugar > 100:
    print('Your blood sugar level is high')
elif hours >=8 and bloodsugar < 100:
    print('Your blood sugar level is normal')

# %%
hours= float(input('How many hours have you fasted:'))
if hours < 2:
    print('You need to fast at least 2 hours to perform this test')

bloodsugar = float(input('What is your blood sugar level:'))

if 2<=hours<8 and bloodsugar > 140:
    print('Your blood sugar level is high')
elif 2<=hours<8 and bloodsugar < 140:
    print('Your blood sugar level is normal')
elif hours >=8 and bloodsugar > 100:
    print('Your blood sugar level is high')
elif hours >=8 and bloodsugar < 100:
    print('Your blood sugar level is normal')


# %%
