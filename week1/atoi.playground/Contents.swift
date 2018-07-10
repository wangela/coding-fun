import Foundation

func stripLeadingSpace(a: String) -> String {
    if let whiteRange = a.range(of: "^ +", options: .regularExpression) {
        let end = whiteRange.upperBound
        if end == a.endIndex {
            return ""
        } else {
            return String(a[end...])
        }
    }
    
    return a
}

let test = "20000000000000000000"
stripLeadingSpace(a: test)

func atoi(_ str: String) -> Int {
    /*
    1. Discard whitespace (' ') characters until first non-whitespace character is found.
    2. Consider optional + or - sign
    3. Interpret numerical digits as numerical values
    4. Ignore any characters after the numbers
    If the first non-whitespace characters are not a valid integral number, no conversion
     If no conversion, return 0

    */
    var negative: Bool = false
    var n: Int = 0
    
    if str.count == 0 {
        return 0
    }
    
    // Step 1
    var stripped = stripLeadingSpace(a: str)
    if stripped.count == 0 {
        return 0
    }

    // Step 2 - begin
    if stripped[stripped.startIndex] == "-" && stripped.count > 1 {
        negative = true
        stripped = String(stripped[stripped.index(stripped.startIndex, offsetBy: 1)...])
    } else if stripped[stripped.startIndex] == "+" && stripped.count > 1 {
        stripped = String(stripped[stripped.index(stripped.startIndex, offsetBy: 1)...])
    }

    // Step 4
    guard let numRange = stripped.range(of: "^[0-9]*", options: .regularExpression) else {
        // Catch if first non-whitespace characters are invalid
        return 0
    }
    let end = numRange.upperBound
    stripped = String(stripped[..<end])
    
    // Step 3
    guard let num = Int(stripped) else {
        print(9)
        return 0
    }
    
    // Step 2 - complete
    n = num
    if negative {
        n.negate()
        if n < Int32.min {
            return Int(Int32.min)
        }
    }
    if n > Int32.max {
        return Int(Int32.max)
    }
    
    return n
}

print(atoi(test))
