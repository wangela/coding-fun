import Foundation

// ARRAYS
// Array Math
// Add One To Number
//func plusOne(_ A: inout [Int]) -> [Int] {
//    var result: [Int] = []
//    let digits: Int = A.count - 1
//    var currentDigit: Int = 0
//    var carryOver: Int = 1
//
//    for power in 0...digits {
//        currentDigit = A[digits - power] + carryOver
//        if currentDigit < 10 {
//            result.insert(currentDigit, at: 0)
//            carryOver = 0
//        } else {
//            result.insert(currentDigit - 10, at: 0)
//            carryOver = 1
//        }
//    }
//    if carryOver == 1 {
//        result.insert(carryOver, at: 0)
//    }
//    while result[0] == 0 {
//        result.remove(at: 0)
//    }
//    return result
//}
//
////var tryThis = [9, 9, 9]
////plusOne(&tryThis)
//
//// Simulation Array
//// Spiral Order Matrix II
//enum Directions {
//    case right, down, left, up
//}
//
//func generateMatrix(_ A: inout Int) -> [[Int]] {
//    var result: [[Int]] = [[]]
//    var direction: Directions = .right
//    var rows: Int = 0
//    var rowCounter: Int = 0
//    var remaining: Int = A
//    let inputSquared: Int = Int(powf(Float(A), 2))
//    var squareCounter: Int = 1
//
//    while squareCounter <= inputSquared {
//        switch direction {
//        case Directions.right:
//            for x in rowCounter..<(A - rowCounter) {
//                result[rowCounter].insert(squareCounter, at: x)
//                squareCounter += 1
//            }
//            direction = .down
//            rowCounter += 1
//            remaining -= 1
//        case Directions.down:
//            for x in rowCounter...(A - rowCounter) {
//                if result.count < A {
//                    result.append([squareCounter])
//                } else {
//                    var place: Int = result[x].count - rows
//                    result[x].insert(squareCounter, at: place)
//                }
//                squareCounter += 1
//            }
//            direction = .left
//        case Directions.left:
//            for x in rowCounter...(A - rowCounter) {
//                result[A - rowCounter].insert(squareCounter, at: rowCounter - 1)
//                squareCounter += 1
//            }
//            direction = .up
//            remaining -= 1
//            rows += 1
//        case Directions.up:
//            for x in (rowCounter...(A - rowCounter - 1)).reversed() {
//                result[x].insert(squareCounter, at: rowCounter - 1)
//                squareCounter += 1
//            }
//            direction = .right
//        }
//    }
//    return result
//}

//var x = 6
//
//generateMatrix(&x)

// STRINGS
// String Math
// Integer to Roman
private func numberOfDigits(in number: Int) -> Int {
    if abs(number) < 10 {
        return 1
    } else {
        return 1 + numberOfDigits(in: number/10)
    }
}

func buildRoman(starter: inout String, single: Character, mid: Character, max: Character, digit: Int) {
    let penmid = 4
    let midmid = 5
    let penultimate = 9
    var thisNum = digit
    
    if thisNum >= midmid && thisNum < penultimate {
        thisNum -= midmid
        buildRoman(starter: &starter, single: single, mid: mid, max: max, digit: thisNum)
        starter.insert(mid, at: starter.startIndex)
    } else if thisNum == 0 {
    } else if thisNum < penmid {
        for _ in 1...digit {
            starter.insert(single, at: starter.startIndex)
        }
    } else if thisNum == penmid {
        starter.insert(mid, at: starter.startIndex)
        starter.insert(single, at: starter.startIndex)
    } else if thisNum == penultimate {
        starter.insert(max, at: starter.startIndex)
        starter.insert(single, at: starter.startIndex)
    }
}

func intToRoman(_ num: Int) -> String {
    var result: String = ""
    let numLength: Int = numberOfDigits(in: num)
    
    if numLength > 0 {
        let ones: Int = num % 10
        buildRoman(starter: &result, single: "I", mid: "V", max: "X", digit: ones)
        if numLength > 1 {
            let tens: Int = ((num % 100) - ones)/10
            buildRoman(starter: &result, single: "X", mid: "L", max: "C", digit: tens)
            if numLength > 2 {
                let hundreds: Int = ((num % 1000) - tens - ones)/100
                buildRoman(starter: &result, single: "C", mid: "D", max: "M", digit: hundreds)
                if numLength > 3 {
                    let thousands: Int = ((num % 10000) - hundreds - tens - ones)/1000
                    buildRoman(starter: &result, single: "M", mid: "V", max: "X", digit: thousands)
                }
            }
        }
    }
    
    return result
}

// intToRoman(6)

// String Simulation
// Longest Common Prefix
func longestCommonPrefix(_ A: [String]) -> String {
    var result = [Character](A[0])
    
    for word in A {
        var wordChars = [Character](word)
        
        if result.count > wordChars.count {
            result = Array(result[0..<wordChars.count])
        }
        
        for i in 0..<result.count {
            if result[i] != wordChars[i] {
                result = Array(result[0..<i])
                break
            }
        }
    }
    return String(result)
}
