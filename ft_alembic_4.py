import alchemy

print("=== Alembic 4 ===")
print("Accessing the alchemy module using 'import alchemy'")
print(f"Testing create_air: {alchemy.create_air()}")
print("Now show that not all functions can be reach")
print("This will raise an exception!")

# Esto es un error esperado
print(alchemy.create_earth())
