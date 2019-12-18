(defrule data_input
=>
(printout t crlf "How old are you?:")
(bind ?age (read))
(assert (age ?age))
(printout t crlf "If your male - 1 / female - 2 (Enter number):")
(bind ?gender (read))
(assert (gender ?gender))
(printout t crlf "How are you? Good - 1 / Normal - 2 / Bad - 3 (Enter number):")
(bind ?mood (read))
(assert (mood ?mood))
(printout t crlf "Choose your favarite film? Harry Potter - 1 / Titanic - 2 / Astral - 3 / The Lion King - 4 / Sherlock - 5 (Enter number):")
(bind ?film (read))
(assert (film ?film)))

(defrule R1
(age ?age)
(gender ?gender)
(test (and (<= ?age 10) (=  ?gender 1)))
=> 
(printout t crlf crlf "You is Young Boy" crlf)
(assert (human "young_boy"))
(assert (humancnst 1)))

(defrule R2
(age ?age)
(gender ?gender)
(test (and (<= ?age 10) (=  ?gender 2)))
=> 
(printout t crlf crlf "You is Young Girl" crlf)
(assert (human "young_girl"))
(assert (humancnst 2)))

(defrule R3
(age ?age)
(gender ?gender)
(test (and ( and (> ?age 10)  (< ?age 18)) (=  ?gender 1)))
=> 
(printout t crlf crlf "You is Teenager Boy" crlf)
(assert (human "teenager_boy"))
(assert (humancnst 3)))

(defrule R4
(age ?age)
(gender ?gender)
(test (and ( and (> ?age 10)  (< ?age 18)) (=  ?gender 2)))
=> 
(printout t crlf crlf "You is Teenager Girl" crlf)
(assert (human "teenager_girl"))
(assert (humancnst 4)))

(defrule R5
(age ?age)
(gender ?gender)
(test (and (> ?age 18) (=  ?gender 1)))
=> 
(printout t crlf crlf "You is Adult Man" crlf)
(assert (human "adult_man"))
(assert (humancnst 5)))

(defrule R6
(age ?age)
(gender ?gender)
(test (and (> ?age 18) (=  ?gender 2)))
=> 
(printout t crlf crlf "You is Adult Woman" crlf)
(assert (human "adult_woman"))
(assert (humancnst 6)))

(defrule R9
(humancnst ?humancnst)
(test (or (= ?humancnst 1) (= ?humancnst 2)))
=> 
(printout t crlf crlf "Recommend genre: Cartoon!" crlf)
(assert (genre "Cartoon")))

(defrule R10
(humancnst ?humancnst)
(mood ?mood)
(film ?film)
(test (and (and (= ?humancnst 3) (= ?mood 1) ) (= ?film 5)))
=> 
(printout t crlf crlf "Recommend genre: Comedy!" crlf)
(assert (genre "Comedy")))

(defrule R11
(humancnst ?humancnst)
(mood ?mood)
(film ?film)
(test (and (= ?film 4) (and (= ?humancnst 3) (= ?mood 1) )))
=> 
(printout t crlf crlf "Recommend genre: Cartoon!" crlf)
(assert (genre "Cartoon")))

(defrule R12
(humancnst ?humancnst)
(mood ?mood)
(film ?film)
(test (and (= ?film 3) (and (= ?humancnst 3) (= ?mood 1) )))
=> 
(printout t crlf crlf "Recommend genre: Horror!" crlf)
(assert (genre "Horror")))

(defrule R13
(humancnst ?humancnst)
(mood ?mood)
(film ?film)
(test (and (= ?film 2) (and (= ?humancnst 3) (= ?mood 1) )))
=> 
(printout t crlf crlf "Recommend genre: Historical!" crlf)
(assert (genre "Historical")))

(defrule R14
(humancnst ?humancnst)
(mood ?mood)
(film ?film)
(test (and (= ?film 1) (and (= ?humancnst 3) (= ?mood 1) )))
=> 
(printout t crlf crlf "Recommend genre: Fantastic!" crlf)
(assert (genre "Fantastic")))

(defrule R15
(humancnst ?humancnst)
(mood ?mood)
(film ?film)
(test (and (= ?film 5) (and (= ?humancnst 4) (= ?mood 1) )))
=> 
(printout t crlf crlf "Recommend genre: Detective!" crlf)
(assert (genre "Detective")))

(defrule R16
(humancnst ?humancnst)
(mood ?mood)
(film ?film)
(test (and (= ?film 4) (and (= ?humancnst 4) (= ?mood 1) )))
=> 
(printout t crlf crlf "Recommend genre: Cartoon!" crlf)
(assert (genre "Cartoon")))

(defrule R17
(humancnst ?humancnst)
(mood ?mood)
(film ?film)
(test (and (= ?film 3) (and (= ?humancnst 4) (= ?mood 1) )))
=> 
(printout t crlf crlf "Recommend genre: Horror!" crlf)
(assert (genre "Horror")))

(defrule R18
(humancnst ?humancnst)
(mood ?mood)
(film ?film)
(test (and (= ?film 2) (and (= ?humancnst 4) (= ?mood 1) )))
=> 
(printout t crlf crlf "Recommend genre: Historical!" crlf)
(assert (genre "Historical")))

(defrule R19
(humancnst ?humancnst)
(mood ?mood)
(film ?film)
(test (and (= ?film 1) (and (= ?humancnst 4) (= ?mood 1) )))
=> 
(printout t crlf crlf "Recommend genre: Adventure!" crlf)
(assert (genre "Adventure")))

(defrule R20
(humancnst ?humancnst)
(mood ?mood)
(test (and (= ?mood 3) (or (= ?humancnst 5) (= ?humancnst 6))))
=> 
(printout t crlf crlf "Recommend genre: Drama!" crlf)
(assert (genre "Drama")))

