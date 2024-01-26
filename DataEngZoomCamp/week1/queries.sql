-- Count records 

select
	count(*)
from
	green_tripdata
where
	lpep_pickup_datetime >= '2019-09-18 00:00:00' and
	lpep_dropoff_datetime < '2019-09-19 00:00:00';


-- Largest trip for each day

select
	max(trip_distance) as max_distance,
	date(lpep_pickup_datetime) as lpep_pickup_date
from
	green_tripdata
group by
	lpep_pickup_date
order by
	max_distance desc
limit 
    1

-- The number of passengers

select
	tz.borough,
	sum(gtd.total_amount) as total_amount
from
	green_tripdata gtd
join
	(
		select
			"LocationID",
			"Borough" as borough
		from
			taxi_zones
		where
			"Borough" != 'Unknown'
	) tz on gtd."PULocationID" = tz."LocationID"
where
	date(gtd.lpep_pickup_datetime) = '2019-09-18'
group by
	tz.borough
having
	sum(total_amount) > 50000
order by
	sum(total_amount) desc
limit 
    3

	
-- Largest tip

with taxi_zones_cte as (
	select
		"LocationID" as location_id,
		"Zone" as zone
	from taxi_zones
)

select
	tzdo.zone,
	max(gtd.tip_amount) as tip_amount
from
	green_tripdata gtd
join
	taxi_zones_cte tzpu on tzpu.location_id = gtd."PULocationID" and tzpu.zone = 'Astoria'
join
	taxi_zones_cte tzdo on tzdo.location_id = gtd."DOLocationID"
where
	extract(year from gtd.lpep_pickup_datetime) = 2019 and
	extract(month from gtd.lpep_pickup_datetime) = 9
group by
	tzdo.zone
order by
	max(gtd.tip_amount) desc
limit 1
