from code.settings import user_table_instance


class UserEducationalInfo:

    @classmethod
    def put_user_educational_info(cls, username, data):
        user = user_table_instance.update_item(
            Key={
                "username": username,
            },
            UpdateExpression="""set 
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
                GraduationPassOutYear=:graduation_pass_out_year,
                GraduationSpecialization=:graduation_specialization
            """,
            ExpressionAttributeValues={
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
                ':graduation_pass_out_year': data.get('GraduationPassOutYear'),
                ':graduation_specialization': data.get('GraduationSpecialization')

            },
            ReturnValues="UPDATED_NEW"
        )
        return user

    @classmethod
    def get_user_educational_info(cls, username):
        user = user_table_instance.get_item(
            Key={
                'username': username,
            }
        )

        return user
