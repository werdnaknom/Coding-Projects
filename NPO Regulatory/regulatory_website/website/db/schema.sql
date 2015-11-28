drop table if exists products;
create table products (
  pid integer primary key autoincrement,
  name text not null,
  customer text not null,
  pba text not null,
  ports text not null,
  silicon text not null,
  status text not null,
  notes text
);

drop table if exists dashroll;
create table dashroll (
    did INTEGER PRIMARY KEY autoincrement,
    roll INTEGER NOT NULL,
    pid INTEGER NOT NULL,
    description text,
    FOREIGN KEY(pid) REFERENCES products(pid)
);

drop table if exists regulatory;
create table regulatory (
  rid INTEGER PRIMARY KEY autoincrement,
  pid INTEGER NOT NULL,
  priority integer,
  job_number text,
  e1_id INTEGER,
  e2_id INTEGER,
  e3_id INTEGER,
  e4_id INTEGER,
  e5_id INTEGER,
  e6_id INTEGER,
  e7_id INTEGER,
  e8_id INTEGER,
  e9_id INTEGER,
  e10_id INTEGER,
  e11_id INTEGER,
  e12_id INTEGER,
  e13_id INTEGER,
  FOREIGN KEY(pid) REFERENCES products(pid),
  FOREIGN KEY(e1_id) REFERENCES regulatory_surge(id),
  FOREIGN KEY(e2_id) REFERENCES regulatory_interrupt(id),
  FOREIGN KEY(e3_id) REFERENCES regulatory_conducted_immunity(id),
  FOREIGN KEY(e4_id) REFERENCES regulatory_electrical_fast_transient(id),
  FOREIGN KEY(e5_id) REFERENCES regulatory_esd(id),
  FOREIGN KEY(e6_id) REFERENCES regulatory_flicker(id),
  FOREIGN KEY(e7_id) REFERENCES regulatory_pwr_freq_magnetic(id),
  FOREIGN KEY(e8_id) REFERENCES regulatory_pwr_line_conducted(id),
  FOREIGN KEY(e9_id) REFERENCES regulatory_power_line_harmonics_id(id),
  FOREIGN KEY(e10_id) REFERENCES regulatory_radiated_emissions(id),
  FOREIGN KEY(e11_id) REFERENCES regulatory_radiated_immunity(id),
  FOREIGN KEY(e12_id) REFERENCES regulatory_telecom_port_conducted_emissions(id),
  FOREIGN KEY(e13_id) REFERENCES regulatory_dip_and_dropout(id)
);

drop table if exists regulatory_surge;
create table regulatory_surge (
   id INTEGER PRIMARY KEY autoincrement,
   system text,
   notes text,
   pass_req text,
   status text
);

drop table if exists regulatory_interrupt;
create table regulatory_interrupt (
   id INTEGER PRIMARY KEY autoincrement,
   system text,
   notes text,
   pass_req text,
   status text
);

drop table if exists regulatory_conducted_immunity;
create table regulatory_conducted_immunity (
   id INTEGER PRIMARY KEY autoincrement,
   system text,
   notes text,
   pass_req text,
   status text
);

drop table if exists regulatory_electrical_fast_transient;
create table regulatory_electrical_fast_transient (
   id INTEGER PRIMARY KEY autoincrement,
   system text,
   notes text,
   pass_req text,
   status text
);

drop table if exists regulatory_esd;
create table regulatory_esd (
   id INTEGER PRIMARY KEY autoincrement,
   system text,
   notes text,
   pass_req text,
   status text
);

drop table if exists regulatory_flicker;
create table regulatory_flicker (
   id INTEGER PRIMARY KEY autoincrement,
   system text,
   notes text,
   pass_req text,
   status text
);

drop table if exists regulatory_pwr_freq_magnetic;
create table regulatory_pwr_freq_magnetic (
   id INTEGER PRIMARY KEY autoincrement,
   system text,
   notes text,
   pass_req text,
   status text
);

drop table if exists regulatory_pwr_line_conducted;
create table regulatory_pwr_line_conducted (
   id INTEGER PRIMARY KEY autoincrement,
   system text,
   notes text,
   pass_req text,
   status text
);

drop table if exists regulatory_power_line_harmonics_id;
create table regulatory_power_line_harmonics_id (
   id INTEGER PRIMARY KEY autoincrement,
   system text,
   notes text,
   pass_req text,
   status text
);

drop table if exists regulatory_radiated_emissions;
create table regulatory_radiated_emissions (
   id INTEGER PRIMARY KEY autoincrement,
   system text,
   notes text,
   pass_req text,
   status text
);

drop table if exists regulatory_radiated_immunity;
create table regulatory_radiated_immunity (
   id INTEGER PRIMARY KEY autoincrement,
   system text,
   notes text,
   pass_req text,
   status text
);

drop table if exists regulatory_telecom_port_conducted_emissions;
create table regulatory_telecom_port_conducted_emissions (
   id INTEGER PRIMARY KEY autoincrement,
   system text,
   notes text,
   pass_req text,
   status text
);

drop table if exists regulatory_dip_and_dropout;
create table regulatory_dip_and_dropout (
   id INTEGER PRIMARY KEY autoincrement,
   system text,
   notes text,
   pass_req text,
   status text
);


