Undefined 是没有定义的变量


# 对象方法

const obj = new Object();
obj.sayName = function () {
    console.log('qianguyihao');
};

// 没加括号，就是获取方法
console.log(obj.sayName);
console.log('-----------');
// 加了括号，就是调用方法。即：执行函数内容，并执行函数体的内容
console.log(obj.sayName());



# 对象方法
是传递地址


# 基本数据数据类型，无法添加属性和方法

所以通过基本的包装类及进行
JS 为我们提供了三个基本包装类：

String()：将基本数据类型字符串，转换为 String 对象。
Number()：将基本数据类型的数字，转换为 Number 对象。
Boolean()：将基本数据类型的布尔值，转换为 Boolean 对象。

# js有内置的数组对象
var arr1 = ['a', 'b', 'c', 'd', 'e', 'f'];

# 函数
function fn1() {
	console.log('我是函数体里面的内容1');
}

function fn2() {
	console.log('我是函数体里面的内容2');
}

fn1(); // 调用函数

fn2.call(); // 调用函数


# 对于函数的参数也是可以的

fn(2, 4);
fn(2, 4, 6);
fn(2, 4, 6, 8);

function fn(a, b) {
    console.log(arguments);
    console.log(fn.length); //获取形参的个数
    console.log(arguments.length); //获取实参的个数

    console.log('----------------');
}



# 立即执行的函数
const sex = 'male';
const nickName = (function () {
  if (sex == 'male') {
    return '帅哥';
  } else {
    return '美女';
  }
})();

console.log(nickName);



# 函数的作用 this指针
内部存在this指针，可以可以传递成员变量和成员方法


function fun() {
    console.log(this);
    console.log(this.name);
}

var obj1 = {
    name: 'smyh',
    sayName: fun,
};

var obj2 = {
    name: 'vae',
    sayName: fun,
};

var name = '全局的name属性';

//以方法的形式调用，this是调用方法的对象
obj2.sayName();


# this 指针还有一些高级用法，apply什么的

暂时不需要了解

https://web.qianguyihao.com/04-JavaScript%E5%9F%BA%E7%A1%80/28-%E5%AF%B9%E8%B1%A1%E7%9A%84%E5%88%9B%E5%BB%BA&%E6%9E%84%E9%80%A0%E5%87%BD%E6%95%B0.html#%E5%88%9B%E5%BB%BA%E8%87%AA%E5%AE%9A%E4%B9%89%E5%AF%B9%E8%B1%A1%E7%9A%84%E5%87%A0%E7%A7%8D%E6%96%B9%E6%B3%95



# 对象总结
js中的对象都是动态的，和随时都能够进行转换


