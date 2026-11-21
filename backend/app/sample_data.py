from app.schema import Education, Experience, Project, Resume

SAMPLE_RESUME = Resume(
    name='Sample Student',
    email='sample@example.com',
    phone='9876543210',
    linkedin='linkedin.com/in/sample',
    github='github.com/sample',
    summary='Final year computer science student skilled in building data pipelines and web applications with Python and SQL, seeking a data engineer role to deliver reliable analytics systems.',
    education=[Education(institution='Sample Institute of Technology', degree='B.Tech Computer Science', start='2022', end='2026', cgpa='8.5')],
    experience=[Experience(
        role='Data Engineering Intern',
        company='Sample Corp',
        start='Jun 2025',
        end='Aug 2025',
        bullets=[
            'Built an ETL pipeline in Python that processed 50000 records daily',
            'Reduced report generation time by 40% by optimizing SQL queries',
        ],
    )],
    projects=[Project(
        name='Air Quality Pipeline',
        tech=['Python', 'SQL', 'FastAPI'],
        bullets=['Developed an alert system that flagged unsafe AQI levels across 12 cities'],
    )],
    skills=['Python', 'SQL', 'FastAPI', 'Git', 'Docker'],
)
