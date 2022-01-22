alert_failure_count = 0

#Let the threshold be 200 degree celcius

def network_alert_stub(celcius):
    print(f'ALERT: Temperature is {celcius} celcius')
    # Return 200 for ok
    if celcius <= 200 :
      return 200
    # Return 500 for not-ok
    elif celcius > 200 :
      return 500

def alert_in_celcius(farenheit):
    celcius = (farenheit - 32) * 5 / 9
    returnCode = network_alert_stub(celcius)
    if returnCode != 200:
        # non-ok response is not an error! Issues happen in life!
        # let us keep a count of failures to report
        # However, this code doesn't count failures!
        # Added a test below to catch this bug. Altered the stub aboveas it was needed.
        global alert_failure_count
        alert_failure_count += 0
        assert(alert_failure_count != 0)


alert_in_celcius(400.5)
alert_in_celcius(303.6)
print(f'{alert_failure_count} alerts failed.')
print('All is well (maybe!)')
