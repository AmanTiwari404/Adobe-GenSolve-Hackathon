<h2>Split It Up</h2><h3><p><span style="font-size: 18px;">Given a tree with <strong>n</strong> nodes and <strong>n-1</strong> edges. Each node in the tree has a weight assigned to it. The value of the tree is determined by adding up the weights of all the nodes in the tree. The weight of the <strong>i<sup>th</sup></strong> node is <strong>i</strong>.</span></p>
<p><span style="font-size: 18px;">Your task is to divide the tree into two separate trees by removing one of the edges. The goal is to find the best way to split the tree so that the absolute difference in values between the two resulting trees is as small as possible. Find the minimum difference of the values of the two trees after splitting the original tree.</span></p>
<blockquote>
<p><span style="font-size: 18px;"><strong>Note:</strong> Given <strong>n</strong> and two arrays <strong>A</strong> and <strong>B</strong>. <strong>A</strong> and <strong>B</strong> have a size of <strong>n-1</strong>, and there exists an edge between <strong>A[i]</strong> and <strong>B[i]</strong>.</span></p>
</blockquote>
<p><span style="font-size: 18px;"><strong>Constraints:</strong></span></p>
<ul>
<li><span style="font-size: 18px;">1 &lt;= n &lt;= 10<sup>5</sup></span></li>
<li><span style="font-size: 18px;">1 &lt;= A[i], B[i] &lt;= n</span></li>
<li><span style="font-size: 18px;">A[i] & B[i] form edges of a tree.</span></li>
</ul>
<p><span style="font-size: 18px;"><strong>Examples</strong></span></p>
<pre><span style="font-size: 18px;"><strong>Input:</strong> n = 3, A = {1, 1} B = {2, 3}
<strong>Output:</strong> 0
<strong>Explanation:</strong> You can remove the edge between 1 and 3 to get the minimum difference.</span></pre>
<pre><span style="font-size: 18px;"><strong>Input:</strong> n = 4, A = {1, 1, 1} B = {2, 3, 4}
<strong>Output:</strong> 2
<strong>Explanation:</strong> <img src="https://media.geeksforgeeks.org/img-practice/prod/addEditProblem/715473/Web/Other/blobid0_1687459250.png" alt="Explanation"></span></pre>
<p><span style="font-size: 18px;"><strong>Expected Time Complexity:</strong> O(n)<br><strong>Expected Auxiliary Space:</strong> O(n)&nbsp;</span></p>
</div>
