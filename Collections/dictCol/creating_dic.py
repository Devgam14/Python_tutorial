noise_makers : dict = {
    "one" : "Great",
    "two" : "Victor",
    "three" : "Gamaleel",
    "four" : "jewel"
}
users_scores = {
    "paul" : 80,
     "John" : 90,
     "peter" : 45,
     "Matt" : 63 ,
}
student_profile : dict = {
    "stu_name" : "Mary ann ",
    "stu_age" : 23,
    "stu_gender" : "Female",
    "stu_subjects" : ["Maths", "English", "Biology"],
     "stu_id" : "abcd123"
}
### note dictionaries can have dictionaries in them  they can have other types in the as a value pairs must be immutable and unique else they would be removed
print(student_profile)
print(noise_makers)
print(users_scores)

## dict() constructor
gam = "hwl"
user = dict(one = "paul" , two = "john", three= "ann", four = gam)
print(user)
print(user["one"])
