def feature_store_lookup(feature_store, requests, defaults):
    """
    Join offline user features with online request-time features.
    """
    # Write code here
    result = []
    for r in requests:
        online = r.get("online_features", {})
        offline = feature_store.get(r.get("user_id"),defaults)

        combine = offline.copy()
        combine.update(online)
        result.append(combine)

    return result

