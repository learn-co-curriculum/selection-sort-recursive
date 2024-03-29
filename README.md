# Day 5: Recursive Selection Sort

## Learning Goals

- Solve algorithm problems using recursion

## Instructions

Sort an array of numbers using selection sort. The selection sort algorithm
sorts an array by repeatedly finding the minimum element (lowest value) in the
input array, and then putting it at the correct location in the sorted array.

Once you're done solving the problem, calculate the average run time and compare
it to the average run time for the iterative version.

```txt
Input: [3, -1, 5, 2]
Output: [-1, 2, 3, 5]
```

You may wish to convert your iterative solution to a recursive one. We've
included our old solutions in Ruby, JavaScript, and Python below:

```ruby
def selection_sort(arr)
  sorted = []

  until arr.length == 0
    min = arr.min
    idx = arr.index(min)
    sorted << min
    arr.delete_at(idx)
  end

  sorted
end
```

```javascript
function selectionSort(arr) {
  const sorted = [];

  while (arr.length > 0) {
    const min = Math.min(...arr);
    const idx = arr.indexOf(min);

    sorted.push(min);
    arr.splice(idx, 1);
  }

  return sorted;
}
```

```python
def selection_sort_out_of_place(list):
    sorted_list = []

    while len(list) > 0:
        min_element = min(list)

        sorted_list.append(min_element)
        list.remove(min_element)

    return sorted_list
```

```python
def selection_sort_in_place(list):
      for i in range(len(list)):
        min_element = list[i]
        min_element_index = i

        for j in range(i + 1, len(list)):
            if list[j] < min_element:
                min_element = list[j]
                min_element_index = j

        temp_element_0 = list[i]
        list[i] = min_element
        list[min_element_index] = temp_element_0

    return list
```

Use the language of your choosing. We've included starter files for some
languages where you can pseudocode, explain your solution and code.

## Before you start coding

1. Rewrite the problem in your own words
2. Validate that you understand the problem
3. Write your own test cases
4. Pseudocode
5. Code!

**_And remember, don't run our tests until you've passed your own!_**

## How to run your own tests

### Ruby

1. `cd` into the ruby folder
2. `ruby <filename>.rb`

### JavaScript

1. `cd` into the javascript folder
2. `node <filename>.js`

## How to run our tests

### Ruby

1. `cd` into the ruby folder
2. `bundle install`
3. `rspec`

### JavaScript

1. `cd` into the javascript folder
2. `npm i`
3. `npm test`
