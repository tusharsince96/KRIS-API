create table Project(
ProjectID varchar(15) primary key,
ProjectName varchar(200),
ProjectDiscription varchar (2000),
);
Drop table Project;
select * from Project;
Insert into Project(ProjectID,ProjectName,ProjectDiscription)values('PRJ1000001','SafeRoads','An initiative to revamp and repair major highways and roads across the country, ensuring safer travel for all.')
Insert into Project(ProjectID,ProjectName,ProjectDiscription)values('PRJ1000002','GreenTransit 2030','A project focused on promoting and integrating eco-friendly public transportation options, reducing carbon emissions and traffic congestion.')
use cafe;
Insert into Project(ProjectID,ProjectName,ProjectDiscription)values('PRJ1000003','Bridge-Strong-Initiative','A dedicated effort to inspect, maintain, and reconstruct aging bridges to ensure they meet modern safety standards.')
use cafe;
create table Asset(
AssetID varchar(15) primary key,
AssetName varchar(200),
Information varchar (2000),
Cost bigint,
AssetType varchar(100),
AssetLocation varchar(100)
);
select * from Asset;
Insert into Asset(AssetID,AssetName,Information,Cost,AssetType,AssetLocation)values('14','Saftey Barriers','Overhead Barriers #1','47000','Road Asset','BedFord');
Insert into Asset(AssetID,AssetName,Information,Cost,AssetType,AssetLocation)values('122','Drainage','Straight Drainage #1','78000','Road Asset','Elagana');
select * from Asset where AssetID='122';
/*Need Table*/
use cafe;
create table Need(
NeedID varchar(15) primary key,
AssetID varchar(15),
Critacility  varchar(200),
Descriptions varchar (2000),
Author varchar(100)
);
select * from Need;
Insert into Need(NeedID,AssetID,Critacility,Descriptions,Author)values('14','14','Urgent','Excessive deformation resulting in extensive in infiteration of soil with roads ways','Bill gates');
Insert into Need(NeedID,AssetID,Critacility,Descriptions,Author)values('122','122','Moderate','Trench not working','James');
