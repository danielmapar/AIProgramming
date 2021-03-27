# AI Programming with Python Nanodegree Program

## Introduction to Python

### Lesson 2: Data Types and Operators

* `**`: Exponentiation
    * `3 ** 2`: 3 to the power of 2
* `//`: Integer division
    * `7 // 2 == 3`: It rounds down the answer to an integer
        * `-5 // 2 == -3` and `5 // 2 == 2` 

* ![reserved](./images/reserved.png)

* Note that this code uses scientific notation to define large numbers. `4.445e8` is equal to `4.445 * 10 ** 8` which is equal to `444500000.0`.

#### Integers and Floats

* Because the float, or approximation, for 0.1 is actually slightly more than 0.1, when we add several of them together we can see the difference between the mathematically correct answer and the one that Python creates.

    * ```python
        >>> print(.1 + .1 + .1 == .3)
        False
        ```

### Lesson 3: Data Structures

#### Slicing a list

* You saw that we can pull more than one value from a list at a time by using slicing. When using slicing, it is important to remember that the `lower` index is `inclusive` and the `upper` index is `exclusive`.

* ```python
    >>> list_of_random_things = [1, 3.4, 'a string', True]
    >>> list_of_random_things[1:2]
    [3.4]
    ```

* will only return 3.4 in a list. Notice this is still different than just indexing a single element, because you get a list back with this indexing. The colon tells us to go from the starting value on the left of the colon up to, but not including, the element on the right.

* If you know that you want to start at the beginning, of the list you can also leave out this value.
    * ```python
        >>> list_of_random_things[:2]
        [1, 3.4]
        ```

* or to return all of the elements to the end of the list, we can leave off a final element.
    * ```python
        >>> list_of_random_things[1:]
        [3.4, 'a string', True]
        ```

#### Mutability and Order

* Mutability is about whether or not we can change an object once it has been created. If an object (like a list or string) can be changed (like a list can), then it is called mutable. However, if an object cannot be changed with creating a completely new object (like strings), then the object is considered immutable.

    * List is mutable and ordered
    * Tuple is immutable and ordered
        * ```(1,2,3,4)```
    * Set is mutable and has no duplicates
    * Dictionary for mutable objects that store mapping of unique keys to values.

* The == operator compares by checking for equality: If these cats were Python objects and we’d compare them with the == operator, we’d get “both cats are equal” as an answer.

* The is operator, however, compares identities: If we compared our cats with the is operator, we’d get “these are two different cats” as an answer.

### Lesson 4: Control Flow

* Zip: 
    * ![zip](./images/zip.png)
    * ```python
        letters = ['a', 'b', 'c']
        nums = [1, 2, 3]

        for letter, num in zip(letters, nums):
            print("{}: {}".format(letter, num))
        ```
    * In addition to zipping two lists together, you can also unzip a list into tuples using an asterisk.
        * ```python
            some_list = [('a', 1), ('b', 2), ('c', 3)]
            letters, nums = zip(*some_list)
            ```
        * ```python
            x_coord = [23, 53, 2, -12, 95, 103, 14, -5]
            y_coord = [677, 233, 405, 433, 905, 376, 432, 445]
            z_coord = [4, 16, -6, -42, 3, -6, 23, -1]
            labels = ["F", "J", "A", "Q", "Y", "B", "W", "X"]

            points = []
            for point in zip(labels, x_coord, y_coord, z_coord):
                points.append("{}: {}, {}, {}".format(*point))

            for point in points:
                print(point)
            ```

* Enumerate
    * ![enumerate](./images/enumerate.png)
    * enumerate is a built in function that returns an iterator of tuples containing indices and values of a list. You'll often use this when you want the index along with each element of an iterable in a loop.
        * ```python
            letters = ['a', 'b', 'c', 'd', 'e']
            for i, letter in enumerate(letters):
                print(i, letter)
            ```

* List Comprehensions
    * ![list-comprehensions](./images/list_comprehensions.png) 
    * ```python
        squares = [x**2 for x in range(9) if x % 2 == 0]
        squares = [x**2 for x in range(9) if x % 2 == 0 else x + 3]
        squares = [x**2 if x % 2 == 0 else x + 3 for x in range(9)]

        names = ["Rick Sanchez", "Morty Smith", "Summer Smith", "Jerry Smith", "Beth Smith"]

        first_names = [name.split(" ")[0].lower() for name in names]# write your list comprehension here
        print(first_names)
        ```

### Lesson 5: Functions

* Lambda Expressions

    * You can use lambda expressions to create anonymous functions. That is, functions that don’t have a name. They are helpful for creating quick functions that aren’t needed later in your code. This can be especially useful for higher order functions, or functions that take in other functions as arguments.

    * ![lambda](./images/lambda.png) 
    * `double = lambda x: x * 2`

* Iterator: An object that represents a stream of data
    * The `yield` key-works is what differentiate a normal object from an iterator object
* Generator: A function that creates an iterator
    * Generators are a lazy way to build iterables. They are useful when the fully realized list would not fit in memory, or when the cost to calculate each list element is high and you want to do it as late as possible. But they can only be iterated over once.

```python
def my_enumerate(iterable, start=0):
    count = start
    for element in iterable:
        yield count, element
        count += 1

for i, lesson in my_enumerate(lessons, 1):
    print("Lesson {}: {}".format(i, lesson))

def chunker(iterable, size):
    """Yield successive chunks from iterable of length size."""
    for i in range(0, len(iterable), size):
        yield iterable[i:i + size]

for chunk in chunker(range(25), 4):
    print(list(chunk))

sq_list = [x**2 for x in range(10)]  # this produces a list of squares

sq_iterator = (x**2 for x in range(10))  # this produces an iterator of squares
```

### Lesson 6: Scripting

* ```python
    names = input("Enter names separated by commas: ").title().split(",")
    assignments = input("Enter assignment counts separated by commas: ").split(",")
    grades = input("Enter grades separated by commas: ").split(",")

    message = "Hi {},\n\nThis is a reminder that you have {} assignments left to \
    submit before you can graduate. You're current grade is {} and can increase \
    to {} if you submit all assignments before the due date.\n\n"

    for name, assignment, grade in zip(names, assignments, grades):
        print(message.format(name, assignment, grade, int(grade) + int(assignment)*2))
    ```

* ```python
    import useful_functions
    useful_functions.add_five([1, 2, 3, 4])

    import useful_functions as uf
    uf.add_five([1, 2, 3, 4])
    ```

* Using a main block

    * To avoid running executable statements in a script when it's imported as a module in another script, include these lines in an if __name__ == "__main__" block. Or alternatively, include them in a function called main() and call this in the if main block.

    * Whenever we run a script like this, Python actually sets a special built-in variable called __name__ for any module. When we run a script, Python recognizes this module as the main program, and sets the __name__ variable for this module to the string "__main__". For any modules that are imported in this script, this built-in __name__ variable is just set to the name of that module. Therefore, the condition if __name__ == "__main__"is just checking whether this module is the main program.

    * Try running `demo.py`

* Techniques for Importing Modules

    * There are other variants of import statements that are useful in different situations.

        * `from module_name import object_name`

        * `from module_name import first_object, second_object`

        * `import module_name as new_name`

        * `from module_name import object_name as new_name`

        * `from module_name import *`
            * **Do not do this**

* Exceptions
    * ```python
        try:
            # some code
        except ZeroDivisionError as e:
        # some code
        print("ZeroDivisionError occurred: {}".format(e))
        ```

### Lesson 7: Intro to Object-Oriented Programming

* ```python
    class Shirt:

    def __init__(self, shirt_color, shirt_size, shirt_style, shirt_price):
        self._price = shirt_price

    def get_price(self):
      return self._price

    def set_price(self, new_price):
      self._price = new_price


    shirt_one = Shirt('yellow', 'M', 'long-sleeve', 15)
    print(shirt_one.get_price())
    shirt_one.set_price(10)
    ```

*  A docstring is a type of comment that describes how a Python module, function, class or method works. Docstrings, therefore, are not unique to object-oriented programming. This section of the course is merely reminding you to use docstrings and to comment your code. It's not just going to help you understand and maintain your code. It will also make you a better job candidate.

* ```python
    class Pants:
    """The Pants class represents an article of clothing sold in a store
    """

    def __init__(self, color, waist_size, length, price):
        """Method for initializing a Pants object

        Args: 
            color (str)
            waist_size (int)
            length (int)
            price (float)

        Attributes:
            color (str): color of a pants object
            waist_size (str): waist size of a pants object
            length (str): length of a pants object
            price (float): price of a pants object
        """

        self.color = color
        self.waist_size = waist_size
        self.length = length
        self.price = price

    def change_price(self, new_price):
        """The change_price method changes the price attribute of a pants object

        Args: 
            new_price (float): the new price of the pants object

        Returns: None

        """
        self.price = new_price

    def discount(self, percentage):
        """The discount method outputs a discounted price of a pants object

        Args:
            percentage (float): a decimal representing the amount to discount

        Returns:
            float: the discounted price
        """
        return self.price * (1 - percentage)
    ```

* Magic methods 
    * `__init__` is one
    * `__add__` and `__repr__` are also examples
    * Those methods let you override and customize default Python behavior
        * `__add__` overrides the behavior of the plus sign
        * `__repr__` when the only code in a line is a variable

### Extra material

* **First-Class Objects**
In Python, functions are first-class objects. This means that functions can be passed around and used as arguments, just like any other object (string, int, float, list, and so on). Consider the following three functions:

* ```python
    def say_hello(name):
        return f"Hello {name}"

    def be_awesome(name):
        return f"Yo {name}, together we are the awesomest!"

    def greet_bob(greeter_func):
        return greeter_func("Bob")
    ```

* **Inner Functions** It’s possible to define functions inside other functions. Such functions are called inner functions. Here’s an example of a function with two inner functions:

* ```python
    def parent():
        print("Printing from the parent() function")

        def first_child():
            print("Printing from the first_child() function")

        def second_child():
            print("Printing from the second_child() function")

        second_child()
        first_child()
    ```

    * Furthermore, the inner functions are not defined until the parent function is called. They are locally scoped to parent(): they only exist inside the parent() function as local variables. Try calling first_child(). You should get an error

* **Simple Decorators** Now that you’ve seen that functions are just like any other object in Python, you’re ready to move on and see the magical beast that is the Python decorator. Let’s start with an example:

* ```python
    def my_decorator(func):
        def wrapper():
            print("Something is happening before the function is called.")
            func()
            print("Something is happening after the function is called.")
        return wrapper

    def say_whee():
        print("Whee!")

    say_whee = my_decorator(say_whee)
    ```

* ```python
    >>> say_whee()
    Something is happening before the function is called.
    Whee!
    Something is happening after the function is called.
    ```
* Put simply: decorators wrap a function, modifying its behavior.

 * Syntactic Sugar!
    * The way you decorated say_whee() above is a little clunky. First of all, you end up typing the name say_whee three times. In addition, the decoration gets a bit hidden away below the definition of the function.
    * Instead, Python allows you to use decorators in a simpler way with the @ symbol, sometimes called the “pie” syntax. The following example does the exact same thing as the first decorator example:

* ```python
    def my_decorator(func):
        def wrapper():
            print("Something is happening before the function is called.")
            func()
            print("Something is happening after the function is called.")
        return wrapper

    @my_decorator
    def say_whee():
        print("Whee!")
    ```

    * Recall that a decorator is just a regular Python function. All the usual tools for easy reusability are available. Let’s move the decorator to its own module that can be used in many other functions.

* **Decorating Functions With Arguments** 

    * ```python
            from decorators import do_twice

            @do_twice
            def greet(name):
                print(f"Hello {name}")
        ```

    * ```python
        def do_twice(func):
        def wrapper_do_twice(*args, **kwargs):
            print(args)
            print(kwargs)
            func(*args, **kwargs)
            func(*args, **kwargs)
        return wrapper_do_twice
        ```

    * There are 2 kinds of arguments in Python, one is positional arguments and other is keyword arguments, the former are specified according to their position and latter are the arguments with keyword which is the name of the argument.   

    * Before looking at the variadic positional/keyword arguments, we’ll talk about the positional arguments and keyword arguments simply.

    * ```python
        # A function that shows the results of running competitions consisting of 2 to 4 runners.
        def save_ranking(first, second, third=None, fourth=None):
            rank = {}
            rank[1], rank[2] = first, second
            rank[3] = third if third is not None else 'Nobody'
            rank[4] = fourth if fourth is not None else 'Nobody'
            print(rank)    

        # Pass the 2 positional arguments
        save_ranking('ming', 'alice')
        # Pass the 2 positional arguments and 1 keyword argument
        save_ranking('alice', 'ming', third='mike')
        # Pass the 2 positional arguments and 2 keyword arguments (But, one of them was passed as like positional argument)
        save_ranking('alice', 'ming', 'mike', fourth='jim')

        ```
    
    * Above function has 2 positional arguments: first, second and 2 keyword arguments: third, fourth. For positional arguments, it is not possible to omit it, and you must pass all positional arguments to the correct location for each number of arguments declared. However, for keyword arguments, you can set a default value of it when declaring a function, and if you omit the argument, the corresponding default value is entered as the value of the argument. That is, the keyword arguments can be omitted.

    * ```python
        def save_ranking(*args, **kwargs):
            print(args)     
            print(kwargs)
        save_ranking('ming', 'alice', 'tom', fourth='wilson', fifth='roy')     # ('ming', 'alice', 'tom')
        # {'fourth': 'wilson', 'fifth': 'roy'}
        ```
    
    * As you can see above, we are passing the arguments which can hold arbitrary numbers of positional or keyword values. The arguments passed as positional are stored in a list called args, and the arguments passed as keyword are stored in a dict called kwargs.

    * ```python
        from functools import reduce

        primes = [2, 3, 5, 7, 11, 13]

        def product(*numbers):
            p = reduce(lambda x, y: x * y, numbers)
            return p 

        product(*primes)
        # 30030

        product(primes)
        # [2, 3, 5, 7, 11, 13]
        ```

    * **For tuple, it could be done exactly same to list, and for dict, just use ** instead of *.**


## Numpy, Pandas, Matplotlib

### Anaconda

* Install Anaconda
    * `conda upgrade conda`
    * `conda upgrade --all`

* Anaconda is an open source distribution for Python designed for large-scale data. With Anaconda you will be able to simplify package management.

* Welcome to this lesson on using Anaconda to manage packages and environments for use with Python. With Anaconda, it's simple to install the packages you'll often use in data science work. You'll also use it to create virtual environments that make working on multiple projects much less mind-twisting. Anaconda has simplified my workflow and solved a lot of issues I had dealing with packages and multiple Python versions.

* Anaconda is actually a distribution of software that comes with conda, Python, and over 150 scientific packages and their dependencies. The application conda is a package and environment manager. Anaconda is a fairly large download (~500 MB) because it comes with the most common data science packages in Python. If you don't need all the packages or need to conserve bandwidth or storage space, there is also Miniconda, a smaller distribution that includes only conda and Python. Miniconda can do everything Anaconda does, but doesn't have the preinstalled packages. You can still install any of the available packages with conda, it just doesn't come with them, so either Anaconda or Miniconda are fine for this course.

* Package managers are used to install libraries and other software on your computer. You’re probably already familiar with `pip`, it’s the default package manager for Python libraries. Conda is similar to pip except that the available packages are focused around data science while pip is for general use. However, conda is not Python specific like pip is, it can also install non-Python packages. It is a package manager for any software stack. That being said, not all Python libraries are available from the Anaconda distribution and conda. You can (and will) still use pip alongside conda to install packages.

* You can install multiple packages at the same time. Something like `conda install numpy scipy pandas` will install all those packages simultaneously. It's also possible to specify which version of a package you want by adding the version number such as `conda install numpy=1.10`.

* Most of the commands are pretty intuitive. To uninstall, use `conda remove package_name`. To update a package `conda update package_name`. If you want to update all packages in an environment, which is often useful, use `conda update --all`. And finally, to list installed packages, it's conda list which you've seen before.

### Managing Anaconda Environments 

* As I mentioned before, conda can be used to create environments to isolate your projects. To create an environment, use `conda create -n env_name list of packages` in your terminal. Here -n env_name sets the name of your environment (-n for name) and list of packages is the list of packages you want installed in the environment. For example, to create an environment named my_env and install numpy in it, type `conda create -n my_env numpy`.

* When creating an environment, you can specify which version of Python to install in the environment. This is useful when you're working with code in both Python 2.x and Python 3.x. To create an environment with a specific Python version, do something like `conda create -n py3 python=3` or `conda create -n py2 python=2`. I actually have both of these environments on my personal computer. I use them as general environments not tied to any specific project, but rather for general work with each Python version easily accessible. These commands will install the most recent version of Python 3 and 2, respectively. To install a specific version, use `conda create -n py python=3.3` for Python 3.3.

* `conda activate my_env` to enter it.

    * When you're in the environment, you'll see the environment name in the terminal prompt. Something like `(my_env) ~ $`. The environment has only a few packages installed by default, plus the ones you installed when creating it. You can check this out with `conda list`. Installing packages in the environment is the same as before: `conda install package_name`. Only this time, the specific packages you install will only be available when you're in the environment. To leave the environment, type `source deactivate` (on OSX/Linux). On Windows, use `deactivate`.

### Saving Environments 

* A really useful feature is sharing environments so others can install all the packages used in your code, with the correct versions. You can save the packages to a YAML file with `conda env export > environment.yaml`. The first part `conda env` export writes out all the packages in the environment, including the Python version.

* To create an environment from an environment file use `conda env create -f environment.yaml`. This will create a new environment with the same name listed in environment.yaml.

* **Listing environments**

    * If you forget what your environments are named (happens to me sometimes), use `conda env list` to list out all the environments you've created. You should see a list of environments, there will be an asterisk next to the environment you're currently in. The default environment, the environment used when you aren't in one, is called root.

* **Removing environments**

    * If there are environments you don't use anymore, `conda env remove -n env_name` will remove the specified environment (here, named env_name).

## Best practices - Environments 

* One thing that’s helped me tremendously is having separate environments for Python 2 and Python 3. I used `conda create -n py2 python=2` and `conda create -n py3 python=3` to create two separate environments, py2 and py3. Now I have a general use environment for each Python version. In each of those environments, I've installed most of the standard data science packages (numpy, scipy, pandas, etc.). Remember that when you set up an environment initially, you'll only start with the standard packages and whatever packages you specify in your conda create statement.

* I’ve also found it useful to create environments for each project I’m working on. It works great for non-data related projects too like web apps with Flask. For example, I have an environment for my personal blog using Pelican.

* **Sharing Environments**

    * When sharing your code on GitHub, it's good practice to make an environment file and include it in the repository. This will make it easier for people to install all the dependencies for your code. I also usually include a pip `requirements.txt` file using `pip freeze` (learn more here) for people not using conda.

### Jupyter notebooks

* Welcome to this lesson on using Jupyter notebooks. The notebook is a web application that allows you to combine explanatory text, math equations, code, and visualizations all in one easily sharable document.

* Notebooks have quickly become an essential tool when working with data. You'll find them being used for data cleaning and exploration, visualization, machine learning, and big data analysis.

* Notebooks are a form of literate programming proposed by Donald Knuth in 1984. With literate programming, the documentation is written as a narrative alongside the code instead of sitting off by its own. In Donald Knuth's words:
    * Instead of imagining that our main task is to instruct a computer what to do, let us concentrate rather on explaining to human beings what we want a computer to do.

* Just a small aside: recently, this idea of literate programming has been extended to a whole programming language, Eve.

* **How notebooks work**

    * Jupyter notebooks grew out of the IPython project started by Fernando Perez. IPython is an interactive shell, similar to the normal Python shell but with great features like syntax highlighting and code completion. Originally, notebooks worked by sending messages from the web app (the notebook you see in the browser) to an IPython kernel (an IPython application running in the background). The kernel executed the code, then sent it back to the notebook. The current architecture is similar, drawn out below.

    * ![notebooks](./images/notebook-components.png)

    * The central point is the notebook server. You connect to the server through your browser and the notebook is rendered as a web app. Code you write in the web app is sent through the server to the kernel. The kernel runs the code and sends it back to the server, then any output is rendered back in the browser. When you save the notebook, it is written to the server as a JSON file with a .ipynb file extension.

    * The great part of this architecture is that the kernel doesn't need to run Python. Since the notebook and the kernel are separate, code in any language can be sent between them. For example, two of the earlier non-Python kernels were for the R and Julia languages. With an R kernel, code written in R will be sent to the R kernel where it is executed, exactly the same as Python code running on a Python kernel. IPython notebooks were renamed because notebooks became language agnostic. The new name Jupyter comes from the combination of Julia, Python, and R. If you're interested, here's a list of available kernels.

    * Another benefit is that the server can be run anywhere and accessed via the internet. Typically you'll be running the server on your own machine where all your data and notebook files are stored. But, you could also set up a server on a remote machine or cloud instance like Amazon's EC2. Then, you can access the notebooks in your browser from anywhere in the world.

    * By far the easiest way to install Jupyter is with Anaconda. Jupyter notebooks automatically come with the distribution. You'll be able to use notebooks from the default environment.

    * Local install: `conda install jupyter notebook`

    * To start a Jupyter notebook just run: `jupyter notebook`

    * You should consider installing Notebook Conda to help manage your environments. Run the following command:

        * `conda install nb_conda`
        * ![py-conda](./images/py-conda.png)
    
    * You can shutdown the entire server by pressing control + C twice in the terminal. Again, this will immediately shutdown all the running notebooks, so make sure your work is saved!

* **Notebook Interface**

    * You’ll see a little box outlined in green. This is called a cell. Cells are where you write and run your code. You can also change it to render Markdown, a popular formatting syntax for writing web content. I'll cover Markdown in more detail later. In the toolbar, click “Code” to change it to Markdown and back. The little play button runs the cell, and the up and down arrows move cells up and down.

    * In the "File" menu, you can download the notebook in multiple formats. You'll often want to download it as an HTML file to share with others who aren't using Jupyter. Also, you can download the notebook as a normal Python file where all the code will run like normal. The Markdown and reST formats are great for using notebooks in blogs or documentation.

    * You can create math expressions in Markdown cells using LaTeX symbols. Notebooks use MathJax to render the LaTeX symbols as math symbols. To start math mode, wrap the LaTeX in dollar signs $y = mx + b$ for inline math. For a math block, use double dollar signs,

        * ```
            $$
            y = \frac{a}{b+c}
            $$
            ```

* **Magic keywords**

    * Magic keywords are special commands you can run in cells that let you control the notebook itself or perform system calls such as changing directories. For example, you can set up matplotlib to work interactively in the notebook with `%matplotlib`.

    * Magic commands are preceded with one or two percent signs (% or %%) for **line magics and cell magics, respectively. Line magics apply only to the line the magic command is written on, while cell magics apply to the whole cell.**

    * **NOTE**: These magic keywords are specific to the normal Python kernel. If you are using other kernels, these most likely won't work.

    * At some point, you'll probably spend some effort optimizing code to run faster. Timing how quickly your code runs is essential for this optimization. You can use the `timeit` magic command to time how long it takes for a function to run, like so:

        * ![magic-timeit](./images/magic-timeit.png)
    
    * If you want to time how long it takes for a whole cell to run, you’d use `%%timeit` like so:

        * ![magic-timeit2](./images/magic-timeit2.png)

* **Embedding visualizations in notebooks**

    * As mentioned before, notebooks let you embed images along with text and code. This is most useful when you’re using `matplotlib` or other plotting packages to create visualizations. You can use `%matplotlib` to set up matplotlib for interactive use in the notebook. By default figures will render in their own window. However, you can pass arguments to the command to select a specific "backend", the software that renders the image. To render figures directly in the notebook, you should use the inline backend with the command `%matplotlib inline`.

    * ![magic-matplotlib](./images/magic-matplotlib.png)

* **Debugging in the Notebook**

    * With the Python kernel, you can turn on the interactive debugger using the magic command `%pdb`. When you cause an error, you'll be able to inspect the variables in the current namespace.

        * ![magic-pdb](./images/magic-pdb.png) 

* **Converting notebooks**

    * Notebooks are just big JSON files with the extension `.ipynb`.

    * Since notebooks are JSON, it is simple to convert them to other formats. Jupyter comes with a utility called `nbconvert` for converting to HTML, Markdown, slideshows, etc.

    * For example, to convert a notebook to an HTML file, in your terminal use    

        * `jupyter nbconvert --to html notebook.ipynb`
    
    * Converting to HTML is useful for sharing your notebooks with others who aren't using notebooks. Markdown is great for including a notebook in blogs and other text editors that accept Markdown formatting.

    * Create slideshows from notebooks is one of my favorite features. The slides are created in notebooks like normal, but you'll need to designate which cells are slides and the type of slide the cell will be. In the menu bar, click View > Cell Toolbar > Slideshow to bring up the slide cell menu on each cell.

    * Running the slideshow

        * To create the slideshow from the notebook file, you'll need to use `nbconvert`:

            * `jupyter nbconvert notebook.ipynb --to slides`
        
        * This just converts the notebook to the necessary files for the slideshow, but you need to serve it with an HTTP server to actually see the presentation.

        * To convert it and immediately see it, use

            * `jupyter nbconvert notebook.ipynb --to slides --post serve`
        
        * This will open up the slideshow in your browser so you can present it.

### NumPy

* NumPy stands for Numerical Python and it is a fundamental package for scientific computing in Python. NumPy provides Python with an extensive math library capable of performing numerical computations **effectively and efficiently**. These lessons are intended as a basic overview of NumPy and introduces some of its most important features.

    * NumPy is written in C and Fortran

    * NumPy is included with Anaconda. If you don't already have Anaconda installed on your computer, please refer to the Anaconda section to get clear instructions on how to install Anaconda on your PC or Mac.

*  The following lessons were created using NumPy version 1.13.0. You can check which version of NumPy you have by typing !conda list numpy in your Jupyter Notebook or by typing `conda list numpy` in the Anaconda prompt.  If you have another version of NumPy installed in your computer, you can update your version by typing `conda install numpy=1.13` in the Anaconda prompt.

* NumPy is an order of magnitude faster compared to normal python arrays, check Jupyter notebook `NumPy.ipynb`

    * Even though Python lists are great on their own, NumPy has a number of key features that give it great advantages over Python lists. One such feature is speed. When performing operations on large arrays NumPy can often perform several orders of magnitude faster than Python lists. This speed comes from the nature of NumPy arrays being memory-efficient and from optimized algorithms used by NumPy for doing arithmetic, statistical, and linear algebra operations.

    * Another great feature of NumPy is that it has multidimensional array data structures that can represent vectors and matrices. You will learn all about vectors and matrices in the Linear Algebra section of this course later on, and as you will soon see, a lot of machine learning algorithms rely on matrix operations. For example, when training a Neural Network, you often have to carry out many matrix multiplications. NumPy is optimized for matrix operations and it allows us to do Linear Algebra operations effectively and efficiently, making it very suitable for solving machine learning problems.

    * Another great advantage of NumPy over Python lists is that NumPy has a large number of optimized built-in mathematical functions. These functions allow you to do a variety of complex mathematical computations very fast and with very little code (avoiding the use of complicated loops) making your programs more readable and easier to understand.

* Creating NumPy arrays (ndarrays -> n dimensional array)

    * Check `NumPy-2.ipynb`, `NumPy-3.ipynb`, etc for complete notes

    * NumPy handles more data types than python 

    * At the core of NumPy is the ndarray, where nd stands for n-dimensional. An ndarray is a multidimensional array of elements all of the same type. In other words, an ndarray is a grid that can take on many shapes and can hold either numbers or strings. In many Machine Learning problems you will often find yourself using ndarrays in many different ways. For instance, you might use an ndarray to hold the pixel values of an image that will be fed into a Neural Network for image classification.

    * Let's pause for a second to introduce some useful terminology. We refer to 1D arrays as rank 1 arrays. In general N-Dimensional arrays have rank N. Therefore, we refer to a 2D array as a rank 2 array. Another important property of arrays is their shape. The shape of an array is the size along each of its dimensions. For example, the shape of a rank 2 array will correspond to the number of rows and columns of the array. As you will see, NumPy ndarrays have attributes that allow us to get information about them in a very intuitive way. For example, the shape of an ndarray can be obtained using the `.shape` attribute. The shape attribute returns a tuple of N positive integers that specify the sizes of each dimension. In the example below we will create a rank 1 array and learn how to obtain its shape, its type, and the data-type (dtype) of its elements.

    * We can see that the shape attribute returns the tuple `(5,)` telling us that x is of rank 1 (i.e. x only has 1 dimension ) and it has 5 elements. The `type()` function tells us that x is indeed a NumPy ndarray. Finally, the `.dtype` attribute tells us that the elements of x are stored in memory as signed 64-bit integers. Another great advantage of NumPy is that it can handle more data-types than Python lists. You can check out all the different data types NumPy supports in the link below:
        * https://docs.scipy.org/doc/numpy-1.13.0/user/basics.types.html

    * **It is important to remember that one big difference between Python lists and ndarrays, is that unlike Python lists, all the elements of an ndarray must be of the same type.**

    * For more details check course material and specially the `.ipynb` files
        * `8 - Mini Project - Mean Normalization and Data Separation` does a good coverage of NumPy in the real world

### Panda

* Pandas is a package for **data manipulation and analysis** in Python. The name Pandas is derived from the econometrics term Panel Data. Pandas incorporates two additional data structures into Python, namely Pandas Series and Pandas DataFrame. These data structures allow us to work with labeled and relational data in an easy and intuitive manner. These lessons are intended as a basic overview of Pandas and introduces some of its most important features.

    * `conda list pandas` -> version 0.24

* **Why use Panda?**
    * The recent success of machine learning algorithms is partly due to the huge amounts of data that we have available to train our algorithms on. However, when it comes to data, quantity is not the only thing that matters, the quality of your data is just as important. It often happens that large datasets don’t come ready to be fed into your learning algorithms. More often than not, large datasets will often have missing values, outliers, incorrect values, etc… Having data with a lot of missing or bad values, for example, is not going to allow your machine learning algorithms to perform well. Therefore, one very important step in machine learning is to look at your data first and make sure it is well suited for your training algorithm by doing some basic data analysis. This is where Pandas comes in. **Pandas Series and DataFrames are designed for fast data analysis and manipulation**, as well as being flexible and easy to use. Below are just a few features that makes Pandas an excellent package for data analysis:

        * Allows the use of labels for rows and columns
        * Can calculate rolling statistics on time series data
        * Easy handling of NaN values
        * Is able to load data of different formats into DataFrames
        * Can join and merge different datasets together
        * It integrates with NumPy and Matplotlib
    
    * For these and other reasons, Pandas DataFrames have become one of the most commonly used Pandas object for data analysis in Python.

    * A Pandas series is a **one-dimensional array-like object that can hold many data types**, such as numbers or strings. One of the main differences between Pandas Series and NumPy ndarrays is that you can assign an **index label to each element in the Pandas Series**. In other words, you can **name the indices of your Pandas Series anything you want**. Another big difference between Pandas Series and NumPy ndarrays is that Pandas Series can hold data of different data types.

        * Let's start by importing Pandas into Python. It has become a convention to import Pandas as pd, therefore, you can import Pandas by typing the following command in your Jupyter notebook: 
            * `import pandas as pd`
        
        * Let's begin by creating a Pandas Series. You can create Pandas Series by using the command `pd.Series(data, index)`, where `index` is a list of index labels. Let's use a Pandas Series to store a grocery list. We will use the food items as index labels and the quantity we need to buy of each item as our data.

            * eggs           30
            * apples         6
            * milk         Yes
            * bread       No
            * dtype: object

        * We see that Pandas Series are displayed with the indices in the first column and the data in the second column. Notice that the data is not indexed 0 to 3 but rather it is indexed with the names of the food we put in, namely eggs, apples, etc... Also notice that the data in our Pandas Series has both integers and strings.

        * Just like NumPy ndarrays, Pandas Series have attributes that allows us to get information from the series in an easy way. Let's see some of them:

            * ```python
                # We print some information about Groceries
                print('Groceries has shape:', groceries.shape)
                print('Groceries has dimension:', groceries.ndim)
                print('Groceries has a total of', groceries.size, 'elements')
                ```
        
        * We can also print the index labels and the data of the Pandas Series separately. This is useful if you don't happen to know what the index labels of the Pandas Series are.

            * ```python
                # We print the index and data of Groceries
                print('The data in Groceries is:', groceries.values)
                print('The index of Groceries is:', groceries.index)
                ```
        
        * If you are dealing with a very large Pandas Series and if you are not sure whether an index label exists, you can check by using the in command

            * ```python
                # We check whether bananas is a food item (an index) in Groceries
                x = 'bananas' in groceries

                # We check whether bread is a food item (an index) in Groceries
                y = 'bread' in groceries

                # We print the results
                print('Is bananas an index label in Groceries:', x)
                print('Is bread an index label in Groceries:', y)
                ```
        
        * Now let's look at how we can access or modify elements in a Pandas Series. One great advantage of Pandas Series is that it allows us to access data in many different ways. Elements can be accessed using index labels or numerical indices inside square brackets, [ ], similar to how we access elements in NumPy ndarrays. Since we can use numerical indices, we can use both positive and negative integers to access data from the beginning or from the end of the Series, respectively. Since we can access elements in various ways, in order to remove any ambiguity to whether we are referring to an index label or numerical index, Pandas Series have two attributes, `.loc` and `.iloc` to explicitly state what we mean. The attribute `.loc` stands for **location** and it is used to explicitly state that we are using a labeled index. Similarly, the attribute `.iloc` stands for **integer location** and it is used to explicitly state that we are using a numerical index. Let's see some examples:

            * ```python
                # We access elements in Groceries using index labels:

                # We use a single index label
                print('How many eggs do we need to buy:', groceries['eggs'])
                print()

                # we can access multiple index labels
                print('Do we need milk and bread:\n', groceries[['milk', 'bread']]) 
                print()

                # we use loc to access multiple index labels
                print('How many eggs and apples do we need to buy:\n', groceries.loc[['eggs', 'apples']]) 
                print()

                # We access elements in Groceries using numerical indices:

                # we use multiple numerical indices
                print('How many eggs and apples do we need to buy:\n',  groceries[[0, 1]]) 
                print()

                # We use a negative numerical index
                print('Do we need bread:\n', groceries[[-1]]) 
                print()

                # We use a single numerical index
                print('How many eggs do we need to buy:', groceries[0]) 
                print()
                # we use iloc to access multiple numerical indices
                print('Do we need milk and bread:\n', groceries.iloc[[2, 3]]) 
                ```
        
        * Pandas Series are also mutable like NumPy ndarrays, which means we can change the elements of a Pandas Series after it has been created. For example, let's change the number of eggs we need to buy from our grocery list

            * ```python
                # We display the original grocery list
                print('Original Grocery List:\n', groceries)

                # We change the number of eggs to 2
                groceries['eggs'] = 2

                # We display the changed grocery list
                print()
                print('Modified Grocery List:\n', groceries)
                ```
        
        * We can also delete items from a Pandas Series by using the `.drop()` method. The `Series.drop(label)` method removes the given `label` from the given Series. We should note that the `Series.drop(label)` method drops elements from the Series out of place, meaning that **it doesn't change the original Series being modified**. Let's see how this works:

            * ```python
                # We display the original grocery list
                print('Original Grocery List:\n', groceries)

                # We remove apples from our grocery list. The drop function removes elements out of place
                print()
                print('We remove apples (out of place):\n', groceries.drop('apples'))

                # When we remove elements out of place the original Series remains intact. To see this
                # we display our grocery list again
                print()
                print('Grocery List after removing apples out of place:\n', groceries)
                ```
        
        * We can delete items from a Pandas Series in place by setting the keyword `inplace` to `True` in the `.drop()` method. Let's see an example:

            * ```python
                # We display the original grocery list
                print('Original Grocery List:\n', groceries)

                # We remove apples from our grocery list in place by setting the inplace keyword to True
                groceries.drop('apples', inplace = True)

                # When we remove elements in place the original Series its modified. To see this
                # we display our grocery list again
                print()
                print('Grocery List after removing apples in place:\n', groceries)
                ```
        
        * Just like with NumPy ndarrays, we can perform element-wise arithmetic operations on Pandas Series. In this lesson we will look at arithmetic operations between **Pandas Series** and single numbers. Let's create a new Pandas Series that will hold a grocery list of just fruits.


            * ```python
                # We create a Pandas Series that stores a grocery list of just fruits
                fruits= pd.Series(data = [10, 6, 3,], index = ['apples', 'oranges', 'bananas'])

                # We display the fruits Pandas Series
                print(fruits)
                ```
        
        * We can now modify the data in fruits by performing basic arithmetic operations. Let's see some examples

            * ```python
                # We print fruits for reference
                print('Original grocery list of fruits:\n ', fruits)

                # We perform basic element-wise operations using arithmetic symbols
                print()
                print('fruits + 2:\n', fruits + 2) # We add 2 to each item in fruits
                print()
                print('fruits - 2:\n', fruits - 2) # We subtract 2 to each item in fruits
                print()
                print('fruits * 2:\n', fruits * 2) # We multiply each item in fruits by 2 
                print()
                print('fruits / 2:\n', fruits / 2) # We divide each item in fruits by 2
                print()
                ```
        
        * You can also apply mathematical functions from NumPy, such assqrt(x), to all elements of a Pandas Series.

            * ```python
                # We import NumPy as np to be able to use the mathematical functions
                import numpy as np

                # We print fruits for reference
                print('Original grocery list of fruits:\n', fruits)

                # We apply different mathematical functions to all elements of fruits
                print()
                print('EXP(X) = \n', np.exp(fruits))
                print() 
                print('SQRT(X) =\n', np.sqrt(fruits))
                print()
                print('POW(X,2) =\n',np.power(fruits,2)) # We raise all elements of fruits to the power of 2
                ```
        
        * Pandas also allows us to only apply arithmetic operations on selected items in our fruits grocery list. Let's see some examples

            * ```python
                # We print fruits for reference
                print('Original grocery list of fruits:\n ', fruits)
                print()

                # We add 2 only to the bananas
                print('Amount of bananas + 2 = ', fruits['bananas'] + 2)
                print()

                # We subtract 2 from apples
                print('Amount of apples - 2 = ', fruits.iloc[0] - 2)
                print()

                # We multiply apples and oranges by 2
                print('We double the amount of apples and oranges:\n', fruits[['apples', 'oranges']] * 2)
                print()

                # We divide apples and oranges by 2
                print('We half the amount of apples and oranges:\n', fruits.loc[['apples', 'oranges']] / 2)
                ```
        
        * You can also apply arithmetic operations on Pandas Series of mixed data type provided that the arithmetic operation is defined for all data types in the Series, otherwise you will get an error. Let's see what happens when we multiply our grocery list by 2

            * ```python
                # We multiply our grocery list by 2
                groceries * 2
                ```
        
        * As we can see, in this case, since we multiplied by 2, Pandas doubles the data of each item including the strings. Pandas can do this because the multiplication operation * is defined both for numbers and strings. If you were to apply an operation that was valid for numbers but not strings, say for instance, / you will get an error. So when you have mixed data types in your Pandas Series make sure the arithmetic operations are valid on all the data types of your elements.

        * ```python
            import pandas as pd

            # Create a Pandas Series that contains the distance of some planets from the Sun.
            # Use the name of the planets as the index to your Pandas Series, and the distance
            # from the Sun as your data. The distance from the Sun is in units of 10^6 km

            distance_from_sun = [149.6, 1433.5, 227.9, 108.2, 778.6]

            planets = ['Earth','Saturn', 'Mars','Venus', 'Jupiter']

            # Create a Pandas Series using the above data, with the name of the planets as
            # the index and the distance from the Sun as your data.
            dist_planets = pd.Series(data = distance_from_sun, index = planets)

            # Calculate the number of minutes it takes sunlight to reach each planet. You can
            # do this by dividing the distance from the Sun for each planet by the speed of light.
            # Since in the data above the distance from the Sun is in units of 10^6 km, you can
            # use a value for the speed of light of c = 18, since light travels 18 x 10^6 km/minute.
            time_light = dist_planets / 18

            # Use Boolean indexing to select only those planets for which sunlight takes less
            # than 40 minutes to reach them.
            close_planets = dist_planets[time_light< 40]
            ```
    
    * **Pandas DataFrames** are two-dimensional data structures with labeled rows and columns, that can hold many data types. If you are familiar with Excel, you can think of Pandas DataFrames as being similar to a spreadsheet. We can create Pandas DataFrames manually or by loading data from a file. In these lessons we will start by learning how to create Pandas DataFrames manually from dictionaries and later we will see how we can load data into a DataFrame from a data file.

    * We will start by creating a DataFrame manually from a dictionary of Pandas Series. In this case the first step is to create the dictionary of Pandas Series. After the dictionary is created we can then pass the dictionary to the `pd.DataFrame()` function.

    * We will create a dictionary that contains items purchased by two people, Alice and Bob, on an online store. The Pandas Series will use the price of the items purchased as data, and the purchased items will be used as the index labels to the Pandas Series. Let's see how this done in code:

        * ```python
            # We import Pandas as pd into Python
            import pandas as pd

            # We create a dictionary of Pandas Series 
            items = {'Bob' : pd.Series(data = [245, 25, 55], index = ['bike', 'pants', 'watch']),
                    'Alice' : pd.Series(data = [40, 110, 500, 45], index = ['book', 'glasses', 'bike', 'pants'])}

            # We print the type of items to see that it is a dictionary
            print(type(items))
            ```
        
        * ![data_frame](./images/data_frame.png)
    
    * Now that we have a dictionary, we are ready to create a DataFrame by passing it to the `pd.DataFrame()` function. We will create a DataFrame that could represent the shopping carts of various users, in this case we have only two users, Alice and Bob.

        * There are several things to notice here that are worth pointing out. We see that DataFrames are displayed in tabular form, much like an Excel spreadsheet, with the labels of rows and columns in bold. Also notice that the row labels of the DataFrame are built from the union of the index labels of the two Pandas Series we used to construct the dictionary. And the column labels of the DataFrame are taken from the keys of the dictionary. Another thing to notice is that the columns are arranged alphabetically and not in the order given in the dictionary. We will see later that this won't happen when we load data into a DataFrame from a data file. The last thing we want to point out is that we see some NaN values appear in the DataFrame. NaN stands for Not a Number, and is Pandas way of indicating that it doesn't have a value for that particular row and column index. For example, if we look at the column of Alice, we see that it has NaN in the watch index. You can see why this is the case by looking at the dictionary we created at the beginning. We clearly see that the dictionary has no item for Alice labeled watches. So whenever a DataFrame is created, if a particular column doesn't have values for a particular row index, Pandas will put a NaN value there. If we were to feed this data into a machine learning algorithm we will have to remove these NaN values first. In a later lesson we will learn how to deal with NaN values and clean our data. For now, we will leave these values in our DataFrame.

        * In the above example we created a Pandas DataFrame from a dictionary of Pandas Series that had clearly defined indexes. If we don't provide index labels to the Pandas Series, Pandas will use numerical row indexes when it creates the DataFrame. Let's see an example:

        * ```python
            # We create a dictionary of Pandas Series without indexes
            data = {'Bob' : pd.Series([245, 25, 55]),
                    'Alice' : pd.Series([40, 110, 500, 45])}

            # We create a DataFrame
            df = pd.DataFrame(data)

            # We display the DataFrame
            df
            ```
        
        * We can see that Pandas indexes the rows of the DataFrame starting from 0, just like NumPy indexes ndarrays.

        * Now, just like with Pandas Series we can also extract information from DataFrames using attributes. Let's print some information from our `shopping_carts` DataFrame

            * ```python
                # We print some information about shopping_carts
                print('shopping_carts has shape:', shopping_carts.shape)
                print('shopping_carts has dimension:', shopping_carts.ndim)
                print('shopping_carts has a total of:', shopping_carts.size, 'elements')
                print()
                print('The data in shopping_carts is:\n', shopping_carts.values)
                print()
                print('The row index in shopping_carts is:', shopping_carts.index)
                print()
                print('The column index in shopping_carts is:', shopping_carts.columns)
                ```

        * When creating the shopping_carts DataFrame we passed the entire dictionary to the `pd.DataFrame()` function. However, there might be cases when you are only interested in a subset of the data. Pandas allows us to select which data we want to put into our DataFrame by means of the keywords columns and index. Let's see some examples:

            * ```python
                # We Create a DataFrame that only has Bob's data
                bob_shopping_cart = pd.DataFrame(items, columns=['Bob'])

                # We display bob_shopping_cart
                bob_shopping_cart

                # We Create a DataFrame that only has selected items for both Alice and Bob
                sel_shopping_cart = pd.DataFrame(items, index = ['pants', 'book'])

                # We display sel_shopping_cart
                sel_shopping_cart

                # We Create a DataFrame that only has selected items for Alice
                alice_sel_shopping_cart = pd.DataFrame(items, index = ['glasses', 'bike'], columns = ['Alice'])

                # We display alice_sel_shopping_cart
                alice_sel_shopping_cart
                ```
        
        * You can also manually create DataFrames from a dictionary of lists (arrays). The procedure is the same as before, we start by creating the dictionary and then passing the dictionary to the `pd.DataFrame()` function. In this case, however, all the lists (arrays) in the dictionary must be of the same length. Let' see an example:

            * ```python
                # We create a dictionary of lists (arrays)
                data = {'Integers' : [1,2,3],
                        'Floats' : [4.5, 8.2, 9.6]}

                # We create a DataFrame 
                df = pd.DataFrame(data)

                # We display the DataFrame
                df
                ```
        
        * Notice that since the data dictionary we created doesn't have label indices, Pandas automatically uses numerical row indexes when it creates the DataFrame. We can however, put labels to the row index by using the index keyword in the `pd.DataFrame()` function. Let's see an example

            * ```python
                # We create a list of Python dictionaries
                items2 = [{'bikes': 20, 'pants': 30, 'watches': 35}, 
                        {'watches': 10, 'glasses': 50, 'bikes': 15, 'pants':5}]

                # We create a DataFrame 
                store_items = pd.DataFrame(items2)

                # We display the DataFrame
                store_items
                ```

            * ![data_frame](./images/data_frame2.png)
        
        * Again, notice that since the items2 dictionary we created doesn't have label indices, Pandas automatically uses numerical row indexes when it creates the DataFrame. As before, we can put labels to the row index by using the index keyword in the `pd.DataFrame()` function. Let's assume we are going to use this DataFrame to hold the number of items a particular store has in stock. So, we will label the row indices as store 1 and store 2.

            * ![data_frame](./images/data_frame3.png)
        
        * We can access elements in Pandas DataFrames in many different ways. In general, we can access rows, columns, or individual elements of the DataFrame by using the row and column labels. We will use the same `store_items` DataFrame created in the previous lesson. Let's see some examples:

            * ```python
                # We import Pandas as pd into Python
                import pandas as pd

                # We create a list of Python dictionaries
                items2 = [{'bikes': 20, 'pants': 30, 'watches': 35}, 
                        {'watches': 10, 'glasses': 50, 'bikes': 15, 'pants':5}]

                # We create a DataFrame  and provide the row index
                store_items = pd.DataFrame(items2, index = ['store 1', 'store 2'])

                # We print the store_items DataFrame
                print(store_items)

                # We access rows, columns and elements using labels
                print()
                print('How many bikes are in each store:\n', store_items[['bikes']])
                print()
                print('How many bikes and pants are in each store:\n', store_items[['bikes', 'pants']])
                print()
                print('What items are in Store 1:\n', store_items.loc[['store 1']])
                print()
                print('How many bikes are in Store 2:', store_items['bikes']['store 2'])
                ```
            
            * ![data_frame](./images/data_frame4.png)
    
    * It is important to know that when accessing individual elements in a DataFrame, as we did in the last example above, the labels should always be provided with the column label first, i.e. in the form `dataframe[column][row]`. For example, when retrieving the number bikes in store 2, we first used the column label bikes and then the row label store 2. If you provide the row label first you will get an error.

    * We can also modify our DataFrames by adding rows or columns. Let's start by learning how to add new columns to our DataFrames. Let's suppose we decided to add shirts to the items we have in stock at each store. To do this, we will need to add a new column to our `store_items` DataFrame indicating how many shirts are in each store. Let's do that:

        * ```python
            # We add a new column named shirts to our store_items DataFrame indicating the number of
            # shirts in stock at each store. We will put 15 shirts in store 1 and 2 shirts in store 2
            store_items['shirts'] = [15,2]

            # We display the modified DataFrame
            store_items
            ```
    
    * Suppose now, that you opened a new store and you need to add the number of items in stock of that new store into your DataFrame. We can do this by adding a new row to the `store_items` Dataframe. To add rows to our DataFrame we first have to create a new Dataframe and then append it to the original DataFrame. Let's see how this works

        * ```python
            # We create a dictionary from a list of Python dictionaries that will number of items at the new store
            new_items = [{'bikes': 20, 'pants': 30, 'watches': 35, 'glasses': 4}]

            # We create new DataFrame with the new_items and provide and index labeled store 3
            new_store = pd.DataFrame(new_items, index = ['store 3'])

            # We display the items at the new store
            new_store

            # We append store 3 to our store_items DataFrame
            store_items = store_items.append(new_store, sort=False)

            # We display the modified DataFrame
            store_items
            ```
    
    * Notice that by appending a new row to the DataFrame, the columns have been put in alphabetical order.

    * We can also add new columns of our DataFrame by using only data from particular rows in particular columns. For example, suppose that you want to stock stores 2 and 3 with new watches and you want the quantity of the new watches to be the same as the watches already in stock for those stores. Let's see how we can do this

        * ```python
            # We add a new column using data from particular rows in the watches column
            store_items['new watches'] = store_items['watches'][1:]

            # We display the modified DataFrame
            store_items
            ```

        * ![data_frame](./images/data_frame5.png)
    

    * It is also possible, to insert new columns into the DataFrames anywhere we want. The `dataframe.insert(loc,label,data)` method allows us to insert a new column in the dataframe at location loc, with the given column label, and given data. Let's add new column named shoes right before the suits column. Since suits has numerical index value 4 then we will use this value as loc. Let's see how this works:

        * ```python
            # We insert a new column with label shoes right before the column with numerical index 4
            store_items.insert(4, 'shoes', [8,5,0])

            # we display the modified DataFrame
            store_items
            ```
    
    * Just as we can add rows and columns we can also delete them. To delete rows and columns from our DataFrame we will use the `.pop()` and `.drop()` methods. The `.pop()` method only allows us to delete columns, while the `.drop()` method can be used to delete both rows and columns by use of the axis keyword. Let's see some examples

        * ```python
            # We remove the new watches column
            store_items.pop('new watches')

            # we display the modified DataFrame
            store_items
            ```

        * ```python
            # We remove the watches and shoes columns
            store_items = store_items.drop(['watches', 'shoes'], axis = 1)

            # we display the modified DataFrame
            store_items
            ```
    
    * Sometimes we might need to change the row and column labels. Let's change the bikes column label to hats using the `.rename()` method

        * ```python
            # We change the column label bikes to hats
            store_items = store_items.rename(columns = {'bikes': 'hats'})

            # we display the modified DataFrame
            store_items

            # We change the row label from store 3 to last store
            store_items = store_items.rename(index = {'store 3': 'last store'})

            # we display the modified DataFrame
            store_items
            ```
    * You can also change the index to be one of the columns in the DataFrame.

        * ```python
            # We change the row index to be the data in the pants column
            store_items = store_items.set_index('pants')

            # we display the modified DataFrame
            store_items
            ```
    
    * As mentioned earlier, before we can begin training our learning algorithms with large datasets, we usually need to clean the data first. This means we need to have a method for detecting and correcting errors in our data. While any given dataset can have many types of bad data, such as outliers or incorrect values, the type of bad data we encounter almost always is missing values. As we saw earlier, Pandas assigns `NaN` values to missing data. In this lesson we will learn how to detect and deal with `NaN` values.

    * We will begin by creating a DataFrame with some `NaN` values in it.

        * ```python
            # We create a list of Python dictionaries
            items2 = [{'bikes': 20, 'pants': 30, 'watches': 35, 'shirts': 15, 'shoes':8, 'suits':45},
            {'watches': 10, 'glasses': 50, 'bikes': 15, 'pants':5, 'shirts': 2, 'shoes':5, 'suits':7},
            {'bikes': 20, 'pants': 30, 'watches': 35, 'glasses': 4, 'shoes':10}]

            # We create a DataFrame  and provide the row index
            store_items = pd.DataFrame(items2, index = ['store 1', 'store 2', 'store 3'])

            # We display the DataFrame
            store_items
            ```
    
    * We can clearly see that the DataFrame we created has 3 `NaN` values: one in store 1 and two in store 3. However, in cases where we load very large datasets into a DataFrame, possibly with millions of items, the number of `NaN` values is not easily visualized. For these cases, we can use a combination of methods to count the number of `NaN` values in our data. The following example combines the `.isnull()` and the `sum()` methods to count the number of NaN values in our DataFrame

        * ```python
            # We count the number of NaN values in store_items
            x =  store_items.isnull().sum().sum()

            # We print x
            print('Number of NaN values in our DataFrame:', x)
            ```

    * In the above example, the `.isnull()` method returns a Boolean DataFrame of the same size as `store_items` and indicates with True the elements that have NaN values and with False the elements that are not. Let's see an example:

        * ```python 
            store_items.isnull()
            ```

    * In Pandas, logical True values have numerical value 1 and logical False values have numerical value 0. Therefore, we can count the number of NaN values by counting the number of logical True values. In order to count the total number of logical True values we use the .sum() method twice. We have to use it twice because the first sum returns a Pandas Series with the sums of logical True values along columns, as we see below: ```store_items.isnull().sum()```

    * The second sum will then add up the 1s in the above Pandas Series.

    * Instead of counting the number of NaN values we can also do the opposite, we can count the number of non-NaN values. We can do this by using the `.count()` method as shown below:

        * ```python
            # We print the number of non-NaN values in our DataFrame
            print()
            print('Number of non-NaN values in the columns of our DataFrame:\n', store_items.count())
            ```
    
    * Now that we learned how to know if our dataset has any `NaN` values in it, the next step is to decide what to do with them. In general we have two options, we can either delete or replace the `NaN` values. In the following examples we will show you how to do both.

    * We will start by learning how to eliminate rows or columns from our DataFrame that contain any `NaN` values. The `.dropna(axis)` method eliminates any rows with `NaN` values when `axis = 0` is used and will eliminate any columns with `NaN` values when `axis = 1` is used. Let's see some examples

        * ```python
            # We drop any rows with NaN values
            store_items.dropna(axis = 0)

            # We drop any columns with NaN values
            store_items.dropna(axis = 1)
            ```
    
    * Notice that the `.dropna()` method eliminates (drops) the rows or columns with NaN values out of place. This means that the original DataFrame is not modified. You can always remove the desired rows or columns in place by setting the keyword `inplace = True` inside the `dropna()` function.

    * Now, instead of eliminating `NaN` values, we can replace them with suitable values. We could choose for example to replace all `NaN` values with the value 0. We can do this by using the `.fillna()` method as shown below.

        * ```python
            # We replace all NaN values with 0
            store_items.fillna(0)
            ```
    
    * We can also use the `.fillna()` method to replace NaN values with previous values in the DataFrame, this is known as forward filling. When replacing NaN values with forward filling, we can use previous values taken from columns or rows. The `.fillna(method = 'ffill', axis)` will use the forward filling (ffill) method to replace NaN values using the previous known value along the given axis. Let's see some examples:

        * ```python
            # We replace NaN values with the previous value in the column
            store_items.fillna(method = 'ffill', axis = 0)
            ```
    
    * Notice that the two NaN values in store 3 have been replaced with previous values in their columns. However, notice that the NaN value in store 1 didn't get replaced. That's because there are no previous values in this column, since the NaN value is the first value in that column. However, if we do forward fill using the previous row values, this won't happen. Let's take a look:

        * ```python
            # We replace NaN values with the previous value in the row
            store_items.fillna(method = 'ffill', axis = 1)
            ```
    
    * We see that in this case all the NaN values have been replaced with the previous row values.

    * Similarly, you can choose to replace the NaN values with the values that go after them in the DataFrame, this is known as backward filling. The `.fillna(method = 'backfill', axis)` will use the backward filling (backfill) method to replace NaN values using the next known value along the given axis. Just like with forward filling we can choose to use row or column values. Let's see some examples:

        * ```python
            # We replace NaN values with the next value in the column
            store_items.fillna(method = 'backfill', axis = 0)
            ```
    
    * Notice that the `NaN` value in store 1 has been replaced with the next value in its column. However, notice that the two NaN values in store 3 didn't get replaced. That's because there are no next values in these columns, since these NaN values are the last values in those columns. However, if we do backward fill using the next row values, this won't happen. Let's take a look:

        * ```python
            # We replace NaN values with the next value in the row
            store_items.fillna(method = 'backfill', axis = 1)
            ```
    
    * Notice that the `.fillna()` method replaces (fills) the NaN values out of place. This means that the original DataFrame is not modified. You can always replace the NaN values in place by setting the keyword `inplace = True` inside the `fillna()` function.

    * We can also choose to replace `NaN` values by using different interpolation methods. For example, the `.interpolate(method = 'linear', axis)` method will use linear interpolation to replace `NaN` values using the values along the given axis. Let's see some examples:

        * ```python
            # We replace NaN values by using linear interpolation using column values
            store_items.interpolate(method = 'linear', axis = 0)
            ```

    * ```python
        import pandas as pd
        import numpy as np

        pd.set_option('precision', 1)

        books = pd.Series(data = ['Great Expectations', 'Of Mice and Men', 'Romeo and Juliet', 'The Time Machine', 'Alice in Wonderland' ])
        authors = pd.Series(data = ['Charles Dickens', 'John Steinbeck', 'William Shakespeare', ' H. G. Wells', 'Lewis Carroll' ])
        user_1 = pd.Series(data = [3.2, np.nan ,2.5])
        user_2 = pd.Series(data = [5., 1.3, 4.0, 3.8])
        user_3 = pd.Series(data = [2.0, 2.3, np.nan, 4])
        user_4 = pd.Series(data = [4, 3.5, 4, 5, 4.2])

        dat = {'Book Title' : books,
            'Author' : authors,
            'User 1' : user_1,
            'User 2' : user_2,
            'User 3' : user_3,
            'User 4' : user_4}

        book_ratings = pd.DataFrame(dat)

        print(book_ratings.mean())
        print()

        book_ratings.fillna(book_ratings.mean(), inplace = True)

        print(book_ratings)
        ```
    
    * In machine learning you will most likely use databases from many sources to train your learning algorithms. Pandas allows us to load databases of different formats into DataFrames. One of the most popular data formats used to store databases is csv. CSV stands for Comma Separated Values and offers a simple format to store data. We can load CSV files into Pandas DataFrames using the pd.read_csv() function. Let's load Google stock data into a Pandas DataFrame. The GOOG.csv file contains Google stock data from 8/19/2004 till 10/13/2017 taken from Yahoo Finance.

    * ```python
        import pandas as pd

        # We load Google stock data in a DataFrame
        Google_stock = pd.read_csv('./GOOG.csv')

        # We print some information about Google_stock
        print('Google_stock is of type:', type(Google_stock))
        print('Google_stock has shape:', Google_stock.shape)
        ```

    * We see that we have loaded the GOOG.csv file into a Pandas DataFrame and it consists of 3,313 rows and 7 columns. Now let's look at the stock data

    * We see that it is quite a large dataset and that Pandas has automatically assigned numerical row indices to the DataFrame. Pandas also used the labels that appear in the data in the CSV file to assign the column labels.

    * When dealing with large datasets like this one, it is often useful just to take a look at the first few rows of data instead of the whole dataset. We can take a look at the first 5 rows of data using the `.head()` method, as shown below: ```Google_stock.head()```

    * We can also optionally use `.head(N)` or `.tail(N)` to display the first and last N rows of data, respectively.

    * Let's do a quick check to see whether we have any `NaN` values in our dataset. To do this, we will use the `.isnull()` method followed by the `.any()` method to check whether any of the columns contain `NaN` values.

        * ```python
            Google_stock.isnull().any()
            ```
    
    * We see that we have no NaN values.

    * When dealing with large datasets, it is often useful to get statistical information from them. Pandas provides the `.describe()` method to get descriptive statistics on each column of the DataFrame. Let's see how this works:

        * ```python
            # We get descriptive statistics on our stock data
            Google_stock.describe()
            ```
    
    * If desired, we can apply the .describe() method on a single column as shown below: ```Google_stock['Adj Close'].describe()```

    * Similarly, you can also look at one statistic by using one of the many statistical functions Pandas provides. Let's look at some examples:

        * ```python
            # We print information about our DataFrame  
            print()
            print('Maximum values of each column:\n', Google_stock.max())
            print()
            print('Minimum Close value:', Google_stock['Close'].min())
            print()
            print('Average value of each column:\n', Google_stock.mean())
            ```
    
    * Another important statistical measure is data correlation. Data correlation can tell us, for example, if the data in different columns are correlated. We can use the .corr() method to get the correlation between different columns, as shown below:

        * ```python
            # We display the correlation between columns
            Google_stock.corr()
            ```
    
    * A correlation value of 1 tells us there is a high correlation and a correlation of 0 tells us that the data is not correlated at all.

    * We will end this Introduction to Pandas by taking a look at the `.groupby()` method. The `.groupby()` method allows us to group data in different ways. Let's see how we can group data to get different types of information. For the next examples we are going to load fake data about a fictitious company.

    * We see that the data contains information for the year 1990 through 1992. For each year we see name of the employees, the department they work for, their age, and their annual salary. Now, let's use the `.groupby()` method to get information.

    * Let's calculate how much money the company spent in salaries each year. To do this, we will group the data by Year using the `.groupby()` method and then we will add up the salaries of all the employees by using the `.sum()` method.

        * ```python
            # We display the total amount of money spent in salaries each year
            data.groupby(['Year'])['Salary'].sum()

            # We display the total salary each employee received in all the years they worked for the company
            data.groupby(['Name'])['Salary'].sum()
            ```


### Matplotlib

* **Univariate Visualization**: Visualization of single variables
    * Bar charts for qualitative variables
    * Histograms for quantitative variables

    * What is Tidy Data?

        * In this course, it is expected that your data is organized in some kind of tidy format. In short, a tidy dataset is a tabular dataset where:

            * each variable is a column
            * each observation is a row
            * each type of observational unit is a table
        
        * The first three images below depict a tidy dataset. This tidy dataset is in the field of healthcare and has two tables: one for patients (with their patient ID, name, and age) and one for treatments (with patient ID, what drug that patient is taking, and the dose of that drug).

            * ![tidy-data-one](./images/tidy-data-one.png)
            * ![tidy-data-two](./images/tidy-data-two.png)
            * ![tidy-data-three](./images/tidy-data-three.png)
        
        * The next image depicts the same data but in one representation of a non-tidy format (there are other possible non-tidy representations). The Drug A, Drug B, and Drug C columns should form one 'Drug' column, since this is one variable. The entire table should be separated into two tables: a patients table and a treatments table.

            * ![tidy-data-four](./images/tidy-data-four.png)
        
        * While the data provided to you in the course will all be tidy, in practice, you may need to perform tidying work before exploration. You should be comfortable with reshaping your data or perform transformations to split or combine features in your data, resulting in new data columns. This work should be performed in the wrangling stage of the data analysis process, so if you need to know more about these operations, it is recommended that you refer back to the data wrangling content from earlier in the program.

        * This is also not to say that tidy data is the only useful form that data can take. In fact, as you work with a dataset, you might need to summarize it in a non-tidy form in order to generate appropriate visualizations. You'll see one example of this in the bivariate plotting lesson, where categorical counts need to put into a matrix form in order to create a heat map.

    * Qualitative variable
        * Qualitative. Qualitative variables take on values that are **names or labels**. The color of a ball (e.g., red, green, blue) or the breed of a dog (e.g., collie, shepherd, terrier) would be examples of qualitative or categorical variables.
    
    * Quantitative variable
        * Quantitative. Quantitative variables are **numeric**. They represent a measurable quantity. For example, when we speak of the population of a city, we are talking about the number of people in the city - a measurable attribute of the city. Therefore, population would be a quantitative variable.

    * Bar charts for **qualitative** variables
        * Quantitative data analysis, which deals with numbers.
        * Qualitative data analysis, which deals with text or pictures.
        * ![qualitative_variables](./images/qualitative_variables.png)
        * ![qualitative_variables2](./images/qualitative_variables2.png)
        * ![nominal_data](./images/nominal_data.png)
            * Which category is the most common, and how the rest of the categories compare 
        * ![ordinal_data](./images/ordinal_data.png)
            * It is more important to know if the most common categories are lower or higher in the spectrum, rather than which label is the most frequent 
            * ![ordinal_data2](./images/ordinal_data2.png)
    
    * **Histograms**
        * A histogram is used to plot the distribution of a numeric variable. It's the **quantitative** version of the bar chart. However, rather than plot one bar for each unique numeric value, values are grouped into continuous bins, and one bar for each bin is plotted depicting the number. For instance, using the default settings for matplotlib's hist function:

            * `bin_edges = np.arange(0, df['num_var'].max()+1, 1)`
            * `plt.hist(data = df, x = 'num_var', bins = bin_edges)`

        * When creating histograms, it's useful to play around with different bin widths to see what represents the data best. Too many bins, and you may see too much noise that interferes with identification of the underlying signal. Too few bins, and you may not be able to see the true signal in the first place.

            * ```python
                plt.figure(figsize = [10, 5]) # larger figure size for subplots

                # histogram on left, example of too-large bin size
                plt.subplot(1, 2, 1) # 1 row, 2 cols, subplot 1
                bin_edges = np.arange(0, df['num_var'].max()+4, 4)
                plt.hist(data = df, x = 'num_var', bins = bin_edges)

                # histogram on right, example of too-small bin size
                plt.subplot(1, 2, 2) # 1 row, 2 cols, subplot 2
                bin_edges = np.arange(0, df['num_var'].max()+1/4, 1/4)
                plt.hist(data = df, x = 'num_var', bins = bin_edges)
                ```
        
        * Scales and Transformations
            * Certain data distributions will find themselves amenable to scale transformations. The most common example of this is data that follows an approximately log-normal distribution. This is data that, in their natural units, can look highly skewed: lots of points with low values, with a very long tail of data points with large values. However, after applying a logarithmic transform to the data, the data will follow a normal distribution. (If you need a refresher on the logarithm function, check out this lesson on Khan Academy.)

            * ```python
                plt.figure(figsize = [10, 5])

                # left histogram: data plotted in natural units
                plt.subplot(1, 2, 1)
                bin_edges = np.arange(0, data.max()+100, 100)
                plt.hist(data, bins = bin_edges)
                plt.xlabel('values')

                # right histogram: data plotted after direct log transformation
                plt.subplot(1, 2, 2)
                log_data = np.log10(data) # direct data transform
                log_bin_edges = np.arange(0.8, log_data.max()+0.1, 0.1)
                plt.hist(log_data, bins = log_bin_edges)
                plt.xlabel('log(values)')
                ```
        
        * If you want to use a different transformation that's not available in xscale, then you'll have to perform some feature engineering. In cases like this, we want to be systematic by writing a function that applies both the transformation and its inverse. The inverse will be useful in cases where we specify values in their transformed units and need to get the natural units back. For the purposes of demonstration, let's say that we want to try plotting the above data on a square-root transformation. (Perhaps the numbers represent areas, and we think it makes sense to model the data on a rough estimation of radius, length, or some other 1-d dimension.) We can create a visualization on this transformed scale like this:

            * ```python
                def sqrt_trans(x, inverse = False):
                    """ transformation helper function """
                    if not inverse:
                        return np.sqrt(x)
                    else:
                        return x ** 2

                bin_edges = np.arange(0, sqrt_trans(data.max())+1, 1)
                plt.hist(data.apply(sqrt_trans), bins = bin_edges)
                tick_locs = np.arange(0, sqrt_trans(data.max())+10, 10)
                plt.xticks(tick_locs, sqrt_trans(tick_locs, inverse = True).astype(int))
                ```
    
    * For quantitative data use a Histogram
    * For qualitative data use a Bar Chart
        * Absolute vs relative frequence
    
    * Bivariable visualization
        * Visualizations of two variables
    
    * Scatterplots
        * For quantitative variables vs quantitative variables
            * ![quantvsquant](./images/quantvsquant.png)
        * We want to quantify the correlation between two variables, for that we use a correlation coefficient
            * example: Person Correlation
                * Statistic quantifying the strength of linear correlation between two numeric variables
                * The scale goes from -1 to 1  (changes on one variable correlated to changes on another variable)
                    * As close to 1, it shows a that when one variable increases, the other variable increases as well
                    * As close to -1, it shows that as one variable increases, the other variables decreases
                    * Values close to 0 indicate a weeker relationship 
            * As you play with the scale of your graph, you may find a strong correlation. That could be a positive situation to do some linear regression on those variables
                * ![correlation-linear](./images/correlation-linear.png)
                * `plt.scatter(data = df, x = 'disc_var1', y = 'disc_var2')`
        * Transparency: Each point has a different color density 
        * Jitter: Adds a small amount of random noise around each point 
        

    * Violin plots
        * For quantitative variables vs qualitative variables

    * Cluster bar charts
        * Qualitative vs qualitative 

    * ![data-types](./images/data-types.png) 

    * **Heat Maps**
        * Good for quantitative variables vs quantitative variables
        * Good for discrete variables vs. discrete variables 
        * Good alternative to transparency for a lot of data
        * Bin sizes are important
        * A heat map is a 2-d version of the histogram that can be used as an alternative to a scatterplot. Like a scatterplot, the values of the two numeric variables to be plotted are placed on the plot axes. Similar to a histogram, the plotting area is divided into a grid and the number of points in each grid rectangle is added up. Since there won't be room for bar heights, counts are indicated instead by grid cell color. A heat map can be implemented with Matplotlib's hist2d function.
        * ```python
            plt.figure(figsize = [12, 5])

            # left plot: scatterplot of discrete data with jitter and transparency
            plt.subplot(1, 2, 1)
            sb.regplot(data = df, x = 'disc_var1', y = 'disc_var2', fit_reg = False,
                    x_jitter = 0.2, y_jitter = 0.2, scatter_kws = {'alpha' : 1/3})

            # right plot: heat map with bin edges between values
            plt.subplot(1, 2, 2)
            bins_x = np.arange(0.5, 10.5+1, 1)
            bins_y = np.arange(-0.5, 10.5+1, 1)
            plt.hist2d(data = df, x = 'disc_var1', y = 'disc_var2',
                    bins = [bins_x, bins_y])
            plt.colorbar();
            ```
    * Violin Plots
        * Violin plots for quantitative variables vs qualitative variables

            * ![violin_plots](./images/violin_plots.png) 
        
        * There are a few ways of plotting the relationship between one quantitative and one qualitative variable, that demonstrate the data at different levels of abstraction. The violin plot is on the lower level of abstraction. For each level of the categorical variable, a distribution of the values on the numeric variable is plotted. The distribution is plotted as a kernel density estimate, something like a smoothed histogram. There is an extra section at the end of the previous lesson that provides more insight into kernel density estimates.

        * Seaborn's violinplot function can be used to create violin plots combined with box plots – we'll discuss box plots on the next page.

        * `sb.violinplot(data = df, x = 'cat_var', y = 'num_var')`
    
    * Box Plots
        * A box plot is another way of showing the relationship between a numeric variable and a categorical variable. Compared to the violin plot, the box plot leans more on summarization of the data, primarily just reporting a set of descriptive statistics for the numeric values on each categorical level. A box plot can be created using seaborn's boxplot function.

        * ```python
            plt.figure(figsize = [10, 5])
            base_color = sb.color_palette()[0]

            # left plot: violin plot
            plt.subplot(1, 2, 1)
            ax1 = sb.violinplot(data = df, x = 'cat_var', y = 'num_var', color = base_color)

            # right plot: box plot
            plt.subplot(1, 2, 2)
            sb.boxplot(data = df, x = 'cat_var', y = 'num_var', color = base_color)
            plt.ylim(ax1.get_ylim()) # set y-axis limits to be same as left plot
            ```
        
        * ![box_plot](./images/boxplot.png) 
    
    * Clustered Bar Charts
        * ![clustered-bar-charts](./images/clustered-bar-charts.png)

        * To depict the relationship between two categorical variables, we can extend the univariate bar chart seen in the previous lesson into a clustered bar chart. Like a standard bar chart, we still want to depict the count of data points in each group, but each group is now a combination of labels on two variables. So we want to organize the bars into an order that makes the plot easy to interpret. In a clustered bar chart, bars are organized into clusters based on levels of the first variable, and then bars are ordered consistently across the second variable within each cluster. This is easiest to see with an example, using seaborn's countplot function. To take the plot from univariate to bivariate, we add the second variable to be plotted under the "hue" argument:

        * `sb.countplot(data = df, x = 'cat_var1', hue = 'cat_var2')`
    
    * Facet Plot (Faceting)
        * ![facet_plot](./images/facet_plot.png) 

        * One general visualization technique that will be useful for you to know about to handle plots of two or more variables is faceting. In faceting, the data is divided into disjoint subsets, most often by different levels of a categorical variable. For each of these subsets of the data, the same plot type is rendered on other variables. Faceting is a way of comparing distributions or relationships across levels of additional variables, especially when there are three or more variables of interest overall. While faceting is most useful in multivariate visualization, it is still valuable to introduce the technique here in our discussion of bivariate plots.

        * For example, rather than depicting the relationship between one numeric variable and one categorical variable using a violin plot or box plot, we could use faceting to look at a histogram of the numeric variable for subsets of the data divided by categorical variable levels. Seaborn's FacetGrid class facilitates the creation of faceted plots. There are two steps involved in creating a faceted plot. First, we need to create an instance of the FacetGrid object and specify the feature we want to facet by ("cat_var" in our example). Then we use the map method on the FacetGrid object to specify the plot type and variable(s) that will be plotted in each subset (in this case, histogram on "num_var").

        * ```python
            g = sb.FacetGrid(data = df, col = 'cat_var')
            g.map(plt.hist, "num_var")
            ```
    
    * Adapted Bar Charts

        * Histograms and bar charts were introduced in the previous lesson as depicting the distribution of numeric and categorical variables, respectively, with the height (or length) of bars indicating the number of data points that fell within each bar's range of values. These plots can be adapted for use as bivariate plots by, instead of indicating count by height, indicating a mean or other statistic on a second variable.

        * For example, we could plot a numeric variable against a categorical variable by adapting a bar chart so that its bar heights indicate the mean of the numeric variable. This is the purpose of seaborn's barplot function:

        * ```python
            base_color = sb.color_palette()[0]
            sb.barplot(data = df, x = 'cat_var', y = 'num_var', color = base_color)
            ```
    
    * Line Plots

        * The line plot is a fairly common plot type that is used to plot the trend of one numeric variable against values of a second variable. In contrast to a scatterplot, where all data points are plotted, in a line plot, only one point is plotted for every unique x-value or bin of x-values (like a histogram). If there are multiple observations in an x-bin, then the y-value of the point plotted in the line plot will be a summary statistic (like mean or median) of the data in the bin. The plotted points are connected with a line that emphasizes the sequential or connected nature of the x-values.

        * If the x-variable represents time, then a line plot of the data is frequently known as a time series plot. Often, we have only one observation per time period, like in stock or currency charts. While there is a seaborn function tsplot that is intended to be used with time series data, it is fairly specialized and (as of this writing's seaborn 0.8) is slated for major changes.

### Linear Algebra

* Vector
    * Arrow
    * Inside a coordinate system (X, Y)
    * Sitting on the origin (0, 0)
        * Horizontal line: X Axis
        * Vertical line: Y Axis
        * The place X and Y intersect is called Origin 
        * ![vector_position](./images/vector_position.png)
    * The first value represents the X Axis
        * Positive values will sit on the right side
        * Negative values will sit on the left side
    * The second value represents the Y Axis
        * Positive values will sit on the top side
        * Negative values will sit on the bottom side
    * In 3D we add a new Axis called the Z Axis
        * X, Y, Z
    
    * Vector Addition
        * ![vector_addition_1](./images/vector_addition_1.png)
        * ![vector_addition_2](./images/vector_addition_2.png)
        * ![vector_addition_3](./images/vector_addition_3.png) 
    
    * Vector Multiplication
        * Scaling
            * 2, 1/2, -1.8 (Scalars)
        * ![scaling_1](./images/vector_scaling1.png)
        * ![scaling_2](./images/vector_scaling2.png)

    * Vectors- Mathematical Definition

        *  What is a Vector? The plain explanation would be that a vector is an ordered list of numbers.

        * Each element in the vector, also called component or coordinate, is a number, denoted here by a_ia 
        
        * This specific vector (in the picture above ) has nn elements and can be in the field of Real Numbers \mathbb{R}R.

        * A vector of nn real elements defines an nn dimensional vector and belongs to \mathbb{R}^nR n.

        * We use the following mathematical notation to define a vector: \vec{x} 
    
    * Vector Transpose

        * It's very important to note that in this lesson we emphasize the column vector. But vectors can also be represented at row vectors.

        * In the world of Linear Algebra we call this change a transpose. The mathematical symbol of a transpose is TT and it's used the following way:

        * ![transpose_vector](./images/transpose_vector.png)
    
    * Magnitude and Direction

        * To calculate the magnitude of a 2D vector we will use the Pythagorean Theorem.

        * In our example the magnitude will be calculated the following way:

        * ![magnitute_vector](./images/magnitute_vector.png)

        * To calculate the direction of the movement we will use an angle. We can use Degrees or Radians. In this example we will focus on Degree. (It is always possible to move Degrees to Radians and vice versa).

        * ![direction_vector](./images/direction_vector.png) 

        * To calculate \thetaθ we will use what we remember from Trigonometry!

        * ![direction_vector2](./images/direction_vector2.png) 

    * Linear Combination, Span and Basis Vectors
        * ![basis_vectors](./images/basis_vectors.png) 

        * ![basis_vectors5](./images/basis_vectors5.png)

        * ![basis_vectors2](./images/basis_vectors2.png)

        * In general terms, the simple definition of a linear combination is a multiplication of a scalar to a variable and addition of those terms.

        * ![basis_vectors3](./images/basis_vectors3.png) 

        * ![basis_vectors4](./images/basis_vectors4.png) 

        * Linearly dependent
            * Vector dont add to the span (the group of all possible vectors)
        
        * Linearly independent
            * Vector does add up to the span
        
        * ![span](./images/span.png) 

        * ![linearly_dependent](./images/linearly_dependent.png) 

        * When each vector in a set of vectors vector can not be defined as a linear combination of the other vectors, they are a set of linearly independent vectors.

        * The easiest way to know if a set of vectors is linear dependent or not, is with the use of determinants. Determinants are beyond the scope of our Linear Algebra Essentials and we will not focus on that.

        * Linear Equations

        * ![linearly_equation1](./images/linearly_equation1.png) 

        * ![linearly_equation2](./images/linearly_equation2.png) 

        * ![linearly_equation3](./images/linearly_equation3.png) 

        * ![linearly_equation4](./images/linearly_equation4.png) 

        * ![linearly_equation5](./images/linearly_equation5.png) 

    * Matrixes

        * Our next step is to understand what a Matrix is.

        * Before we dive into the video, let's cover a few necessary definitions and calculations!

        * So what is a Matrix? No, not that Matrix. The Matrix we are referring to was designed and created well before 1999.

        * A Matrix is a two dimensional array that contains the same elements as the vector.

        * A Matrix can have mm rows and nn columns.

        * If a Matrix has mm rows and nn columns is it called an mm x nn matrix.

        * Each element a_{ij}a ij in the matrix displayed in equation 11 is a numerical value displayed in row ii and column jj.

        * ![matrix](./images/matrix.png)  

        * Multiplication of a Square Matrices

            * When multiplying 2 matrices we need to consider the dimensions of each, as multiplication is not possible if the dimensions are not aligned appropriately.

            * A square matrix is a matrix that has the same number of rows and columns
        
        * ![matrix1](./images/matrix1.png)

        * ![matrix2](./images/matrix2.png)

        * ![matrix3](./images/matrix3.png)

        * ![matrix4](./images/matrix4.png)

        * ![matrix5](./images/matrix5.png)
    
    * Linear Algebra and Neural Networks

        * ![nns](./images/nns.png)
            * In practice, these lines symbolize a coefficient (a scalar) that is mathematically connecting one neuron to the next. These coefficients are called weights.

            * The "lines" connect each neuron in a specific layer to all of the neurons on the following. For example, in our example, you can see how each neuron in the hidden layer is connected to a neuron in the output one.
        
        * Since there are so many weights connecting one layer to the next, we mathematically organize those coefficients in a matrix, denoted as the weight matrix.

            * ![nns1](./images/nns1.png) 
        
        * ![nns2](./images/nns2.png) 

        * ![nns3](./images/nns3.png) 

            * The next layer you receive a sum of all inputs multipled by their respective scalars (weights). Also, we have a fixed value called a bias that will be used as part of the equation

        * Training
            * During the training phase, we take the data set (also called the training set), which includes many pairs of inputs and their corresponding targets (outputs). Our goal is to find a set of weights that would best map the inputs to the desired outputs.
        

        * Evaluation

            * In the evaluation phase, we use the network that was created in the training phase, apply our new inputs and expect to obtain the desired outputs.

        
        * The training phase will include two steps:

            * Feedforward
            * Backpropagation
        

        * We will repeat these steps as many times as we need until we decide that our system has reached the best set of weights, giving us the best possible outputs.

        * To show you how relevant Linear Algebra is here, we will focus on the feedforward process. And again, focus on the mathematical calculations. All of these new definitions (training, evaluation, feedforward, backpropagation, etc will be emphasized very soon!)
    
    * ![nns4](./images/nns4.png)  

    * ![nns5](./images/nns5.png) 

    * ![nns6](./images/nns6.png)

* Calculus

    * `dt`: Tiny change in time
    * Hard problem: Sum of many small values
    * Since `dt` tends to 0, we will endup drawing a geometric figure

    * ![calculus](./images/calculus.png) 

    * The Integral of any function will help us find the area in a graph

    * `dx`: Difference in x
    * `dA`: Difference in Area

    * ![calculus1](./images/calculus1.png) 

    * ![calculus2](./images/calculus2.png)

    * ![calculus3](./images/calculus3.png) 

    * ![calculus4](./images/calculus4.png)

    * In this back and forth between Integrals and Derivatives, where the Derivative of a function for the area under a graph gives you back the function defining the graph it self, its called the Fundamental Theorem of Calculus

    * Derivative

        * ![calculus5](./images/calculus5.png)  
            * This gives you velocity in meters per second
        
        * ![calculus6](./images/calculus6.png)  

        * ![calculus7](./images/calculus7.png)  

        * ![calculus8](./images/calculus8.png)  

        * ![calculus9](./images/calculus9.png)  

        * ![calculus10](./images/calculus10.png)  

        * ![calculus11](./images/calculus11.png)  

        * ![calculus12](./images/calculus12.png)  

        * ![calculus13](./images/calculus13.png)

        * Derivative mesures the difference between to points (stats of time)

        * In geometry, the tangent line (or simply tangent) to a plane curve at a given point is the straight line that "just touches" the curve at that point.

        * The derivative of a function of a real variable measures the sensitivity to change of the function value (output value) with respect to a change in its argument (input value). Derivatives are a fundamental tool of calculus. For example, the derivative of the position of a moving object with respect to time is the object's velocity: this measures how quickly the position of the object changes when time advances.

        * ![derivatives0](./images/derivatives0.png)

        * ![derivatives1](./images/derivatives1.png)

        * ![derivatives2](./images/derivatives2.png)

        * ![derivatives3](./images/derivatives3.png)

        * ![derivatives4](./images/derivatives4.png)

            * Lets say `dx` is 0.001, that means `dx^2` is 0.001 x 0.001 which is 0.000001.

            * It is safe to ignore values of `dx` with a power greater than 1
        
        * ![derivatives5](./images/derivatives5.png)

        * ![derivatives6](./images/derivatives6.png)

        * ![derivatives7](./images/derivatives7.png)

            * Each facet is `x^2` times 3 (X * X * X)

            * A cube has 6 facets, that leaves us with 3 relevant ones
        
        * ![derivatives8](./images/derivatives8.png)

        * ![derivatives9](./images/derivatives9.png)

            * We can ignore `dx^3` and `dx^2` since ultimately this will get devided by `dx`

        * ![derivatives10](./images/derivatives10.png)

        * ![derivatives11](./images/derivatives11.png)

            * If their still any `dx` remaining, those terms wont survive the approximation to 0
        
        * ![derivatives12](./images/derivatives12.png)

        * ![derivatives13](./images/derivatives13.png)

        * ![derivatives14](./images/derivatives14.png)

        * ![derivatives15](./images/derivatives15.png)
        
        * ![derivatives16](./images/derivatives16.png)

            * We can ignore the multiples of `dx^2`. That means that no matter the power, the "power rule" will always work since `dx` will be approximated to 0

        * ![sin-cos0](./images/sin-cos0.png)

        * ![sin-cos01](./images/sin-cos011.png)

        * ![sin-cos1](./images/sin-cos1.png)

        * ![sin-cos2](./images/sin-cos2.png)

        * ![sin-cos3](./images/sin-cos3.png)

        * ![sin-cos4](./images/sin-cos4.png)

        * ![sin-cos5](./images/sin-cos5.png)

        * ![sin-cos6](./images/sin-cos6.png)

        * ![sin-cos7](./images/sin-cos7.png)

        * ![sin-cos7](./images/sin-cos7.png)

        * ![sin-cos8](./images/sin-cos8.png)

        * The Chain Rule

        * ![chain-rule](./images/chain-rule.png)

            * You can Add them together 
            * You can Multiply them
            * You can put one inside the other (compositing)
        
        * ![chain-rule1](./images/chain-rule1.png)

            * The sum of two functions, will lead to the sum of their derivatives 
        
        * ![chain-rule2](./images/chain-rule2.png)

        * ![chain-rule3](./images/chain-rule3.png)

        * ![chain-rule4](./images/chain-rule4.png)

        * ![chain-rule5](./images/chain-rule5.png)

        * ![chain-rule6](./images/chain-rule6.png)

            * Products are a bit different 
        
        * ![chain-rule7](./images/chain-rule7.png)

            * This will lead us to the Area of this box
        

        * ![chain-rule8](./images/chain-rule8.png)

        * ![chain-rule9](./images/chain-rule9.png)

        * ![chain-rule10](./images/chain-rule10.png)

        * ![chain-rule11](./images/chain-rule11.png)

        * ![chain-rule12](./images/chain-rule12.png)

        * ![chain-rule13](./images/chain-rule13.png)

        * ![chain-rule14](./images/chain-rule14.png)

        * ![chain-rule15](./images/chain-rule15.png)

        * ![chain-rule16](./images/chain-rule16.png)

        * Derivatives of exponentials

        * ![der-expo](./images/der-expo.png)

        * ![der-expo1](./images/der-expo1.png)

        * ![der-expo2](./images/der-expo2.png)

        * ![der-expo3](./images/der-expo3.png)

        * ![der-expo3-1](./images/der-expo3-1.png)

        * ![der-expo4](./images/der-expo4.png)

        * ![der-expo5](./images/der-expo5.png)

        * ![der-expo6](./images/der-expo6.png)

        * ![der-expo7](./images/der-expo7.png)

        * ![der-expo8](./images/der-expo8.png)

        * ![der-expo9](./images/der-expo9.png)

        * Implicit Differentiation

        * ![impl-dif](./images/impl-dif.png)

        * ![impl-dif1](./images/impl-dif1.png)

        * Limit

        * ![limit](./images/limit.png)

        * ![limit1](./images/limit1.png)

        * ![limit2](./images/limit2.png)

        * ![limit3](./images/limit3.png)

        * ![limit4](./images/limit4.png)

        * ![limit5](./images/limit5.png)

    * Integral

        * Inverse of derivatives 

        * ![integral0](./images/integral0.png)   

        * ![integral](./images/integral.png)   

        * ![integral1](./images/integral1.png)   

        * ![integral2](./images/integral2.png)  

        * ![integral3](./images/integral3.png)  

        * ![integral4](./images/integral4.png)  

        * ![integral5](./images/integral5.png)  

        * ![integral6](./images/integral6.png)  

        * ![integral7](./images/integral7.png)  

        * ![integral8](./images/integral8.png)  

        * ![integral9](./images/integral9.png)  

        * ![integral10](./images/integral10.png)  

        * ![integral11](./images/integral11.png)  

        * ![integral12](./images/integral12.png)

        * ![integral13](./images/integral13.png)   
            * Fundamental theorem of calculus 

        * ![integral14](./images/integral14.png)   

        * ![integral15](./images/integral15.png)   

        * ![integral16](./images/integral16.png)   
    
    * Calculus in Neural Networks

        * ![calc-nn](./images/calc-nn.png)   

            * The weights tell you what pixel pattern this neuron is picking up on (green for positive, and red for negative), and the bias tells how high the weighted sum needs to be before the neuron gets to be meaningfully active. 
        
        * ![calc-nn](./images/calc-nn1.png)   

        * ![calc-nn](./images/calc-nn2.png)   

        * ![calc-nn](./images/calc-nn3.png)   

        * ![calc-nn](./images/calc-nn4.png)   

        * ![calc-nn](./images/calc-nn5.png)   

        * ![calc-nn](./images/calc-nn6.png)   

        * ![calc-nn](./images/calc-nn7.png)   

        * ![calc-nn](./images/calc-nn8.png)   

        * ![calc-nn](./images/calc-nn9.png)   
        
        * ![calc-nn](./images/calc-nn10.png)   

        * ![calc-nn](./images/calc-nn11.png)   

        * ![calc-nn](./images/calc-nn12.png)   

        * ![calc-nn](./images/calc-nn13.png)   

        * ![calc-nn](./images/calc-nn14.png)   

        * ![calc-nn](./images/calc-nn15.png)   

        * ![calc-nn](./images/calc-nn16.png)   

        * ![calc-nn](./images/calc-nn17.png)   

        * ![calc-nn](./images/calc-nn18.png)   

        * ![calc-nn](./images/calc-nn19.png)   
            * Gradient descent will minimize the cost function value
            * Backpropagation 
        
        * ![calc-nn](./images/calc-nn20.png) 

        * ![calc-nn](./images/calc-nn25.png)

        * ![calc-nn](./images/calc-nn27.png) 
            * Everything that is blue is a positive weight 
            * Everything that is red is a negative weight
            * We need to make the blue weights stronger, and the red weaker

        * ![calc-nn](./images/calc-nn21.png) 

        * ![calc-nn](./images/calc-nn22.png) 

        * ![calc-nn](./images/calc-nn23.png) 

        * ![calc-nn](./images/calc-nn24.png) 

        * ![calc-nn](./images/calc-nn26.png) 

            * This average is the gradient descent

            * Stochastic gradiant descent 
                * Calculate the gradiant per batch size to minimize computing

        * ![calc-nn](./images/calc-nn28.png) 

        * ![calc-nn](./images/calc-nn29.png)  

        * ![calc-nn](./images/calc-nn30.png) 

        * ![calc-nn](./images/calc-nn31.png) 

        * ![calc-nn](./images/calc-nn32.png) 

        * ![calc-nn](./images/calc-nn33.png) 

        *  ![calc-nn](./images/calc-nn34.png) 

        *  ![calc-nn](./images/calc-nn35.png) 

        *  ![calc-nn](./images/calc-nn36.png) 

        *  ![calc-nn](./images/calc-nn37.png) 

        *  ![calc-nn](./images/calc-nn38.png) 

        *  ![calc-nn](./images/calc-nn39.png) 

        *  ![calc-nn](./images/calc-nn40.png) 

    * Neural Networks

        *  ![nn](./images/nn.png) 

        *  ![nn1](./images/nn1.png) 

        *  ![nn2](./images/nn2.png) 

        *  ![nn3](./images/nn3.png)

        *  ![nn8](./images/nn8.png)

        *  ![nn9](./images/nn9.png)

        *  ![nn10](./images/nn10.png) 
        
        * `AND` Neural Network

        * ```python
            import pandas as pd

            # TODO: Set weight1, weight2, and bias
            weight1 = 1
            weight2 = 1
            bias = -2


            # DON'T CHANGE ANYTHING BELOW
            # Inputs and outputs
            test_inputs = [(0, 0), (0, 1), (1, 0), (1, 1)]
            correct_outputs = [False, False, False, True]
            outputs = []

            # Generate and check output
            for test_input, correct_output in zip(test_inputs, correct_outputs):
                linear_combination = weight1 * test_input[0] + weight2 * test_input[1] + bias
                output = int(linear_combination >= 0)
                is_correct_string = 'Yes' if output == correct_output else 'No'
                outputs.append([test_input[0], test_input[1], linear_combination, output, is_correct_string])

            # Print output
            num_wrong = len([output[4] for output in outputs if output[4] == 'No'])
            output_frame = pd.DataFrame(outputs, columns=['Input 1', '  Input 2', '  Linear Combination', '  Activation Output', '  Is Correct'])
            if not num_wrong:
                print('Nice!  You got it all correct.\n')
            else:
                print('You got {} wrong.  Keep trying!\n'.format(num_wrong))
            print(output_frame.to_string(index=False))
            ```

        *  ![nn12](./images/nn11.png)  
        
        * `OR` Neural Network

        *  ```python
            # TODO: Set weight1, weight2, and bias
            weight1 = 1
            weight2 = 1
            bias = -1

            # DON'T CHANGE ANYTHING BELOW
            # Inputs and outputs
            test_inputs = [(0, 0), (0, 1), (1, 0), (1, 1)]
            correct_outputs = [False, False, False, True]
            outputs = []

            # Generate and check output
            for test_input, correct_output in zip(test_inputs, correct_outputs):
                linear_combination = weight1 * test_input[0] + weight2 * test_input[1] + bias
                output = int(linear_combination >= 0)
                is_correct_string = 'Yes' if output == correct_output else 'No'
                outputs.append([test_input[0], test_input[1], linear_combination, output, is_correct_string])

            # Print output
            num_wrong = len([output[4] for output in outputs if output[4] == 'No'])
            output_frame = pd.DataFrame(outputs, columns=['Input 1', '  Input 2', '  Linear Combination', '  Activation Output', '  Is Correct'])
            if not num_wrong:
                print('Nice!  You got it all correct.\n')
            else:
                print('You got {} wrong.  Keep trying!\n'.format(num_wrong))
            print(output_frame.to_string(index=False))
            ```
        
        *  ![nn12](./images/nn12.png) 

        * `NOT` Neural Network

            * Consider only input 2

        * ```python
            import pandas as pd

            # TODO: Set weight1, weight2, and bias
            weight1 = 0
            weight2 = -2
            bias = 1

            # DON'T CHANGE ANYTHING BELOW
            # Inputs and outputs
            test_inputs = [(0, 0), (0, 1), (1, 0), (1, 1)]
            correct_outputs = [True, False, True, False]
            outputs = []

            # Generate and check output
            for test_input, correct_output in zip(test_inputs, correct_outputs):
                linear_combination = weight1 * test_input[0] + weight2 * test_input[1] + bias
                output = int(linear_combination >= 0)
                is_correct_string = 'Yes' 
                if output == correct_output else 'No'
                outputs.append([test_input[0], test_input[1], linear_combination, output, is_correct_string])

            # Print output
            num_wrong = len([output[4] for output in outputs if output[4] == 'No'])
            output_frame = pd.DataFrame(outputs, columns=['Input 1', '  Input 2', '  Linear Combination', '  Activation Output', '  Is Correct'])
            if not num_wrong:
                print('Nice!  You got it all correct.\n')
            else:
                print('You got {} wrong.  Keep trying!\n'.format(num_wrong))
            print(output_frame.to_string(index=False))
            ```
        
        *  ![nn13](./images/nn13.png) 

        *  ![nn14](./images/nn14.png) 

            * Multiply those numbers by a **learning rate**

            * Negative point in the positive area, so we subtract the function

        *  ![nn15](./images/nn15.png) 

        *  ![nn16](./images/nn16.png) 
            * We obtain a new equation to approximate the value to the line

        *  ![nn17](./images/nn17.png) 
            * Positive point in the negative area, so we add to the function
        
        *  ![nn18](./images/nn18.png) 


            * ```python
                import numpy as np
                # Setting the random seed, feel free to change it and see different solutions.
                np.random.seed(42)

                def stepFunction(t):
                    if t >= 0:
                        return 1
                    return 0

                def prediction(X, W, b):
                    return stepFunction((np.matmul(X,W)+b)[0])

                # TODO: Fill in the code below to implement the perceptron trick.
                # The function should receive as inputs the data X, the labels y,
                # the weights W (as an array), and the bias b,
                # update the weights and bias W, b, according to the perceptron algorithm,
                # and return W and b.
                def perceptronStep(X, y, W, b, learn_rate = 0.01):
                    for i in range(len(X)):
                        y_hat = prediction(X[i],W,b)
                        if y[i]-y_hat == 1:
                            W[0] += X[i][0]*learn_rate
                            W[1] += X[i][1]*learn_rate
                            b += learn_rate
                        elif y[i]-y_hat == -1:
                            W[0] -= X[i][0]*learn_rate
                            W[1] -= X[i][1]*learn_rate
                            b -= learn_rate
                    return W, b
                    
                # This function runs the perceptron algorithm repeatedly on the dataset,
                # and returns a few of the boundary lines obtained in the iterations,
                # for plotting purposes.
                # Feel free to play with the learning rate and the num_epochs,
                # and see your results plotted below.
                def trainPerceptronAlgorithm(X, y, learn_rate = 0.01, num_epochs = 25):
                    x_min, x_max = min(X.T[0]), max(X.T[0])
                    y_min, y_max = min(X.T[1]), max(X.T[1])
                    W = np.array(np.random.rand(2,1))
                    b = np.random.rand(1)[0] + x_max
                    # These are the solution lines that get plotted below.
                    boundary_lines = []
                    for i in range(num_epochs):
                        # In each epoch, we apply the perceptron step.
                        W, b = perceptronStep(X, y, W, b, learn_rate)
                        boundary_lines.append((-W[0]/W[1], -b/W[1]))
                    return boundary_lines

                ```
            
            *  ![nn19](./images/nn19.png) 

        *  ![nn20](./images/nn20.png) 

            * A linear function won't work, we need to draw a line. Perceptron won't work, we need to adapt it

            * Lets create an **Error Function**
        
        *  ![nn21](./images/nn21.png) 

        *  ![nn22](./images/nn22.png) 

        *  ![nn23](./images/nn23.png) 

            * We will use Gradiant Descent to find our local minimal, but we gotta remember that the erro function values must be continuos for it to work. Otherwise, Gradiant Descent will get stuck without small variations.

            * Differentiable function of one real variable is a function whose derivative exists at each point in its domain.

        
        * ![nn24](./images/nn24.png) 

        * ![nn25](./images/nn25.png) 

        * ![nn26](./images/nn26.png) 

        * ![nn27](./images/nn27.png) 

        * ![nn28](./images/nn28.png) 

        * ![nn29](./images/nn29.png) 

            * The number `e` is a mathematical constant that is the base of the natural logarithm: the unique number whose natural logarithm is equal to one. It is approximately equal to 2.71828,[1] and is the limit of (1 + 1/n)n as n approaches infinity, an expression that arises in the study of compound interest. It can also be calculated as the sum of the infinite series[2]
        
        * ![nn30](./images/nn30.png) 

        * We'll learn about the softmax function, which is the equivalent of the sigmoid activation function, but when the problem has 3 or more classes.

        * ![nn31](./images/nn31.png) 

        * ![nn32](./images/nn32.png) 

        * ![nn33](./images/nn33.png) 

            * Euler constant = 2.718
            * `2.71^2 / (2.71^2 + 2.71^1 + 2.71^0)` = `0.66437792312`
            * `2.71^1 / (2.71^2 + 2.71^1 + 2.71^0)` = `0.24515790521`
            * `2.71^0 / (2.71^2 + 2.71^1 + 2.71^0)` = `0.09046417166`

            * We are using the `exp` function, because numbers cant be negative

            * This is called the `softmax` function

            * ```python
                import numpy as np

                def softmax(L):
                    expL = np.exp(L)
                    sumExpL = sum(expL)
                    result = []
                    for i in expL:
                        result.append(i*1.0/sumExpL)
                    return result
                    
                    # Note: The function np.divide can also be used here, as follows:
                    # def softmax(L):
                    #     expL = np.exp(L)
                    #     return np.divide (expL, expL.sum())
                ```
            
        * ![nn34](./images/nn34.png) 

        * Maximum Likelihood

            * The probability the points were classified correctly 

        * ![nn35](./images/nn35.png) 

        * ![nn36](./images/nn36.png) 

        * ![nn37](./images/nn37.png) 

        * ![nn38](./images/nn38.png) 

        * In this lesson and quiz, we will learn how to maximize a probability, using some math. Nothing more than high school math, so get ready for a trip down memory lane!

        * ![nn39](./images/nn39.png) 

        * ![nn40](./images/nn40.png) 

        * ![nn41](./images/nn41.png) 

        * We will take `log` base `e` instead of base `10`

        * The `log` of a number between `0` and `1` is always a negative number, since log of 1 is 0

        * So it makes sense to think of the negative of `log` of the probabilities, that way we have positive numbers 

        * The sum of those negative logarithms of the probabilities is called **Cross-entropy**

        * ![nn42](./images/nn42.png) 

        * A **bad model** will give us a high Cross Entropy (log-loss), and a **good model** will give us a low Cross Entropy

        * ![nn43](./images/nn43.png)  

            * The points that are misclassified have large values

            * Points that are correctly classified will have values close to 1 (small values)
        
        * Minimizing the Cross Entropy is our objective

        * So we're getting somewhere, there's definitely a connection between probabilities and error functions, and it's called Cross-Entropy. This concept is tremendously popular in many fields, including Machine Learning. Let's dive more into the formula, and actually code it!

        * ![nn44](./images/nn44.png)  

        * ![nn45](./images/nn45.png)  

        * ![nn46](./images/nn46.png)  

            * The Cross Entropy for 1 (if present on box) is low, that means its a good model for for that. However, if we switch that to 0, the model is pretty bad

        * Now, time to shine! Let's code the formula for cross-entropy in Python. As in the video, Y in the quiz is for the category, and P is the probability.

        * ```python
            import numpy as np

            def cross_entropy(Y, P):
                Y = np.float_(Y)
                P = np.float_(P)
                return -np.sum(Y * np.log(P) + (1 - Y) * np.log(1 - P))
            ```
        
        * Now, time to shine! Let's code the formula for cross-entropy in Python. As in the video, Y in the quiz is for the category, and P is the probability.

        * ![nn47](./images/nn47.png)  

        * ![nn48](./images/nn48.png)  

        * ![nn49](./images/nn49.png)  

        * ![nn50](./images/nn50.png)  

        * Logistic Regression

            * Now, we're finally ready for one of the most popular and useful algorithms in Machine Learning, and the building block of all that constitutes Deep Learning. The Logistic Regression Algorithm. And it basically goes like this:

                * Take your data

                * Pick a random model

                * Calculate the error

                * Minimize the error, and obtain a better model

                * Enjoy!
        
        * Calculating the Error Function

            * ![nn51](./images/nn51.png)  

            * ![nn52](./images/nn52.png)  

            * ![nn53](./images/nn53.png)  

            * ![nn54](./images/nn54.png)  

                * We want the average `1/m` of all points
            
            * ![nn55](./images/nn55.png)  

            * ![nn56](./images/nn56.png)  

        * Minimizing the error function

            * ![nn57](./images/nn57.png)  

            * Gradiant Descent

            * ![nn58](./images/nn58.png)  

            * ![nn59](./images/nn59.png)  

            * ![nn60](./images/nn60.png)  

                * The gradient   of the error function is the vector formed by the partial derivatives of the error function with respect to the weights and bias.

                * We take a step on the direction of the negative of the gradient

                * We also introduce a small learning rate called alpha (example: 0.1)

            * ![nn61](./images/nn61.png)  

                * We will multiple the gradient by the learning rate (alpha)
            
            * ![nn62](./images/nn62.png)  

                * The new weight (w1') will be the current weigth value (w1) minus the alpha (learning rate) multiplied by the partial derivative of the error with respect to the weigth (w1).
            
            * ![nn63](./images/nn63.png)  

            * ![nn64](./images/nn64.png)  

                * The bias will become the current bias minus alpha multiplied by the partial derivative of the error with respect to the bias.
            
            * ![nn65](./images/nn65.png)  
        
        * Gradient Calculation

            * In the last few videos, we learned that in order to minimize the error function, we need to take some derivatives. So let's get our hands dirty and actually compute the derivative of the error function. The first thing to notice is that the sigmoid function has a really nice derivative. Namely,

            * ![nn66](./images/nn66.png)  

            * ![nn67](./images/nn67.png) 

                * Calculate the derivative of the prediction 

            * ![nn68](./images/nn68.png) 

                * Calculate the derivative of the Error 

            * ![nn69](./images/nn69.png) 

                * If you think about it, this is fascinating. The gradient is actually a scalar times the coordinates of the point! And what is the scalar? Nothing less than a multiple of the difference between the label and the prediction. What significance does this have?
            
            * ![nn70](./images/nn70.png) 

            * So, a small gradient means we'll change our coordinates by a little bit, and a large gradient means we'll change our coordinates by a lot.

            * If this sounds anything like the perceptron algorithm, this is no coincidence! We'll see it in a bit.

        * Gradient Descent Step

            * ![nn71](./images/nn71.png) 

            * ![nn72](./images/nn72.png)

            * ![nn73](./images/nn73.png)

            * ![nn74](./images/nn74.png)

            * ![nn75](./images/nn75.png)

    * Check `GradientDescent.ipynb` for more

        * ```python
            # Implement the following functions

            # Activation (sigmoid) function
            def sigmoid(x):
                return 1 / (1 + np.exp(-x))

            # Output (prediction) formula
            def output_formula(features, weights, bias):
                # np.dot is the Dot product of two arrays. Specifically,. If both a and b are 1-D arrays, it is inner product of vectors (without complex conjugation).
                # two weights and two features
                return sigmoid(np.dot(features, weights) + bias)

            # Error (log-loss) formula
            def error_formula(y, output):
                return - y*np.log(output) - (1 - y) * np.log(1-output)

            # Gradient descent step
            def update_weights(x, y, weights, bias, learnrate):
                output = output_formula(x, weights, bias)
                d_error = y - output
                weights += learnrate * d_error * x
                bias += learnrate * d_error
                return weights, bias
            
            np.random.seed(44)

            epochs = 100
            learnrate = 0.01

            def train(features, targets, epochs, learnrate, graph_lines=False):
                
                errors = []
                n_records, n_features = features.shape
                last_loss = None
                # two weights and two features
                weights = np.random.normal(scale=1 / n_features**.5, size=n_features)
                bias = 0
                for e in range(epochs):
                    del_w = np.zeros(weights.shape)
                    for x, y in zip(features, targets):
                        output = output_formula(x, weights, bias)
                        error = error_formula(y, output)
                        weights, bias = update_weights(x, y, weights, bias, learnrate)
                    
                    # Printing out the log-loss error on the training set
                    out = output_formula(features, weights, bias)
                    loss = np.mean(error_formula(targets, out))
                    errors.append(loss)
                    if e % (epochs / 10) == 0:
                        print("\n========== Epoch", e,"==========")
                        if last_loss and last_loss < loss:
                            print("Train loss: ", loss, "  WARNING - Loss Increasing")
                        else:
                            print("Train loss: ", loss)
                        last_loss = loss
                        predictions = out > 0.5
                        accuracy = np.mean(predictions == targets)
                        print("Accuracy: ", accuracy)
                    if graph_lines and e % (epochs / 100) == 0:
                        display(-weights[0]/weights[1], -bias/weights[1])
                        

                # Plotting the solution boundary
                plt.title("Solution boundary")
                display(-weights[0]/weights[1], -bias/weights[1], 'black')

                # Plotting the data
                plot_points(features, targets)
                plt.show()

                # Plotting the error
                plt.title("Error Plot")
                plt.xlabel('Number of epochs')
                plt.ylabel('Error')
                plt.plot(errors)
                plt.show()

            ```
        
    * ![nn76](./images/nn76.png)

        * In the Gradient Descent algorithm we always changes the weigths. In the Perceptron Algorithm only the misclassified points changes the weigths

        * ![nn77](./images/nn77.png)

        * For correctly classied points, Gradient Descent is telling the line to move away. 
    
    * ![nn78](./images/nn78a.png)

        * We will check next how to deal with non linear models.
    
    * ![nn79](./images/nn79a.png)

    * ![nn80](./images/nn80a.png) 

        * We will create a probability function to cover that
        
    * Neural Networks (Multi Layer Perceptron)

    * ![nn78](./images/nn78.png)

        * We will combine two linear models into a non-linear model

    * ![nn79](./images/nn79.png)

    * ![nn80](./images/nn80.png) 

        * We will sum the two probabilities and run `sigmoid` on top of it to normalize the number (from 0 to 1)
    
    * ![nn81](./images/nn81.png)

    * ![nn82](./images/nn82.png) 

        * Since we are "adding" two linear models, we could add weigths for each of them. That tells us that one model is more relevant than the other, creating a new combination

    * ![nn83](./images/nn83.png) 

        * We have a Perceptron for the first linear model, and another one for the second one.

        * As we combine the two and add weights for each, we create our first Neural Network.

        * ![nn84](./images/nn84.png)  
    
    * ![nn85](./images/nn85.png) 

        * The weights on the left tell us what equations the linears model have. On the other hand, the weigths on the right tell us what the linear combination is of the two models to obtain the curved non linear model on the right.
    
    * ![nn86](./images/nn86.png) 

    * ![nn87](./images/nn87.png)

        * We can write this using the notations with the **bias** inside the node, or out side it.

    * Multiple layers

        * Now, not all neural networks look like the one above. They can be way more complicated! In particular, we can do the following things:

            * Add more nodes to the input, hidden, and output layers.

            * Add more layers.

        * The first layer is called the input layer

        * ![nn88](./images/nn88.png)

        * The next layer is the **linear layer** which is the set of linear models created from this first input layer

        * ![nn89](./images/nn89.png)

        * The final layer is called output layer, where the linear models get combined to obtain a non-linear model

        * ![nn90](./images/nn90.png)

        * ![nn91](./images/nn91.png)

        * ![nn92](./images/nn92.png)

            * With 3 inputs now we are reaching 3D space, and as we add input units we increase dimensions 

        * ![nn93](./images/nn93.png)

        * ![nn94](./images/nn94.png)

            * We can have many hidden layer, having then many linear combinations

        * ![nn95](./images/nn95.png)
    
    * Multi-Class Classification

        * And here we elaborate a bit more into what can be done if our neural network needs to model data with more than one output.

        * ![nn96](./images/nn96.png)
    
    * Feedforward

        * Feedforward is the process neural networks use to turn the input into an output. Let's study it more carefully, before we dive into how to train the networks.

        * ![nn97](./images/nn97.png)

        * ![nn98](./images/nn98.png)

        * ![nn99](./images/nn99.png)

        * ![nn100](./images/nn100.png)
    
    * Error Function

        * Just as before, neural networks will produce an error function, which at the end, is what we'll be minimizing. The following video shows the error function for a neural network.

        * ![nn101](./images/nn101.png) 
    
    * Backpropagation

        * Now, we're ready to get our hands into training a neural network. For this, we'll use the method known as backpropagation. In a nutshell, backpropagation will consist of:

            * Doing a feedforward operation.

            * Comparing the output of the model with the desired output.

            * Calculating the error.

            * Running the feedforward operation backwards (backpropagation) to spread the error to each of the weights.

            * Use this to update the weights, and get a better model.

            * Continue this until we have a model that is good.
        
        * Sounds more complicated than what it actually is. Let's take a look in the next few videos. The first video will show us a conceptual interpretation of what backpropagation is.

        * ![nn102](./images/nn102.png) 

        * ![nn103](./images/nn103.png) 

        * ![nn104](./images/nn104.png) 

            * In this case we know that the top model is the one doing the miscalssification. 

            * That means that we want to reduce the weight coming from the top model and increase the weight coming from the bottom model.
        
        * ![nn105](./images/nn105.png) 

        * ![nn106](./images/nn106.png) 

        * ![nn107](./images/nn107.png) 

    * Backpropagation Math

        * And the next few videos will go deeper into the math. Feel free to tune out, since this part gets handled by Keras pretty well. If you'd like to go start training networks right away, go to the next section. But if you enjoy calculating lots of derivatives, let's dive in!

        * ![nn108](./images/nn108.png) 

        * ![nn109](./images/nn109.png) 

        * ![nn110](./images/nn110.png) 

    * Chain Rule

        * We'll need to recall the chain rule to help us calculate derivatives.

        * ![nn111](./images/nn111.png) 

        * ![nn112](./images/nn112.png) 

        * ![nn113](./images/nn113.png) 

        * ![nn114](./images/nn114.png) 

        * ![nn115](./images/nn115.png) 

        * ![nn116](./images/nn116.png) 

        * ![nn117](./images/nn117.png) 

        * ```python
            # Activation (sigmoid) function
            def sigmoid(x):
                return 1 / (1 + np.exp(-x))
            def sigmoid_prime(x):
                return sigmoid(x) * (1-sigmoid(x))
            def error_formula(y, output):
                return - y*np.log(output) - (1 - y) * np.log(1-output)
            def error_term_formula(y, output):
                return (y-output) * output * (1 - output)

            # Neural Network hyperparameters
            epochs = 1000
            learnrate = 0.5

            # Training function
            def train_nn(features, targets, epochs, learnrate):
                
                # Use to same seed to make debugging easier
                np.random.seed(42)

                n_records, n_features = features.shape
                last_loss = None

                # Initialize weights
                weights = np.random.normal(scale=1 / n_features**.5, size=n_features)

                for e in range(epochs):
                    del_w = np.zeros(weights.shape)
                    for x, y in zip(features.values, targets):
                        # Loop through all records, x is the input, y is the target

                        # Activation of the output unit
                        #   Notice we multiply the inputs and the weights here 
                        #   rather than storing h as a separate variable 
                        output = sigmoid(np.dot(x, weights))

                        # The error, the target minus the network output
                        error = error_formula(y, output)

                        # The error term
                        #   Notice we calulate f'(h) here instead of defining a separate
                        #   sigmoid_prime function. This just makes it faster because we
                        #   can re-use the result of the sigmoid function stored in
                        #   the output variable
                        error_term = error_term_formula(y, output)

                        # The gradient descent step, the error times the gradient times the inputs
                        del_w += error_term * x

                    # Update the weights here. The learning rate times the 
                    # change in weights, divided by the number of records to average
                    weights += learnrate * del_w / n_records

                    # Printing out the mean square error on the training set
                    if e % (epochs / 10) == 0:
                        out = sigmoid(np.dot(features, weights))
                        loss = np.mean((out - targets) ** 2)
                        print("Epoch:", e)
                        if last_loss and last_loss < loss:
                            print("Train loss: ", loss, "  WARNING - Loss Increasing")
                        else:
                            print("Train loss: ", loss)
                        last_loss = loss
                        print("=========")
                print("Finished training!")
                return weights

            weights = train_nn(features, targets, epochs, learnrate)
            ```

    * Cross Entropy (Log-Loss) vs Mean Squared Error

        * In the previous section, Luis taught you about the log-loss function. There are many other error functions used for neural networks. Let me teach you another one, called the mean squared error. As the name says, this one is the mean of the squares of the differences between the predictions and the labels. In the following section I'll go over it in detail, then we'll get to implement backpropagation with it on the same student admissions dataset.

        * And as a bonus, we'll be implementing this in a very effective way using matrix multiplication with NumPy!

    * Gradient Descent with Squared Errors

        * ![nn118](./images/nn118.png)

        * ![nn119](./images/nn119.png)

            * Intuitively, square loss is bad for classification because the model needs the targets to hit specific values (0/1) rather than having larger values correspond to higher probabilities. This makes it really hard for the model to learn to express high and low confidence, and lots of times the model will struggle to keep values on 0/1 instead of doing something useful.

            * Cross-entropy (or softmax loss, but cross-entropy works better) is a better measure than MSE for classification, because the decision boundary in a classification task is large (in comparison with regression). MSE doesn't punish misclassifications enough, but is the right loss for regression, where the distance between two values that can be predicted is small.
        
        * ![nn120](./images/nn120.png)

        * ![nn121](./images/nn121.png)

        * ![nn122](./images/nn122.png)

        * ![nn123](./images/nn123.png)

            * In the case of neural nets, local minima are not necessarily that much of a problem. Some of the local minima are due to the fact that you can get a functionally identical model by permuting the hidden layer units, or negating the inputs and output weights of the network etc. Also if the local minima is only slightly non-optimal, then the difference in performance will be minimal and so it won't really matter. Lastly, and this is an important point, the key problem in fitting a neural network is over-fitting, so aggressively searching for the global minima of the cost function is likely to result in overfitting and a model that performs poorly.

            * Adding a regularisation term, e.g. weight decay, can help to smooth out the cost function, which can reduce the problem of local minima a little, and is something I would recommend anyway as a means of avoiding overfitting.

        * ![nn124](./images/nn124.png)

            * Sum of many predictions (many data points)
        
        * ![nn125](./images/nn125.png)

            * We add 1/2 to clean the math
        
        * ![nn126](./images/nn126.png)

        * ![nn127](./images/nn127.png)

        * ![nn128](./images/nn128.png)

        * ![nn129](./images/nn129.png)

        * ![nn130](./images/nn130.png)

        * ![nn131](./images/nn131.png)

        * ![nn132](./images/nn132.png)

        * ![nn133](./images/nn133.png)

        * ![nn134](./images/nn134.png)

        * ```python
            import numpy as np

            def sigmoid(x):
                """
                Calculate sigmoid
                """
                return 1/(1+np.exp(-x))

            def sigmoid_prime(x):
                """
                # Derivative of the sigmoid function
                """
                return sigmoid(x) * (1 - sigmoid(x))

            learnrate = 0.5
            x = np.array([1, 2, 3, 4])
            y = np.array(0.5)

            # Initial weights
            w = np.array([0.5, -0.5, 0.3, 0.1])

            ### Calculate one gradient descent step for each weight
            ### Note: Some steps have been consolidated, so there are
            ###       fewer variable names than in the above sample code

            # TODO: Calculate the node's linear combination of inputs and weights
            h = np.dot(x, w)

            # TODO: Calculate output of neural network
            nn_output = sigmoid(h)

            # TODO: Calculate error of neural network
            error = y - nn_output

            # TODO: Calculate the error term
            #       Remember, this requires the output gradient, which we haven't
            #       specifically added a variable for.
            error_term = error * sigmoid_prime(h)
            # Note: The sigmoid_prime function calculates sigmoid(h) twice,
            #       but you've already calculated it once. You can make this
            #       code more efficient by calculating the derivative directly
            #       rather than calling sigmoid_prime, like this:
            # error_term = error * nn_output * (1 - nn_output)

            # TODO: Calculate change in weights
            del_w = learnrate * error_term * x

            print('Neural Network output:')
            print(nn_output)
            print('Amount of Error:')
            print(error)
            print('Change in Weights:')
            print(del_w)
            ```
    
    * You've seen how to implement that for a single update, but how do we translate that code to calculate many weight updates so our network will learn?

        * ![nn135](./images/nn135.png)

        * ![nn136](./images/nn136.png)

        * ![nn137](./images/nn137.png)

        * ```python
            import numpy as np
            from data_prep import features, targets, features_test, targets_test


            def sigmoid(x):
                """
                Calculate sigmoid
                """
                return 1 / (1 + np.exp(-x))

            # TODO: We haven't provided the sigmoid_prime function like we did in
            #       the previous lesson to encourage you to come up with a more
            #       efficient solution. If you need a hint, check out the comments
            #       in solution.py from the previous lecture.

            # Use to same seed to make debugging easier
            np.random.seed(42)

            n_records, n_features = features.shape
            last_loss = None

            # Initialize weights
            weights = np.random.normal(scale=1 / n_features**.5, size=n_features)

            # Neural Network hyperparameters
            epochs = 1000
            learnrate = 0.5

            for e in range(epochs):
                del_w = np.zeros(weights.shape)
                for x, y in zip(features.values, targets):
                    # Loop through all records, x is the input, y is the target

                    # Activation of the output unit
                    #   Notice we multiply the inputs and the weights here 
                    #   rather than storing h as a separate variable 
                    output = sigmoid(np.dot(x, weights))

                    # The error, the target minus the network output
                    error = y - output

                    # The error term
                    #   Notice we calulate f'(h) here instead of defining a separate
                    #   sigmoid_prime function. This just makes it faster because we
                    #   can re-use the result of the sigmoid function stored in
                    #   the output variable
                    error_term = error * output * (1 - output)

                    # The gradient descent step, the error times the gradient times the inputs
                    del_w += error_term * x

                # Update the weights here. The learning rate times the 
                # change in weights, divided by the number of records to average
                weights += learnrate * del_w / n_records

                # Printing out the mean square error on the training set
                if e % (epochs / 10) == 0:
                    out = sigmoid(np.dot(features, weights))
                    loss = np.mean((out - targets) ** 2)
                    if last_loss and last_loss < loss:
                        print("Train loss: ", loss, "  WARNING - Loss Increasing")
                    else:
                        print("Train loss: ", loss)
                    last_loss = loss


            # Calculate accuracy on test data
            tes_out = sigmoid(np.dot(features_test, weights))
            predictions = tes_out > 0.5
            accuracy = np.mean(predictions == targets_test)
            print("Prediction accuracy: {:.3f}".format(accuracy))
            ```
    * Backpropagation

        * ![backprop](./images/backprop.png)
            * We will revert the neural network and propagate the error backwards.

        * ![backprop1](./images/backprop1.png)

        * Now we've come to the problem of how to make a multilayer neural network learn. Before, we saw how to update weights with gradient descent. The backpropagation algorithm is just an extension of that, using the chain rule to find the error with the respect to the weights connecting the input layer to the hidden layer (for a two layer network).

        * To update the weights to hidden layers using gradient descent, you need to know how much error each of the hidden units contributed to the final output. **Since the output of a layer is determined by the weights between layers, the error resulting from units is scaled by the weights going forward through the network.** Since we know the error at the output, we can use the weights to work backwards to hidden layers.

        * ![backprop2](./images/backprop2.png)

        * ![backprop3](./images/backprop3.png)

        * ![backprop4](./images/backprop4.png)

        * ![backprop5](./images/backprop5.png)

        * ![backprop6](./images/backprop6.png)

        * ![backprop7](./images/backprop7.png)

        * ![backprop8](./images/backprop8.png)

        * ![backprop9](./images/backprop9.png)

            * You can see that if you have a lot of layers, using a sigmoid activation function will quickly reduce the weight steps to tiny values in layers near the input. This is known as the **vanishing gradient problem**.
        
        * ```python
            import numpy as np

            def sigmoid(x):
                """
                Calculate sigmoid
                """
                return 1 / (1 + np.exp(-x))


            x = np.array([0.5, 0.1, -0.2])
            target = 0.6
            learnrate = 0.5

            weights_input_hidden = np.array([[0.5, -0.6], 
            [0.1, -0.2],                     [0.1, 0.7]])

            weights_hidden_output = np.array([0.1, -0.3])

            ## Forward pass
            hidden_layer_input = np.dot(x, weights_input_hidden)
            hidden_layer_output = sigmoid(hidden_layer_input)

            output_layer_in = np.dot(hidden_layer_output, weights_hidden_output)
            output = sigmoid(output_layer_in)

            ## Backwards pass
            ## TODO: Calculate output error
            error = target - output

            # TODO: Calculate error term for output layer
            output_error_term = error * output * (1 - output)

            # TODO: Calculate error term for hidden layer
            hidden_error_term = np.dot(output_error_term, weights_hidden_output) * \
                                hidden_layer_output * (1 - hidden_layer_output)

            # TODO: Calculate change in weights for hidden layer to output layer
            delta_w_h_o = learnrate * output_error_term * hidden_layer_output

            # TODO: Calculate change in weights for input layer to hidden layer
            delta_w_i_h = learnrate * hidden_error_term * x[:, None]

            print('Change in weights for hidden layer to output layer:')
            print(delta_w_h_o)
            print('Change in weights for input layer to hidden layer:')
            print(delta_w_i_h)
            ```

        * ![backprop10](./images/backprop10.png)

        * ```python
            import numpy as np
        * ```python
            from data_prep import features, targets, features_test, targets_test

            np.random.seed(21)

            def sigmoid(x):
                """
                Calculate sigmoid
                """
                return 1 / (1 + np.exp(-x))


            # Hyperparameters
            n_hidden = 2  # number of hidden units
            epochs = 900
            learnrate = 0.005

            n_records, n_features = features.shape
            last_loss = None
            # Initialize weights
            weights_input_hidden = np.random.normal(scale=1 / n_features ** .5,
                                                    size=(n_features, n_hidden))
            weights_hidden_output = np.random.normal(scale=1 / n_features ** .5,
                                                    size=n_hidden)

            for e in range(epochs):
                del_w_input_hidden = np.zeros(weights_input_hidden.shape)
                del_w_hidden_output = np.zeros(weights_hidden_output.shape)
                for x, y in zip(features.values, targets):
                    ## Forward pass ##
                    # TODO: Calculate the output
                    hidden_input = np.dot(x, weights_input_hidden)
                    hidden_output = sigmoid(hidden_input)

                    output = sigmoid(np.dot(hidden_output,
                                            weights_hidden_output))

                    ## Backward pass ##
                    # TODO: Calculate the network's prediction error
                    error = y - output

                    # TODO: Calculate error term for the output unit
                    output_error_term = error * output * (1 - output)

                    ## propagate errors to hidden layer

                    # TODO: Calculate the hidden layer's contribution to the error
                    hidden_error = np.dot(output_error_term, weights_hidden_output)

                    # TODO: Calculate the error term for the hidden layer
                    hidden_error_term = hidden_error * hidden_output * (1 - hidden_output)

                    # TODO: Update the change in weights
                    del_w_hidden_output += output_error_term * hidden_output
                    del_w_input_hidden += hidden_error_term * x[:, None]

                # TODO: Update weights
                weights_input_hidden += learnrate * del_w_input_hidden / n_records
                weights_hidden_output += learnrate * del_w_hidden_output / n_records

                # Printing out the mean square error on the training set
                if e % (epochs / 10) == 0:
                    hidden_output = sigmoid(np.dot(x, weights_input_hidden))
                    out = sigmoid(np.dot(hidden_output,
                                        weights_hidden_output))
                    loss = np.mean((out - targets) ** 2)

                    if last_loss and last_loss < loss:
                        print("Train loss: ", loss, "  WARNING - Loss Increasing")
                    else:
                        print("Train loss: ", loss)
                    last_loss = loss

            # Calculate accuracy on test data
            hidden = sigmoid(np.dot(features_test, weights_input_hidden))
            out = sigmoid(np.dot(hidden, weights_hidden_output))
            predictions = out > 0.5
            accuracy = np.mean(predictions == targets_test)
            print("Prediction accuracy: {:.3f}".format(accuracy))
            ```

    * How to optimize trainning 

        * ![testing](./images/testing.png)

        * ![testing1](./images/testing1.png)

        * ![testing2](./images/testing2.png)

        * ![testing3](./images/testing3.png)

        * ![testing4](./images/testing4.png)

        * ![testing5](./images/testing5.png)

        * ![testing6](./images/testing6.png)
    
    * Early Stop

        * ![testing7](./images/testing7.png)

        * ![testing8](./images/testing8.png)

        * ![testing9](./images/testing9.png)

        * ![testing10](./images/testing10.png)

        * ![testing11](./images/testing11.png)

        * ![testing12](./images/testing12.png) 

    * Regularization

        * ![testing13](./images/testing13.png) 

        * ![testing14](./images/testing14.png) 

        * ![testing15](./images/testing15.png) 

        * ![testing16](./images/testing16.png) 

        * ![testing17](./images/testing17.png) 

        * ![testing18](./images/testing18.png) 

        * ![testing19](./images/testing19.png) 

        * ![testing21](./images/testing21.png)

        * ![testing22](./images/testing22.png) 

        * ![testing23](./images/testing23.png) 

            * L2 will prefer a vector (0.5, 0.5) over a vector (1, 0) since the sum of the weights is lower. That means a lower penalization on our error function
        
        * We wan't to regularize our error function so we don't overfit.
    
    * Dropout

        * You are not allowed to use a specific node at a specific epoch. It is like we are turning nodes on and off.

        * Sometimes one part of the network has very large weights and it ends up dominating all the training. 

        * ![dropout](./images/dropout.png)  

        * ![dropout1](./images/dropout1.png)

        * ![dropout2](./images/dropout2.png) 

        * ![dropout3](./images/dropout3.png)

            * We set a parameter that determines the probability of each node being dropped at a particular epoch
    
    * Local Minima and Random Restart

        * ![local-minima](./images/local-minima.png)

        * ![local-minima1](./images/local-minima1.png)

            * We start from a few different random places and do gradient descent from all of them.

            * This increases the probability that we will get to the global minima
    
    * Vanishing Gradient

        * ![vanishing-gradient](./images/vanishing-gradient.png) 

        * ![vanishing-gradient1](./images/vanishing-gradient1.png)

        * ![vanishing-gradient2](./images/vanishing-gradient2.png)

        * ![vanishing-gradient3](./images/vanishing-gradient3.png)

        * The best way to fix this tiny gradient descent over layers is to change the activation function.

        * ![vanishing-gradient4](./images/vanishing-gradient4.png)

            * Since this function has a range from -1 and 1, the derivatives are larger

        * ![vanishing-gradient5](./images/vanishing-gradient5.png)

            * ReLu improves training significantly without sacrificing much accuracy, since the derivative is one if the number is positive 
        
        * ![vanishing-gradient6](./images/vanishing-gradient6.png)
    
    * Batch and Stochastic Gradient Descent 

        * ![stochastic-1](./images/stochastic-1.png)

        * ![stochastic-2](./images/stochastic-2.png)

            * We take small subsets of data, run them through the neural network calculate the gradient of the error function based on those points and then move one step in that direction.

            * We still want to use all our data, so we split it in batches.
    
    * Learning Rate

        * The question of what learning rate to use is pretty much a research question itself, but here's a general rule. 

        * ![learning-rate1](./images/learning-rate1.png)

            * This could be fast in the beginning, but you may miss the minimum and keep going.
        
        * ![learning-rate2](./images/learning-rate2.png)

            * If your model is not working, decrease the learning rate

            * The best learning rates are those which decrease as the model is getting closer to a solution.
        
        * ![learning-rate3](./images/learning-rate3.png)
    
    * Momentum 

        * ![momentum](./images/momentum.png)

        * ![momentum1](./images/momentum1.png)

        * ![momentum2](./images/momentum2.png)

        * ![momentum3](./images/momentum3.png)

            * In order to explore other local minimuns (maybe the global minimum), we will average the last steps done for gradient descent to get momentum and explore the function.
        
        * ![momentum4](./images/momentum4.png)

        * ![momentum5](./images/momentum5.png)

        * ![momentum6](./images/momentum6.png)

        * ![momentum7](./images/momentum7.png)
        
        * ![momentum8](./images/momentum8.png)

        * ![momentum9](./images/momentum9.png)

        * ![momentum10](./images/momentum10.png)

        * ![momentum11](./images/momentum11.png)

        * ![momentum12](./images/momentum12.png)

        * ![momentum13](./images/momentum13.png)
        
    * Error functions

        * Besides square error and cross-entropy, there are many other functions out there.

* Deep Learning with PyTorch 

    * Welcome! In this lesson, you'll learn how to use PyTorch for building deep learning models. PyTorch was released in early 2017 and has been making a pretty big impact in the deep learning community. It's developed as an open source project by the Facebook AI Research team, but is being adopted by teams everywhere in industry and academia. In my experience, it's the best framework for learning deep learning and just a delight to work with in general. By the end of this lesson, you'll have trained your own deep learning model that can classify images of cats and dogs.

    * I'll first give you a basic introduction to PyTorch, where we'll cover **tensors** - the main data structure of PyTorch. I'll show you how to create tensors, how to do simple operations, and how tensors interact with NumPy.

    * Then you'll learn about a module called **autograd** that PyTorch uses to calculate gradients for training neural networks. Autograd, in my opinion, is amazing. It does all the work of backpropagation for you by calculating the gradients at each operation in the network which you can then use to update the network weights.

    * Next you'll use PyTorch to build a network and run data forward through it. After that, you'll define a loss and an optimization method to train the neural network on a dataset of handwritten digits. You'll also learn how to test that your network is able to generalize through **validation**.

    * However, you'll find that your network doesn't work too well with more complex images. You'll learn how to use pre-trained networks to improve the performance of your classifier, a technique known as **transfer learning**.

    * Follow along with the videos and work through the exercises in your own notebooks. If you get stuck, check out my solution videos and notebooks.

    * Get the notebooks

        * The notebooks for this lesson will be provided in the classroom, but if you wish to follow along on your local machine, then the instructions below will help you get setup and ready to learn!

        * All the notebooks for this lesson are available from our deep learning repo on GitHub. Please clone the repo by typing

        * `git clone https://github.com/udacity/deep-learning-v2-pytorch.git`

        * in your terminal. Then navigate to the intro-to-pytorch directory in the repo.

        * Follow along in your notebooks to complete the exercises. I'll also be providing solutions to the exercises, both in videos and in the notebooks marked `(Solution)`.

        * Dependencies

            * These notebooks require PyTorch v0.4 or newer, and torchvision. The easiest way to install PyTorch and torchvision locally is by [following the instructions on the PyTorch site](https://pytorch.org/get-started/locally/). Choose the stable version, your appropriate OS and Python versions, and how you'd like to install it. You'll also need to install numpy and jupyter notebooks, the newest versions of these should work fine. Using the conda package manager is generally best for this,

            * `conda install numpy jupyter notebook`

            * If you haven't used conda before, please read the documentation to learn how to create environments and install packages. I suggest installing Miniconda instead of the whole Anaconda distribution. The normal package manager pip also works well. If you have a preference, go with that.

            * The final part of the series has a soft requirement of a GPU used to accelerate network computations. Even if you don't have a GPU available, you'll still be able to run the code and finish the exercises. PyTorch uses a library called CUDA to accelerate operations using the GPU. If you have a GPU that CUDA supports, you'll be able to install all the necessary libraries by installing PyTorch with conda. If you can't use a local GPU, you can use cloud platforms such as AWS, GCP, and FloydHub to train your networks on a GPU.

    * Notebooks: Intro to PyTorch

        * Check the notebooks inside the `deep-learning-v2-pytorch` folder.

        * Remember that for matrix multiplications, the number of columns in the first tensor must equal to the number of rows in the second column

        * When you use `*`, the multiplication is elementwise, when you use torch.mm it is matrix multiplication.

        * ```python
            a = torch.rand(2,5)
            b = torch.rand(2,5)
            result = a*b 
            ```
        
        * `result` will be shaped the same as `a` or `b` i.e `(2,5)` whereas considering operation

        * `result = torch.mm(a,b)`

        * It will give a size mismatch error, as this is proper matrix multiplication (as we study in linear algebra) and `a.shape[1] != b.shape[0]`. When you apply the view operation in torch.mm you are trying to match the dimensions.

        * In the special case of the shape in some particular dimension being 1, it becomes a dot product and hence `sum (a*b)` is same as `mm(a, b.view(5,1))`

        * `torch.matmul` will do broadcasting, that means it will try to "fix" the output if dimensions are not matching.

        * The networks you've seen so far are called *fully-connected* or *dense* networks. Each unit in one layer is connected to each unit in the next layer. In fully-connected networks, the input to each layer must be a one-dimensional vector (which can be stacked into a 2D tensor as a batch of multiple examples). However, our images are 28x28 2D tensors, so we need to convert them into 1D vectors. Thinking about sizes, we need to convert the batch of images with shape `(64, 1, 28, 28)` to a have a shape of `(64, 784)`, 784 is 28 times 28. This is typically called *flattening*, we flattened the 2D images into 1D vectors.

        * This way PyTorch will divide the 10 values in each row of a by the one value in each row of b. Pay attention to how you take the sum as well. You'll need to define the dim keyword in torch.sum. Setting `dim=0` takes the sum across the rows while `dim=1` takes the sum across the columns.


        * ```python
            import torch
            from torch import nn
            import torch.nn.functional as F
            from torchvision import datasets, transforms

            # Define a transform to normalize the data
            transform = transforms.Compose([transforms.ToTensor(),
                                            transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5)),
                                        ])
            # Download and load the training data
            trainset = datasets.MNIST('~/.pytorch/MNIST_data/', download=True, train=True, transform=transform)
            trainloader = torch.utils.data.DataLoader(trainset, batch_size=64, shuffle=True)

            model = nn.Sequential(nn.Linear(784, 128),
                      nn.ReLU(),
                      nn.Linear(128, 64),
                      nn.ReLU(),
                      nn.Linear(64, 10),
                      nn.LogSoftmax(dim=1))

            criterion = nn.NLLLoss()
            optimizer = optim.SGD(model.parameters(), lr=0.003)

            epochs = 5
            for e in range(epochs):
                running_loss = 0
                for images, labels in trainloader:
                    # Flatten MNIST images into a 784 long vector
                    images = images.view(images.shape[0], -1)
                
                    # TODO: Training pass
                    optimizer.zero_grad()
                    
                    output = model.forward(images)
                    loss = criterion(output, labels)
                    loss.backward()
                    optimizer.step()
                    
                    running_loss += loss.item()
                else:
                    print(f"Training loss: {running_loss/len(trainloader)}")
            ```

        * ```python
            from torch import nn, optim
            import torch.nn.functional as F

            # TODO: Define your network architecture here
            class Classifier(nn.Module):
                def __init__(self):
                    super().__init__()
                    self.fc1 = nn.Linear(784, 256)
                    self.fc2 = nn.Linear(256, 128)
                    self.fc3 = nn.Linear(128, 64)
                    self.fc4 = nn.Linear(64, 10)
                    
                def forward(self, x):
                    # make sure input tensor is flattened
                    x = x.view(x.shape[0], -1)
                    
                    x = F.relu(self.fc1(x))
                    x = F.relu(self.fc2(x))
                    x = F.relu(self.fc3(x))
                    x = F.log_softmax(self.fc4(x), dim=1)
                    
                    return x
            
            # TODO: Create the network, define the criterion and optimizer
            model = Classifier()
            criterion = nn.NLLLoss()
            optimizer = optim.Adam(model.parameters(), lr=0.003)

            # TODO: Train the network here
            epochs = 5

            for e in range(epochs):
                running_loss = 0
                for images, labels in trainloader:
                    log_ps = model(images)
                    loss = criterion(log_ps, labels)
                    
                    optimizer.zero_grad()
                    loss.backward()
                    optimizer.step()
                    
                    running_loss += loss.item()
                else:
                    print(f"Training loss: {running_loss}")
            
            %matplotlib inline
            %config InlineBackend.figure_format = 'retina'

            import helper

            # Test out your network!

            dataiter = iter(testloader)
            images, labels = dataiter.next()
            img = images[1]

            # TODO: Calculate the class probabilities (softmax) for img
            ps = torch.exp(model(img))

            # Plot the image and probabilities
            helper.view_classify(img, ps, version='Fashion')
            ```

        * Now that you have a trained network, you can use it for making predictions. This is typically called inference, a term borrowed from statistics. However, neural networks have a tendency to perform too well on the training data and aren't able to generalize to data that hasn't been seen before. This is called overfitting and it impairs inference performance. To test for overfitting while training, we measure the performance on data not in the training set called the validation set. We avoid overfitting through regularization such as dropout while monitoring the validation performance during training. In this notebook, I'll show you how to do this in PyTorch.

        * As usual, let's start by loading the dataset through torchvision. You'll learn more about torchvision and loading data in a later part. This time we'll be taking advantage of the test set which you can get by setting train=False here:

        * `testset = datasets.FashionMNIST('~/.pytorch/F_MNIST_data/', download=True, train=False, transform=transform)`
        
        * The test set contains images just like the training set. Typically you'll see 10-20% of the original dataset held out for testing and validation with the rest being used for training.

        * ![precision](./images/precision.png)

        * ![recall](./images/recall.png)

        * ```python
            model = Classifier()
            criterion = nn.NLLLoss()
            optimizer = optim.Adam(model.parameters(), lr=0.003)

            epochs = 30
            steps = 0

            train_losses, test_losses = [], []
            for e in range(epochs):
                running_loss = 0
                for images, labels in trainloader:
                    
                    optimizer.zero_grad()
                    
                    log_ps = model(images)
                    loss = criterion(log_ps, labels)
                    loss.backward()
                    optimizer.step()
                    
                    running_loss += loss.item()
                    
                else:
                    test_loss = 0
                    accuracy = 0
                    
                    # Turn off gradients for validation, saves memory and computations
                    with torch.no_grad():
                        for images, labels in testloader:
                            log_ps = model(images)
                            test_loss += criterion(log_ps, labels)
                            
                            ps = torch.exp(log_ps)
                            top_p, top_class = ps.topk(1, dim=1)
                            equals = top_class == labels.view(*top_class.shape)
                            accuracy += torch.mean(equals.type(torch.FloatTensor))
                            
                    train_losses.append(running_loss/len(trainloader))
                    test_losses.append(test_loss/len(testloader))

                    print("Epoch: {}/{}.. ".format(e+1, epochs),
                        "Training Loss: {:.3f}.. ".format(running_loss/len(trainloader)),
                        "Test Loss: {:.3f}.. ".format(test_loss/len(testloader)),
                        "Test Accuracy: {:.3f}".format(accuracy/len(testloader)))

            %matplotlib inline
            %config InlineBackend.figure_format = 'retina'

            import matplotlib.pyplot as plt

            plt.plot(train_losses, label='Training loss')
            plt.plot(test_losses, label='Validation loss')
            plt.legend(frameon=False)
            ```

        * ![overfitting](./images/overfitting.png)

        * The network learns the training set better and better, resulting in lower training losses. However, it starts having problems generalizing to data outside the training set leading to the validation loss increasing. The ultimate goal of any deep learning model is to make predictions on new data, so we should strive to get the lowest validation loss possible. One option is to use the version of the model with the lowest validation loss, here the one around 8-10 training epochs. This strategy is called early-stopping. In practice, you'd save the model frequently as you're training then later choose the model with the lowest validation loss.

        * The most common method to reduce overfitting (outside of early-stopping) is dropout, where we randomly drop input units. This forces the network to share information between weights, increasing it's ability to generalize to new data. Adding dropout in PyTorch is straightforward using the nn.Dropout module.

        * ```python
            class Classifier(nn.Module):
            def __init__(self):
                super().__init__()
                self.fc1 = nn.Linear(784, 256)
                self.fc2 = nn.Linear(256, 128)
                self.fc3 = nn.Linear(128, 64)
                self.fc4 = nn.Linear(64, 10)

                # Dropout module with 0.2 drop probability
                self.dropout = nn.Dropout(p=0.2)

            def forward(self, x):
                # make sure input tensor is flattened
                x = x.view(x.shape[0], -1)

                # Now with dropout
                x = self.dropout(F.relu(self.fc1(x)))
                x = self.dropout(F.relu(self.fc2(x)))
                x = self.dropout(F.relu(self.fc3(x)))

                # output so no dropout here
                x = F.log_softmax(self.fc4(x), dim=1)

                return x
            ```
        
        * During training we want to use dropout to prevent overfitting, but during inference we want to use the entire network. So, we need to turn off dropout during validation, testing, and whenever we're using the network to make predictions. To do this, you use model.eval(). This sets the model to evaluation mode where the dropout probability is 0. You can turn dropout back on by setting the model to train mode with model.train(). In general, the pattern for the validation loop will look like this, where you turn off gradients, set the model to evaluation mode, calculate the validation loss and metric, then set the model back to train mode.

        * ```python
            # turn off gradients
            with torch.no_grad():

                # set model to evaluation mode
                model.eval()

                # validation pass here
                for images, labels in testloader:
                    ...

            # set model back to train mode
            model.train()
            ```

        * ```python
            model = Classifier()
            criterion = nn.NLLLoss()
            optimizer = optim.Adam(model.parameters(), lr=0.003)

            epochs = 30
            steps = 0

            train_losses, test_losses = [], []
            for e in range(epochs):
                running_loss = 0
                for images, labels in trainloader:
                    
                    optimizer.zero_grad()
                    
                    log_ps = model(images)
                    loss = criterion(log_ps, labels)
                    loss.backward()
                    optimizer.step()
                    
                    running_loss += loss.item()
                    
                else:
                    test_loss = 0
                    accuracy = 0
                    
                    # Turn off gradients for validation, saves memory and computations
                    with torch.no_grad():
                        model.eval()
                        for images, labels in testloader:
                            log_ps = model(images)
                            test_loss += criterion(log_ps, labels)
                            
                            ps = torch.exp(log_ps)
                            top_p, top_class = ps.topk(1, dim=1)
                            equals = top_class == labels.view(*top_class.shape)
                            accuracy += torch.mean(equals.type(torch.FloatTensor))
                    
                    model.train()
                    
                    train_losses.append(running_loss/len(trainloader))
                    test_losses.append(test_loss/len(testloader))

                    print("Epoch: {}/{}.. ".format(e+1, epochs),
                        "Training Loss: {:.3f}.. ".format(running_loss/len(trainloader)),
                        "Test Loss: {:.3f}.. ".format(test_loss/len(testloader)),
                        "Test Accuracy: {:.3f}".format(accuracy/len(testloader)))
            ```

            * ![dropout-ex](./images/dropout-ex.png)

        
        * Loading PyTorch model

            * ```python
                torch.save(model.state_dict(), 'checkpoint.pth')

                state_dict = torch.load('checkpoint.pth')
                print(state_dict.keys())

                model.load_state_dict(state_dict)

                # Seems pretty straightforward, but as usual it's a bit more complicated. Loading the state dict works only if the model architecture is exactly the same as the checkpoint architecture. If I create a model with a different architecture, this fails.

                # This means we need to rebuild the model exactly as it was when trained. Information about the model architecture needs to be saved in the checkpoint, along with the state dict. To do this, you build a dictionary with all the information you need to compeletely rebuild the model.
                checkpoint = {'input_size': 784,
                    'output_size': 10,
                    'hidden_layers': [each.out_features for each in model.hidden_layers],
                    'state_dict': model.state_dict()
                }

                torch.save(checkpoint, 'checkpoint.pth')

                def load_checkpoint(filepath):
                    checkpoint = torch.load(filepath)
                    model = fc_model.Network(checkpoint['input_size'],
                                            checkpoint['output_size'],
                                            checkpoint['hidden_layers'])
                    model.load_state_dict(checkpoint['state_dict'])
                    
                    return model
                
                model = load_checkpoint('checkpoint.pth')
                print(model)
                ```
        * Data Augmentation
            
            * A common strategy for training neural networks is to introduce randomness in the input data itself. For example, you can randomly rotate, mirror, scale, and/or crop your images during training. This will help your network generalize as it's seeing the same images but in different locations, with different sizes, in different orientations, etc.

            * To randomly rotate, scale and crop, then flip your images you would define your transforms like this:

            * ```python
                train_transforms = transforms.Compose([transforms.RandomRotation(30),
                                       transforms.RandomResizedCrop(224),
                                       transforms.RandomHorizontalFlip(),
                                       transforms.ToTensor(),
                                       transforms.Normalize([0.5, 0.5, 0.5], 
                                                            [0.5, 0.5, 0.5])])
                ```

    * Few things to check if your network isn't training appropriately

        * Make sure you're clearing the gradients in the training loop with `optimizer.zero_grad()`. If you're doing a validation loop, be sure to set the network to evaluation mode with `model.eval()`, then back to training mode with `model.train()`.

        * You'll notice the second type is torch.cuda.FloatTensor, this means it's a tensor that has been moved to the GPU. It's expecting a tensor with type torch.FloatTensor, no .cuda there, which means the tensor should be on the CPU. PyTorch can only perform operations on tensors that are on the same device, so either both CPU or both GPU. If you're trying to run your network on the GPU, check to make sure you've moved the model and all necessary tensors to the GPU with .to(device) where device is either "cuda" or "cpu".

