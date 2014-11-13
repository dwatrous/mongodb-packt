use coursetracker

# Student
db.student.insert(
  {"name": {"first": "John", "last": "Shore"}, "email": "john.shore@gmail.com", "major": "Electrical Engineering", "test_scores": [{"test": "ACT", "score": 34}, {"test": "SAT", "score": 680}], "course_gpas": [3.09, 2.72, 2.83, 3.16, 2.99, 3.49, 3.96, 2.22, 2.69, 2.12, 2.84, 2.8, 3.83, 2.62, 3.47, 2.9, 2.78, 2.77, 3.54, 2.13, 2.0, 3.97, 3.27, 3.63, 2.63, 2.41, 4.0, 2.88]}
);
db.student.find().pretty();

# Instructor
db.instructor.insert(
  {"name": {"first": "Wally", "middle": "r", "last": "Binns"}, "email": "wally.r.binns@ssu.edu", "bio": "I was born in the middle of my mother's doctoral dissertation on Faraday Cage isolation. I've been an academic ever since...", "publications": [], "courses": []}
)
db.instructor.find().pretty();

# Course
db.course.insert(
  {"name": "History of the World 1010", "description": "A bunch of really interesting things that actually happened", "number_of_students": 0, "evaluations": []}
);
db.course.find().pretty();

# show stats for the student collection
db.student.stats(1024)

#### Updating MongoDB ####

# Update
db.course.update({}, {$set: {"name": "An Interesting History of the World 1010"}});
db.course.find().pretty();

# Update entire document (doesn't update a value, but replaces the entire document)
#db.course.update({}, {name: "An Interesting History of the World 1010"});
#db.course.find().pretty();

# Increment number_of_students in a course
db.course.update({}, {$inc: {"number_of_students": 1}});
db.course.find().pretty();

# Evaluation
db.course.update({},{$push: {"evaluations": {"eval_comment": "This course was fabulous..."}}});
db.course.find().pretty();

