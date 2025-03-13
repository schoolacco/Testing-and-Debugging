# Testing and Debugging

---

Compare boundary testing, path coverage testing and faulty and abnormal data testing.

---

Boundary testing is where you test the exact boundaries of what should and shouldn't be allowed, for instance if you wanted to allow a maximum value of 4 you would test the numbers: 3, 4, and 5. Path testing instead is testing every intended path the program can take to see if everything is working as intended, rather than testing the very boundaries of what is allowed you instead test for each intended path to ensure there are no errors in each segment. Faulty/Abnormal data testing differs from both as instead of testing anything intended it tests what isn't expected, Faulty/Abnormal data testing tests cases which aren't intended (such as entering a string into a mathematical operation) to see what happens for the unintended exception that may occur.

---

Compare unit testing, integration testing and system testing.

---

Unit testing the most basic test, testing an individual function to see if it functions as intended. This is done via using:

~~~python
def cool_function(num, num2):
  return "intended result"
def test_function():
  assert cool_function(1, 2) == "intended result", "test failed, didn't recieve intended result"
~~~

this tests if the function using certain numbers returns the intended result, integration testing is an extension of this, instead testing how the module interacts with other components of the code and checking if those work as intended, and finally system testing is an extension of integration testing seeing how the module interacts with the final system code and seeing if everything once more works as intended.
