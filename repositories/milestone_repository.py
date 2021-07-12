from db.run_sql import run_sql

from models.milestone import Milestone
from models.goal import Goal
import repositories.goal_repository as goal_repository


def save(milestone):
    sql = "INSERT INTO milestone (mile_title, mile_desc, mile_position, mile_date, goal_id) VALUES (%s, %s, %s, %s, %s) RETURNING *"
    values = [milestone.mile_title, milestone.mile_desc, milestone.mile_position, milestone.mile_date, milestone.goal.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    milestone.id = id
    return milestone