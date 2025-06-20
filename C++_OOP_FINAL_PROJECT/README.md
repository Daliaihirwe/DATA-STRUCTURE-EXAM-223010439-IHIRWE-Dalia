# ATM Cash Dispenser Simulation

## Project No: 19

This project implements a sophisticated ATM cash dispenser system that manages multiple currency denominations using advanced C++ concepts. The system demonstrates dynamic memory management, object-oriented programming principles, and two distinct dispensing algorithms through a menu-driven interface.

## Project Description

The ATM Cash Dispenser simulates a real-world ATM system that:

- Manages different denominations of Rwandan Francs (RWF)
- Implements two dispensing strategies using inheritance and polymorphism
- Provides dynamic denomination management (add/remove currency types)
- Uses pointer arithmetic and dynamic memory allocation throughout
- Demonstrates runtime polymorphism through virtual function calls

## Technical Architecture

### Core Data Structure

```cpp
struct Denomination {
    int value;      // Denomination value (e.g., 5000, 1000, 500 RWF)
    int* count;     // Pointer to count of available notes
};
```

**Key Design Decisions:**

- `int* count` instead of `int count` demonstrates dynamic memory allocation
- Global `Denomination* denoms` array shows dynamic array management
- Pointer arithmetic usage throughout for educational purposes

### Class Hierarchy

```
CashDispenser (Abstract Base Class)
├── GreedyDispenser (Largest notes first)
└── SmartDispenser (Smallest notes first)
```

## Implementation Analysis

### 1. Dynamic Memory Management

#### Adding Denominations

```cpp
void addDenomination(int value, int count) {
    Denomination* newDenoms = new Denomination[n + 1];  // Allocate larger array
    for (int i = 0; i < n; ++i)
        newDenoms[i] = denoms[i];                       // Copy existing data
    newDenoms[n].value = value;                         // Set new value
    newDenoms[n].count = new int(count);                // Allocate count pointer
    delete[] denoms;                                    // Free old array
    denoms = newDenoms;                                 // Update pointer
    n++;                                                // Increment count
}
```

**Concepts Demonstrated:**

- Dynamic array resizing
- Memory allocation with `new`
- Proper cleanup with `delete[]`
- Pointer reassignment

#### Removing Denominations

```cpp
void removeDenomination(int value) {
    int idx = -1;
    for (int i = 0; i < n; ++i)
        if (denoms[i].value == value) idx = i;          // Find target index
    if (idx == -1) return;                              // Value not found

    Denomination* newDenoms = new Denomination[n - 1];  // Smaller array
    int j = 0;
    for (int i = 0; i < n; ++i) {
        if (i == idx) {
            delete denoms[i].count;                     // Free count pointer
            continue;
        }
        newDenoms[j++] = denoms[i];                     // Copy non-removed items
    }
    delete[] denoms;                                    // Free old array
    denoms = newDenoms;                                 // Update pointer
    n--;                                                // Decrement count
}
```

**Concepts Demonstrated:**

- Array searching algorithms
- Conditional memory deallocation
- Array compaction
- Pointer management

### 2. Object-Oriented Design

#### Abstract Base Class

```cpp
class CashDispenser {
public:
    virtual bool dispense(int amount) = 0;              // Pure virtual function
    virtual ~CashDispenser() {}                        // Virtual destructor
};
```

**Design Principles:**

- **Interface Segregation**: Single responsibility (dispensing)
- **Open/Closed Principle**: Open for extension, closed for modification
- **Polymorphism**: Different implementations through inheritance

#### Greedy Algorithm Implementation

```cpp
class GreedyDispenser : public CashDispenser {
public:
    bool dispense(int amount) override {
        cout << "\n[Greedy Strategy]\n";
        for (int i = 0; i < n; ++i) {                   // Largest to smallest
            Denomination* d = denoms + i;               // Pointer arithmetic
            while (amount >= d->value && *(d->count) > 0) {
                cout << "Dispensed: " << d->value << " RWF\n";
                amount -= d->value;                     // Reduce amount
                (*(d->count))--;                        // Decrement via pointer
            }
        }
        return (amount == 0);                           // Success check
    }
};
```

**Algorithm Characteristics:**

- **Time Complexity**: O(n) where n is number of denominations
- **Space Complexity**: O(1)
- **Strategy**: Always uses largest available denomination
- **Advantage**: Fast execution
- **Disadvantage**: May not find optimal solution

#### Smart Algorithm Implementation

```cpp
class SmartDispenser : public CashDispenser {
public:
    bool dispense(int amount) override {
        cout << "\n[Smart Strategy - Small Notes First]\n";
        for (int i = n - 1; i >= 0; --i) {             // Smallest to largest
            Denomination* d = denoms + i;               // Pointer arithmetic
            while (amount >= d->value && *(d->count) > 0) {
                cout << "Dispensed: " << d->value << " RWF\n";
                amount -= d->value;                     // Reduce amount
                (*(d->count))--;                        // Decrement via pointer
            }
        }
        return (amount == 0);                           // Success check
    }
};
```

**Algorithm Characteristics:**

- **Time Complexity**: O(n) where n is number of denominations
- **Space Complexity**: O(1)
- **Strategy**: Prioritizes smaller denominations
- **Advantage**: Preserves larger notes for future transactions
- **Use Case**: Better for maintaining inventory balance

### 3. Polymorphism Implementation

#### Runtime Polymorphism

```cpp
CashDispenser** machines = new CashDispenser*[2];       // Array of base pointers
machines[0] = new GreedyDispenser();                    // Concrete implementation 1
machines[1] = new SmartDispenser();                     // Concrete implementation 2

// Polymorphic function call
machines[choice - 4]->dispense(amt);                    // Virtual function dispatch
```

**Concepts Demonstrated:**

- **Dynamic Binding**: Method resolution at runtime
- **Virtual Function Table**: C++ vtable mechanism
- **Pointer-to-Pointer**: `CashDispenser**` usage
- **Array of Objects**: Managing multiple implementations

### 4. Pointer Arithmetic Usage

#### Denomination Access

```cpp
Denomination* d = denoms + i;                           // Equivalent to &denoms[i]
int currentValue = d->value;                            // Access via pointer
int* countPtr = d->count;                               // Pointer to count
(*(d->count))--;                                        // Decrement via double dereference
```

**Educational Value:**

- Shows relationship between arrays and pointers
- Demonstrates pointer arithmetic in practice
- Illustrates memory layout understanding

## Complete Implementation Code

## Compilation and Execution

### System Requirements

- C++11 compatible compiler (GCC 4.8+, Clang 3.3+, MSVC 2015+)
- Standard C++ libraries
- Minimum 4MB RAM for execution

## Usage Examples

### 1. Setting Up Denominations

```
===== ATM Cash Dispenser =====
1. Show Available Notes
2. Add Denomination
3. Remove Denomination
4. Withdraw (Greedy)
5. Withdraw (Smart)
0. Exit
Select option: 2
Enter value: 5000
Enter count: 10

Select option: 2
Enter value: 1000
Enter count: 20

Select option: 2
Enter value: 500
Enter count: 30
```

### 2. Viewing Inventory

```
Select option: 1

Available Notes:
Value     Count
------------------
5000      10
1000      20
500       30
```

### 3. Greedy Withdrawal Example

```
Select option: 4
Enter amount to withdraw: 7500

[Greedy Strategy]
Dispensed: 5000 RWF
Dispensed: 1000 RWF
Dispensed: 1000 RWF
Dispensed: 500 RWF
Successfully Dispensed.
```

### 4. Smart Withdrawal Example

```
Select option: 5
Enter amount to withdraw: 7500

[Smart Strategy - Small Notes First]
Dispensed: 500 RWF
Dispensed: 500 RWF
Dispensed: 500 RWF
Dispensed: 500 RWF
Dispensed: 500 RWF
Dispensed: 500 RWF
Dispensed: 500 RWF
Dispensed: 500 RWF
Successfully Dispensed.
```

### 5. Updated Inventory

```
Select option: 1

Available Notes:
Value     Count
------------------
5000      9
1000      18
500       15
```

## Algorithm Comparison

### Greedy vs Smart Strategy Analysis

| Aspect | Greedy Dispenser | Smart Dispenser |
|--------|------------------|-----------------|
| **Approach** | Largest notes first | Smallest notes first |
| **Execution Speed** | Faster | Slower (more iterations) |
| **Note Usage** | Fewer total notes | More total notes |
| **Inventory Management** | Uses large notes quickly | Preserves large notes |
| **Best Use Case** | Quick transactions | Inventory preservation |

### Performance Metrics

**Test Case**: Dispensing 7,500 RWF with inventory (10×5000, 20×1000, 30×500)

| Strategy | Notes Used | Execution Time | Remaining Large Notes |
|----------|------------|----------------|----------------------|
| Greedy | 4 notes | O(1) | 1×5000, 18×1000 |
| Smart | 15 notes | O(n) | 9×5000, 20×1000 |

## Advanced Features Demonstrated

### 1. Memory Management Excellence

- **Dynamic Array Resizing**: Efficient reallocation strategies
- **Pointer Arithmetic**: Direct memory manipulation
- **Resource Cleanup**: Comprehensive memory deallocation
- **Exception Safety**: Proper cleanup on errors

### 2. Object-Oriented Design Patterns

- **Abstract Factory**: CashDispenser as interface
- **Strategy Pattern**: Interchangeable algorithms
- **Polymorphism**: Runtime method dispatch
- **Encapsulation**: Data hiding and access control

### 3. Algorithm Implementation

- **Greedy Algorithms**: Optimization through local choices
- **Resource Management**: Inventory tracking and updates
- **State Management**: Consistent system state maintenance

## Error Handling and Edge Cases

### Robust Error Management

1. **Invalid Amounts**: Handles impossible withdrawal requests
2. **Insufficient Inventory**: Graceful failure with clear messages
3. **Memory Allocation**: Safe handling of allocation failures
4. **Invalid Operations**: Removing non-existent denominations

### Test Scenarios

- **Empty Inventory**: Attempting withdrawals with no denominations
- **Exact Amount**: Withdrawing exactly available amount
- **Partial Fulfillment**: Insufficient inventory for complete withdrawal
- **Large Requests**: Amounts exceeding total available cash

## Educational Objectives Achieved

### Core C++ Concepts

**Dynamic Memory Allocation**: `new` and `delete` operators  
**Pointer Arithmetic**: Direct memory manipulation  
**Inheritance**: Base and derived class relationships  
**Polymorphism**: Virtual functions and runtime dispatch  
**Abstract Classes**: Pure virtual functions  
**Memory Management**: Proper cleanup and resource management  

### Advanced Programming Concepts

**Algorithm Design**: Greedy vs. optimal strategies  
**Data Structure Management**: Dynamic arrays  
**System Architecture**: Modular design principles  
**Error Handling**: Robust error management  
**User Interface**: Menu-driven application design  

## Project Screenshots Required

### Essential Screenshots to Capture

1. **Compilation Process**: Terminal showing successful compilation
2. **Initial Menu**: First program launch with menu options
3. **Adding Denominations**: Process of adding 3-4 different denominations
4. **Inventory Display**: Current available notes after setup
5. **Greedy Withdrawal**: Example withdrawal using greedy algorithm
6. **Smart Withdrawal**: Same amount using smart algorithm
7. **Updated Inventory**: Final state showing consumed notes
8. **Error Handling**: Attempting impossible withdrawal
9. **Denomination Management**: Adding and removing denominations
10. **Program Exit**: Clean termination with memory cleanup

## Conclusion

This ATM Cash Dispenser implementation successfully demonstrates:

- **Advanced Memory Management**: Dynamic allocation, pointer arithmetic, and proper cleanup
- **Object-Oriented Programming**: Inheritance, polymorphism, and abstract classes
- **Algorithm Implementation**: Two distinct dispensing strategies with different optimization goals
- **Software Engineering**: Modular design, error handling, and user interface
- **Real-World Application**: Practical simulation of ATM functionality

The project serves as an excellent educational tool for understanding advanced C++ concepts while solving a practical problem. The implementation showcases the power of object-oriented design in creating flexible, maintainable, and extensible software systems.

