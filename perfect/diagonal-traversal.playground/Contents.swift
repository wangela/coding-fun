//: Playground - noun: a place where people can play

import UIKit

func numPaths(n: Int) -> Int {
    var fQueue = [1]
    if n == 1 {
        return 1
    }
    for _ in 2...n {
        guard !fQueue.isEmpty else { return 0 }
        var nQueue: [Int] = []
        var currSum = 1
        while !fQueue.isEmpty {
            let x = fQueue.first!
            print(x)
            fQueue.remove(at: 0)
            currSum += x
            nQueue.append(currSum)
        }
        nQueue.append(currSum)
        print(nQueue)
        fQueue = nQueue

    }
    guard let sum = fQueue.last else { return 0 }
    return sum
}

numPaths(n: 7)
