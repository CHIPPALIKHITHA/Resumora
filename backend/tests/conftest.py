import pytest

from app.schema import Education, Project, Resume


@pytest.fixture
def good_resume():
    return Resume(
        name='Test Student',
        email='test@example.com',
        phone='9876543210',
        linkedin='linkedin.com/in/test',
        github='github.com/test',
        summary='Final year computer science student skilled in building data pipelines and web applications with Python and SQL, seeking a data engineer role to deliver reliable analytics systems.',
        education=[Education(institution='SRM IST', degree='B.Tech CSE', start='2022', end='2026', cgpa='8.5')],
        projects=[Project(
            name='Air Quality Pipeline',
            tech=['Python', 'SQL'],
            bullets=['Built an ETL pipeline in Python that processed 50000 records daily and cut manual effort by 40%'],
        )],
        skills=['Python', 'SQL', 'FastAPI', 'Git', 'Docker'],
    )
