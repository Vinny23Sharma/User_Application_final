import re


class PersonalInfoValidator:
    allowed_fields = ["FirstName",
                      "LastName",
                      "MotherName",
                      "FatherName",
                      "DateOfBirth",
                      "Gender",
                      "BloodGroup",
                      "MaritalStatus",
                      "Occupation",
                      "Nationality"]
    allowed_fields.sort()

    @classmethod
    def validate_name_field_values(cls, value_to_check):
        value = value_to_check.replace(" ", "")
        return value.isalpha()

    # For validating values
    @classmethod
    def value_validator(cls, request_data_values):
        request_data_value_dict = request_data_values

        check = True

        if request_data_value_dict.get('FirstName'):
            if not cls.validate_name_field_values(request_data_value_dict.get('FirstName')):
                check = False
                return check

        if request_data_value_dict.get("LastName"):
            if not cls.validate_name_field_values(request_data_value_dict.get("LastName")):
                check = False
                return check

        if request_data_value_dict.get("MotherName"):
            if not cls.validate_name_field_values(request_data_value_dict.get("MotherName")):
                check = False
                return check

        if request_data_value_dict.get("FatherName"):
            if not cls.validate_name_field_values(request_data_value_dict.get("FatherName")):
                check = False
                return check

        if request_data_value_dict.get("Gender"):
            if not cls.validate_name_field_values(request_data_value_dict.get("Gender")):
                check = False
                return check

        if request_data_value_dict.get("MaritalStatus"):
            if not cls.validate_name_field_values(request_data_value_dict.get("MaritalStatus")):
                check = False
                return check

        if request_data_value_dict.get("Occupation"):
            if not cls.validate_name_field_values(request_data_value_dict.get("Occupation")):
                check = False
                return check

        if request_data_value_dict.get("Nationality"):
            if not cls.validate_name_field_values(request_data_value_dict.get("Nationality")):
                check = False
                return check

        if request_data_value_dict.get("BloodGroup"):
            regex_blood_group = "^(A|B|AB|O)[-+]$"
            if not re.fullmatch(regex_blood_group, request_data_value_dict.get("BloodGroup")):
                check = False
                return check

        if request_data_value_dict.get("DateOfBirth"):
            regex_dob = "^(0[1-9]|1[012])[-/.](0[1-9]|[12][0-9]|3[01])[-/.](19|20)\\d\\d$"
            if not re.fullmatch(regex_dob, request_data_value_dict.get("DateOfBirth")):
                check = False
                return check

        return check

    # For validating keys
    @classmethod
    def field_validator(cls, request_data):

        # validation on length
        if len(request_data) != 10:
            return False

        # validation on keys passed
        key_list = list(request_data.keys())
        key_list.sort()

        if key_list != cls.allowed_fields:
            return False

        return True


