class UserTemplate:

    @classmethod
    def get_user_instance(cls, username, password):
        user_instance = {
            "username": username,
            "password": password,

            "Mobile_No_1": "NULL",
            "Mobile_No_2": "NULL",
            "Landline": "NULL",
            "Company_email_address": "NULL",
            "Personal_email_address": "NULL",
            "Work_address": "NULL",
            "Emergency_contact_1": "NULL",
            "Emergency_contact_2": "NULL",
            "Current_address": "NULL",
            "Permanent_address": "NULL",

            "FirstName": "NULL",
            "LastName": "NULL",
            "MotherName": "NULL",
            "FatherName": "NULL",
            "DateOfBirth": "NULL",
            "Gender": "NULL",
            "BloodGroup": "NULL",
            "MaritalStatus": "NULL",
            "Occupation": "NULL",
            "Nationality": "NULL",

            "TenthSchoolName": "NULL",
            "TenthBoard": "NULL",
            "TenthPercentage": "NULL",
            "TenthPassingYear": "NULL",
            "TwelfthSchoolName": "NULL",
            "TwelfthBoard": "NULL",
            "TwelfthPercentage": "NULL",
            "TwelfthPassingYear": "NULL",
            "GraduatingUniversityName": "NULL",
            "GraduationPercentage": "NULL",
            "GraduationPassOutYear": "NULL"
        }
        return user_instance


class UserEducationalInfoHelper:
    @classmethod
    def get_key(cls, username):
        return {
            "username": username,
        }

    @classmethod
    def get_update_expression(cls):
        return """set 
                TenthSchoolName=:tenth_school_name,
                TenthBoard=:tenth_board,
                TenthPercentage=:tenth_percentage, 
                TenthPassingYear=:tenth_passing_year,
                TwelfthSchoolName=:twelfth_school_name,
                TwelfthBoard=:twelfth_board,
                TwelfthPercentage=:twelfth_percentage,
                TwelfthPassingYear=:twelfth_passing_year,
                GraduatingUniversityName=:graduating_university_name,
                GraduationPercentage=:graduation_percentage,
                GraduationPassOutYear=:graduation_pass_out_year
            """

    @classmethod
    def get_expression_attribute_values(cls, data):
        return {
            ':tenth_school_name': data.get('TenthSchoolName'),
            ':tenth_board': data.get('TenthBoard'),
            ':tenth_percentage': data.get('TenthPercentage'),
            ':tenth_passing_year': data.get('TenthPassingYear'),
            ':twelfth_school_name': data.get('TwelfthSchoolName'),
            ':twelfth_board': data.get('TwelfthBoard'),
            ':twelfth_percentage': data.get('TwelfthPercentage'),
            ':twelfth_passing_year': data.get('TwelfthPassingYear'),
            ':graduating_university_name': data.get('GraduatingUniversityName'),
            ':graduation_percentage': data.get('GraduationPercentage'),
            ':graduation_pass_out_year': data.get('GraduationPassOutYear')
        }


class UserPersonalInfoHelper:
    @classmethod
    def get_key(cls, username):
        return {
            "username": username,
        }

    @classmethod
    def get_update_expression(cls):
        return """set 
                 FirstName=: first_name,
                 LastName=: last_name,
                 MotherName=: mother_name,
                 FatherName=: father_name,
                 DateOfBirth=: date_of_birth,
                 Gender=: gender,
                 BloodGroup=: blood_group,
                 MaritalStatus=: marital_status,
                 Occupation=: occupation,
                 Nationality=: nationality"""

    @classmethod
    def get_expression_attribute_values(cls, data):
        return {
            ':first_name': data.get('FirstName'),
            ':last_name': data.get('LastName'),
            ':mother_name': data.get('MotherName'),
            ':father_name': data.get('FatherName'),
            ':date_of_birth': data.get('DateOfBirth'),
            ':gender': data.get('Gender'),
            ':blood_group': data.get('BloodGroup'),
            ':marital_status': data.get('MaritalStatus'),
            ':occupation': data.get('Occupation'),
            ':nationality': data.get('Nationality')
        }
