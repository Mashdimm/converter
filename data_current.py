from dadata import Dadata
token = "1d52231e2fba75be30c1f448aef1b4d240437b09"
dadata = Dadata(token)
result = dadata.suggest("currency", "руб")

print(result)
