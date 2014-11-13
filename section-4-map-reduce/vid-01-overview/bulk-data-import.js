// create student records
db.students.insert({"_id": "john.shore", "name": {"first": "John", "last": "Shore"}, "email": "john.shore@gmail.com", "major": "Electrical Engineering"})
db.students.insert({"_id": "jeff", "name": {"first": "Jeff", "last": "Holland"}, "email": "jeff@yahoo.com", "major": "Business"})
db.students.insert({"_id": "scott", "name": {"first": "Scott", "last": "Mills"}, "email": "scott@hotmail.com", "major": "Humanities/Art"})
db.students.insert({"_id": "rcotter", "name": {"first": "Ray", "last": "Cotter"}, "email": "rcotter@msn.com", "major": "Computer Science"})
db.students.insert({"_id": "lee2331", "name": {"first": "Lee", "last": "Aldwell"}, "email": "lee2331@aol.com", "major": "Graphic Design"})

// create course records
db.courses.insert({"_id": "HIST-1010", "name": "History of the World 1010", "description": "A bunch of really interesting things that actually happened", "students": ["scott","john.shore"], "ratings": [3,5,4,5,4,4,2,4]})
db.courses.insert({"_id": "ENGCOMP-1010", "name": "English Composition 1010", "description": "If you can't write well, you've got nothing!", "students": ["scott","lee2331","rcotter","john.shore","jeff"], "ratings": [4,4,5,4,5,1,5]})
db.courses.insert({"_id": "ART-1050", "name": "Artistic Interpretation 1050", "description": "Discover your inner beholder", "students": ["rcotter","scott","jeff"], "ratings": [3,4,3,4,4,3,4,4]})
 
// create instructor records
db.instructors.insert({"_id": "wally.r.binns", "name": {"first": "Wally", "middle": "r", "last": "Binns"}, "email": "wally.r.binns@ssu.edu", "bio": "I was born in the middle of my mother's doctoral dissertation on Faraday Cage isolation. I've been an academic ever since...", "publications": [{"title": "Inverted Celestial Poetry", "source": "http://www.pubcentral.com/poetry/inverted-celestial-poetry"}], "courses": ["ENGLIT-2500"]})
db.instructors.insert({"_id": "gerald.waterford.iii", "name": {"first": "Gerald", "last": "Waterford", "suffix": "III"}, "email": "gerald.waterford.iii@ssu.edu", "bio": "My father's father was a great man. My father, not so much. I am restoring the family honor.", "publications": [{"title": "Grow, grow, little Dandelion", "source": "http://www.hopefulstories.com/my-dandelion"},{"title": "The teapot and the spoon", "source": "http://www.dishsoap.com/teapot-spoon"}], "courses": ["ENGCOMP-1010","HIST-1010"]})
db.instructors.insert({"_id": "kim.b", "name": {"prefix": "Mrs.", "first": "Kim", "last": "Binnley"}, "email": "kim.b@ssu.edu", "bio": "My mother told me 'Don't let those dopes push you around'. My life has been a constant struggle against dopeness ever since. Sigh...", "publications": [], "courses": ["ART-1050"]})

