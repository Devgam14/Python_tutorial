from faker import Faker
fk = Faker('DUE')

fn = fk.first_name()
sn = fk.last_name()
# full_name = fk.full_name()
jb = fk.job()
profile = fk.profile()
print(f"firstname : {fn} lastname : {sn} , job : {jb} \n profile : {profile} " )