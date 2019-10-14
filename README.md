# solutionAssignment2
This is a solution to the Assignment problem at https://hackmd.io/@N7nxXdBFSk6_7dihdnv-xg/SywqoqyJE?type=view


Following is complete problem statement for reference

	Assignment 2: Parse blogposts

	We have a large number of blog posts which are stored in files. The task is to parse the file and convert the data in the file into a json object(or a dictionary/hash data structure if json support is not present in the language of your choice).
  
	DO NOT USE ANY KIND OF MARKDOWN OR BLOG PARSERS FOR THIS ASSIGNMENT.

	INPUT (SAMPLE BLOG POST FILE)
	---
	title: "What is SRP?"
	description: "SRP is a programming paradigm which advocates code writing as per responsibility."
	preview_image: /images/blog/2018/what-is-srp/article-header.png
	section: blog
	author: John Doe
	date: 2018-01-08 10:00 UTC
	tags: Development, Programming, principle
	published: true
	---

	The single responsibility principle is a computer programming principle that states that every module, class, or function[1] should have responsibility over a single part of the functionality provided by the software, and that responsibility should be entirely encapsulated by the class. All its services should be narrowly aligned with that responsibility. Robert C. Martin expresses the principle as, "A class should have only one reason to change,"[1] although, because of confusion around the word "reason" he more recently stated "This principle is about people.(Actor)"[2]

	READMORE

	![SRP](/images/blog/2018/what-is-srp/article-header.png)

	## History

	CThe term was introduced by Robert C. Martin in an article by the same name as part of his Principles of Object Oriented Design,[3] made popular by his book Agile Software Development, Principles, Patterns, and Practices.[4] Martin described it as being based on the principle of cohesion, as described by Tom DeMarco in his book Structured Analysis and System Specification,[5] and Meilir Page-Jones in The Practical Guide to Structured Systems Design.[6] In 2014 Martin wrote a blog post entitled The Single Responsibility Principle with a goal to clarify what was meant by the phrase "reason for change."

	## Annotation Types
	
	OUTPUT (JSON or Dictionary)
	{
	  "title": "What is SRP?",
	  "description": "SRP is a programming paradigm which advocates code writing as per responsibility.",
	  "author": "John Doe",
	  "date": "2018-01-08 10:00 UTC",
	  "tags": ["Development", "Programming", "principle"],
	  "published": true,
	  "short-content": "The single responsibility principle is a computer programming principle that states that every module, class, or function[1] should have responsibility over a single part of the functionality provided by the software, and that responsibility should be entirely encapsulated by the class. All its services should be narrowly aligned with that responsibility. Robert C. Martin expresses the principle as, 'A class should have only one reason to change,'[1] although, because of confusion around the word 'reason' he more recently stated 'This principle is about people.(Actor)''[2]",
	  "content": "![SRP](/images/blog/2018/what-is-srp/article-header.png) ## History The term was introduced by Robert C. Martin in an article by the same name as part of his Principles of Object Oriented Design,[3] made popular by his book Agile Software Development, Principles, Patterns, and Practices.[4] Martin described it as being based on the principle of cohesion, as described by Tom DeMarco in his book Structured Analysis and System Specification,[5] and Meilir Page-Jones in The Practical Guide to Structured Systems Design.[6] In 2014 Martin wrote a blog post entitled The Single Responsibility Principle with a goal to clarify what was meant by the phrase 'reason for change.## Annotation Types"
	}
	
	Key short-content in output json is used to show a short glimpse of the blog post.
	Key content is used to show the complete blog post content.

	The fields such as name, description, tags etc. can differ for different blogposts such as has_comments can also appear in metadata section which is not present in the file given above.

	Parse this blog post and store data in json format without using any mardown parsers.

	Feel free to save this blog file(.md or .txt) for the sake of convenience.

	Use the data structures provided by the language of your choice to parse the document.
