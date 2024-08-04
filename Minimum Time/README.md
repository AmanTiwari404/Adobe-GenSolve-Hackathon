<h2>Minimum Time</h2><p><span style="font-size: 18px;">Geek being the brightest student of the class is given the task to solve <strong>n</strong> puzzles by his teacher in minimum possible time. The puzzles are numbered from 1 to n and he has to complete them in the order of their numbers. Geek can solve a puzzle in two ways: either solve on his own or he can copy from his book. As Geek is busy these days, he has asked for your help to calculate the minimum possible time in which he can solve all puzzles in the order of their numbers.</span></p>
<p><span style="font-size: 18px;">For you to do this task, he has provided an array of integers <strong>time[]</strong> of size <strong>n</strong> where <strong>time[i]</strong> tells the time Geek would have taken to solve the <strong>i<sup>th</sup></strong> puzzle on his own. Also, he gave you an integer array <strong>search[]</strong> of size <strong>n</strong> where <strong>search[i]</strong> represents the time Geek will take to search the <strong>i<sup>th</sup></strong> puzzle in his book. When Geek searches for the <strong>i<sup>th</sup></strong> puzzle, he also gets to know the answer for the next <strong>k</strong> puzzles (including the <strong>i<sup>th</sup></strong> puzzle). If fewer than <strong>k</strong> puzzles exist after <strong>i</strong>, then he gets answers for all remaining puzzles including <strong>i</strong>. After the search, he can directly jump to any puzzle (<strong>i+j</strong>) where <strong>1-j &lt;= min(k, n-i)</strong> by copying answers for all puzzles from index <strong>i</strong> to (<strong>i+j-1</strong>). It is not necessary for Geek to copy all <strong>k</strong> puzzles after <strong>i</strong> when he searched in the book for the <strong>i<sup>th</sup></strong> puzzle. You have to determine the minimum time Geek will take to solve all puzzles.</span></p>
<blockquote>
<p><span style="font-size: 18px;"><strong>Note:</strong> Copying answers does not take any time and it is not necessary for Geek to copy all <strong>k</strong> puzzles.</span></p>
</blockquote>
<p><span style="font-size: 18px;"><strong>Constraints:</strong></span></p>
<ul>
<li><span style="font-size: 18px;">1 &lt;= n &lt;= 10<sup>3</sup></span></li>
<li><span style="font-size: 18px;">1 &lt;= k &lt;= n</span></li>
<li><span style="font-size: 18px;">1 &lt;= time[i] &lt;= 10<sup>5</sup></span></li>
<li><span style="font-size: 18px;">1 &lt;= search[i] &lt;= 10<sup>5</sup></span></li>
</ul>
<p><span style="font-size: 18px;"><strong>Examples</strong></span></p>
<pre><span style="font-size: 18px;"><strong>Input:</strong> n = 4, k = 2, time = {3, 1, 8, 7}, search = {4, 4, 6, 2}
<strong>Output:</strong> 9
<strong>Explanation:</strong> Optimal way to solve all puzzles is to solve puzzle 1 on your own that will take 3 mins and then we can search for puzzle 2 in the book that will take 4 units of time and also by doing this search we will also know the answer for puzzle 3, which we can directly copy. Now again for puzzle 4, we can just search and copy the answer. So total it takes 3+4+2 = 9 mins to complete all puzzles.</span></pre>
<pre><span style="font-size: 18px;"><strong>Input:</strong> n = 3, k = 1, time = {1, 2, 2}, search = {4, 6, 6}
<strong>Output:</strong> 5
<strong>Explanation:</strong> It is optimal to solve all the problems on your own. So the answer is (1+2+2) = 5.</span></pre>
<p><span style="font-size: 18px;"><strong>Expected Time Complexity:</strong> O(n*k)<br><strong>Expected Auxiliary Space:</strong> O(n)&nbsp;</span></p>
</div>
