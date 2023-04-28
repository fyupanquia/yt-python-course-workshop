alert_system= 'email' # console|email
error_severity = 'lower' #critical|medium|lower
error_message= 'OMG!'

if alert_system == 'console':
    print(error_message)
elif alert_system == 'email':
    if error_severity == 'critical':
        print('sending message to admin@example.com', error_message)
    elif error_severity == 'medium':
        print('sending message to support.1@example.com', error_message)
    else:
        print('sending message to support.2@example.com', error_message)