def test_get_activities_returns_initial_activities(client):
    response = client.get("/activities")

    assert response.status_code == 200
    activities = response.json()
    assert "Chess Club" in activities
    assert activities["Chess Club"]["description"] == (
        "Learn strategies and compete in chess tournaments"
    )
    assert activities["Chess Club"]["participants"] == [
        "michael@mergington.edu",
        "daniel@mergington.edu",
    ]


def test_get_activities_includes_activity_details(client):
    activity = client.get("/activities").json()["Programming Class"]

    assert set(activity) == {
        "description",
        "schedule",
        "max_participants",
        "participants",
    }
