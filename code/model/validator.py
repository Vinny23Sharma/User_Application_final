import re


# For validating personal info
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


# For validating educational info
class EducationalInfoValidator:
    allowed_fields = [
        "TenthSchoolName",
        "TenthBoard",
        "TenthPercentage",
        "TenthPassingYear",
        "TwelfthSchoolName",
        "TwelfthBoard",
        "TwelfthPercentage",
        "TwelfthPassingYear",
        "GraduatingUniversityName",
        "GraduationPercentage",
        "GraduationPassOutYear",
        "GraduationSpecialization"
    ]
    allowed_fields.sort()

    @classmethod
    def name_field_values_validator(cls, value_to_check):
        value = value_to_check.replace(" ", "")
        value = value.replace(".", "")
        return value.isalpha()

    @classmethod
    def percentage_validator(cls, value_to_check):
        regex_percentage = "\\d+(?:\\.\\d+)?%"
        return re.fullmatch(regex_percentage, value_to_check)

    @classmethod
    def year_validator(cls, value_to_check):
        regex_year = "^\d{4}$"
        return re.fullmatch(regex_year, value_to_check)

    # For validating values
    @classmethod
    def value_validator(cls, request_data_values):
        check = True

        if request_data_values.get("TenthSchoolName"):
            if not cls.name_field_values_validator("TenthSchoolName"):
                check = False
                return check

        if request_data_values.get("TenthBoard"):
            if not cls.name_field_values_validator("TenthBoard"):
                check = False
                return check
        if request_data_values.get("TwelfthSchoolName"):
            if not cls.name_field_values_validator("TwelfthSchoolName"):
                check = False
                return check

        if request_data_values.get("TwelfthBoard"):
            if not cls.name_field_values_validator("TwelfthBoard"):
                check = False
                return check

        if request_data_values.get("GraduatingUniversityName"):
            if not cls.name_field_values_validator("GraduatingUniversityName"):
                check = False
                return check
        if request_data_values.get("GraduationSpecialization"):
            if not cls.name_field_values_validator("GraduationSpecialization"):
                check = False
                return check
        if request_data_values.get("TenthPassingYear"):
            if not cls.year_validator("TenthPassingYear"):
                check = False
                return check

        if request_data_values.get("TwelfthPassingYear"):
            if not cls.year_validator("TwelfthPassingYear"):
                check = False
                return check
        if request_data_values.get("GraduationPassOutYear"):
            if not cls.year_validator("GraduationPassOutYear"):
                check = False
                return check
        if request_data_values.get("TwelfthPercentage"):
            if not cls.year_validator("TwelfthPercentage"):
                check = False
                return check
        if request_data_values.get("TenthPercentage"):
            if not cls.year_validator("TenthPercentage"):
                check = False
                return check

        if request_data_values.get("GraduationPercentage"):
            if not cls.year_validator("GraduationPercentage"):
                check = False
                return check
        return check

    # For validating keys
    @classmethod
    def field_validator(cls, request_data):
        # validation on length
        if len(request_data) != 12:
            return False

        key_list = list(request_data.keys())
        key_list.sort()

        if key_list != cls.allowed_fields:
            return False

        return True
