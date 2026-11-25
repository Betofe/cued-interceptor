from health import battery_action, Status


def test_full_battery_is_ok():
    assert battery_action(100) == Status.OK


def test_battery_at_30():
    assert battery_action(30) == Status.OK


def test_battery_at_29():
    assert battery_action(29) == Status.WARN


def test_battery_at_20():
    assert battery_action(20) == Status.WARN


def test_battery_at_19():
    assert battery_action(19) == Status.RETURN_HOME


def test_battery_at_10():
    assert battery_action(10) == Status.RETURN_HOME


def test_battery_at_9():
    assert battery_action(9) == Status.LAND


def test_empty_battery():
    assert battery_action(0) == Status.LAND
