import movieClass
import fresh_tomatoes

avengers = movieClass.Movie("The Avengers",
                            "Group of superheros fighthing a group of bad guys and get this eventhough bad guys have and army we have hulk.",
                            "https://upload.wikimedia.org/wikipedia/en/8/8a/The_Avengers_%282012_film%29_poster.jpg",
                            "https://www.youtube.com/watch?v=eOrNdBpGMv8")
avengers2 = movieClass.Movie("Avengers: Age of Ultron",
                            "Tony Stark builds an artificial intelligence system named Ultron with the help of Bruce Banner. When the sentient Ultron makes plans to wipe out the human race, the Avengers set out to stop him.",
                            "https://upload.wikimedia.org/wikipedia/en/f/ff/Avengers_Age_of_Ultron_poster.jpg",
                            "https://www.youtube.com/watch?v=tmeOjFno6Do")
avengers3 = movieClass.Movie("Avengers: Infinity War",
                            "The Avengers must stop Thanos, an intergalactic warlord, from getting his hands on all the infinity stones. However, Thanos is prepared to go to any lengths to carry out his insane plan.",
                            "https://upload.wikimedia.org/wikipedia/en/4/4d/Avengers_Infinity_War_poster.jpg",
                            "https://www.youtube.com/watch?v=QwievZ1Tx-8")
avengers4 = movieClass.Movie("Avengers: Endgame",
                            "After Thanos, an intergalactic warlord, disintegrates half of the universe, the Avengers must reunite and assemble again to reinvigorate their trounced allies and restore balance.",
                            "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcQA_-tL18_rj9zEcjN6n41NEaJm-kRNF9UeOtvksZ4z_OW6jRA9",
                            "https://www.youtube.com/watch?v=TcMBFSGVi1c")
gotg1 = movieClass.Movie("Guardians of the Galaxy",
                            "Peter escapes from the planet Morag with a valuable orb that Ronan the Accuser wants. He eventually forms a group with unwilling heroes to stop Ronan.",
                            "https://upload.wikimedia.org/wikipedia/en/b/b5/Guardians_of_the_Galaxy_poster.jpg",
                            "https://www.youtube.com/watch?v=2LIQ2-PZBC8")
gotg2 = movieClass.Movie("Guardians of the Galaxy Vol. 2",
                            "After a successful mission, Quill and his team of galactic defenders meet Ego, a man claiming to be Quill's father. However, they soon learn some disturbing truths about Ego.",
                            "https://upload.wikimedia.org/wikipedia/en/thumb/a/ab/Guardians_of_the_Galaxy_Vol_2_poster.jpg/220px-Guardians_of_the_Galaxy_Vol_2_poster.jpg",
                            "https://www.youtube.com/watch?v=dW1BIid8Osg")
fresh_tomatoes.open_movies_page([avengers,avengers2,avengers3,avengers4,gotg1,gotg2])

#print(movieClass.Movie.__doc__+ "\n"+movieClass.Movie.__name__+ "\n"+movieClass.Movie.__module__)