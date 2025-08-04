import importlib.util
import pathlib
import sys

# .so ফাইল একই ডিরেক্টরিতে থাকতে হবে
so_path = pathlib.Path(__file__).with_name("BhauTheUltimateTools-312.so")

# এখানে "bhau" হল একটু টেম্পরারি নাম; যদি PyInit_<name> আলাদা হয়, পরে ঠিক করে নিবে
spec = importlib.util.spec_from_file_location("bhau", so_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

print("Imported module:", module)
print("Available attributes/functions:")
for name in sorted(dir(module)):
    if not name.startswith("__"):
        print(" ", name)
