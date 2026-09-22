def test_get_activities_returns_initial_activities(client):
    # Arrange
    expected_participants = [
        "michael@mergington.edu",
        "daniel@mergington.edu",
    ]

    # Act
    response = client.get("/activities")
    activities = response.json()

    # Assert
    assert response.status_code == 200
    assert "Chess Club" in activities
    assert activities["Chess Club"]["description"] == (
        "Learn strategies and compete in chess tournaments"
    )
    assert activities["Chess Club"]["participants"] == expected_participants


def test_get_activities_includes_activity_details(client):
    # Arrange
    expected_fields = {
        "description",
        "schedule",
        "max_participants",
        "participants",
    }

    # Act
    activity = client.get("/activities").json()["Programming Class"]

    # Assert
    assert set(activity) == expected_fields
