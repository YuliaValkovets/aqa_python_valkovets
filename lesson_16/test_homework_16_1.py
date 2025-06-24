import pytest
from homework_16_1 import TeamLead


@pytest.mark.parametrize('attributes', ['name', 'salary', 'department', 'programming_language',
                                        'team_size'])
def test_teamlead_has_all_attr(attributes):
    team_lead = TeamLead('Vasyl', '4000', 'IT', 'Java',
                         6)
    assert getattr(team_lead, attributes, 'Unknown') != 'Unknown'