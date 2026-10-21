BASE_RATE = 30.00
FAT_STEP_VALUE = 0.40
SNF_STEP_VALUE = 0.30

def rate_per_litre(fat, snf):
    """Calculate the milk rate per litre."""
    if not 2.0 <= fat <= 7.0 or snf < 0:
        raise ValueError("Invalid fat or SNF value")

    fat_steps = round((fat - 3.5) / 0.1)
    snf_steps = round((snf - 8.5) / 0.1)

    rate = BASE_RATE + fat_steps * FAT_STEP_VALUE + snf_steps * SNF_STEP_VALUE
    return round(rate, 2)


def payout(litres, fat, snf):
    """Calculate the farmer's payment."""
    if litres < 0:
        raise ValueError("Litres cannot be negative")

    return round(litres * rate_per_litre(fat, snf), 2)


def test_calculator():
    assert rate_per_litre(3.5, 8.5) == 30.00
    assert rate_per_litre(4.2, 8.7) == 33.40
    assert rate_per_litre(3.1, 8.3) == 27.80
    assert rate_per_litre(2.0, 8.5) == 24.00
    assert rate_per_litre(7.0, 8.5) == 44.00
    assert payout(10, 3.5, 8.5) == 300.00

    try:
        payout(-5, 3.5, 8.5)
        assert False, "Negative litres should be rejected"
    except ValueError:
        pass

    try:
        rate_per_litre(8.0, 8.5)
        assert False, "Invalid fat should be rejected"
    except ValueError:
        pass

    print("All tests passed!")


if __name__ == "__main__":
    test_calculator()