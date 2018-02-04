func fib(n: Int) -> Int {
    var sum = 0
    
    var fibQueue = [0, 1]
    for _ in 0...n {
        guard !fibQueue.isEmpty, let x = fibQueue.first else { return 0 }
        fibQueue.remove(at: 0)
        sum += x
        fibQueue.append(sum)
    }
    
    return sum
}

fib(n: 0)
fib(n: 1)
fib(n: 2)
fib(n: 3)
fib(n: 5)
fib(n: 8)
