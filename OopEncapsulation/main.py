from Bus import Bus

MicroBus = Bus("Micro Bus",4)
MicroBus.set__sit(8)
MiniBus = Bus("Mini Bus", 6)
MiniBus.set__sit(36)
MegaBus = Bus("Mega Bus", 10)
MegaBus.set__sit(52)

print(f"\n{MicroBus}\n")
print(f"{MiniBus}\n")
print(f"{MegaBus}\n")