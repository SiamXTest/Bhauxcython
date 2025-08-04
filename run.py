import BhauTheUltimateTools

# ফাংশন তালিকা দেখা
print("Available functions/objects in BhauTheUltimateTools:")
print(dir(BhauTheUltimateTools))

# যদি main() থাকে
if hasattr(BhauTheUltimateTools, "main"):
    BhauTheUltimateTools.main()

# অথবা যদি start() থাকে
elif hasattr(BhauTheUltimateTools, "start"):
    BhauTheUltimateTools.start()
