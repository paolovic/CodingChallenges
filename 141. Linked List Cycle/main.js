let linkedListWithCycle = { val: 1 };
let node1 = { val: 2 };
let node2 = { val: 3 };
let node3 = { val: 4 };
linkedListWithCycle.next = node1;
node1.next = node2;
node2.next = node3;
node3.next = node1;

const linkedListWithoutCycle = {
    val: 1,
    next: {
        val: 2,
        next: {
            val: 3,
            next: {
                val: 4,
                next: null
            }
        }
    }
};

function solution(head) {
    if (!head) return false;
    let slow = head;
    let fast = head.next;

    while (fast && fast.next) {
        slow = slow.next;
        fast = fast.next.next;
        if (slow === fast) return true;
    }
    return false;
};

console.log(solution(linkedListWithCycle));
console.log(solution(linkedListWithoutCycle));