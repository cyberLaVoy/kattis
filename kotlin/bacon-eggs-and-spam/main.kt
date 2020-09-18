
fun main(args: Array<String>) {
    var orders = mutableMapOf<String, MutableList<String>>()
    var numCustomers = readLine()!!.toInt()
    while (numCustomers != 0) {
        for (i in 0..numCustomers-1) {
            var order = readLine()!!.split(' ')
            var name = order[0]
            for (j in 1..order.size-1) {
                if (order[j] !in orders) {
                    var names = mutableListOf<String>()
                    orders.put(order[j], names)
                }
                orders.get(order[j])!!.add(name)
            }
        }
        for ( key in orders.keys.sorted() ) {
            print(key + ' ')
            for (name in orders[key]!!.sorted()) {
                print(name + ' ')
            }
            println()
        }
        println()
        orders.clear()
        numCustomers = readLine()!!.toInt()
    }
}