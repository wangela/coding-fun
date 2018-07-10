import Foundation

func meetingPlanner(slotsA: [[Int]], slotsB: [[Int]], dur: Int) -> [Int]? {
    var indexA = 0
    var indexB = 0
    
    while (indexA < slotsA.count && indexB < slotsB.count) {
        let start = max(slotsA[indexA][0], slotsB[indexB][0])
        let end = min(slotsA[indexA][1], slotsB[indexB][1])
        
        if end - start >= dur {
            return [start, start + dur]
        } else {
            if slotsA[indexA][1] < slotsB[indexB][1] {
                indexA += 1
            } else {
                indexB += 1
            }
        }
    }
    
    return nil
}

let sA = [[10, 50], [60, 120], [140, 210]]
let sB = [[0, 15], [60, 70]]

print(meetingPlanner(slotsA: sA, slotsB: sB, dur: 8))
