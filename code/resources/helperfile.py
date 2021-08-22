from flask_restful import reqparse


class UserEducationalInfoRequestParser:
    @classmethod
    def get_user_educational_info_request_parser(cls):
        parser = reqparse.RequestParser()
        parser.add_argument('TenthSchoolName',
                            type=str,
                            required=True,
                            help="This field cannot be left blank!"
                            )
        parser.add_argument('TenthBoard',
                            type=str,
                            required=True,
                            help="This field cannot be left blank"
                            )
        parser.add_argument('TenthPercentage',
                            type=str,
                            required=True,
                            help="This field cannot be left blank!"
                            )
        parser.add_argument('TenthPassingYear',
                            type=str,
                            required=True,
                            help="This field cannot be left blank"
                            )
        parser.add_argument('TwelfthSchoolName',
                            type=str,
                            required=True,
                            help="This field cannot be left blank!"
                            )
        parser.add_argument('TwelfthBoard',
                            type=str,
                            required=True,
                            help="This field cannot be left blank"
                            )
        parser.add_argument('TwelfthPercentage',
                            type=str,
                            required=True,
                            help="This field cannot be left blank!"
                            )
        parser.add_argument('TwelfthPassingYear',
                            type=str,
                            required=True,
                            help="This field cannot be left blank"
                            )
        parser.add_argument('GraduatingUniversityName',
                            type=str,
                            required=True,
                            help="This field cannot be left blank!"
                            )
        parser.add_argument('GraduationPercentage',
                            type=str,
                            required=True,
                            help="This field cannot be left blank"
                            )
        parser.add_argument('GraduationPassOutYear',
                            type=str,
                            required=True,
                            help="This field cannot be left blank"
                            )
        return parser

    @classmethod
    def get_user_educational_info_response(cls, data):
        return {
                   'TenthSchoolName': data.get('TenthSchoolName'),
                   'TenthBoard': data.get('TenthBoard'),
                   'TenthPercentage': data.get('TenthPercentage'),
                   'TenthPassingYear': data.get('TenthPassingYear'),
                   'TwelfthSchoolName': data.get('TwelfthSchoolName'),
                   'TwelfthBoard': data.get('TwelfthBoard'),
                   'TwelfthPercentage': data.get('TwelfthPercentage'),
                   'TwelfthPassingYear': data.get('TwelfthPassingYear'),
                   'GraduatingUniversityName': data.get('GraduatingUniversityName'),
                   'GraduationPercentage': data.get('GraduationPercentage'),
                   'GraduationPassOutYear': data.get('GraduationPassOutYear')

               }, 200


class UserPersonalInfoRequestParser:
    @classmethod
    def get_user_personal_info_request_parser(cls):
        parser = reqparse.RequestParser()
        parser.add_argument('FirstName',
                            type=str,
                            required=True,
                            help="This field cannot be left blank!"
                            )
        parser.add_argument('LastName',
                            type=str,
                            required=True,
                            help="This field cannot be left blank"
                            )
        parser.add_argument('MotherName',
                            type=str,
                            required=True,
                            help="This field cannot be left blank!"
                            )
        parser.add_argument('FatherName',
                            type=str,
                            required=True,
                            help="This field cannot be left blank"
                            )
        parser.add_argument('DateOfBirth',
                            type=str,
                            required=True,
                            help="This field cannot be left blank!"
                            )
        parser.add_argument('Gender',
                            type=str,
                            required=True,
                            help="This field cannot be left blank"
                            )
        parser.add_argument('BloodGroup',
                            type=str,
                            required=True,
                            help="This field cannot be left blank!"
                            )
        parser.add_argument('MaritalStatus',
                            type=str,
                            required=True,
                            help="This field cannot be left blank"
                            )
        parser.add_argument('Occupation',
                            type=str,
                            required=True,
                            help="This field cannot be left blank!"
                            )
        parser.add_argument('Nationality',
                            type=str,
                            required=True,
                            help="This field cannot be left blank"
                            )

        return parser

    @classmethod
    def get_user_personal_info_response(cls, data):
        return {
                   'FirstName': data.get('FirstName'),
                   'LastName': data.get('LastName'),
                   'MotherName': data.get('MotherName'),
                   'FatherName': data.get('FatherName'),
                   'DateOfBirth': data.get('DateOfBirth'),
                   'Gender': data.get('Gender'),
                   'BloodGroup': data.get('BloodGroup'),
                   'MaritalStatus': data.get('MaritalStatus'),
                   'Occupation': data.get('Occupation'),
                   'Nationality': data.get('Nationality')
               }, 200
