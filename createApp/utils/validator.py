# from django.http import JsonResponse
# import json

# def return_error_response(status_code,err_msg):
#     return {
#             "success":False,
#             "status_code":status_code, # Bad request 
#             "err_msg":err_msg
#             }

# class Validator:

#     def validateId(json_data):
#         if 'id' in json_data and isinstance(json_data["id"], int) and json_data["id"] >0:
#             return json_data["id"]
#         else:
#             return return_error_response(400,"Missing or Invalid id.")

#     def validateEmployeeId(json_data):
#         if 'employeeId' in json_data and isinstance(json_data["employeeId"], str) and json_data["employeeId"] !='':
#             return json_data["employeeId"]
#         else:
#             return return_error_response(400,"Missing or Invalid employeeId.")

#     def validateName(json_data):
#         if 'name' in json_data and isinstance(json_data["name"], str) and json_data["name"] !='':
#             return json_data["name"]
#         else:
#             return return_error_response(400,"Missing or Invalid name.")

#     def validateDOJ(json_data):
#         if 'DOJ' in json_data and isinstance(json_data["DOJ"], str) and json_data["DOJ"] !='' :
#             return json_data["DOJ"]
#         else:
#             return return_error_response(400,"Missing or Invalid DOJ.")

#     def validateTerminationDate(json_data):
#         if 'terminationDate' in json_data and isinstance(json_data["terminationDate"], str) and json_data["terminationDate"] !='':
#             return json_data["terminationDate"]
#         else:
#             return return_error_response(400,"Missing or Invalid terminationDate.")
