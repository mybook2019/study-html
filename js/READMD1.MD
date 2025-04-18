# js的事件

事件的三要素
事件的三要素：事件源、事件、事件驱动程序。

```javascript
<body>
<div id="box1"></div>

<script type="text/javascript">
    // 1、获取事件源
    var div = document.getElementById("box1");
    // 2、绑定事件
    div.onclick = function () {
        // 3、书写事件驱动程序
        alert("我是弹出的内容");
    }
</script>

</body>
```

# DOM

DOM：文档对象模型（Document object Model），操作网页上的元素的API。比如让盒子移动、变色、轮播图等。

BOM：浏览器对象模型（Browser Object Model），操作浏览器部分功能的API。比如让浏览器自动滚动。


DOM的数据结构如下：

![img](https://jiangshuying-1253623030.cos.ap-guangzhou.myqcloud.com/new_linux/typoar/img/liuhaocun/20180126_2105.png)

在HTML当中，一切都是节点（非常重要）

兄弟、父亲、孩子

# 设置行类样式


在DOM当中，如果想设置样式，有两种形式：

    className（针对内嵌样式）

    style（针对行内样式）

这篇文章，我们就来讲一下style。

需要注意的是：style是一个对象，只能获取行内样式，不能获取内嵌的样式和外链的样式。例如：



行内样式具有最高的优先级


当然可以！下面是对你提到的JS动画主要内容的详细讲解：

### 1. 三大家族和一个事件对象

#### 三大家族
- **offset**: 这个系列主要涉及元素相对于其最近的定位祖先元素的位置。使用 `offsetTop` 和 `offsetLeft` 属性可以获取元素的偏移量。
  
- **scroll**: 这个系列涉及页面的滚动位置。使用 `scrollTop` 和 `scrollLeft` 属性可以获取或设置元素的滚动位置。对于整个文档，可以使用 `window.scrollY` 和 `window.scrollX`。

- **client**: 这个系列涉及元素的可视区域。使用 `clientWidth` 和 `clientHeight` 属性可以获取元素的可见宽度和高度。

#### 事件对象
- **事件对象**: 当事件被触发时，JavaScript会创建一个事件对象，包含有关事件的信息（如鼠标位置、按下的键等）。可以通过事件处理函数的参数访问这个对象，通常命名为 `event` 或 `e`。常用的属性包括：
  - `event.type`: 事件的类型（如 `click`、`keydown`）。
  - `event.target`: 触发事件的元素。
  - `event.clientX` 和 `event.clientY`: 鼠标相对于视口的位置。

### 2. 动画类型

- **闪现**: 这种动画通常是瞬间的变化，可能是元素的显示和隐藏，或者颜色的快速切换。

- **匀速**: 动画以恒定的速度进行，元素在一定时间内以相同的速率移动。

- **缓动**: 这种动画的速度在开始和结束时较慢，中间较快，常用于使动画看起来更自然。常见的缓动函数有线性、二次方、三次方等。

### 3. 冒泡/兼容/封装

- **冒泡**: 事件冒泡是指事件从最具体的元素（事件目标）向上冒泡到最不具体的元素（通常是 `document`）。可以通过 `event.stopPropagation()` 来阻止事件冒泡。

- **兼容**: 在不同浏览器中，事件处理的实现可能有所不同，因此需要编写兼容性代码，以确保在所有浏览器中都能正常工作。例如，使用 `addEventListener` 和 `attachEvent` 来处理事件。

- **封装**: 封装是指将动画逻辑封装在函数或对象中，以便于重用和维护。可以创建一个动画库，提供简单的接口来执行各种动画效果。

希望这些解释能帮助你更好地理解JS动画的主要内容！如果你有任何具体问题或需要更深入的讲解，请随时问我。



# 事件委托
总结：事件委托是利用了冒泡机制，减少了事件绑定的次数，减少内存消耗，提高性能。


我们希望，只绑定一次事件，即可应用到多个元素上，即使元素是后来添加的。


因此，比较好的方法就是把这个点击事件绑定到他的父层，也就是 ul 上，然后在执行事件函数的时候再去匹配判断目标元素


# 鼠标键盘事件

onkeydown：按键被按下。
onkeyup：按键被松开



# BOM 操作浏览器对象
JavaScript的组成

JavaScript基础分为三个部分：

    ECMAScript：JavaScript的语法标准。包括变量、表达式、运算符、函数、if语句、for语句等。

    DOM：文档对象模型（Document object Model），操作网页上的元素的API。比如让盒子移动、变色、轮播图等。

    BOM：浏览器对象模型（Browser Object Model），操作浏览器部分功能的API。比如让浏览器自动滚动。




