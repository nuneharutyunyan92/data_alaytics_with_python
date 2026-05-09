def age_group_label(age):
    if age >= 60:
        return "Senior"
    elif age >= 30 and age <= 59:
        return "Middle"
    else:
        "Young"


def income_band (income):
    if income > 72000:
        return "High income"
    elif income >= 42000 and income <= 72000:
        return "Middle income"
    else:
        "Low income"