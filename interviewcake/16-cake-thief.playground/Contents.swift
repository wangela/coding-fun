import Foundation

struct CakeType {
    let weight: Int
    let value: Int
}

func maxDuffelBagValue(for cakeTypes: [CakeType], with capacity: Int) -> Int {
    var maxValueForCapacities: [Int] = Array(repeating: 0, count: capacity + 1)
    
    for x in 0...capacity {
        var maxValueForCapacity = 0
        for cake in cakeTypes {
            if cake.weight == 0 && cake.value > 0 {
                return Int.max
            }
            if cake.weight <= x {
                let remainingCapacity = x - cake.weight
                let valueWithCake = cake.value + maxValueForCapacities[remainingCapacity]
                maxValueForCapacity = max(valueWithCake, maxValueForCapacity)
            }
        }
        maxValueForCapacities[x] = maxValueForCapacity
    }

    return maxValueForCapacities[capacity]
}




func maxDuffelBagValue2(for cakeTypes: [CakeType], withCapacity weightCapacity: Int) -> Int {
    
    // we make an array to hold the maximum possible value at every
    // duffel bag weight capacity from 0 to weightCapacity
    // starting each index with value 0
    var maxValuesAtCapacities: [Int] = Array(repeating: 0, count: Int(weightCapacity) + 1)
    
    for currentCapacity in 0...weightCapacity {
        
        // set a variable to hold the max monetary value so far for currentCapacity
        var currentMaxValue: Int = 0
        
        for cakeType in cakeTypes {
            
            // if a cake weighs 0 and has a positive value the value of our duffel bag is infinite!
            if cakeType.weight == 0 && cakeType.value != 0 {
                return 0
            }
            
            // if the current cake weighs as much or less than the current weight capacity
            // it's possible taking the cake would get a better value
            if cakeType.weight <= currentCapacity {
                
                // so we check: should we use the cake or not?
                // if we use the cake, the most kilograms we can include in addition to the cake
                // we're adding is the current capacity minus the cake's weight. we find the max
                // value at that integer capacity in our array maxValuesAtCapacities
                let maxValueUsingCake = cakeType.value + maxValuesAtCapacities[Int(currentCapacity - cakeType.weight)]
                
                
                // now we see if it's worth taking the cake. how does the
                // value with the cake compare to the currentMaxValue?
                currentMaxValue = max(maxValueUsingCake, currentMaxValue)
            }
        }
        
        // add each capacity's max value to our array so we can use them
        // when calculating all the remaining capacities
        maxValuesAtCapacities[Int(currentCapacity)] = currentMaxValue
    }
    
    return maxValuesAtCapacities[Int(weightCapacity)]
}

let cakeType1 = CakeType(weight: 7, value: 160)
let cakeType2 = CakeType(weight: 3, value: 90)
let cakeType3 = CakeType(weight: 2, value: 15)
let someTypes = [cakeType1, cakeType2, cakeType3]
maxDuffelBagValue(for: someTypes, with: 10)
maxDuffelBagValue2(for: someTypes, withCapacity: 10)
