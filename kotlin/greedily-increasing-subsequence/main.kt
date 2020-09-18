
fun main(args: Array<String>) {
    val max = readLine()!!.toInt()
    val sequence = readLine()!!.split(' ').map(String::toInt)
    var greedilyIncreasing = mutableListOf<Int>()
    var highestFound = sequence[0]
    greedilyIncreasing.add(highestFound);
    for (v in sequence) {
        if (v > highestFound) {
            highestFound = v
            greedilyIncreasing.add(highestFound);
        }
        if (highestFound == max) {
            break
        }
    }
    println(greedilyIncreasing.size)
    for (v in greedilyIncreasing) {
        print(v)
        print(' ')
    }
    println()
}