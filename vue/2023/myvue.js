const app = Vue.createApp({
    data(){
        return{
            message: "Hello duniya"
        }
    }
})

app.mount('#app')



class FindLarge{

    arr = [50, 20, 30, 77, 59]

    #name = 'Al Mamun'

    getName(){
        return this.#name + ' ' + this.arr;
    }

}

class Largeds extends FindLarge{

    arr = [...this.arr, 550];

    msg = this.getName() + ' Hello';



}




// Created Object
const Larged = new Largeds;

var largest = [0]
for (let j = 0; j < Larged.arr.length; j++) {
    if(Larged.arr[j] > largest[0]){
        largest[0] = Larged.arr[j]

    }
}
console.log(largest[0])

const largeNumber = Vue.createApp({
    data(){
        return{
            message: Larged.msg,
            numArr: Larged.arr,
            numArrLg: largest[0]
        }
    }
})
largeNumber.mount('#largeNumber')