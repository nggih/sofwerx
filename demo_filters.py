# the geo json geometry object we got from geojson.io
geo_json_geometry = {
  "type": "Polygon",
  "coordinates": [
    [
      [
        126.4879,
        33.755
      ],
      [
        127.3842,
        33.755
      ],
      [
        127.3842,
        34.3728
      ],
      [
        126.4879,
        34.3728
      ],
      [
        126.4879,
        33.755
      ]
    ]
  ]
}

# filter for items the overlap with our chosen geometry
geometry_filter = {
  "type": "GeometryFilter",
  "field_name": "geometry",
  "config": geo_json_geometry
}

# filter images acquired in a certain date range
date_range_filter = {
  "type": "DateRangeFilter",
  "field_name": "acquired",
  "config": {
    "gte": "2017-04-27T00:00:00.000Z",
    "lte": "2017-04-30T00:00:00.000Z"
  }
}

# filter any images which are more than 50% clouds
cloud_cover_filter = {
  "type": "RangeFilter",
  "field_name": "cloud_cover",
  "config": {
    "lte": 0.5
  }
}

# create a filter that combines our geo and date filters
# could also use an "OrFilter"
Vessel_Search = {
  "type": "AndFilter",
  "config": [geometry_filter, date_range_filter, cloud_cover_filter]
}
