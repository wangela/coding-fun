/*:
 func flattenDictionaryHelper(initialKey: String, dict: [String: Any], flatDict: inout [String: String]) {
    for key in dict.keys {
        let val = dict[key]
        
        if val is Dictionary<String: Any> {
            guard let val = val as? [String: Any] else {
                return
            }
            if initialKey == "" {
                flattenDictionaryHelper(initialKey: key, dict: val, flatDict: &flatDict)
            } else {
                flattenDictionaryHelper(initialKey: initialKey + "." + key, dict: val, flatDict: &flatDict)
            }
        } else {
            guard let val = val as? String else {
                return
            }
            if initialKey == "" {
                flatDict[key] = val
            } else {
                flattenDictionaryHelper(initialKey: initialKey + "." + key, dict: dict, flatDict: &flatDict)
            }
        }
    }
}

func flattenDictionary(dict: [String: Any]) -> [String: String] {
    var flatDictionary: [String: String] = [:]
    flattenDictionaryHelper(initialKey: "", dict: dict, flatDict: &flatDictionary)
    
    return flatDictionary
}
*/
func findGrantsCap(grantsArray: [Double], newBudget: Double) -> Double {
    grantsArray.sort()
    
}
