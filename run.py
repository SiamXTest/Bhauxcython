import BhauTheUltimateTools


print("Available functions/objects in BhauTheUltimateTools:")
print(dir(BhauTheUltimateTools))


if hasattr(BhauTheUltimateTools, "main"):
    BhauTheUltimateTools.main()


elif hasattr(BhauTheUltimateTools, "start"):
    BhauTheUltimateTools.start()
