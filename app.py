def add(a, b):
 return a + b
def main():
st.title("Addition of 2 given numbers")
st.write("This is a simple adding app")
a = st.number_input("Enter a number")
b = st.number_input("Enter another number")
st.write(add(a, b))
main()
