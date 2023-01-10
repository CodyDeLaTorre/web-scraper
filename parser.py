from bs4 import BeautifulSoup


def parse(markup):
    soup = BeautifulSoup(markup, "html.parser")

    courses = soup.select('.calendar-event')

    course_info = "Course Info\n"

    for course in courses:
        if "Python" in course.h1.text:
           course_info += course.h1.text + '\n'
           course_info += course.h2.text + '\n'


    return course_info