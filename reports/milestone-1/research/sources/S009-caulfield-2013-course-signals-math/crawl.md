---
id: S009
url: https://hapgood.us/2013/09/26/why-the-course-signals-math-does-not-add-up/
requested: https://hapgood.us/2013/09/26/why-the-course-signals-math-does-not-add-up/
fetched: 2026-11-02T00:51+07:00
tool: fetch.py (curl + html-text; ladder L1)
fetch_prompt: "none (full text conversion, not a model extract)"
status: ok
task: T03
part: 5
raw: raw.html (182 KB)
conversion: html-text of https://hapgood.us/2013/09/26/why-the-course-signals-math-does-not-add-up/ (readable, 1916 words)
---
title: Why the Course Signals Math Does Not Add Up – Hapgood

Skip to content

-
-
-
-

# Hapgood

Mike Caulfield's latest web incarnation. Networked Learning, Open Education, and Online Digital Literacy

September 26, 2013

## Why the Course Signals Math Does Not Add Up

I see that there’s a new Course Signals press release out that claims Course Signals boosts graduation rate 21%. Or, more exactly, it claims taking *two* classes using Course Signals boosts graduation rates by 21%.

Why does it claim that? Well, I haven’t looked at the new data, but I did look at it last year, and assuming the trends didn’t change it’s because taking *one* CS course correlates with a *lower* retention rate than the non-CS population.

(Note that Purdue has since moved this study off their site). UPDATE: Found a version of this study, moved here.

The press release then contains this maddening quote:

“For some reason, two courses is the magic number. Taking just one course with Course Signals is beneficial for students, but we’ve seen significant improvement when students are enrolled in at least two courses using the system,” Pistilli says.

“We need to continue to do more research on why this is significant,” Pistilli continues. “We think it is because if a student gets feedback from two different instructors, they can make better links between their performance and their behaviors. For example, a student may be taking a course in biology and and another in communications, which are very different courses, but if they get the same feedback in both courses about study habits and needing to spend more time on task – and they hear suggestions on how to improve from two different professors – they appear to make the change. What’s notable is that this improvement stays with them in their other courses and for the rest of their academic careers.”

Ok, that’s a great theory about the “magic number”. But I actually have another one.

Only a portion of Purdue’s classes are Course Signals classes, so the chance any course a freshman takes is a Course Signals course can be expressed as a percentage, say 25%. In an overly dramatic simplification of this model, a freshman who takes four classes the first semester and drops out has a has about a 16% chance of having taken two Course Signals courses (as always, beware my math here, but I think I’m right). Meanwhile they have a 74% chance of having taken 1 or fewer, and a 42% chance of having taken exactly one.

What about about a student who does *not* drop out first semester, and takes a full load of five courses each semester? Well, the chance of that student having two or more Course Signals courses is 75%. That’s right — just by taking a full load of classes and not dropping out first semester you’re likely to be tagged as a CS 2+ student.

In other words, each class you take is like an additional coin flip. A lot of what Course Signals “analysis” is measuring is how many classes students are taking.

Are there predictions this model makes that we can test? Absolutely. As we saw in the above example, at a 25% CS adoption rate, the median dropout has a 42% chance of having taken exactly one CS course. So it’s quite normal for a dropout to have had a CS course. But early on in the program the adoption rate would have much lower. What are the odds of a first semester dropout having a CS course in those early pilots? For the sake of argument let’s say adoption at that point was 5%. In that case, the chance our 4-course semester drop out would have exactly one CS course drops from 42% to 17%. In other words, as adoption grows having had one course in CS will cease to be a useful predictor of first to second-year persistence.

Is that what we see? Assuming adoption grew between 2007 and 2009, that’s *exactly* what we see. Here’s the early pilot days of Course Signals:

As you can see, in what were likely the lower adoption days taking one Course Signals course is a huge predictor of persistence. The one year retention rate is 97% for the one-CS course student, compared to just 83% for the no-CS student. As adoption expands, changing the median experience of the drop out, that difference disappears, just like the model predicts:

Two years later, that retention effect has disappeared entirely, with the same percentage of one-CS students dropping out as non-CS students. Why? Without access to dropout data, I can’t say for sure. But I submit a large part of the shift of one-CS as predictor of retention to one-CS as non-predictor is that having one-CS class is now the average experience of both low course-load students and first semester dropouts. The effect disappears because the confounding variable is no longer correlated with the dependent variable.

So, do I believe that Course Signals works? Maybe, it’s possible. There are other measures with grades and such that look a bit more promising. But the problem is that until they control for this issue, the percentage increases they cite might as well be random numbers. It would be trivially easy to account for these things — for example, by removing first semester dropouts from the equation, and only looking at students under full course load. When I looked at the (now removed) 2012 report, I saw nothing to indicate they had done these things. Now, in 2013, I still see nothing to indicate they have taken these factors into account.

I could be wrong. I’m a Literature and Linguistics M.A. who works in educational technology, not a statistician. But if I am right, this is sloppy, sloppy work.

### Share this:

-
Share on Facebook (Opens in new window)
Facebook

-
Share on X (Opens in new window)
X

-

Like Loading…

Mike Caulfield

Posted by:

mikecaulfield

The infolit guy.

«Previous Post

Next Post»

### 18 responses to “Why the Course Signals Math Does Not Add Up”

-

Digging into the Purdue Course Signals Results |e-Literate

September 26, 2013 at 12:34 pm

[…] spectacular Mike Caulfield casts a skeptical eye on the Course Signals […]

Reply

-

Ted

September 27, 2013 at 11:43 am

Check the math (or typo) on a 16% chance of a student taking 2 CS courses if they take 4 courses first semester then drop out. I get 26%, which is confirmed by your statement of “74% chance of having taken 1 or fewer”–this directly implies 26% chance of having taken 2 or more.

Reply

-

A Simple, Less Mathematical Way to Understand the Course Signals Issue | Hapgood

September 26, 2013 at 1:38 pm

[…] Why the Course Signals Math Does Not Add Up → […]

Reply

-

Reflections on “Purdue software boosts graduation rate 21 percent” [Purdue.edu]

September 27, 2013 at 7:38 am

[…] Why the Course Signals Math Does Not Add Up — from hapgood.us. by Mike Caulfield […]

Reply

-

Pamela Wik-Grimm (@pwikgrimm)

September 27, 2013 at 8:36 am

Thanks for saying it. Much of what passes for data-proven “facts” is simply someone who does not really understand regression formulas and how to cancel out for unrelated factors publishing a faulty analysis. The emperor has no clothes — glad to hear you say so. #awesome

Reply

-

Hack Education Weekly News: Students “Hack” Their iPads, the MacArthur Genius Grants, and More

September 27, 2013 at 11:42 am

[…] about course performance. More details on the study will be published soon, good news since Mike Caulfield is already looking at the claims with some […]

Reply

-

Ted

September 27, 2013 at 2:41 pm

Think I put this in the wrong spot the first time:

Check the math (or typo) on a 16% chance of a student taking 2 CS courses if they take 4 courses first semester then drop out. I get 26%, which is confirmed by your statement of “74% chance of having taken 1 or fewer”–this directly implies 26% chance of having taken 2 or more.

Reply

-

Mike Caulfield (@holden)

September 30, 2013 at 10:59 am

Thanks Ted, I noticed the typo myself just after posting. I appreciate the heads up, so easy to get lost in the numbers when working through something like this — which I guess is one reason I’ve left comments on. 😉

Reply

-

Can We Improve Retention Rates by Giving Students Chocolates? | Analytics | Innovation | Research

October 14, 2013 at 3:15 am

[…] I owe the insight to Mike Caulfield who pointed out anomalies in the data and re-framed, correctly I believe, how the Course Signals data should be viewed. The aim of the […]

Reply

-

Looking harder at Course Signals | Doug Clow's Imaginatively-Titled Blog

November 13, 2013 at 6:51 am

[…] in August, Mike Cauldfield spotted a problem, which he expanded on in late September when he saw a Purdue press release repeating the claim. The Purdue researchers didn’t appear […]

Reply

-

Jonathan D. Becker, J.D., Ph.D. – Learning, Analytics, Assessment, Big Data, etc.

November 15, 2013 at 9:45 am

[…] been released as a commercial product by Ellucian called CourseSignals). That research has been called into question by the great Mike Caulfield. Also, Alfred Essa, who, interestingly, works for McGraw-Hill, ran some simulations to effectively […]

Reply

-

sell

April 2, 2014 at 12:00 am

Howdy would you mind sharing which blog

platform you’re using? I’m planning to start my own blog soon but I’m having a tough time deciding

between BlogEngine/Wordpress/B2evolution and Drupal.

The reason I ask is because your design and style seems different then most

blogs and I’m looking for something completely unique.

P.S Sorry for being off-topic but I had to ask!

Reply

-

The problem of agency | þoht-hord

July 7, 2014 at 9:36 am

[…] responded to an Anya Kamenetz story on Purdue’s Course Signals initiative. Course Signals reported successes have been questioned, but I want to focus on something else. Warner […]

Reply

-

Certified Nursing

August 20, 2014 at 4:24 pm

Generally, your certification will lapse after a period of 24

months without completing any paid healthcare work.

For instance, a school nurse gets a fixed salary with small yearly

increases, but gets excellent benefits from the state or

county that includes a generous vacation package and retirement plan. Failure

rates are high as the pass rate for the test is 90% or more.

Reply

-

http://cnatrainingonline00.wordpress.com

September 17, 2014 at 10:20 pm

– Ensuring sufferers do their regular physical exercise and

supporting wherein needed. I have attended training sessions in (insert name of some training you have done in recent years), and am

very interested in continuing to develop my skills in this area.

They could be on offer at private hospitals, on-going care organisations and various other wellness

establishments.

Reply

-

Can We Improve Retention Rates by Giving Students Chocolates? – stlyoga

October 11, 2016 at 11:04 am

[…] I owe the insight to Mike Caulfield who pointed out anomalies in the data and re-framed, correctly I believe, how the Course Signals data should be viewed. The aim of the […]

Reply

-

Can We Improve Retention Rates by Giving Students Chocolates? – Alfred Essa

October 20, 2016 at 6:27 pm

[…] I owe the insight to Mike Caulfield who pointed out anomalies in the data and re-framed, correctly I believe, how the Course Signals data should be viewed. The aim of the […]

Reply

-

Course Signals Effectiveness Data Appears to be Meaningless (and Why You Should Care) -e-Literate

April 26, 2017 at 1:55 pm

[…] problem was speculatively raised and then re-explained by Mike Caulfield (who we are proud to now have as an e-Literate featured […]

Reply

### Leave a Reply Cancel reply

### About Me

My current work focuses on how students and citizens can use AI for “co-reasoning”, learning to tap into the power of LLMs to both model and critique arguments.

As creator of the SIFT methodology, I have taught thousands of teachers and students how to verify claims and sources through his workshops. My book with Sam Wineburg, Verified: How to Think Straight, Get Duped Less, and Make Better Decisions about What to Believe Online, was published by the University of Chicago Press in November 2023.

- Tumblr

- Share Icon

- Instagram

### Recent Posts

- Couch to 4k (my film podcast) is now on Spotify

- I’m a film podcaster now

- The structure of a #DiedSuddenly argument

- The open argument must be fed: The peculiar case of Fox News and the pleasant smoke

- Reasonableness: An Introduction

### Newsletter

###

-
-
-

###

###

-

Comment

-

Reblog

-

Subscribe

Subscribed

Hapgood

Have a WordPress.com account? Log in now.

-

Hapgood

Copy shortlinkView post in Reader

Manage subscriptionsSign upLog in

Report this content

Collapse this bar

%d
