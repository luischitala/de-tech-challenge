-- public.mayoralties definition

-- Drop table

-- DROP TABLE public.mayoralties;

CREATE TABLE public.mayoralties (
	id serial4 NOT NULL,
	nomgeo varchar NULL,
	cve_mun int4 NULL,
	cve_ent int4 NULL,
	cvegeo int4 NULL,
	geo_point_2d varchar NULL,
	geo_shape public.geometry(polygon, 4326) NULL,
	municipio int4 NULL,
	CONSTRAINT mayoralties_pkey PRIMARY KEY (id)
);
CREATE INDEX idx_mayoralties_geo_shape ON public.mayoralties USING gist (geo_shape);

-- public.transport_units definition

-- Drop table

-- DROP TABLE public.transport_units;

CREATE TABLE public.transport_units (
	id serial4 NOT NULL,
	date_updated timestamp NULL,
	vehicle_id int4 NULL,
	vehicle_label int4 NULL,
	vehicle_current_status int4 NULL,
	position_latitude float8 NULL,
	position_longitude float8 NULL,
	geographic_point public.geometry(point, 4326) NULL,
	position_speed int4 NULL,
	position_odometer int4 NULL,
	trip_schedule_relationship int4 NULL,
	trip_id int4 NULL,
	trip_start_date int4 NULL,
	trip_route_id int4 NULL,
	mayoralty varchar NULL,
	CONSTRAINT transport_units_pkey PRIMARY KEY (id)
);
CREATE INDEX idx_transport_units_geographic_point ON public.transport_units USING gist (geographic_point);