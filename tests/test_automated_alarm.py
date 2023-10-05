import alarm


def test_automatedAlarmForWednesdayOff():
    # Capture the results of the function
    result = alarm.set_alarm("Wednesday", True)
    # Check for expected output
    assert result == '8:30'


def test_automatedAlarmForMondayOff():
    # Capture the results of the function
    result = alarm.set_alarm("Monday", True)
    # Check for expected output
    assert result == '9:30'


def test_automatedAlarmForMondaySchool():
    # Capture the results of the function
    result = alarm.set_alarm("Monday", False)
    # Check for expected output
    assert result == '7:00'


def test_automatedAlarmForWednesdaySchool():
    # Capture the results of the function
    result = alarm.set_alarm("Wednesday", False)
    # Check for expected output
    assert result == '7:30'


def test_automatedAlarmForSaturdayOff():
    # Capture the results of the function
    result = alarm.set_alarm("Saturday", True)
    # Check for expected output
    assert result == '9:00'


def test_automatedAlarmForSaturdaySchool():
    # Capture the results of the function
    result = alarm.set_alarm("Saturday", False)
    # Check for expected output
    assert result == '9:00'


def test_automatedAlarmForFridaySchool():
    # Capture the results of the function
    result = alarm.set_alarm("Friday", False)
    # Check for expected output
    assert result == '7:00'


def test_automatedAlarmForThursdaySchool():
    # Capture the results of the function
    result = alarm.set_alarm("Thursday", False)
    # Check for expected output
    assert result == '7:00'


def test_automatedAlarmForThursdayOff():
    # Capture the results of the function
    result = alarm.set_alarm("Thursday", True)
    # Check for expected output
    assert result == '8:30'
