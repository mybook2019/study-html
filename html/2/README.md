<div> 行之间

<span> 列之间


css 包括 选择器和样式


# 选择器

CSS 选择器是用来选取 HTML 元素并为其应用样式的工具。CSS 选择器种类非常多，可以根据不同的规则选择不同的元素。下面是常见的 CSS 选择器种类：

### 1. **基本选择器**
这些选择器用于选取单一元素或者元素组。

- **元素选择器（Type Selector）**：
  选择指定的 HTML 标签元素。
  ```css
  p {
      color: blue;
  }
  ```
  选择所有 `<p>` 元素。

- **类选择器（Class Selector）**：
  选择指定类名的所有元素，类名以 `.` 开头。
  ```css
  .my-class {
      color: red;
  }
  ```
  选择所有 class 为 `my-class` 的元素。

- **ID 选择器（ID Selector）**：
  选择指定 ID 的元素，ID 以 `#` 开头。
  ```css
  #my-id {
      color: green;
  }
  ```
  选择 ID 为 `my-id` 的元素。

- **通配符选择器（Universal Selector）**：
  选择所有元素。
  ```css
  * {
      color: black;
  }
  ```
  选择页面中的所有元素。

- **后代选择器（Descendant Selector）**：
  选择某个元素内部的所有子元素，不管深度。
  ```css
  div p {
      color: purple;
  }
  ```
  选择所有 `div` 标签内部的 `p` 元素。

- **子元素选择器（Child Selector）**：
  只选择直接子元素。
  ```css
  div > p {
      color: yellow;
  }
  ```
  只选择 `div` 元素下的直接 `p` 子元素。

- **相邻兄弟选择器（Adjacent Sibling Selector）**：
  选择紧接在指定元素后的兄弟元素。
  ```css
  h1 + p {
      color: orange;
  }
  ```
  选择紧接在 `h1` 后面的第一个 `p` 元素。

- **通用兄弟选择器（General Sibling Selector）**：
  选择某个元素后面所有相同父元素下的兄弟元素。
  ```css
  h1 ~ p {
      color: pink;
  }
  ```
  选择所有在 `h1` 后面的 `p` 元素。

### 2. **群组选择器**
群组选择器允许我们同时为多个选择器设置样式。

- **多个选择器组合**：
  通过逗号（`,`）将多个选择器组合在一起，给它们应用相同的样式。
  ```css
  h1, h2, h3 {
      color: brown;
  }
  ```
  选择 `h1`、`h2`、`h3` 元素，并为它们设置相同的颜色。

### 3. **属性选择器**
这些选择器根据元素的属性来选取元素。

- **基本属性选择器**：
  选择具有某个特定属性的元素。
  ```css
  input[type="text"] {
      background-color: yellow;
  }
  ```
  选择 `type` 为 `text` 的 `input` 元素。

- **部分匹配属性选择器**：
  根据属性值的一部分进行选择。
  - `^=`：匹配属性值以指定值开头。
  - `$=`：匹配属性值以指定值结尾。
  - `*=`：匹配属性值包含指定值。

  示例：
  ```css
  a[href^="https"] {
      color: blue;  /* 选择所有以 https 开头的链接 */
  }

  a[href$=".pdf"] {
      color: red;  /* 选择所有以 .pdf 结尾的链接 */
  }

  a[href*="example"] {
      color: green;  /* 选择所有包含 "example" 的链接 */
  }
  ```

### 4. **伪类选择器**
伪类选择器允许我们选择元素的特殊状态（例如鼠标悬停、焦点等）。

- **`:hover`**：
  选择当鼠标悬停在元素上的时候。
  ```css
  a:hover {
      color: red;
  }
  ```
  选择所有 `<a>` 元素，在鼠标悬停时设置颜色为红色。

- **`:active`**：
  选择被激活（点击）的元素。
  ```css
  a:active {
      color: green;
  }
  ```

- **`:focus`**：
  选择获取焦点的元素（通常是表单元素）。
  ```css
  input:focus {
      border-color: blue;
  }
  ```

- **`:nth-child()`**：
  选择特定的子元素，例如第 `n` 个元素。
  ```css
  li:nth-child(2) {
      background-color: gray;
  }
  ```
  选择每个父元素下第二个 `li` 元素。

- **`:nth-of-type()`**：
  选择特定类型的子元素。
  ```css
  p:nth-of-type(1) {
      color: pink;
  }
  ```

- **`:first-child`、`:last-child`**：
  选择父元素的第一个或最后一个子元素。
  ```css
  p:first-child {
      color: blue;
  }

  p:last-child {
      color: red;
  }
  ```

- **`:not()`**：
  选择不符合某个选择器的元素。
  ```css
  p:not(.highlight) {
      color: gray;
  }
  ```
  选择所有不包含 `.highlight` 类的 `p` 元素。

### 5. **伪元素选择器**
伪元素选择器用于选取元素的特定部分（如首字母、首行等）。

- **`:before`**：
  在元素的内容前插入内容。
  ```css
  p::before {
      content: "★";
      color: gold;
  }
  ```

- **`:after`**：
  在元素的内容后插入内容。
  ```css
  p::after {
      content: "★";
      color: gold;
  }
  ```

- **`:first-letter`**：
  选择元素的首字母。
  ```css
  p::first-letter {
      font-size: 2em;
      font-weight: bold;
  }
  ```

- **`:first-line`**：
  选择元素的首行。
  ```css
  p::first-line {
      font-variant: small-caps;
  }
  ```

### 6. **组合选择器**
组合选择器可以通过多个选择器的组合来选择元素。

- **后代选择器**：
  选择元素内部的后代元素（包括嵌套）。
  ```css
  div p {
      color: red;
  }
  ```

- **子元素选择器**：
  选择直接子元素。
  ```css
  div > p {
      color: blue;
  }
  ```

- **相邻兄弟选择器**：
  选择紧接在某个元素后的兄弟元素。
  ```css
  h1 + p {
      color: green;
  }
  ```

### 7. **媒体查询选择器**
用于根据设备的特性（如屏幕大小、分辨率等）应用不同的样式。

```css
@media screen and (max-width: 600px) {
    .container {
        flex-direction: column;
    }
}
```

### 总结：
CSS 选择器种类繁多，可以根据不同的需求选择合适的选择器来精确定位元素，从而为页面应用样式。掌握不同类型的选择器，有助于更高效地进行网页样式设计。