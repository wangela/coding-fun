func findMissingDrone(deliveryIdConfirmations: [Int]) -> Int {
    var missingID = 0
    
    for ID in deliveryIdConfirmations {
        missingID ^= ID
    }
    
    return missingID
}

let sampleIDs = [1, 2, 3, 4, 5, 6, 1, 2, 4, 5, 6]
findMissingDrone(deliveryIdConfirmations: sampleIDs)
