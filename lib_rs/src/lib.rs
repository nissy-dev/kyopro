struct Node {
    value: i32,
    next: Option<Box<Node>>,
}

pub struct SinglyLinkedList {
    // サイズは、事前に計算することで O(1) で求められる
    size: i32,
    // Boxはヒープ領域を利用するので、一定量のメモリまでしか確保されない
    // スタックだと無限にメモリを確保しようとしてしまう
    head: Option<Box<Node>>,
}

impl SinglyLinkedList {
    pub fn new() -> Self {
        Self {
            size: 0,
            head: None,
        }
    }

    pub fn push(&mut self, value: i32) {
        self.size += 1;
        let new_node = Box::new(Node {
            value: value,
            next: self.head.take(),
        });
        self.head = Some(new_node)
    }

    pub fn pop(&mut self) -> Option<i32> {
        self.size -= 1;
        match self.head.take() {
            None => None,
            Some(node) => {
                self.head = node.next;
                Some(node.value)
            }
        }
    }

    pub fn peek(self) -> Option<i32> {
        self.head.as_ref().map(|node| node.value)
    }

    pub fn remove_by_value(&mut self, value: i32) {
        // let mut curr_node = &mut self.head;
        // while let Some(boxed_node) = curr_node {
        //     if boxed_node.value == value {
        //         *curr_node = boxed_node.next.take();
        //     } else {
        //         curr_node = &mut boxed_node.next;
        //     }
        // }
        let mut current = &mut self.head;
        loop {
            match current {
                None => return,
                Some(node) if node.value == value => {
                    *current = node.next.take();
                }
                Some(node) => {
                    current = &mut node.next;
                }
            }
        }
    }

    pub fn len(self) -> i32 {
        self.size
    }

    pub fn show(&mut self) {
        let mut curr_node = &self.head;
        while let Some(boxed_node) = curr_node {
            println!("{}", boxed_node.value);
            curr_node = &boxed_node.next;
        }
    }
}

// // LinkedListで簡単にスタックは実装できる
// pub struct Stack {
//     linked_list: SinglyLinkedList,
// }

// impl Stack {
//     pub fn new(&mut self) {
//         self.linked_list = SinglyLinkedList::new();
//     }

//     pub fn push(&mut self, value: i32) {
//         self.linked_list.push(value)
//     }

//     pub fn pop(&mut self) -> Option<i32> {
//         self.linked_list.pop()
//     }

//     pub fn len(self) -> i32 {
//         self.linked_list.size
//     }
// }

#[cfg(test)]
mod tests {
    use super::SinglyLinkedList;

    #[test]
    fn linked_list_test() {
        let mut list = SinglyLinkedList::new();

        assert_eq!(list.pop(), None);

        // Populate list
        list.push(1);
        list.push(2);
        list.push(3);

        list.show();

        // Check normal removal
        assert_eq!(list.pop(), Some(3));
        assert_eq!(list.pop(), Some(2));

        // Push some more just to make sure nothing's corrupted
        list.push(4);
        list.push(5);

        // Check normal removal
        assert_eq!(list.pop(), Some(5));
        assert_eq!(list.pop(), Some(4));

        // Check exhaustion
        assert_eq!(list.pop(), Some(1));
        assert_eq!(list.pop(), None);

        // Populate list
        list.push(1);
        list.push(2);
        list.push(3);

        list.remove_by_value(2);

        // Check exhaustion
        assert_eq!(list.pop(), Some(3));
        assert_eq!(list.pop(), Some(1));
        assert_eq!(list.pop(), None);
    }
}
