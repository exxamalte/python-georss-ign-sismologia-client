"""Test the IGN Instituto Geográfico Nacional Sismología feed manager."""
import datetime
from unittest import mock

from georss_ign_sismologia_client import IgnSismologiaFeedManager

from .utils import load_fixture

HOME_COORDINATES = (40.38, -3.72)


@mock.patch("requests.Request")
@mock.patch("requests.Session")
def test_feed_manager(mock_session, mock_request):
    """Test the feed manager."""
    mock_session.return_value.__enter__.return_value.send.return_value.ok = True
    mock_session.return_value.__enter__.return_value.send.return_value.text = (
        load_fixture("ign_sismologia_feed.xml")
    )

    # This will just record calls and keep track of external ids.
    generated_entity_external_ids = []
    updated_entity_external_ids = []
    removed_entity_external_ids = []

    def _generate_entity(external_id):
        """Generate new entity."""
        generated_entity_external_ids.append(external_id)

    def _update_entity(external_id):
        """Update entity."""
        updated_entity_external_ids.append(external_id)

    def _remove_entity(external_id):
        """Remove entity."""
        removed_entity_external_ids.append(external_id)

    feed_manager = IgnSismologiaFeedManager(
        _generate_entity, _update_entity, _remove_entity, HOME_COORDINATES
    )
    assert (
        repr(feed_manager) == "<IgnSismologiaFeedManager("
        "feed=<IgnSismologiaFeed(home="
        "(40.38, -3.72), "
        "url=http://www.ign.es/ign/"
        "RssTools/sismologia.xml, "
        "radius=None, magnitude=None)>)>"
    )
    feed_manager.update()
    entries = feed_manager.feed_entries
    assert entries is not None
    assert len(entries) == 4
    assert feed_manager.last_timestamp == datetime.datetime(2019, 3, 18, 19, 34, 55)
    assert len(generated_entity_external_ids) == 4
    assert len(updated_entity_external_ids) == 0
    assert len(removed_entity_external_ids) == 0
