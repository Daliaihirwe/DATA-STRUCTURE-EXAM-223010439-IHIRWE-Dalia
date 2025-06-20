#include <iostream>
#include <iomanip>
#include <algorithm>
using namespace std;

struct Denomination {
    int value;
    int* count;
};

Denomination* denoms = nullptr;
int n = 0;


void addDenomination(int value, int count) {
    Denomination* newDenoms = new Denomination[n + 1];
    for (int i = 0; i < n; ++i)
        newDenoms[i] = denoms[i];
    newDenoms[n].value = value;
    newDenoms[n].count = new int(count);
    delete[] denoms;
    denoms = newDenoms;
    n++;
}


void removeDenomination(int value) {
    int idx = -1;
    for (int i = 0; i < n; ++i)
        if (denoms[i].value == value) idx = i;
    if (idx == -1) return;

    Denomination* newDenoms = new Denomination[n - 1];
    int j = 0;
    for (int i = 0; i < n; ++i) {
        if (i == idx) {
            delete denoms[i].count;
            continue;
        }
        newDenoms[j++] = denoms[i];
    }
    delete[] denoms;
    denoms = newDenoms;
    n--;
}


class CashDispenser {
public:
    virtual bool dispense(int amount) = 0;
    virtual ~CashDispenser() {}
};


class GreedyDispenser : public CashDispenser {
public:
    bool dispense(int amount) override {
        cout << "\n[Greedy Strategy]\n";
        for (int i = 0; i < n; ++i) {
            Denomination* d = denoms + i;
            while (amount >= d->value && *(d->count) > 0) {
                cout << "Dispensed: " << d->value << " RWF\n";
                amount -= d->value;
                (*(d->count))--;
            }
        }
        if (amount == 0) {
            cout << "Successfully Dispensed.\n";
            return true;
        } else {
            cout << "Cannot dispense full amount.\n";
            return false;
        }
    }
};


class SmartDispenser : public CashDispenser {
public:
    bool dispense(int amount) override {
        cout << "\n[Smart Strategy - Small Notes First]\n";
        for (int i = n - 1; i >= 0; --i) {
            Denomination* d = denoms + i;
            while (amount >= d->value && *(d->count) > 0) {
                cout << "Dispensed: " << d->value << " RWF\n";
                amount -= d->value;
                (*(d->count))--;
            }
        }
        if (amount == 0) {
            cout << "Successfully Dispensed.\n";
            return true;
        } else {
            cout << "Cannot dispense full amount.\n";
            return false;
        }
    }
};


void showDenoms() {
    cout << "\nAvailable Notes:\n";
    cout << left << setw(10) << "Value" << "Count\n";
    cout << "------------------\n";
    for (int i = 0; i < n; ++i)
        cout << left << setw(10) << denoms[i].value << *(denoms[i].count) << "\n";
}


int main() {
    int choice;
    CashDispenser** machines = new CashDispenser*[2];
    machines[0] = new GreedyDispenser();
    machines[1] = new SmartDispenser();


    sort(denoms, denoms + n, [](Denomination a, Denomination b) {
        return a.value > b.value;
    });

    do {
        cout << "\n===== ATM Cash Dispenser =====\n";
        cout << "1. Show Available Notes\n";
        cout << "2. Add Denomination\n";
        cout << "3. Remove Denomination\n";
        cout << "4. Withdraw (Greedy)\n";
        cout << "5. Withdraw (Smart)\n";
        cout << "0. Exit\n";
        cout << "Select option: ";
        cin >> choice;

        if (choice == 1) {
            showDenoms();
        } else if (choice == 2) {
            int val, cnt;
            cout << "Enter value: "; cin >> val;
            cout << "Enter count: "; cin >> cnt;
            addDenomination(val, cnt);
        } else if (choice == 3) {
            int val;
            cout << "Enter value to remove: "; cin >> val;
            removeDenomination(val);
        } else if (choice == 4 || choice == 5) {
            int amt;
            cout << "Enter amount to withdraw: ";
            cin >> amt;
            machines[choice - 4]->dispense(amt);
        }
    } while (choice != 0);

    for (int i = 0; i < n; ++i)
        delete denoms[i].count;
    delete[] denoms;
    for (int i = 0; i < 2; ++i)
        delete machines[i];
    delete[] machines;

    return 0;
}
