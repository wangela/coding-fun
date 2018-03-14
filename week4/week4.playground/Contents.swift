import Foundation

// Single Number II
func singleNumber(_ A: [Int]) -> Int {
    // Parameter: A is an array of integers with every element appearing 3x except one which only appears 1x
    // Output: The integer that does not appear 3x
    // Goal: O(n) time and no extra memory
    var bitOnce = 0
    var bitTwice = 0
    
    for each in A {
        bitTwice |= (bitOnce & each)
        bitOnce ^= each
        var commonBits = ~(bitOnce & bitTwice)
        bitOnce &= commonBits
        bitTwice &= commonBits
    }

    return bitOnce
}

let sample = [1, 2, 4, 3, 2, 3, 3, 2, 1, 1]

singleNumber(sample)
