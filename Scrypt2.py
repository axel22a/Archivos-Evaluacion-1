vlan = int(input("Cual es la vlan? "))
if vlan >= 1 and vlan <= 1005:
    print("Esta vlan es normal")
elif vlan >=1006 and vlan <= 4095:
    print("Esta vlan es de rango extendido")
else:
    print("Esta vlan no es normal o de rango extendido .")
