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
        value = value.replace(",", "")
        return value.isalpha()

    @classmethod
    def percentage_validator(cls, value_to_check):
        regex_percentage = "\\d+(?:\\.\\d+)?%"
        return re.fullmatch(regex_percentage, value_to_check)

    @classmethod
    def year_validator(cls, value_to_check):
        return value_to_check.isdigit() and (len(value_to_check) == 4)

    # For validating values
    @classmethod
    def value_validator(cls, request_data_values):
        check = True

        if request_data_values.get("TenthSchoolName"):
            if not cls.name_field_values_validator(request_data_values.get("TenthSchoolName")):
                check = False
                return check

        if request_data_values.get("TenthBoard"):
            if not cls.name_field_values_validator(request_data_values.get("TenthBoard")):
                check = False
                return check
        if request_data_values.get("TwelfthSchoolName"):
            if not cls.name_field_values_validator(request_data_values.get("TwelfthSchoolName")):
                check = False
                return check

        if request_data_values.get("TwelfthBoard"):
            if not cls.name_field_values_validator(request_data_values.get("TwelfthBoard")):
                check = False
                return check

        if request_data_values.get("GraduatingUniversityName"):
            if not cls.name_field_values_validator(request_data_values.get("GraduatingUniversityName")):
                check = False
                return check
        if request_data_values.get("GraduationSpecialization"):
            if not cls.name_field_values_validator(request_data_values.get("GraduationSpecialization")):
                check = False
                return check
        if request_data_values.get("TenthPassingYear"):
            if not cls.year_validator(request_data_values.get("TenthPassingYear")):
                check = False
                return check

        if request_data_values.get("TwelfthPassingYear"):
            if not cls.year_validator(request_data_values.get("TwelfthPassingYear")):
                check = False
                return check
        if request_data_values.get("GraduationPassOutYear"):
            if not cls.year_validator(request_data_values.get("GraduationPassOutYear")):
                check = False
                return check
        if request_data_values.get("TwelfthPercentage"):
            if not cls.percentage_validator(request_data_values.get("TwelfthPercentage")):
                check = False
                return check
        if request_data_values.get("TenthPercentage"):
            if not cls.percentage_validator(request_data_values.get("TenthPercentage")):
                check = False
                return check

        if request_data_values.get("GraduationPercentage"):
            if not cls.percentage_validator(request_data_values.get("GraduationPercentage")):
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


# For validating contact info
class ContactInfoValidator:
    allowed_fields = [
        "Mobile_No_1",
        "Mobile_No_2",
        "Landline",
        "Company_email_address",
        "Personal_email_address",
        "Work_address",
        "Emergency_contact_1",
        "Emergency_contact_2",
        "Current_address",
        "Permanent_address"
    ]
    allowed_fields.sort()

    @classmethod
    def check_email(cls, email):
        regex_for_email = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        return re.fullmatch(regex_for_email, email)

    @classmethod
    def value_validator(cls, data):
        check = True
        if data.get('Mobile_No_1'):
            if not data.get('Mobile_No_1').isdigit():
                check = False
                print("1")
                return check

        if data.get('Mobile_No_2'):
            if not data.get('Mobile_No_2').isdigit():
                check = False
                return check

        if data.get('Landline'):
            if not data.get('Landline').isdigit():
                check = False
                return check

        if data.get('Emergency_contact_1'):
            if not data.get('Emergency_contact_1').isdigit():
                check = False
                return check

        if data.get('Emergency_contact_2'):
            if not data.get('Emergency_contact_2').isdigit():
                check = False
                return check

        if data.get("Personal_email_address"):
            if not cls.check_email(data.get("Personal_email_address")):
                check = False
                return check

        if data.get('Company_email_address'):
            if not cls.check_email(data.get("Company_email_address")):
                check = False
                return check

        return check

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
