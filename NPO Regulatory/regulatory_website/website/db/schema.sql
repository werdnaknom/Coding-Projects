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
