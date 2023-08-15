function solution(myString, pat) {
    let cPat = pat.toUpperCase()
    let cMyString = myString.toUpperCase()
    return cMyString.includes(cPat) ? 1 : 0
}