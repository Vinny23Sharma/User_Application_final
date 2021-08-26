from code.settings import user_table_instance
from validator import PersonalInfoValidator


class UserPersonalInfo:
    @classmethod
    def put_user_personal_info(cls, username, data):
        if not PersonalInfoValidator.field_validator(data):
            return {"message": "Invalid keys",
                    "status": "404"
                    }

        if not PersonalInfoValidator.value_validator(data):
            return {"message": "Invalid values",
                    "status": "404"
                    }

        user = user_table_instance.update_item(
            Key={
                "username": username,
            },
            UpdateExpression="""set 
                 FirstName=:first_name,
                 LastName=:last_name,
                 MotherName=:mother_name,
                 FatherName=:father_name,
                 DateOfBirth=:date_of_birth,
                 Gender=:gender,
                 BloodGroup=:blood_group,
                 MaritalStatus=:marital_status,
                 Occupation=:occupation,
                 Nationality=:nationality""",
            ExpressionAttributeValues={
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
            },
            ReturnValues="UPDATED_NEW"
        )

        return user

    @classmethod
    def get_user_personal_info(cls, username):
        user = user_table_instance.get_item(
            Key={
                "username": username,
            }
        )

        return user
